#!/usr/bin/env python3
"""
Step 1 Chart Generator - Brian's Final Build Plan
Creates stacked bar chart showing all 6 competitors' sentiment breakdown
"""

import matplotlib.pyplot as plt
import numpy as np
import json
import os
from datetime import datetime
from collections import defaultdict
import subprocess
from config import *

def get_git_commit_hash():
    """Get current git commit hash"""
    try:
        result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], 
                              capture_output=True, text=True, cwd='.')
        return result.stdout.strip()
    except:
        return "unknown"

def load_data():
    """Load the working dataset"""
    if os.path.exists(WORKING_DATA_FILE):
        with open(WORKING_DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError("No working data found. Run accurate_scraper.py first.")

def analyze_brand_sentiment(data):
    """Analyze sentiment breakdown by brand (all competitors for Step 1)"""
    # Initialize all 6 brands with zeros
    brand_sentiment = {brand: {'positive': 0, 'negative': 0, 'neutral': 0} for brand in ALL_COMPETITORS}
    
    posts = data.get('posts', [])
    
    # Count sentiment for each brand (using primary_brand to ensure accuracy)
    for post in posts:
        primary_brand = post.get('primary_brand')
        sentiment = post.get('sentiment', 'neutral')
        
        if primary_brand and primary_brand in brand_sentiment:
            brand_sentiment[primary_brand][sentiment] += 1
    
    return brand_sentiment

def create_chart(brand_sentiment, data):
    """Create Step 1 chart per Brian's exact specifications"""
    
    # Prepare data for stacking
    positive_counts = [brand_sentiment[brand]['positive'] for brand in ALL_COMPETITORS]
    negative_counts = [brand_sentiment[brand]['negative'] for brand in ALL_COMPETITORS]
    neutral_counts = [brand_sentiment[brand]['neutral'] for brand in ALL_COMPETITORS]
    
    # Create figure with Brian's specified size
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE)
    
    # Create stacked bars (Positive/Negative/Neutral as per spec)
    x = np.arange(len(ALL_COMPETITORS))
    width = 0.6
    
    # Stack: Positive (bottom), Negative (middle), Neutral (top)
    p1 = ax.bar(x, positive_counts, width, label='Positive', color='#2E8B57', alpha=0.8)
    p2 = ax.bar(x, negative_counts, width, bottom=positive_counts, label='Negative', color='#DC143C', alpha=0.8)
    
    # Calculate bottom for neutral (positive + negative)
    neutral_bottom = [positive_counts[i] + negative_counts[i] for i in range(len(ALL_COMPETITORS))]
    p3 = ax.bar(x, neutral_counts, width, bottom=neutral_bottom, label='Neutral', color='#808080', alpha=0.8)
    
    # Title (2 lines as per Brian's spec)
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '2025-10-20').split('T')[0]
    end_date = date_range.get('end', '2025-10-27').split('T')[0]
    
    # Format dates properly for title (Mon-Fri format)
    try:
        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)
        # Check if it's Mon-Fri (5 days) or Mon-Sat (6 days)
        days_diff = (end_dt - start_dt).days
        if days_diff == 4:  # Mon-Fri
            date_str = f"{start_dt.strftime('%b %d')} – {end_dt.strftime('%b %d, %Y')}"
        elif days_diff == 5:  # Mon-Sat
            date_str = f"{start_dt.strftime('%b %d')} – {end_dt.strftime('%b %d, %Y')} (incl. Sat)"
        else:
            date_str = f"{start_dt.strftime('%b %d')} – {end_dt.strftime('%b %d, %Y')}"
    except:
        date_str = f"{start_date} – {end_date}"
    
    ax.set_title(f'Reddit Competitor Sentiment Analysis (Past 7 Days)\n{date_str}', 
                fontsize=16, fontweight='bold', pad=20)
    
    # X-axis - no label, just brand names
    ax.set_xticks(x)
    
    # Add (HF) label to HelloFresh family brands
    brand_labels = [f"{brand} (HF)" if brand in HF_FAMILY_BRANDS else brand for brand in ALL_COMPETITORS]
    # 45° rotation for maximum readability and no overlap
    ax.set_xticklabels(brand_labels, rotation=45, ha='right', fontsize=10)
    
    # Y-axis - count by 2s as requested
    max_y = max([sum([positive_counts[i], negative_counts[i], neutral_counts[i]]) for i in range(len(ALL_COMPETITORS))])
    
    # Always count by 2s (0, 2, 4, 6, 8, ...)
    if max_y > 0:
        # Round up to nearest even number
        max_y_rounded = max_y + (2 - max_y % 2) if max_y % 2 != 0 else max_y
        y_ticks = list(range(0, max_y_rounded + 2, 2))
        ax.set_yticks(y_ticks)
        ax.set_ylim(0, max_y_rounded + 2)
    else:
        ax.set_yticks([0, 2, 4, 6, 8, 10])
        ax.set_ylim(0, 10)
    
    ax.set_ylabel('Number of Posts', fontsize=12, fontweight='bold')
    
    # Legend
    ax.legend(loc='upper right')
    
    # Grid for better readability
    ax.grid(True, alpha=0.3, axis='y')
    
    # Footer with metadata - maximum spacing to prevent overlap with rotated labels
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    commit_hash = get_git_commit_hash()
    
    # Line 1: Data period and metadata (top line)
    footer_text = f"Data period: {start_date}–{end_date}  •  Generated (UTC): {timestamp}  •  Commit: {commit_hash}"
    plt.figtext(0.5, 0.08, footer_text, ha='center', fontsize=8, color='#666')
    
    # Line 2: Note about counts (bottom line - right at the bottom)
    plt.figtext(0.5, 0.02, 'Counts are unique posts (no comments/reposts)', 
                ha='center', fontsize=10, style='italic', color='#333')
    
    # Adjust layout with extra bottom margin for 45° rotated labels
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.20)
    
    # Save chart (stable name as per Brian's spec)
    # MAXIMUM DPI (600) for crystal-clear viewing when opened
    os.makedirs('reports', exist_ok=True)
    plt.savefig(CHART_OUTPUT, dpi=600, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"[SUCCESS] Step 1 chart saved to {CHART_OUTPUT} (Ultra high-res: 600 DPI)")
    
    # Also save as PDF for email attachment (vector format, never blurry)
    pdf_output = CHART_OUTPUT.replace('.png', '.pdf')
    plt.savefig(pdf_output, format='pdf', bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"[SUCCESS] Step 1 chart also saved as PDF: {pdf_output}")
    
    return CHART_OUTPUT

def print_run_summary(brand_sentiment, data):
    """Print run summary in Brian's exact format"""
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', 'unknown').split('T')[0]
    end_date = date_range.get('end', 'unknown').split('T')[0]
    
    print(f"\nDate window (UTC): {start_date} to {end_date}")
    
    for brand in ALL_COMPETITORS:
        pos = brand_sentiment[brand]['positive']
        neg = brand_sentiment[brand]['negative']
        neu = brand_sentiment[brand]['neutral']
        total = pos + neg + neu
        print(f"{brand:12}: {pos}/{neg}/{neu} = {total}")

def main():
    """Main function"""
    try:
        data = load_data()
        brand_sentiment = analyze_brand_sentiment(data)
        chart_path = create_chart(brand_sentiment, data)
        
        # Print summary in Brian's format
        print_run_summary(brand_sentiment, data)
        
        return chart_path
        
    except Exception as e:
        print(f"[ERROR] Error generating Step 1 chart: {e}")
        return None

if __name__ == "__main__":
    main()