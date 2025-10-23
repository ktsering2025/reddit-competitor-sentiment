#!/usr/bin/env python3
"""
Weekly Report Generator for Brian
Generates Step 1 chart + Step 2 analysis + sends email
"""

import subprocess
import os
from datetime import datetime

def run_weekly_report():
    """Generate complete weekly report for Brian"""
    print("🚀 GENERATING WEEKLY REPORT FOR BRIAN")
    print("=" * 50)
    
    # Step 1: Generate Step 1 chart
    print("\n[1/3] Generating Step 1 chart...")
    result1 = subprocess.run(['python3', 'step1_chart.py'], capture_output=True, text=True)
    if result1.returncode == 0:
        print("✅ Step 1 chart generated successfully")
    else:
        print(f"❌ Step 1 chart failed: {result1.stderr}")
        return False
    
    # Step 2: Generate Step 2 deep dive analysis
    print("\n[2/3] Generating Step 2 deep dive analysis...")
    result2 = subprocess.run(['python3', 'step2_comprehensive_analysis.py'], capture_output=True, text=True)
    if result2.returncode == 0:
        print("✅ Step 2 analysis generated successfully")
        # Extract the generated filename from output
        output_lines = result2.stdout.split('\n')
        html_file = None
        for line in output_lines:
            if 'Report saved:' in line:
                html_file = line.split('reports/')[-1]
                break
        
        if html_file:
            print(f"📊 Step 2 analysis: reports/{html_file}")
        else:
            print("⚠️ Could not determine Step 2 filename")
    else:
        print(f"❌ Step 2 analysis failed: {result2.stderr}")
        return False
    
    # Step 3: Send email report
    print("\n[3/3] Sending email report...")
    result3 = subprocess.run(['python3', 'send_to_gmail.py'], capture_output=True, text=True)
    if result3.returncode == 0:
        print("✅ Email sent successfully")
    else:
        print(f"❌ Email failed: {result3.stderr}")
        return False
    
    print("\n🎉 WEEKLY REPORT COMPLETE!")
    print("=" * 50)
    print("📊 Step 1: Competitor sentiment chart")
    print("🎯 Step 2: HelloFresh & Factor deep dive")
    print("📧 Email: Sent to Brian's inbox")
    
    if html_file:
        print(f"\n🔗 Direct link for Brian:")
        print(f"https://ktsering2025.github.io/reddit-competitor-sentiment/reports/{html_file}")
    
    return True

if __name__ == "__main__":
    success = run_weekly_report()
    if success:
        print("\n✅ All systems working - Brian's weekly intelligence ready!")
    else:
        print("\n❌ Some issues occurred - check the logs above")
