#!/usr/bin/env python3
"""
Generate Step 1 chart with Brian's specific feedback implemented
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import json
import os

def load_weekly_data():
    """Load actual weekly data from scraper results"""
    try:
        if os.path.exists('reports/working_reddit_data.json'):
            with open('reports/working_reddit_data.json', 'r') as f:
                data = json.load(f)
            
            # Process actual scraped data from last 7 days
            brand_stats = {}
            posts = data.get('posts', [])
            seven_days_ago = datetime.now() - timedelta(days=7)
            seven_days_timestamp = seven_days_ago.timestamp()
            
            weekly_posts = 0
            for post in posts:
                # Only count posts from last 7 days
                created = post.get('created_utc', 0)
                if created >= seven_days_timestamp:
                    weekly_posts += 1
                    mentioned_brands = post.get('competitors_mentioned', [])
                    sentiment = post.get('sentiment', 'neutral')
                    
                    for brand in mentioned_brands:
                        if brand not in brand_stats:
                            brand_stats[brand] = {'positive': 0, 'negative': 0, 'neutral': 0}
                        
                        brand_stats[brand][sentiment] += 1
            
            print(f"Processing {weekly_posts} posts from last 7 days...")
            
            # Convert to chart format (same as original)
            chart_data = []
            for brand, stats in brand_stats.items():
                total = stats['positive'] + stats['negative'] + stats['neutral']
                if total > 0:  # Only include brands with data
                    # Add (HF) designation for HelloFresh family brands
                    if brand in ['HelloFresh', 'Factor', 'EveryPlate', 'Green Chef']:
                        brand_name = f"{brand} (HF)"
                    else:
                        brand_name = brand
                    
                    chart_data.append((brand_name, {
                        'total_posts': total,
                        'positive': stats['positive'],
                        'negative': stats['negative'], 
                        'neutral': stats['neutral']
                    }))
            
            # Sort by total posts (volume) - same as original
            chart_data.sort(key=lambda x: x[1]['total_posts'], reverse=True)
            print(f"Processed {len(chart_data)} brands with weekly data")
            return chart_data
            
    except Exception as e:
        print(f"Could not load weekly data: {e}")
    
    # Fallback - this shouldn't happen now
    return []

def create_chart_with_brian_feedback():
    """Create chart implementing Brian's weekly feedback"""
    
    # Load actual weekly data from scraper
    chart_data = load_weekly_data()

    competitors = [name for name, data in chart_data]
    positive = [data['positive'] for name, data in chart_data]
    negative = [data['negative'] for name, data in chart_data]
    neutral = [data['neutral'] for name, data in chart_data]

    # Create chart
    fig, ax = plt.subplots(figsize=(16, 9))

    x = np.arange(len(competitors))
    width = 0.65

    # Original colors
    bars1 = ax.bar(x, positive, width, label='Positive', color='#2E8B57', alpha=0.8)
    bars2 = ax.bar(x, negative, width, bottom=positive, label='Negative', color='#DC143C', alpha=0.8)
    bars3 = ax.bar(x, neutral, width, bottom=np.array(positive) + np.array(negative), 
                   label='Neutral', color='#708090', alpha=0.8)

    # BRIAN'S FEEDBACK #1: Clear timeframe in title (WEEKLY DATA)
    from datetime import datetime, timedelta
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    date_range = f"{start_date.strftime('%b %d')} – {end_date.strftime('%b %d, %Y')}"
    
    ax.set_title(f'Reddit Post Volume by Competitor — {date_range} (Weekly Sentiment Analysis - HelloFresh vs Competitors)', 
                 fontsize=15, fontweight='bold', pad=25)

    # BRIAN'S FEEDBACK #2: Clarify post count meaning (WEEKLY DATA)
    ax.set_ylabel('# of Posts (Weekly)', fontsize=13, fontweight='bold')
    ax.set_xlabel('Competitor Brand Name - Reddit posts from last 7 days (not comments or reposts)', 
                  fontsize=12, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(competitors, rotation=45, ha='right', fontsize=11)
    ax.legend(loc='upper right', fontsize=12)

    # Add totals on bars
    totals = [data['total_posts'] for name, data in chart_data]
    for i, total in enumerate(totals):
        ax.text(i, total + max(totals) * 0.02, str(total), ha='center', va='bottom', fontweight='bold', fontsize=10)

    plt.tight_layout()
    plt.grid(axis='y', alpha=0.3)
    
    # Force Y-axis to show whole numbers only (no 1.5, 2.5, etc.)
    import matplotlib.ticker as ticker
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    # Save chart
    plt.savefig('reports/step1_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    date_range = f"{start_date.strftime('%b %d')} – {end_date.strftime('%b %d, %Y')}"
    
    print("Chart updated with Brian's weekly feedback:")
    print(f"1. Weekly timeframe: {date_range}")
    print("2. Post count clarification: Each count = unique Reddit post from last 7 days")
    print("3. Data source: Actual weekly Reddit scraper results")

if __name__ == "__main__":
    create_chart_with_brian_feedback()
