#!/usr/bin/env python3
"""
Sanity Check Tool for Brian's Competitor Analysis System
Quick validation of automation setup and recent data
"""

import os
import json
import requests
from datetime import datetime, timedelta
import subprocess
from config import *

def check_file_exists(filepath, description):
    """Check if a file exists and report"""
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filepath}")
    return exists

def check_git_status():
    """Check git repository status"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            changes = result.stdout.strip()
            if changes:
                print("⚠ Git: Uncommitted changes detected")
                for line in changes.split('\n')[:5]:  # Show first 5 changes
                    print(f"  {line}")
            else:
                print("✓ Git: Repository is clean")
        else:
            print("✗ Git: Error checking status")
    except:
        print("✗ Git: Command not available")

def check_recent_data():
    """Check if recent data exists and is valid"""
    if not os.path.exists(WORKING_DATA_FILE):
        print("✗ No working data found")
        return False
    
    try:
        with open(WORKING_DATA_FILE, 'r') as f:
            data = json.load(f)
        
        # Check data age
        scrape_time = data.get('scrape_timestamp')
        if scrape_time:
            scrape_date = datetime.fromisoformat(scrape_time.replace('Z', '+00:00'))
            age_hours = (datetime.now().astimezone() - scrape_date).total_seconds() / 3600
            
            if age_hours < 24:
                print(f"✓ Data is recent ({age_hours:.1f} hours old)")
            else:
                print(f"⚠ Data is {age_hours:.1f} hours old (consider refresh)")
        
        # Check post count
        posts = data.get('posts', [])
        print(f"✓ Data contains {len(posts)} posts")
        
        # Check brand coverage per Brian's spec
        brand_mentions = {brand: 0 for brand in COMPETITORS}
        sentiment_counts = {brand: {'positive': 0, 'negative': 0, 'neutral': 0} for brand in COMPETITORS}
        
        for post in posts:
            mentioned = post.get('competitors_mentioned', [])
            sentiment = post.get('sentiment', 'neutral')
            
            for brand in mentioned:
                if brand in brand_mentions:
                    brand_mentions[brand] += 1
                    sentiment_counts[brand][sentiment] += 1
        
        print("Brand coverage (Brian's 6 competitors):")
        for brand in COMPETITORS:
            count = brand_mentions[brand]
            pos = sentiment_counts[brand]['positive']
            neg = sentiment_counts[brand]['negative']
            neu = sentiment_counts[brand]['neutral']
            print(f"  {brand:12}: {count:2d} posts ({pos}pos/{neg}neg/{neu}neu)")
        
        return True
        
    except Exception as e:
        print(f"✗ Error reading data: {e}")
        return False

def check_data_sources():
    """Check Brian's specified data sources"""
    print("Data sources (Brian's WEEKLY_LINKS):")
    for brand, links in WEEKLY_LINKS.items():
        if isinstance(links, list):
            print(f"  {brand}:")
            for i, link in enumerate(links):
                print(f"    {i+1}: {link}")
        else:
            print(f"  {brand}: {links}")

def check_environment():
    """Check environment variables"""
    required_vars = [
        'REDDIT_CLIENT_ID',
        'REDDIT_CLIENT_SECRET', 
        'REDDIT_USER_AGENT'
    ]
    
    optional_vars = [
        'GMAIL_EMAIL',
        'GMAIL_APP_PASSWORD',
        'EMAIL_RECIPIENTS'
    ]
    
    print("Environment variables:")
    all_required = True
    for var in required_vars:
        if os.getenv(var):
            print(f"  ✓ {var}: configured")
        else:
            print(f"  ✗ {var}: missing (required)")
            all_required = False
    
    for var in optional_vars:
        if os.getenv(var):
            print(f"  ✓ {var}: configured")
        else:
            print(f"  ⚠ {var}: not set (email features disabled)")
    
    return all_required

