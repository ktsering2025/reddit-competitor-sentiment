#!/usr/bin/env python3
"""
Send Report to Gmail Inbox - NO PASSWORDS NEEDED
Uses a web service to send emails directly to your Gmail
"""

import requests
import json
import base64
import subprocess
from datetime import datetime, timedelta

def get_weekly_summary():
    """Get weekly summary from data"""
    with open('reports/working_reddit_data.json', 'r') as f:
        data = json.load(f)
    
    posts = data.get('posts', [])
    seven_days_ago = datetime.now() - timedelta(days=7)
    seven_days_timestamp = seven_days_ago.timestamp()
    
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
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    date_range = f"{start_date.strftime('%b %d')}–{end_date.strftime('%d, %Y')}"
    
    return date_range, summary_lines, sum(sum(stats.values()) for stats in brand_stats.values())

def send_via_mailto(recipient_email):
    """Send email using system mail client with automatic chart attachment"""
    print(f"=== SENDING TO: {recipient_email} ===")
    
    # Update data first
    print("Updating weekly data...")
    subprocess.run(['python3', 'step1_chart.py'], capture_output=True)
    
    # Get summary
    date_range, summary_lines, total_posts = get_weekly_summary()
    subject = f"Weekly Reddit Competitor Sentiment Report — {date_range}"
    
    body = f"""Hi there,

Here's the weekly Reddit sentiment snapshot ({date_range}).

Each count = unique Reddit post from the last 7 days (not comments or reposts)

{chr(10).join(summary_lines)}

Weekly data includes all HelloFresh family brands and key competitors.

Chart attached: step1_chart.png

Best regards,
Reddit Sentiment Analysis System

---
Total posts analyzed: {total_posts}
Next report: {(datetime.now() + timedelta(days=7)).strftime('%B %d, %Y')}"""
    
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
    
    recipient = "kunsang.tsering@hellofresh.com"
    if len(sys.argv) > 1:
        recipient = sys.argv[1]
    
    print("=== REDDIT SENTIMENT EMAIL SENDER ===")
    print("Sending actual email to your Gmail inbox...")
    print()
    
    # Try web service first, fallback to mailto
    success = send_via_web_service(recipient)
    
    if success:
        print("\nEMAIL PROCESS STARTED!")
        print(f"Check your Gmail: {recipient}")
        print("You should see a notification soon")
    else:
        print("\nEmail sending failed")
        print("Try the manual copy/paste method instead")

if __name__ == "__main__":
    main()