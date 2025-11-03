#!/usr/bin/env python3
"""
Send Report to Gmail Inbox - NO PASSWORDS NEEDED
Uses Mail.app on Mac to send enhanced HTML emails
Enhanced with embedded chart and top posts per Assaf's feedback
"""

import requests
import json
import base64
import subprocess
import os
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import tempfile

def calculate_engagement_score(post):
    """Calculate engagement score: score + 3×comments"""
    score = max(0, post.get('score', 0))
    comments = post.get('num_comments', 0)
    return score + (3 * comments)

def get_top_posts_for_brand(posts, brand, sentiment, limit=3):
    """Get top posts for a specific brand and sentiment"""
    brand_posts = [p for p in posts if brand in p.get('competitors_mentioned', []) 
                   and p.get('sentiment') == sentiment]
    
    # Add engagement scores
    for post in brand_posts:
        post['engagement_score'] = calculate_engagement_score(post)
    
    # Sort by engagement
    sorted_posts = sorted(brand_posts, key=lambda x: x['engagement_score'], reverse=True)
    return sorted_posts[:limit]

def format_post_for_email(post, index):
    """Format a single post for email display"""
    title = post.get('title', 'No title')
    url = post.get('url', '#')
    score = post.get('score', 0)
    comments = post.get('num_comments', 0)
    subreddit = post.get('subreddit', 'unknown')
    sentiment = post.get('sentiment', 'neutral')
    
    # Truncate title if too long
    if len(title) > 80:
        title = title[:77] + '...'
    
    # Sentiment indicator (only ✅ and ❌)
    sentiment_indicator = {
        'positive': '✅',
        'negative': '❌',
        'neutral': ''
    }
    indicator = sentiment_indicator.get(sentiment, '')
    
    return f"""
    <div style="margin: 10px 0; padding: 12px; background-color: #f8f9fa; border-left: 4px solid {'#22c55e' if sentiment == 'positive' else '#ef4444' if sentiment == 'negative' else '#64748b'}; border-radius: 4px;">
        <div style="font-weight: bold; margin-bottom: 5px;">
            {indicator} {index}. <a href="{url}" style="color: #1a73e8; text-decoration: none;">{title}</a>
        </div>
        <div style="font-size: 12px; color: #666;">
            r/{subreddit} | {score} upvotes | {comments} comments
        </div>
    </div>
    """