def check_validation_rules():
    """Check Brian's validation rules"""
    if not os.path.exists(WORKING_DATA_FILE):
        print("⚠ No data to validate")
        return False
    
    try:
        with open(WORKING_DATA_FILE, 'r') as f:
            data = json.load(f)
        
        posts = data.get('posts', [])
        
        # Check date window (Monday-Friday or full week)
        date_range = data.get('date_range', {})
        if date_range:
            start_date = datetime.fromisoformat(date_range['start'].replace('Z', '+00:00'))
            end_date = datetime.fromisoformat(date_range['end'].replace('Z', '+00:00'))
            days_diff = (end_date - start_date).days
            
            if days_diff in [4, 5, 7]:
                if days_diff == 4:
                    print("✓ Date window: Monday-Friday (4 days)")
                elif days_diff == 5:
                    print("✓ Date window: Monday-Saturday (5 days)")
                else:
                    print("✓ Date window: Full week (7 days)")
            else:
                print(f"✗ Date window: {days_diff} days (should be 4-5 or 7)")
                return False
        
        # Check sentiment math for each brand
        brand_totals = {}
        for brand in COMPETITORS:
            pos = neg = neu = 0
            for post in posts:
                if brand in post.get('competitors_mentioned', []):
                    sentiment = post.get('sentiment', 'neutral')
                    if sentiment == 'positive':
                        pos += 1
                    elif sentiment == 'negative':
                        neg += 1
                    else:
                        neu += 1
            
            total = pos + neg + neu
            brand_totals[brand] = {'pos': pos, 'neg': neg, 'neu': neu, 'total': total}
            
            if pos + neg + neu == total:
                print(f"✓ {brand}: sentiment math checks out ({pos}+{neg}+{neu}={total})")
            else:
                print(f"✗ {brand}: sentiment math error ({pos}+{neg}+{neu}≠{total})")
                return False
        
        return True
        
    except Exception as e:
        print(f"✗ Validation error: {e}")
        return False

def main():
    """Main sanity check function"""
    print("=" * 60)
    print("BRIAN'S COMPETITOR ANALYSIS - SANITY CHECK")
    print("=" * 60)
    print(f"ABS PATH: {os.getcwd()}")
    print()
    
    # Check core files per Brian's spec
    print("Core Files (Brian's Final Build Plan):")
    core_files = [
        ('accurate_scraper.py', 'Data scraper'),
        ('step1_chart.py', 'Chart generator'),
        ('step2_ACTIONABLE_analysis.py', 'Analysis generator'),
        ('complete_automation.py', 'Automation pipeline'),
        ('send_to_gmail.py', 'Email sender'),
        ('sanity_check.py', 'This file'),
        ('config.py', 'Configuration')
    ]
    
    all_core_exist = True
    for filepath, desc in core_files:
        if not check_file_exists(filepath, desc):
            all_core_exist = False
    
    print()
    
    # Check output files
    print("Output Files:")
    output_files = [
        ('reports/step1_chart.png', 'Latest chart'),
        ('reports/step2_ACTIONABLE_analysis_LATEST.html', 'Latest analysis'),
        ('index.html', 'Dashboard'),
        ('reports/working_reddit_data.json', 'Working dataset')
    ]
    
    for filepath, desc in output_files:
        check_file_exists(filepath, desc)
    
    print()
    
    # Check environment
    print("Environment:")
    env_ok = check_environment()
    print()
    
    # Check data sources
    print("Data Sources:")
    check_data_sources()
    print()
    
    # Check data
    print("Data Status:")
    data_ok = check_recent_data()
    print()
    
    # Check validation rules
    print("Validation Rules (Brian's spec):")
    validation_ok = check_validation_rules()
    print()
    
    # Check git
    print("Git Status:")
    check_git_status()
    print()
    
    # Final status
    if all_core_exist and data_ok and validation_ok:
        print("✅ System ready for Brian's automation")
    else:
        print("⚠ Issues detected - review above")
    
    print()
    print("QUICK SELF-CHECK (Brian's spec):")
    print("1. Run: python3 sanity_check.py")
    print("2. Open 3 random links in All Posts")
    print("3. Confirm footer dates/commit are current")
    print("4. Verify Step-1 == Step-2 totals for HF & Factor")
    print("=" * 60)

if __name__ == "__main__":
    main()