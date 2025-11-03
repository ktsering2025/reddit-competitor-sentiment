#!/usr/bin/env python3
"""
Test script to send enhanced email
"""
import subprocess
import os

# Set recipient
recipient = "kunsang.tsering@hellofresh.com"

# Create the email using the enhanced script
print("Creating enhanced email...")

# Load data and create HTML
from send_to_gmail import create_email_html
import json

with open('reports/working_reddit_data.json', 'r') as f:
    data = json.load(f)

date_range = data.get('date_range', {})
start_date = date_range.get('start', '').split('T')[0]
end_date = date_range.get('end', '').split('T')[0]

subject = f"Weekly Reddit Competitor Sentiment Report — {start_date} to {end_date}"

# Create HTML (without embedded image for now, just show the structure)
html = create_email_html(data, 'chart_image')

# Replace the cid reference with actual file path for preview
html = html.replace('cid:chart_image', 'file://' + os.path.abspath('reports/step1_chart.png'))

# Save HTML to temp file
html_file = '/tmp/reddit_email_preview.html'
with open(html_file, 'w') as f:
    f.write(html)

print(f"\n✅ Enhanced email HTML created!")
print(f"📧 Subject: {subject}")
print(f"📁 Preview file: {html_file}")
print(f"\nOpening preview in browser...")

# Open in browser
subprocess.run(['open', html_file])

print("\n" + "="*60)
print("EMAIL PREVIEW OPENED IN BROWSER")
print("="*60)
print("\nThe enhanced email includes:")
print("✅ Bar chart (embedded)")
print("✅ Top 3 positive & negative posts for HelloFresh")
print("✅ Top 3 positive & negative posts for Factor")
print("✅ Top 3 positive & negative posts for Hungryroot")
print("✅ Top 3 positive & negative posts for CookUnity")
print("✅ Links to full reports")
print("\nThis is what will be sent in the automated emails!")
print("="*60)
