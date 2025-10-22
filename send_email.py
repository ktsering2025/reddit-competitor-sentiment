#!/usr/bin/env python3
"""
Simple email sender - creates email and opens it
"""

import subprocess
import sys
import os

def send_email_simple():
    print("📧 HELLOFRESH REDDIT REPORT SENDER")
    print("=" * 35)
    
    email_file = "hellofresh_report_20251022.eml"
    
    if not os.path.exists(email_file):
        print(f"❌ Email file not found: {email_file}")
        print("Run: python3 email_generator.py first")
        return
    
    print(f"📧 Opening email file: {email_file}")
    print("📎 Chart attachment included")
    print()
    
    try:
        # Method 1: Try default open
        result = subprocess.run(['open', email_file], capture_output=True)
        if result.returncode == 0:
            print("✅ Email opened successfully!")
            print("📧 Check your Mail app - email should be ready to send")
            return
        
        # Method 2: Try with Mail app specifically
        result = subprocess.run(['open', '-a', 'Mail', email_file], capture_output=True)
        if result.returncode == 0:
            print("✅ Email opened in Mail app!")
            print("📧 Email should be ready to send to you and Brian")
            return
            
        # Method 3: Try with Gmail in browser
        print("⚠️ Mail app didn't work, trying browser method...")
        print("📧 Copy the email content and paste in Gmail:")
        
        with open(email_file, 'r') as f:
            content = f.read()
            
        # Extract key parts for manual sending
        subject_line = "HelloFresh Reddit Sentiment Report"
        recipients = "kunsang.tsering@hellofresh.com, brian.leung@hellofresh.com"
        
        print(f"To: {recipients}")
        print(f"Subject: {subject_line}")
        print("Attachment: reports/step1_chart.png")
        print()
        print("Email body:")
        print("HelloFresh Reddit Sentiment Report — 2024-Present")
        print("• HelloFresh (HF): 184 posts (73% positive)")
        print("• Factor (HF): 126 posts (52% positive)")
        print("• EveryPlate (HF): 146 posts (41% positive)")
        print("• Green Chef (HF): 74 posts (57% positive)")
        print()
        print("Each count = unique Reddit post (not comments or reposts)")
        print("Visual Chart: See attached step1_chart.png")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("📧 Manual method: Open Gmail and attach reports/step1_chart.png")

if __name__ == "__main__":
    send_email_simple()
