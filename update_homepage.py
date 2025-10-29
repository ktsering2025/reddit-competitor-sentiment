#!/usr/bin/env python3
"""
Update homepage with current actionable data
"""

import json
import os
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
        brand_posts = [post for post in posts if brand in post.get('competitors_mentioned', [])]
        
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
    
    # Update the stats section
    html_content = html_content.replace(
        f'<p><strong>Current Data:</strong> 37 actionable posts from global Reddit search (Oct 27-Nov 01, 2025)</p>',
        f'<p><strong>Current Data:</strong> {total_posts} actionable posts from global Reddit search ({start_date} to {end_date})</p>'
    )
    
    html_content = html_content.replace(
        '<div class="stat-number">7</div>',
        f'<div class="stat-number">{hf_stats.get("total", 0)}</div>'
    )
    
    html_content = html_content.replace(
        '<p style="margin-top: 0.5rem; color: #27ae60; font-weight: bold;">57% Positive</p>',
        f'<p style="margin-top: 0.5rem; color: #27ae60; font-weight: bold;">{hf_stats.get("positive_pct", 0):.0f}% Positive</p>'
    )
    
    html_content = html_content.replace(
        '<div class="stat-number">8</div>',
        f'<div class="stat-number">{f75_stats.get("total", 0)}</div>'
    )
    
    html_content = html_content.replace(
        '<p style="margin-top: 0.5rem; color: #27ae60; font-weight: bold;">50% Positive</p>',
        f'<p style="margin-top: 0.5rem; color: #27ae60; font-weight: bold;">{f75_stats.get("positive_pct", 0):.0f}% Positive</p>'
    )
    
    html_content = html_content.replace(
        '<div class="stat-number">37</div>',
        f'<div class="stat-number">{total_posts}</div>'
    )
    
    # Update email summary
    hf_performance = "Excellent performance" if hf_stats.get("positive_pct", 0) >= 70 else "Mixed performance" if hf_stats.get("positive_pct", 0) >= 50 else "Needs attention"
    f75_performance = "Excellent performance" if f75_stats.get("positive_pct", 0) >= 70 else "Balanced sentiment" if f75_stats.get("positive_pct", 0) >= 50 else "Needs attention"
    
    html_content = html_content.replace(
        f'<li><strong>HelloFresh:</strong> 7 posts (57% positive) - Mixed performance</li>',
        f'<li><strong>HelloFresh:</strong> {hf_stats.get("total", 0)} posts ({hf_stats.get("positive_pct", 0):.0f}% positive) - {hf_performance}</li>'
    )
    
    html_content = html_content.replace(
        f'<li><strong>Factor75:</strong> 8 posts (50% positive) - Balanced sentiment</li>',
        f'<li><strong>Factor75:</strong> {f75_stats.get("total", 0)} posts ({f75_stats.get("positive_pct", 0):.0f}% positive) - {f75_performance}</li>'
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