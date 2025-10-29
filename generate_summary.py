#!/usr/bin/env python3
"""
Generate SUMMARY.json for dashboard synchronization
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

def generate_summary():
    """Generate SUMMARY.json for dashboard sync"""
    data = load_latest_data()
    if not data:
        print("No data found to generate summary")
        return
    
    brand_stats = calculate_brand_stats(data)
    
    # Calculate totals
    total_posts = sum(stats['total'] for stats in brand_stats.values())
    
    # Get date range
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '').split('T')[0] if date_range.get('start') else 'Unknown'
    end_date = date_range.get('end', '').split('T')[0] if date_range.get('end') else 'Unknown'
    
    # Get filter stats
    filter_stats = data.get('filter_stats', {})
    
    # Create summary
    summary = {
        "generated_utc": datetime.now().isoformat(),
        "date_range": {
            "start": start_date,
            "end": end_date,
            "period": f"{start_date} to {end_date}"
        },
        "total_posts": total_posts,
        "brands": brand_stats,
        "filter_stats": filter_stats,
        "data_quality": {
            "spam_filtered": True,
            "actionable_only": True,
            "source": "Reddit API + Web Scraping"
        },
        "dashboard_stats": {
            "hellofresh": {
                "posts": brand_stats.get('HelloFresh', {}).get('total', 0),
                "positive_pct": brand_stats.get('HelloFresh', {}).get('positive_pct', 0),
                "performance": "Excellent" if brand_stats.get('HelloFresh', {}).get('positive_pct', 0) >= 70 else "Mixed" if brand_stats.get('HelloFresh', {}).get('positive_pct', 0) >= 50 else "Needs attention"
            },
            "factor75": {
                "posts": brand_stats.get('Factor75', {}).get('total', 0),
                "positive_pct": brand_stats.get('Factor75', {}).get('positive_pct', 0),
                "performance": "Excellent" if brand_stats.get('Factor75', {}).get('positive_pct', 0) >= 70 else "Balanced" if brand_stats.get('Factor75', {}).get('positive_pct', 0) >= 50 else "Needs attention"
            },
            "total_actionable": total_posts
        }
    }
    
    # Write summary
    with open('reports/SUMMARY.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"SUMMARY.json generated:")
    print(f"  Date range: {start_date} to {end_date}")
    print(f"  Total posts: {total_posts}")
    print(f"  HelloFresh: {brand_stats.get('HelloFresh', {}).get('total', 0)} posts ({brand_stats.get('HelloFresh', {}).get('positive_pct', 0):.1f}% positive)")
    print(f"  Factor75: {brand_stats.get('Factor75', {}).get('total', 0)} posts ({brand_stats.get('Factor75', {}).get('positive_pct', 0):.1f}% positive)")

if __name__ == "__main__":
    generate_summary()