def create_email_html(data, chart_cid):
    """Create HTML email body with embedded chart and top posts"""
    
    posts = data.get('posts', [])
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '').split('T')[0]
    end_date = date_range.get('end', '').split('T')[0]
    
    # Calculate summary stats
    hf_posts = [p for p in posts if p.get('primary_brand') == 'HelloFresh']
    f75_posts = [p for p in posts if p.get('primary_brand') == 'Factor75']
    hr_posts = [p for p in posts if 'Hungryroot' in p.get('competitors_mentioned', [])]
    cu_posts = [p for p in posts if 'CookUnity' in p.get('competitors_mentioned', [])]
    
    def calc_stats(brand_posts):
        positive = len([p for p in brand_posts if p['sentiment'] == 'positive'])
        negative = len([p for p in brand_posts if p['sentiment'] == 'negative'])
        neutral = len([p for p in brand_posts if p['sentiment'] == 'neutral'])
        total = len(brand_posts)
        pct = int((positive / total * 100)) if total > 0 else 0
        return positive, negative, neutral, total, pct
    
    hf_pos, hf_neg, hf_neu, hf_total, hf_pct = calc_stats(hf_posts)
    f75_pos, f75_neg, f75_neu, f75_total, f75_pct = calc_stats(f75_posts)
    hr_pos, hr_neg, hr_neu, hr_total, hr_pct = calc_stats(hr_posts)
    cu_pos, cu_neg, cu_neu, cu_total, cu_pct = calc_stats(cu_posts)
    
    # Get top posts
    hf_top_positive = get_top_posts_for_brand(posts, 'HelloFresh', 'positive', 3)
    hf_top_negative = get_top_posts_for_brand(posts, 'HelloFresh', 'negative', 3)
    f75_top_positive = get_top_posts_for_brand(posts, 'Factor75', 'positive', 3)
    f75_top_negative = get_top_posts_for_brand(posts, 'Factor75', 'negative', 3)
    hr_top_positive = get_top_posts_for_brand(posts, 'Hungryroot', 'positive', 3)
    hr_top_negative = get_top_posts_for_brand(posts, 'Hungryroot', 'negative', 3)
    cu_top_positive = get_top_posts_for_brand(posts, 'CookUnity', 'positive', 3)
    cu_top_negative = get_top_posts_for_brand(posts, 'CookUnity', 'negative', 3)
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 0; background-color: #f5f5f5;">
    <div style="max-width: 800px; margin: 0 auto; background-color: #ffffff;">
        
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #86efac 0%, #4ade80 100%); color: white; padding: 30px; text-align: center;">
            <h1 style="margin: 0; font-size: 24px;">Weekly Reddit Competitor Sentiment Report</h1>
            <p style="margin: 10px 0 0 0; font-size: 14px; opacity: 0.9;">Analysis Period: {start_date} to {end_date}</p>
        </div>
        
        <!-- Quick Summary -->
        <div style="padding: 25px; background-color: #f0fdf4; border-bottom: 2px solid #86efac;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #166534;">Quick Summary</h2>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #22c55e;">
                    <div style="font-weight: bold; color: #166534;">HelloFresh</div>
                    <div style="font-size: 24px; font-weight: bold; margin: 5px 0;">{hf_total} posts ({hf_pct}% positive)</div>
                    <div style="font-size: 12px; color: #666;">{hf_pos} positive | {hf_neg} negative | {hf_neu} neutral</div>
                </div>
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                    <div style="font-weight: bold; color: #1e40af;">Factor</div>
                    <div style="font-size: 24px; font-weight: bold; margin: 5px 0;">{f75_total} posts ({f75_pct}% positive)</div>
                    <div style="font-size: 12px; color: #666;">{f75_pos} positive | {f75_neg} negative | {f75_neu} neutral</div>
                </div>
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                    <div style="font-weight: bold; color: #92400e;">Hungryroot</div>
                    <div style="font-size: 24px; font-weight: bold; margin: 5px 0;">{hr_total} posts ({hr_pct}% positive)</div>
                    <div style="font-size: 12px; color: #666;">{hr_pos} positive | {hr_neg} negative | {hr_neu} neutral</div>
                </div>
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #8b5cf6;">
                    <div style="font-weight: bold; color: #5b21b6;">CookUnity</div>
                    <div style="font-size: 24px; font-weight: bold; margin: 5px 0;">{cu_total} posts ({cu_pct}% positive)</div>
                    <div style="font-size: 12px; color: #666;">{cu_pos} positive | {cu_neg} negative | {cu_neu} neutral</div>
                </div>
            </div>
        </div>
        
        <!-- Embedded Chart -->
        <div style="padding: 25px; background-color: white;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #166534;">Sentiment Overview</h2>
            <div style="text-align: center;">
                <img src="cid:{chart_cid}" alt="Sentiment Chart" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            </div>
        </div>
        
        <!-- HelloFresh Top Posts -->
        <div style="padding: 25px; background-color: #f0fdf4; border-top: 2px solid #86efac;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #166534;">HelloFresh - Top Posts</h2>
            
            <h3 style="margin: 15px 0 10px 0; font-size: 14px; color: #22c55e; text-transform: uppercase;">✅ Top Positive</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(hf_top_positive)]) if hf_top_positive else '<p style="color: #666; font-style: italic;">No positive posts this week</p>'}
            
            <h3 style="margin: 20px 0 10px 0; font-size: 14px; color: #ef4444; text-transform: uppercase;">❌ Top Negative</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(hf_top_negative)]) if hf_top_negative else '<p style="color: #666; font-style: italic;">No negative posts this week</p>'}
        </div>
        
        <!-- Factor Top Posts -->
        <div style="padding: 25px; background-color: white;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #1e40af;">Factor - Top Posts</h2>
            
            <h3 style="margin: 15px 0 10px 0; font-size: 14px; color: #22c55e; text-transform: uppercase;">✅ Top Positive</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(f75_top_positive)]) if f75_top_positive else '<p style="color: #666; font-style: italic;">No positive posts this week</p>'}
            
            <h3 style="margin: 20px 0 10px 0; font-size: 14px; color: #ef4444; text-transform: uppercase;">❌ Top Negative</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(f75_top_negative)]) if f75_top_negative else '<p style="color: #666; font-style: italic;">No negative posts this week</p>'}
        </div>
        
        <!-- Hungryroot Top Posts -->
        <div style="padding: 25px; background-color: #fef3c7; border-top: 2px solid #f59e0b;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #92400e;">Hungryroot - Top Posts</h2>
            
            <h3 style="margin: 15px 0 10px 0; font-size: 14px; color: #22c55e; text-transform: uppercase;">✅ Top Positive</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(hr_top_positive)]) if hr_top_positive else '<p style="color: #666; font-style: italic;">No positive posts this week</p>'}
            
            <h3 style="margin: 20px 0 10px 0; font-size: 14px; color: #ef4444; text-transform: uppercase;">❌ Top Negative</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(hr_top_negative)]) if hr_top_negative else '<p style="color: #666; font-style: italic;">No negative posts this week</p>'}
        </div>
        
        <!-- CookUnity Top Posts -->
        <div style="padding: 25px; background-color: white;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #5b21b6;">CookUnity - Top Posts</h2>
            
            <h3 style="margin: 15px 0 10px 0; font-size: 14px; color: #22c55e; text-transform: uppercase;">✅ Top Positive</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(cu_top_positive)]) if cu_top_positive else '<p style="color: #666; font-style: italic;">No positive posts this week</p>'}
            
            <h3 style="margin: 20px 0 10px 0; font-size: 14px; color: #ef4444; text-transform: uppercase;">❌ Top Negative</h3>
            {''.join([format_post_for_email(post, i+1) for i, post in enumerate(cu_top_negative)]) if cu_top_negative else '<p style="color: #666; font-style: italic;">No negative posts this week</p>'}
        </div>
        
        <!-- Links to Full Reports -->
        <div style="padding: 25px; background-color: #f0fdf4; border-top: 2px solid #86efac;">
            <h2 style="margin: 0 0 15px 0; font-size: 18px; color: #166534;">Full Reports & Dashboards</h2>
            <div style="background-color: white; padding: 15px; border-radius: 8px;">
                <p style="margin: 5px 0;"><strong>Main Dashboard:</strong><br>
                <a href="https://ktsering2025.github.io/reddit-competitor-sentiment/" style="color: #1a73e8;">https://ktsering2025.github.io/reddit-competitor-sentiment/</a></p>
                
                <p style="margin: 15px 0 5px 0;"><strong>Deep Dive (HelloFresh & Factor):</strong><br>
                <a href="https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html" style="color: #1a73e8;">View Detailed Analysis</a></p>
                
                <p style="margin: 15px 0 5px 0;"><strong>All Competitors Analysis:</strong><br>
                <a href="https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html" style="color: #1a73e8;">View Full Competitor Report</a></p>
            </div>
        </div>
        
        <!-- Footer -->
        <div style="padding: 20px; text-align: center; background-color: #f5f5f5; color: #666; font-size: 12px;">
            <p style="margin: 5px 0;">Data refreshed weekly - Built for competitive intelligence</p>
        </div>
        
    </div>
