#!/usr/bin/env python3
"""
Send Report via SMTP (for GitHub Actions / Linux)
Works on any platform that supports SMTP
"""

import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def send_email_smtp(recipients):
    """Send email via Gmail SMTP (works on Linux/GitHub Actions)"""
    
    # Convert single string to list
    if isinstance(recipients, str):
        recipients = [recipients]
    
    print(f"=== SENDING VIA SMTP TO: {', '.join(recipients)} ===")
    
    # Get credentials from environment
    gmail_email = os.getenv('GMAIL_EMAIL')
    gmail_password = os.getenv('GMAIL_APP_PASSWORD')
    
    if not gmail_email or not gmail_password:
        print("[ERROR] Missing GMAIL_EMAIL or GMAIL_APP_PASSWORD environment variables")
        return False
    
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
    
    # Build email body
    body = f"""Weekly Reddit Competitor Sentiment Report
============================================================

Analysis Period: {start_date} to {end_date}

QUICK SUMMARY:
------------------------------------------------------------
HelloFresh: {hf_total} posts ({hf_pct}% positive)
  • {hf_positive} positive, {hf_negative} negative, {hf_neutral} neutral

Factor75: {f75_total} posts ({f75_pct}% positive)
  • {f75_positive} positive, {f75_negative} negative, {f75_neutral} neutral

DASHBOARD ACCESS:
------------------------------------------------------------
Main Dashboard:
https://ktsering2025.github.io/reddit-competitor-sentiment/

Step 1 Chart (see attachment: step1_chart.pdf)
  • Or view online: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png

Step 2 Deep Dive (HelloFresh & Factor75):
https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html

Step 3 Competitor Analysis:
https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html

============================================================
Data refreshed weekly • Built for Brian's competitive intelligence"""
    
    # Send to each recipient
    success_count = 0
    for recipient in recipients:
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = gmail_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach body
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach PDF
            pdf_path = 'reports/step1_chart.pdf'
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as f:
                    part = MIMEBase('application', 'pdf')
                    part.set_payload(f.read())
                
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename=step1_chart.pdf')
                msg.attach(part)
            else:
                print(f"[WARNING] PDF not found: {pdf_path}")
            
            # Send via Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_email, gmail_password)
            server.send_message(msg)
            server.quit()
            
            print(f"[SUCCESS] Email sent to {recipient}")
            success_count += 1
            
        except Exception as e:
            print(f"[ERROR] Failed to send to {recipient}: {e}")
    
    return success_count == len(recipients)

def main():
    """Main function"""
    import sys
    
    # Use command line args or environment variable for recipients
    recipients = []
    if len(sys.argv) > 1:
        recipients = sys.argv[1:]
    else:
        # Default recipients
        recipients_env = os.getenv('EMAIL_RECIPIENTS', '')
        if recipients_env:
            recipients = [r.strip() for r in recipients_env.split(',')]
        else:
            recipients = ['brian.leung@hellofresh.com', 'assaf.ronen@hellofresh.com', 'kunsang.tsering@hellofresh.com']
    
    print("=== REDDIT SENTIMENT EMAIL SENDER (SMTP) ===")
    print(f"Recipients: {', '.join(recipients)}")
    print()
    
    success = send_email_smtp(recipients)
    
    if success:
        print(f"\n[SUCCESS] All emails sent!")
    else:
        print(f"\n[ERROR] Some emails failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
