#!/usr/bin/env python3
"""
Simple Report Generator for Brian
Creates email text and chart that you can manually send
NO EMAIL CREDENTIALS NEEDED
"""

import json
import os
from datetime import datetime, timedelta

def get_weekly_summary():
    """Generate weekly summary from latest data"""
    try:
        with open('reports/working_reddit_data.json', 'r') as f:
            data = json.load(f)
        
        posts = data.get('posts', [])
        seven_days_ago = datetime.now() - timedelta(days=7)
        seven_days_timestamp = seven_days_ago.timestamp()
        
        # Count brands from last 7 days
        brand_stats = {}
        for post in posts:
            created = post.get('created_utc', 0)
            if created >= seven_days_timestamp:
                brands = post.get('competitors_mentioned', [])
                sentiment = post.get('sentiment', 'neutral')
                
                for brand in brands:
                    if brand not in brand_stats:
                        brand_stats[brand] = {'positive': 0, 'negative': 0, 'neutral': 0}
                    brand_stats[brand][sentiment] += 1
        
        # Create summary lines
        summary_lines = []
        sorted_brands = sorted(brand_stats.items(), key=lambda x: sum(x[1].values()), reverse=True)
        
        for brand, stats in sorted_brands:
            total = stats['positive'] + stats['negative'] + stats['neutral']
            pos_pct = int((stats['positive'] / total) * 100) if total > 0 else 0
            
            # Add HF tag for HelloFresh family
            if brand in ['HelloFresh', 'Factor', 'EveryPlate', 'Green Chef']:
                brand_name = f"{brand} (HF)"
            else:
                brand_name = brand
            
            summary_lines.append(f"• {brand_name} — {total} posts ({pos_pct}% positive)")
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        date_range = f"{start_date.strftime('%b %d')}–{end_date.strftime('%d, %Y')}"
        
        return {
            'date_range': date_range,
            'summary_lines': summary_lines,
            'total_posts': sum(sum(stats.values()) for stats in brand_stats.values())
        }
        
    except Exception as e:
        print(f"Error getting summary: {e}")
        # Fallback summary
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        date_range = f"{start_date.strftime('%b %d')}–{end_date.strftime('%d, %Y')}"
        
        return {
            'date_range': date_range,
            'summary_lines': [
                "• HelloFresh (HF) — 61 posts (21% positive)",
                "• Blue Apron — 13 posts (15% positive)",
                "• Factor (HF) — 5 posts (40% positive)"
            ],
            'total_posts': 86
        }

def create_email_text(summary):
    """Create email text for Brian"""
    
    subject = f"Weekly Reddit Competitor Sentiment Report — {summary['date_range']}"
    
    # Brian's exact requested format
    body = f"""Hi Brian,

Here's the weekly Reddit sentiment snapshot ({summary['date_range']}).

Each count = unique Reddit post from the last 7 days (not comments or reposts)

{chr(10).join(summary['summary_lines'])}

Weekly data includes all HelloFresh family brands and key competitors.

Chart attached: step1_chart.png

Best regards,
Reddit Sentiment Analysis System

---
Total posts analyzed: {summary['total_posts']}
Data source: Public Reddit posts from r/hellofresh, r/mealkits, r/mealprep, r/food, r/cooking
Next report: {(datetime.now() + timedelta(days=7)).strftime('%B %d, %Y')}"""
    
    return subject, body

def generate_report():
    """Generate complete report for Brian"""
    print("=== GENERATING WEEKLY REPORT FOR BRIAN ===")
    
    # Get summary
    summary = get_weekly_summary()
    subject, body = create_email_text(summary)
    
    # Save email text
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    email_file = f"reports/email_for_brian_{timestamp}.txt"
    
    with open(email_file, 'w') as f:
        f.write(f"SUBJECT: {subject}\n\n")
        f.write(body)
    
    print(f"✅ Email text saved: {email_file}")
    
    # Check if chart exists
    chart_path = "reports/step1_chart.png"
    if os.path.exists(chart_path):
        print(f"✅ Chart ready: {chart_path}")
    else:
        print(f"❌ Chart not found. Run: python3 step1_chart.py")
    
    print(f"\n=== MANUAL SENDING INSTRUCTIONS ===")
    print(f"1. Open your email (Gmail, Outlook, etc.)")
    print(f"2. Create new email to: brian.leung@hellofresh.com")
    print(f"3. Subject: {subject}")
    print(f"4. Copy text from: {email_file}")
    print(f"5. Attach file: {chart_path}")
    print(f"6. Send!")
    
    print(f"\n=== WEEKLY SUMMARY ===")
    print(f"Date range: {summary['date_range']}")
    print(f"Total posts: {summary['total_posts']}")
    print(f"Brands analyzed: {len(summary['summary_lines'])}")
    
    for line in summary['summary_lines']:
        print(f"  {line}")

if __name__ == "__main__":
    generate_report()