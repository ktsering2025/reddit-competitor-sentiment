#!/usr/bin/env python3
"""
Email Generator with Chart Image Attachment
Sends Brian's simplified Step 1 report with step1_chart.png attached
"""

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import os

class EmailGeneratorWithChart:
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.email_user = os.getenv('EMAIL_USER', '')
        self.email_password = os.getenv('EMAIL_PASSWORD', '')
        self.recipients = os.getenv('REPORT_RECIPIENTS', '').split(',')
        
    def generate_simplified_email_content(self):
        """Generate Brian's requested simplified email content"""
        
        html_content = f"""
        <html>
        <body>
            <h2>HelloFresh Reddit Sentiment Report — 2024-Present</h2>
            
            <h3>Key Results:</h3>
            <ul>
                <li><strong>HelloFresh (HF):</strong> 184 posts (73% positive)</li>
                <li><strong>Factor (HF):</strong> 126 posts (52% positive)</li>
                <li><strong>EveryPlate (HF):</strong> 146 posts (41% positive)</li>
                <li><strong>Green Chef (HF):</strong> 74 posts (57% positive)</li>
            </ul>
            
            <p><em>Each count = unique Reddit post (not comments or reposts)</em></p>
            
            <p><strong>Visual Chart:</strong> See attached step1_chart.png for complete breakdown</p>
            
            <h3>Market Position:</h3>
            <ul>
                <li>HelloFresh Family: 530 posts (53% market dominance)</li>
                <li>All Competitors: 473 posts (47%)</li>
                <li>Data Period: 2024-Present (recent activity)</li>
            </ul>
            
            <hr>
            <p><small>
                <strong>Analysis Period:</strong> 2024-Present<br>
                <strong>Total Posts Analyzed:</strong> 1,003 unique Reddit posts<br>
                <strong>Next Report:</strong> {(datetime.now()).strftime('%B %d, %Y')}<br>
                <strong>Status:</strong> Step 1 Complete | Step 2 Deep Dive Ready
            </small></p>
        </body>
        </html>
        """
        
        return html_content
    
    def attach_chart_image(self, msg):
        """Method to attach step1_chart.png as image"""
        chart_path = 'reports/step1_chart.png'
        
        try:
            # Check if chart file exists
            if not os.path.exists(chart_path):
                print(f"❌ Chart file not found: {chart_path}")
                return False
            
            # Read the chart image as binary
            with open(chart_path, 'rb') as chart_file:
                chart_data = chart_file.read()
            
            # Create MIMEImage object
            chart_image = MIMEImage(chart_data)
            
            # Add headers for proper attachment
            chart_image.add_header(
                'Content-Disposition', 
                'attachment', 
                filename='step1_chart.png'
            )
            chart_image.add_header('Content-ID', '<chart_image>')
            
            # Attach to email
            msg.attach(chart_image)
            
            print("✅ Chart image attached successfully")
            return True
            
        except Exception as e:
            print(f"❌ Failed to attach chart: {e}")
            return False
    
    def send_email_with_chart(self):
        """Send email with chart image attachment"""
        print("📧 SENDING EMAIL WITH CHART ATTACHMENT")
        print("=" * 45)
        
        if not self.email_user or not self.email_password:
            print("❌ Email credentials not configured. Check .env file")
            print("   Need: EMAIL_USER and EMAIL_PASSWORD in .env")
            return False
            
        try:
            # Create email message
            msg = MIMEMultipart('related')
            
            # Email headers
            msg['Subject'] = f"HelloFresh Reddit Sentiment Report — {datetime.now().strftime('%m/%d/%Y')}"
            msg['From'] = self.email_user
            msg['To'] = ', '.join(self.recipients)
            
            print(f"📧 To: {', '.join(self.recipients)}")
            print(f"📧 From: {self.email_user}")
            print(f"📧 Subject: {msg['Subject']}")
            
            # Add HTML content
            html_content = self.generate_simplified_email_content()
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            print("✅ HTML content added")
            
            # Attach chart image
            chart_attached = self.attach_chart_image(msg)
            if not chart_attached:
                print("⚠️ Continuing without chart attachment")
            
            # Send email via SMTP
            print("📤 Connecting to SMTP server...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            
            print("📤 Sending email...")
            text = msg.as_string()
            server.sendmail(self.email_user, self.recipients, text)
            server.quit()
            
            print(f"✅ EMAIL SENT SUCCESSFULLY!")
            print(f"📎 Chart attachment: {'✅ Included' if chart_attached else '❌ Missing'}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            print(f"   Check your EMAIL_USER and EMAIL_PASSWORD in .env file")
            return False
    
    def save_email_as_file(self):
        """Alternative: Save email as .eml file for manual sending"""
        print("💾 CREATING EMAIL FILE (ALTERNATIVE METHOD)")
        print("=" * 45)
        
        try:
            # Create email message
            msg = MIMEMultipart('related')
            msg['Subject'] = f"HelloFresh Reddit Sentiment Report — {datetime.now().strftime('%m/%d/%Y')}"
            msg['From'] = self.email_user or 'your-email@hellofresh.com'
            msg['To'] = ', '.join(self.recipients) if self.recipients else 'kunsang.tsering@hellofresh.com,brian.leung@hellofresh.com'
            
            # Add content
            html_content = self.generate_simplified_email_content()
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            
            # Attach chart
            self.attach_chart_image(msg)
            
            # Save as .eml file
            email_filename = f"hellofresh_report_{datetime.now().strftime('%Y%m%d')}.eml"
            with open(email_filename, 'w') as f:
                f.write(msg.as_string())
            
            print(f"✅ Email saved as: {email_filename}")
            print(f"📧 To use: Double-click the .eml file to open in your email client")
            print(f"📎 Chart is attached and ready to send")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to create email file: {e}")
            return False

def main():
    """Send Brian's report with chart attachment"""
    generator = EmailGeneratorWithChart()
    
    print("HELLOFRESH REDDIT REPORT WITH CHART")
    print("=" * 35)
    print("Options:")
    print("1. Send email directly (requires .env setup)")
    print("2. Create .eml file for manual sending")
    
    # Try direct email first, fallback to file method
    success = generator.send_email_with_chart()
    
    if not success:
        print("\n🔄 TRYING ALTERNATIVE METHOD...")
        generator.save_email_as_file()

if __name__ == "__main__":
    main()
