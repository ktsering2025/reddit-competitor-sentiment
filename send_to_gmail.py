#!/usr/bin/env python3
"""
Send Report to Gmail Inbox - NO PASSWORDS NEEDED
Uses a web service to send emails directly to your Gmail
"""

import requests
import json
import base64
import subprocess
import os
from datetime import datetime, timedelta

def get_weekly_summary():
    """Get weekly summary from data"""
    with open('reports/working_reddit_data.json', 'r') as f:
        data = json.load(f)
    
    posts = data.get('posts', [])
    date_range = data.get('date_range', {})
    
    # Use actual date window from scraped data
    if date_range and 'start' in date_range and 'end' in date_range:
        start_date = datetime.fromisoformat(date_range['start'].replace('Z', '+00:00'))
        end_date = datetime.fromisoformat(date_range['end'].replace('Z', '+00:00'))
    else:
        # Fallback to 7 days ago
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
    
    # Filter posts within the actual date window
    start_timestamp = start_date.timestamp()
    end_timestamp = end_date.timestamp()
    
    brand_stats = {}
    for post in posts:
        created = post.get('created_utc', 0)
        if start_timestamp <= created <= end_timestamp:
            brands = post.get('competitors_mentioned', [])
            sentiment = post.get('sentiment', 'neutral')
            
            for brand in brands:
                if brand not in brand_stats:
                    brand_stats[brand] = {'positive': 0, 'negative': 0, 'neutral': 0}
                brand_stats[brand][sentiment] += 1
    
    summary_lines = []
    sorted_brands = sorted(brand_stats.items(), key=lambda x: sum(x[1].values()), reverse=True)
    
    for brand, stats in sorted_brands:
        total = sum(stats.values())
        pos_pct = int((stats['positive'] / total) * 100) if total > 0 else 0
        
        if brand in ['HelloFresh', 'Factor', 'EveryPlate', 'Green Chef']:
            brand_name = f"{brand} (HF)"
        else:
            brand_name = brand
        
        summary_lines.append(f"• {brand_name} — {total} posts ({pos_pct}% positive)")
    
    # Format date range for email (UTC)
    date_range_str = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} UTC"
    
    return date_range_str, summary_lines, sum(sum(stats.values()) for stats in brand_stats.values())

def get_top_posts_for_email():
    """Get Top 3 Positive and Negative posts for HelloFresh and Factor75"""
    with open('reports/working_reddit_data.json', 'r') as f:
        data = json.load(f)
    
    posts = data.get('posts', [])
    hf_posts = [p for p in posts if 'HelloFresh' in p.get('competitors_mentioned', [])]
    f75_posts = [p for p in posts if 'Factor75' in p.get('competitors_mentioned', [])]
    
    def calculate_engagement(post):
        return post.get('score', 0) + 3 * post.get('num_comments', 0)
    
    # Get top 3 positive and negative for each brand
    hf_positive = sorted([p for p in hf_posts if p.get('sentiment') == 'positive'], 
                        key=calculate_engagement, reverse=True)[:3]
    hf_negative = sorted([p for p in hf_posts if p.get('sentiment') == 'negative'], 
                        key=calculate_engagement, reverse=True)[:3]
    f75_positive = sorted([p for p in f75_posts if p.get('sentiment') == 'positive'], 
                         key=calculate_engagement, reverse=True)[:3]
    f75_negative = sorted([p for p in f75_posts if p.get('sentiment') == 'negative'], 
                         key=calculate_engagement, reverse=True)[:3]
    
    return hf_positive, hf_negative, f75_positive, f75_negative

