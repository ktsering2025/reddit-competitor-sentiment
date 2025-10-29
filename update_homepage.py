#!/usr/bin/env python3
"""
Update homepage with current actionable data
"""

import json
import os
import re
from datetime import datetime
from config import ALL_COMPETITORS, PRIMARY_DEEPDIVE

def load_latest_data():
    """Load the latest working data"""
    if os.path.exists('reports/working_reddit_data.json'):
        with open('reports/working_reddit_data.json', 'r') as f:
            return json.load(f)
    return None

def calculate_brand_stats(data):
    """Calculate current brand statistics"""
    if not data:
        return {}
    
    brand_stats = {}
    posts = data.get('posts', [])
    
    for brand in ALL_COMPETITORS:
        # Use primary_brand to ensure accurate counts
        brand_posts = [post for post in posts if post.get('primary_brand') == brand]
        
        if brand_posts:
            positive = len([p for p in brand_posts if p.get('sentiment') == 'positive'])
            negative = len([p for p in brand_posts if p.get('sentiment') == 'negative'])
            neutral = len([p for p in brand_posts if p.get('sentiment') == 'neutral'])
            total = len(brand_posts)
            
            positive_pct = (positive / total * 100) if total > 0 else 0
            
            brand_stats[brand] = {
                'total': total,
                'positive': positive,
                'negative': negative,
                'neutral': neutral,
                'positive_pct': positive_pct
            }
        else:
            brand_stats[brand] = {
                'total': 0,
                'positive': 0,
                'negative': 0,
                'neutral': 0,
                'positive_pct': 0
            }
    
    return brand_stats

def update_homepage():
    """Update homepage with current data"""
    data = load_latest_data()
    if not data:
        print("No data found to update homepage")
        return
    
    brand_stats = calculate_brand_stats(data)
    
    # Calculate totals
    total_posts = sum(stats['total'] for stats in brand_stats.values())
    hf_stats = brand_stats.get('HelloFresh', {})
    f75_stats = brand_stats.get('Factor75', {})
    
    # Get date range
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '').split('T')[0] if date_range.get('start') else 'Unknown'
    end_date = date_range.get('end', '').split('T')[0] if date_range.get('end') else 'Unknown'
    
    # Read current index.html
    with open('index.html', 'r') as f:
        html_content = f.read()
    
    # Update using regex for more robust replacements
    # Update HelloFresh stats (first occurrence after "hellofresh" class)
    html_content = re.sub(
        r'(<div class="stat-card hellofresh">.*?<div class="stat-number">)\d+(</div>)',
        rf'\g<1>{hf_stats.get("total", 0)}\g<2>',
        html_content,
        count=1,
        flags=re.DOTALL
    )
    
    html_content = re.sub(
        r'(<div class="stat-card hellofresh">.*?<p[^>]*>)\d+% Positive(</p>)',
        rf'\g<1>{hf_stats.get("positive_pct", 0):.0f}% Positive\g<2>',
        html_content,
        count=1,
        flags=re.DOTALL
    )
    
    # Update Factor75 stats (first occurrence after "factor75" class)
    html_content = re.sub(
        r'(<div class="stat-card factor75">.*?<div class="stat-number">)\d+(</div>)',
        rf'\g<1>{f75_stats.get("total", 0)}\g<2>',
        html_content,
        count=1,
        flags=re.DOTALL
    )
    
    html_content = re.sub(
        r'(<div class="stat-card factor75">.*?<p[^>]*>)\d+% Positive(</p>)',
        rf'\g<1>{f75_stats.get("positive_pct", 0):.0f}% Positive\g<2>',
        html_content,
        count=1,
        flags=re.DOTALL
    )
    
    # Update total posts (first occurrence after "total" class)
    html_content = re.sub(
        r'(<div class="stat-card total">.*?<div class="stat-number">)\d+(</div>)',
        rf'\g<1>{total_posts}\g<2>',
        html_content,
        count=1,
        flags=re.DOTALL
    )
    
    # Update current data description
    html_content = re.sub(
        r'<p><strong>Current Data:</strong> \d+ actionable posts from global Reddit search \([^)]+\)</p>',
        f'<p><strong>Current Data:</strong> {total_posts} actionable posts from global Reddit search ({start_date} to {end_date})</p>',
        html_content
    )
    
    # Update email summary
    hf_performance = "Excellent performance" if hf_stats.get("positive_pct", 0) >= 70 else "Mixed performance" if hf_stats.get("positive_pct", 0) >= 50 else "Needs attention"
    f75_performance = "Excellent performance" if f75_stats.get("positive_pct", 0) >= 70 else "Balanced sentiment" if f75_stats.get("positive_pct", 0) >= 50 else "Needs attention"
    
    html_content = re.sub(
        r'<li><strong>HelloFresh:</strong> \d+ posts \(\d+% positive\) - [^<]+</li>',
        f'<li><strong>HelloFresh:</strong> {hf_stats.get("total", 0)} posts ({hf_stats.get("positive_pct", 0):.0f}% positive) - {hf_performance}</li>',
        html_content
    )
    
    html_content = re.sub(
        r'<li><strong>Factor75:</strong> \d+ posts \(\d+% positive\) - [^<]+</li>',
        f'<li><strong>Factor75:</strong> {f75_stats.get("total", 0)} posts ({f75_stats.get("positive_pct", 0):.0f}% positive) - {f75_performance}</li>',
        html_content
    )
    
    # Write updated content
    with open('index.html', 'w') as f:
        f.write(html_content)
    
    print(f"Homepage updated with current data:")
    print(f"  Total posts: {total_posts}")
    print(f"  HelloFresh: {hf_stats.get('total', 0)} posts ({hf_stats.get('positive_pct', 0):.0f}% positive)")
    print(f"  Factor75: {f75_stats.get('total', 0)} posts ({f75_stats.get('positive_pct', 0):.0f}% positive)")

if __name__ == "__main__":
    update_homepage()
