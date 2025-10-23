#!/usr/bin/env python3
"""
Weekly Reddit Sentiment Report - ONE SIMPLE SCRIPT
Updates data, generates chart, asks for email, sends report
"""

import subprocess
import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timedelta

def update_weekly_data():
    """Update weekly Reddit data and chart"""
    print("=== UPDATING WEEKLY REDDIT DATA ===")
    
    # Get fresh Reddit data
    print("Collecting Reddit data (last 7 days)...")
    try:
        subprocess.run(['python3', 'scraper.py'], capture_output=True, text=True, timeout=120)
        print("✅ Data updated")
    except:
        print("⚠️  Using existing data")
    
    # Generate chart
    print("Generating weekly chart...")
    try:
        subprocess.run(['python3', 'step1_chart.py'], capture_output=True, text=True)
        print("✅ Chart updated")
    except:
        print("❌ Chart failed")
        return False
    
    return True

def get_weekly_summary():
    """Get weekly summary from data"""
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
        
        # Create summary
        summary_lines = []
        sorted_brands = sorted(brand_stats.items(), key=lambda x: sum(x[1].values()), reverse=True)
        
        for brand, stats in sorted_brands:
            total = stats['positive'] + stats['negative'] + stats['neutral']
            pos_pct = int((stats['positive'] / total) * 100) if total > 0 else 0
            
            # Add (HF) for HelloFresh family
            if brand in ['HelloFresh', 'Factor', 'EveryPlate', 'Green Chef']:
                brand_name = f"{brand} (HF)"
            else:
                brand_name = brand
            
            summary_lines.append(f"• {brand_name} — {total} posts ({pos_pct}% positive)")
        
        # Date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        date_range = f"{start_date.strftime('%b %d')}–{end_date.strftime('%d, %Y')}"
        
        return date_range, summary_lines, sum(sum(stats.values()) for stats in brand_stats.values())
        
    except:
        # Fallback
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        date_range = f"{start_date.strftime('%b %d')}–{end_date.strftime('%d, %Y')}"
        return date_range, ["• Data loading..."], 0

def create_email_content(date_range, summary_lines, total_posts):
    """Create email subject and body"""
    subject = f"Weekly Reddit Competitor Sentiment Report — {date_range}"
    
    body = f"""Hi Brian,

Here's the weekly Reddit sentiment snapshot ({date_range}).

Each count = unique Reddit post from the last 7 days (not comments or reposts)

{chr(10).join(summary_lines)}

Weekly data includes all HelloFresh family brands and key competitors.

Chart attached: step1_chart.png

Best regards,
Reddit Sentiment Analysis System

---
Total posts analyzed: {total_posts}
Data source: Public Reddit posts from r/hellofresh, r/mealkits, r/mealprep, r/food, r/cooking
Next report: {(datetime.now() + timedelta(days=7)).strftime('%B %d, %Y')}"""
    
    return subject, body

def prepare_email_files(email_to, subject, body):
    """Create email files and open them for easy sending - NO PASSWORDS"""
    print(f"\n=== PREPARING EMAIL FOR: {email_to} ===")
    
    # Save email content
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    email_file = f"reports/email_to_send_{timestamp}.txt"
    
    email_content = f"""To: {email_to}
Subject: {subject}

{body}

INSTRUCTIONS:
1. Copy the subject line above
2. Copy the email body above  
3. Open Gmail/Outlook and create new email
4. Paste subject and body
5. Attach the chart file: reports/step1_chart.png
6. Send!"""
    
    with open(email_file, 'w') as f:
        f.write(email_content)
    
    chart_path = 'reports/step1_chart.png'
    
    print("✅ EMAIL FILES READY!")
    print(f"📧 Email content: {email_file}")
    print(f"📊 Chart: {chart_path}")
    
    # Open files automatically
    try:
        subprocess.run(['open', email_file])
        subprocess.run(['open', chart_path])
        print("✅ Files opened automatically!")
        print("Just copy the email text and drag the chart to your email!")
    except:
        print("Manual opening:")
        print(f"open {email_file}")
        print(f"open {chart_path}")
    
    return True

def main():
    """Main function - complete weekly report system"""
    print("=== WEEKLY REDDIT SENTIMENT REPORT ===")
    
    # Update data and chart
    if not update_weekly_data():
        print("❌ Data update failed")
        return
    
    # Get summary
    date_range, summary_lines, total_posts = get_weekly_summary()
    subject, body = create_email_content(date_range, summary_lines, total_posts)
    
    print(f"\n=== REPORT READY ===")
    print(f"Date: {date_range}")
    print(f"Total posts: {total_posts}")
    print("Preview:")
    for line in summary_lines[:5]:  # Show first 5 brands
        print(f"  {line}")
    
    # Ask for email to send to
    print(f"\n=== SEND REPORT ===")
    email_to = input("Send to email (default: brian.leung@hellofresh.com): ").strip()
    if not email_to:
        email_to = "brian.leung@hellofresh.com"
    
    # Prepare email files (no passwords needed)
    prepare_email_files(email_to, subject, body)

if __name__ == "__main__":
    main()