def send_via_mailto(recipient_email):
    """Send email using system mail client with automatic chart attachment"""
    print(f"=== SENDING TO: {recipient_email} ===")
    
    # Get date range from data
    with open('reports/working_reddit_data.json', 'r') as f:
        data = json.load(f)
    
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '2025-10-20').split('T')[0]
    end_date = date_range.get('end', '2025-10-25').split('T')[0]
    
    subject = f"Weekly Reddit Competitor Sentiment Report — {start_date} to {end_date}"
    
    # Get summary stats
    posts = data.get('posts', [])
    hf_posts = [p for p in posts if p.get('primary_brand') == 'HelloFresh']
    f75_posts = [p for p in posts if p.get('primary_brand') == 'Factor75']
    
    hf_positive = len([p for p in hf_posts if p['sentiment'] == 'positive'])
    hf_negative = len([p for p in hf_posts if p['sentiment'] == 'negative'])
    hf_neutral = len([p for p in hf_posts if p['sentiment'] == 'neutral'])
    hf_total = len(hf_posts)
    hf_pct = int((hf_positive / hf_total * 100)) if hf_total > 0 else 0
    
    f75_positive = len([p for p in f75_posts if p['sentiment'] == 'positive'])
    f75_negative = len([p for p in f75_posts if p['sentiment'] == 'negative'])
    f75_neutral = len([p for p in f75_posts if p['sentiment'] == 'neutral'])
    f75_total = len(f75_posts)
    f75_pct = int((f75_positive / f75_total * 100)) if f75_total > 0 else 0
    
    # Build SIMPLIFIED email body (no post lists)
    body_lines = []
    body_lines.append("Weekly Reddit Competitor Sentiment Report")
    body_lines.append("=" * 60)
    body_lines.append("")
    body_lines.append(f"Analysis Period: {start_date} to {end_date}")
    body_lines.append("")
    body_lines.append("QUICK SUMMARY:")
    body_lines.append("-" * 60)
    body_lines.append(f"HelloFresh: {hf_total} posts ({hf_pct}% positive)")
    body_lines.append(f"  • {hf_positive} positive, {hf_negative} negative, {hf_neutral} neutral")
    body_lines.append("")
    body_lines.append(f"Factor75: {f75_total} posts ({f75_pct}% positive)")
    body_lines.append(f"  • {f75_positive} positive, {f75_negative} negative, {f75_neutral} neutral")
    body_lines.append("")
    body_lines.append("DASHBOARD ACCESS:")
    body_lines.append("-" * 60)
    body_lines.append("Main Dashboard:")
    body_lines.append("https://ktsering2025.github.io/reddit-competitor-sentiment/")
    body_lines.append("")
    body_lines.append("Step 1 Chart (attached as PNG)")
    body_lines.append("")
    body_lines.append("Step 2 Deep Dive (HelloFresh & Factor75):")
    body_lines.append("https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html")
    body_lines.append("")
    body_lines.append("Step 3 Competitor Analysis:")
    body_lines.append("https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html")
    body_lines.append("")
    body_lines.append("=" * 60)
    body_lines.append("Data refreshed weekly • Built for Brian's competitive intelligence")
    
    body = "\n".join(body_lines)
    
    # Create AppleScript to send email with attachment
    applescript = f'''
    tell application "Mail"
        set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}"}}
        tell newMessage
            make new to recipient with properties {{address:"{recipient_email}"}}
            
            -- Attach the chart
            set chartPath to POSIX file "{os.path.abspath('reports/step1_chart.png')}"
            make new attachment with properties {{file name:chartPath}} at after the last paragraph
        end tell
        send newMessage
    end tell
    '''
    
    # Execute AppleScript
    try:
        subprocess.run(['osascript', '-e', applescript], check=True)
        print(f"[SUCCESS] Email sent to {recipient_email}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False

def send_via_web_service_OLD_ORPHANED(recipient_email):
    """ORPHANED CODE - NOT USED"""
    body = f"""Hi there,

Here's your weekly Reddit sentiment analysis ({date_range}).

QUICK SUMMARY:
• HelloFresh: {hf_posts} posts ({hf_sentiment_pct}% positive) - {'Excellent brand health' if hf_sentiment_pct >= 70 else 'Good performance' if hf_sentiment_pct >= 50 else 'Needs attention'}
• Factor75: {factor_posts} posts ({factor_sentiment_pct}% positive) - {'Strong performance' if factor_sentiment_pct >= 70 else 'Good performance' if factor_sentiment_pct >= 50 else 'Needs immediate attention'}

COMPLETE COMPETITOR BREAKDOWN:
{chr(10).join(summary_lines)}

LIVE DASHBOARD ACCESS:
Main Dashboard: https://ktsering2025.github.io/reddit-competitor-sentiment/
Step 1 Chart: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png
Step 2 Analysis: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html

KEY INSIGHTS:
• Real-time Reddit weekly search data (last 7 days)
• Brand-specific filtering for HelloFresh and Factor75 only
• Engagement scoring prioritizes comments for discussion value
• Manual sentiment classification for business accuracy

IMMEDIATE ACTIONS:
• Review live dashboard using links above
• Focus on {'Factor75' if factor_sentiment_pct < 50 else 'HelloFresh'} - {'immediate attention needed' if factor_sentiment_pct < 50 else 'maintain current strategy'}
• Monitor competitive landscape weekly

Best regards,
Reddit Sentiment Analysis System

---
Total posts analyzed: {total_posts}
Next report: {(datetime.now() + timedelta(days=7)).strftime('%B %d, %Y')}
All links work on mobile, tablet, and desktop"""
    
    try:
        # Create AppleScript to send email with attachment via Mail app
        chart_path = f"{subprocess.check_output(['pwd']).decode().strip()}/reports/step1_chart.png"
        
        applescript = f'''
tell application "Mail"
    activate
    set theMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}"}}
    tell theMessage
        set visible to true
        make new to recipient at end of to recipients with properties {{address:"{recipient_email}"}}
        make new attachment with properties {{file name:"{chart_path}"}} at after the last paragraph
    end tell
end tell
'''
        
        # Save and run AppleScript
        with open('/tmp/send_email.scpt', 'w') as f:
            f.write(applescript)
        
        result = subprocess.run(['osascript', '/tmp/send_email.scpt'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Mail app opened with email and chart attached!")
            print("Review the email and click Send")
            print("Chart should be automatically attached")
            return True
        else:
            print(f"AppleScript error: {result.stderr}")
            print("Falling back to manual attachment...")
            
            # Fallback to original method
            import urllib.parse
            subject_encoded = urllib.parse.quote(subject)
            body_encoded = urllib.parse.quote(body)
            mailto_url = f"mailto:{recipient_email}?subject={subject_encoded}&body={body_encoded}"
            
            subprocess.run(['open', mailto_url])
            subprocess.run(['open', 'reports/step1_chart.png'])
            print("Mail client opened - manually drag chart to attach")
            return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def send_via_web_service(recipient_email):
    """Try sending via a free web email service"""
    print(f"=== TRYING WEB SERVICE TO: {recipient_email} ===")
    
    date_range, summary_lines, total_posts = get_weekly_summary()
    subject = f"Weekly Reddit Competitor Sentiment Report — {date_range}"
    
    # Simple text email
    text_body = f"""Weekly Reddit Sentiment Report - {date_range}

{chr(10).join(summary_lines)}

Total posts: {total_posts}
Chart available at: reports/step1_chart.png

Sent from Reddit Sentiment Analysis System"""
    
    # Try EmailJS or similar service (requires setup)
    print("Web services require API keys")
    print("Using mailto instead for reliability...")
    
    return send_via_mailto(recipient_email)

def main():
    """Main function"""
    import sys
    
    # Use command line args or environment variable for recipients
    recipients = []
    if len(sys.argv) > 1:
        recipients = sys.argv[1:]
    else:
        # Default recipients per Brian's spec
        recipients_env = os.getenv('EMAIL_RECIPIENTS', '')
        if recipients_env:
            recipients = [r.strip() for r in recipients_env.split(',')]
        else:
            recipients = ['brian.leung@hellofresh.com', 'asaf@hellofresh.com']
    
    print("=== REDDIT SENTIMENT EMAIL SENDER ===")
    print(f"Recipients: {', '.join(recipients)}")
    print()
    
    # Send to each recipient
    for recipient in recipients:
        success = send_via_web_service(recipient)
        
        if success:
            print(f"\n[SUCCESS] EMAIL SENT to {recipient}")
        else:
            print(f"\n[ERROR] Email failed for {recipient}")

if __name__ == "__main__":
    main()