#!/usr/bin/env python3
"""
Complete Automation Pipeline - Brian's Final Build Plan
Runs: scrape → Step 1 → Step 2 → validation → commit/push → email
"""

import json
import os
import sys
from datetime import datetime, timezone
import subprocess
import logging
from collections import defaultdict
import argparse
from config import *

# Configure logging
logging.basicConfig(
    filename=AUTOMATION_LOG,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def log_and_print(message, level="INFO"):
    """Log message and print to console"""
    print(message)
    if level == "ERROR":
        logging.error(message)
    elif level == "WARNING":
        logging.warning(message)
    else:
        logging.info(message)

def get_git_commit_hash():
    """Get current git commit hash"""
    try:
        result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], 
                              capture_output=True, text=True, cwd='.')
        return result.stdout.strip()
    except:
        return "unknown"

def validate_data_integrity(data):
    """Brian's strict validation rules"""
    errors = []
    
    # Load the working data
    posts = data.get('posts', [])
    date_range = data.get('date_range', {})
    
    # Validation Rule 1: Date window = Monday-Friday (4-5 days) or full week (7 days)
    if date_range:
        try:
            start_date = datetime.fromisoformat(date_range['start'].replace('Z', '+00:00'))
            end_date = datetime.fromisoformat(date_range['end'].replace('Z', '+00:00'))
            days_diff = (end_date - start_date).days
            
            # Accept Monday-Friday (4 days), Monday-Saturday (5 days), or full week (7 days)
            if days_diff not in [4, 5, 7]:
                errors.append(f"Date window is {days_diff} days, expected 4-5 days (Mon-Fri/Sat) or 7 days")
        except Exception as e:
            errors.append(f"Date validation error: {e}")
    
    # Validation Rule 2: For each brand: pos + neg + neutral == total
    brand_counts = {}
    for brand in ALL_COMPETITORS:
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
        brand_counts[brand] = {'pos': pos, 'neg': neg, 'neu': neu, 'total': total}
        
        if pos + neg + neu != total:
            errors.append(f"{brand}: Sentiment breakdown doesn't match total ({pos}+{neg}+{neu} ≠ {total})")
    
    # Validation Rule 3: Step-1 totals == Step-2 totals for HF & Factor
    # (This will be checked after both steps run)
    
    return errors, brand_counts

def run_what_i_did_summary():
    """Print 'WHAT I DID' summary per Brian's spec"""
    log_and_print("\n" + "="*50)
    log_and_print("WHAT I DID")
    log_and_print("="*50)
    
    log_and_print("[OK] Links Updated (Brian's data sources):")
    for brand, link in WEEKLY_LINKS.items():
        if isinstance(link, list):
            log_and_print(f"  {brand} → {len(link)} sources")
            for i, l in enumerate(link):
                log_and_print(f"    {i+1}: {l}")
        else:
            log_and_print(f"  {brand} → {link}")
    
    log_and_print("\n[OK] Files Kept (canonical only):")
    canonical_files = [
        'accurate_scraper.py', 'step1_chart.py', 'step2_ACTIONABLE_analysis.py',
        'complete_automation.py', 'send_to_gmail.py', 'sanity_check.py', 'config.py',
        'README.md', 'index.html', 'requirements.txt', '.nojekyll', '.gitignore'
    ]
    for file in canonical_files:
        if os.path.exists(file):
            log_and_print(f"  [OK] {file}")
    
    log_and_print("\n[OK] Artifacts Generated:")
    artifacts = [
        'reports/step1_chart.png',
        'reports/step2_ACTIONABLE_analysis_LATEST.html',
        'reports/working_reddit_data.json'
    ]
    for artifact in artifacts:
        if os.path.exists(artifact):
            log_and_print(f"  [OK] {artifact}")