</body>
</html>
    """
    
    return html

def send_via_mailto(recipient_email):
    """Send enhanced HTML email using Mail.app via AppleScript"""
    print(f"=== SENDING TO: {recipient_email} ===")
    
    # Load data
    with open('reports/working_reddit_data.json', 'r') as f:
        data = json.load(f)
    
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '').split('T')[0]
    end_date = date_range.get('end', '').split('T')[0]
    
    subject = f"Weekly Reddit Competitor Sentiment Report — {start_date} to {end_date}"
    
    # Create MIME message with HTML
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['To'] = recipient_email
    
    # Create HTML body with embedded chart
    chart_cid = 'chart_image'
    html_body = create_email_html(data, chart_cid)
    
    # Attach HTML
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(html_body, 'html'))
    
    # Embed chart image (inline only, no PDF attachment)
    chart_path = 'reports/step1_chart.png'
    if os.path.exists(chart_path):
        with open(chart_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', f'<{chart_cid}>')
            img.add_header('Content-Disposition', 'inline', filename='chart.png')
            msg.attach(img)
    
    # Save as .eml file and open with Mail.app
    with tempfile.NamedTemporaryFile(mode='w', suffix='.eml', delete=False) as tmp:
        tmp.write(msg.as_string())
        eml_path = tmp.name
    
    # Use AppleScript to open and send the email
    applescript = f'''
    tell application "Mail"
        set theMessage to open POSIX file "{eml_path}"
        send theMessage
    end tell
    '''
    
    try:
        subprocess.run(['osascript', '-e', applescript], check=True)
        os.unlink(eml_path)
        print(f"[SUCCESS] Email sent to {recipient_email}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        if os.path.exists(eml_path):
            os.unlink(eml_path)
        return False

def send_via_web_service(recipient_email):
    """Send email via Mail.app"""
    print(f"=== SENDING EMAIL TO: {recipient_email} ===")
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
            recipients = ['brian.leung@hellofresh.com', 'assaf.ronen@hellofresh.com', 'kunsang.tsering@hellofresh.com']
    
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