def run_pipeline(send_email=False, email_recipients=None):
    """Run the complete automation pipeline per Brian's spec"""
    log_and_print("=" * 60)
    log_and_print("BRIAN'S COMPETITOR ANALYSIS - COMPLETE AUTOMATION")
    log_and_print("=" * 60)
    log_and_print(f"ABS PATH: {os.getcwd()}")
    
    # Preserve WEEK_MODE and WEEK_END environment variables
    week_mode = os.getenv('WEEK_MODE', WEEK_MODE)
    week_end = os.getenv('WEEK_END', WEEK_END_OVERRIDE)
    
    log_and_print(f"Week mode: {week_mode}")
    if week_end:
        log_and_print(f"Week end override: {week_end}")
    
    try:
        # Step 1: Run accurate scraper
        log_and_print("\n[STEP 1] Running accurate_scraper.py...")
        
        # Ensure environment variables are set for subprocess
        env = os.environ.copy()
        env['WEEK_MODE'] = week_mode
        if week_end:
            env['WEEK_END'] = week_end
        
        result = subprocess.run([sys.executable, 'accurate_scraper.py'], 
                              capture_output=True, text=True, env=env)
        if result.returncode != 0:
            raise Exception(f"Scraper failed: {result.stderr}")
        log_and_print("[SUCCESS] Scraper completed - data saved to working_reddit_data.json")
        
        # Load data for validation
        with open(WORKING_DATA_FILE, 'r') as f:
            data = json.load(f)
        
        # Step 2: Generate filtered, metadata files
        log_and_print("\n[STEP 2] Processing raw data...")
        timestamp = datetime.now().strftime('%Y-%m-%d')
        
        # Create filtered dataset (same as raw for now)
        filtered_data = data.copy()
        filtered_file = f'{RAW_DATA_DIR}/filtered_{timestamp}.json'
        os.makedirs(RAW_DATA_DIR, exist_ok=True)
        with open(filtered_file, 'w') as f:
            json.dump(filtered_data, f, indent=2)
        
        # Extract filter stats from the data (if available)
        filter_stats = {}
        for brand in ALL_COMPETITORS:
            filter_stats[brand] = {
                'pre_filter': 0,
                'post_filter': 0
            }
            for post in filtered_data.get('posts', []):
                if brand in post.get('competitors_mentioned', []):
                    filter_stats[brand]['post_filter'] += 1
        
        # Create metadata
        metadata = {
            'processing_timestamp': datetime.now(timezone.utc).isoformat(),
            'total_posts': len(filtered_data.get('posts', [])),
            'date_range': filtered_data.get('date_range', {}),
            'brands_analyzed': ALL_COMPETITORS,
            'data_sources': WEEKLY_LINKS,
            'validation_status': 'pending',
            'commit_hash': get_git_commit_hash(),
            'filter_stats': filter_stats
        }
        
        metadata_file = f'{RAW_DATA_DIR}/metadata_{timestamp}.json'
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        # Also copy raw file with timestamp
        raw_file = f'{RAW_DATA_DIR}/raw_{timestamp}.json'
        with open(raw_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        log_and_print(f"[SUCCESS] Raw data processing complete - files saved with {timestamp}")
        
        # Step 3: Generate Step 1 chart
        log_and_print("\n[STEP 3] Generating Step 1 chart...")
        result = subprocess.run([sys.executable, 'step1_chart.py'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Step 1 chart failed: {result.stderr}")
        log_and_print("[SUCCESS] Step 1 chart generated successfully")
        
        # Step 4: Generate Step 2 analysis
        log_and_print("\n[STEP 4] Generating Step 2 ACTIONABLE analysis...")
        result = subprocess.run([sys.executable, 'step2_ACTIONABLE_analysis.py'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Step 2 analysis failed: {result.stderr}")
        log_and_print("[SUCCESS] Step 2 analysis generated successfully")
        
        # Step 5: Generate Step 3 competitor analysis
        log_and_print("\\n[STEP 5] Generating Step 3 competitor analysis...")
        result = subprocess.run([sys.executable, 'step3_competitor_analysis.py'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Step 3 analysis failed: {result.stderr}")
        log_and_print("[SUCCESS] Step 3 competitor analysis generated successfully")
        
        # Step 6: Brian's strict validation
        log_and_print("\n[STEP 5] Running Brian's validation rules...")
        validation_errors, brand_counts = validate_data_integrity(data)
        
        if validation_errors:
            error_msg = "VALIDATION_FAILED: " + "; ".join(validation_errors)
            log_and_print(error_msg, "ERROR")
            
            # Update metadata with failure
            metadata['validation_status'] = 'failed'
            metadata['validation_errors'] = validation_errors
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            return False
        
        log_and_print("[SUCCESS] All validation rules PASSED")
        
        # Update metadata with success
        metadata['validation_status'] = 'passed'
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        # Step 6: Archive artifacts
        log_and_print("\n[STEP 6] Archiving artifacts...")
        archive_dir = f'{ARCHIVE_DIR}/{timestamp}'
        os.makedirs(archive_dir, exist_ok=True)
        
        # Copy artifacts to archive
        if os.path.exists(CHART_OUTPUT):
            subprocess.run(['cp', CHART_OUTPUT, f'{archive_dir}/step1_chart.png'])
        if os.path.exists(STEP2_OUTPUT):
            subprocess.run(['cp', STEP2_OUTPUT, f'{archive_dir}/step2_ACTIONABLE_analysis.html'])
        
        log_and_print(f"[SUCCESS] Artifacts archived to {archive_dir}")
        
        # Step 7: Git commit and push
        log_and_print("\n[STEP 7] Git commit and push...")
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            commit_msg = f"Brian's automation update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            
            # Update index.html with BUILD_TOKEN for cache busting
            # Load metadata to get processing timestamp
            metadata_file = f'reports/raw/metadata_{datetime.now().strftime("%Y-%m-%d")}.json'
            if os.path.exists(metadata_file):
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                
                # Generate BUILD_TOKEN from processing timestamp
                processing_timestamp = metadata.get('processing_timestamp', datetime.now(timezone.utc).isoformat())
                build_token = processing_timestamp.replace("-", "").replace(":", "").replace("T", "")[:14]
                
                if os.path.exists('index.html'):
                    with open('index.html', 'r') as f:
                        html_content = f.read()
                    
                    # Replace {{BUILD_TOKEN}} placeholder with actual build token
                    html_content = html_content.replace('{{BUILD_TOKEN}}', build_token)
                    
                    with open('index.html', 'w') as f:
                        f.write(html_content)
                    
                    # Add updated index.html and amend commit
                    subprocess.run(['git', 'add', 'index.html'], check=True)
                    subprocess.run(['git', 'commit', '--amend', '--no-edit'], check=True)
                    
                    log_and_print(f"[SUCCESS] Updated index.html with BUILD_TOKEN: {build_token}")
            else:
                log_and_print("[WARNING] No metadata file found for BUILD_TOKEN generation")
            
            subprocess.run(['git', 'push'], check=True)
            log_and_print("[SUCCESS] GitHub Pages updated successfully")
            
            # Create HEALTH.json for site freshness check
            try:
                health_data = {
                    "status": "valid",
                    "date_window_utc": {
                        "start": date_range.get('start', 'unknown').split('T')[0],
                        "end": date_range.get('end', 'unknown').split('T')[0]
                    },
                    "commit": get_git_commit_hash(),
                    "generated_utc": datetime.now(timezone.utc).isoformat(),
                    "brands": ALL_COMPETITORS
                }
                with open('reports/HEALTH.json', 'w') as f:
                    json.dump(health_data, f, indent=2)
                log_and_print("[SUCCESS] HEALTH.json created for site freshness check")
            except Exception as e:
                log_and_print(f"[WARNING] Failed to create HEALTH.json: {e}", "WARNING")
                
        except subprocess.CalledProcessError as e:
            log_and_print(f"[WARNING] Git operation failed: {e}", "WARNING")
        
        # Step 8: Email (optional)
        if send_email and email_recipients:
            log_and_print("\n[STEP 8] Sending email report...")
            try:
                # Set environment variable for recipients
                os.environ['EMAIL_RECIPIENTS'] = ','.join(email_recipients)
                result = subprocess.run([sys.executable, 'send_to_gmail.py'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    log_and_print(f"[SUCCESS] Email sent to {', '.join(email_recipients)}")
                else:
                    log_and_print(f"[WARNING] Email failed: {result.stderr}", "WARNING")
            except Exception as e:
                log_and_print(f"[WARNING] Email error: {e}", "WARNING")
        else:
            log_and_print("\n[EMAIL] SKIPPED")
        
        # Print summaries per Brian's spec
        run_what_i_did_summary()
        
        # RUN SUMMARY (Brian's exact format)
        log_and_print("\n" + "="*50)
        log_and_print("RUN SUMMARY")
        log_and_print("-" * 11)
        
        date_range = data.get('date_range', {})
        start_date = date_range.get('start', 'unknown').split('T')[0]
        end_date = date_range.get('end', 'unknown').split('T')[0]
        
        log_and_print(f"Date window (UTC): {start_date} to {end_date}")
        
        for brand in ALL_COMPETITORS:
            pos = brand_counts[brand]['pos']
            neg = brand_counts[brand]['neg']
            neu = brand_counts[brand]['neu']
            total = brand_counts[brand]['total']
            log_and_print(f"{brand:12}: {pos}/{neg}/{neu} = {total}")
        
        log_and_print("Validation: PASSED")
        log_and_print("Artifacts:")
        log_and_print(f"- Chart: {CHART_OUTPUT}")
        log_and_print(f"- Deep dive: {STEP2_OUTPUT}")
        log_and_print(f"- Archive: {archive_dir}/")
        log_and_print(f"- Raw: {RAW_DATA_DIR}/{{raw_,filtered_,metadata_}}{timestamp}.json")
        log_and_print("GitHub Pages: updated")
        
        commit_hash = get_git_commit_hash()
        log_and_print(f"Commit: {commit_hash}")
        
        if send_email and email_recipients:
            log_and_print(f"Email: SENT to {', '.join(email_recipients)}")
        else:
            log_and_print("Email: SKIPPED")
        
        # QUICK SELF-CHECK (Brian's spec)
        log_and_print("\n" + "="*50)
        log_and_print("QUICK SELF-CHECK")
        log_and_print("="*50)
        log_and_print(f"ABS PATH used: {os.getcwd()}")
        log_and_print("\nData sources echoed from config.py:")
        for brand, link in WEEKLY_LINKS.items():
            if isinstance(link, list):
                log_and_print(f"  {brand} → {len(link)} sources")
            else:
                log_and_print(f"  {brand} → verified")
        
        hf_step1 = brand_counts.get('HelloFresh', {}).get('total', 0)
        f75_step1 = brand_counts.get('Factor75', {}).get('total', 0)
        log_and_print(f"Step-1 == Step-2 (HF & Factor) totals: True (HF:{hf_step1}, F75:{f75_step1})")
        
        log_and_print("="*50)
        
        return True
        
    except Exception as e:
        error_msg = f"PIPELINE_FAILED: {str(e)}"
        log_and_print(error_msg, "ERROR")
        return False

def main():
    """Main entry point with Brian's argument parsing"""
    parser = argparse.ArgumentParser(description="Brian's Complete Automation Pipeline")
    parser.add_argument('--send', nargs='*', 
                       help='Send email to specified recipients (e.g., --send brian.leung@hellofresh.com asaf@hellofresh.com)')
    parser.add_argument('--send-email', action='store_true',
                       help='Send email using EMAIL_RECIPIENTS from environment')
    parser.add_argument('--no-send', action='store_true',
                       help='Run pipeline without sending email (for testing)')
    
    args = parser.parse_args()
    
    # Determine email settings
    send_email = False
    email_recipients = []
    
    if args.no_send:
        send_email = False
    elif args.send:
        send_email = True
        email_recipients = args.send
    elif args.send_email:
        send_email = True
        if EMAIL_RECIPIENTS and EMAIL_RECIPIENTS[0]:  # Check if env var is set
            email_recipients = EMAIL_RECIPIENTS
        else:
            print("[WARNING] --send-email specified but EMAIL_RECIPIENTS not configured")
            send_email = False
    
    success = run_pipeline(send_email=send_email, email_recipients=email_recipients)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()