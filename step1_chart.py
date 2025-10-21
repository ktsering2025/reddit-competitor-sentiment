"""
Brian's Step 1 Chart - UPDATED WITH FRESH DATA
Purpose: Use fresh Reddit data (77 posts) for accurate Step 1 chart
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from ai_sentiment import AdvancedSentimentAnalyzer
import os

def load_fresh_data():
    """Load fresh Reddit data from working scraper"""
    try:
        with open('reports/working_reddit_data.json', 'r') as f:
            data = json.load(f)
        return data['posts']
    except FileNotFoundError:
        print("#  Fresh data not found. Run working_scraper.py first.")
        return []

def generate_step1_chart():
    """Generate Step 1 chart with fresh Reddit data"""
    
    print("STEP 1: REDDIT POST BREAKDOWN BY COMPETITOR")
    print("=" * 70)
    
    # Step 1: Load fresh data
    print("\n[1/4] Loading fresh Reddit data...")
    posts = load_fresh_data()
    
    if not posts:
        print("#  No data found. Please run working_scraper.py first.")
        return None, None
    
    print(f"#  Loaded {len(posts)} fresh posts")
    
    # Step 2: Organize data by competitor
    print("\n[2/4] Organizing data by competitor...")
    
    competitor_data = defaultdict(lambda: {'positive': 0, 'negative': 0, 'neutral': 0, 'total': 0})
    
    for post in posts:
        sentiment = post.get('sentiment', 'neutral')
        competitors = post.get('competitors_mentioned', [])
        
        for competitor in competitors:
            # Normalize competitor names
            if competitor.lower() in ['hello fresh', 'hello-fresh']:
                competitor = 'HelloFresh'
            elif competitor.lower() in ['factor meals', 'factor75']:
                competitor = 'Factor'
            elif competitor.lower() in ['every plate', 'every-plate']:
                competitor = 'EveryPlate'
            elif competitor.lower() in ['green chef', 'green-chef']:
                competitor = 'Green Chef'
            elif competitor.lower() in ['chefs plate', 'chefs-plate']:
                competitor = "Chef's Plate"
            elif competitor.lower() in ['butcher box', 'butcherbox']:
                competitor = 'ButcherBox'
            elif competitor.lower() in ['hungry root', 'hungryroot']:
                competitor = 'HungryRoot'
            elif competitor.lower() in ['blue apron', 'blueapron']:
                competitor = 'Blue Apron'
            elif competitor.lower() in ['home chef', 'homechef']:
                competitor = 'Home Chef'
            elif competitor.lower() in ['marley spoon', 'marleyspoon']:
                competitor = 'Marley Spoon'
            elif competitor.lower() in ['sunbasket']:
                competitor = 'Sunbasket'
            elif competitor.lower() in ['gobble']:
                competitor = 'Gobble'
            elif competitor.lower() in ['cook unity', 'cookunity']:
                competitor = 'CookUnity'
            elif competitor.lower() in ['the farmers dog', 'farmers dog']:
                competitor = "The Farmer's Dog"
            elif competitor.lower() in ['ollie']:
                competitor = 'Ollie'
            elif competitor.lower() in ['nom nom', 'nomnom']:
                competitor = 'Nom Nom'
            
            competitor_data[competitor][sentiment] += 1
            competitor_data[competitor]['total'] += 1
    
    # Step 3: Prepare chart data
    print("\n[3/4] Preparing chart data...")
    
    # Sort by total posts (volume)
    sorted_competitors = sorted(
        competitor_data.items(), 
        key=lambda x: x[1]['total'], 
        reverse=True
    )
    
    competitors = []
    positive_counts = []
    negative_counts = []
    neutral_counts = []
    
    for competitor, data in sorted_competitors:
        competitors.append(competitor)
        positive_counts.append(data['positive'])
        negative_counts.append(data['negative'])
        neutral_counts.append(data['neutral'])
    
    # Step 4: Create optimized stacked bar chart
    print("\n[4/4] Creating visualization...")
    
    # Optimized figure size for presentations
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # Professional color scheme
    colors = {
        'positive': '#2E8B57',  # Sea green
        'negative': '#DC143C',  # Crimson  
        'neutral': '#808080'    # Gray
    }
    
    x_positions = np.arange(len(competitors))
    bar_width = 0.8
    
    # Create stacked bars with thicker borders
    p1 = ax.bar(x_positions, positive_counts, bar_width, 
                label='Positive', color=colors['positive'], 
                edgecolor='white', linewidth=1.0)
    
    p2 = ax.bar(x_positions, negative_counts, bar_width,
                bottom=positive_counts, label='Negative', 
                color=colors['negative'], 
                edgecolor='white', linewidth=1.0)
    
    p3 = ax.bar(x_positions, neutral_counts, bar_width,
                bottom=np.array(positive_counts) + np.array(negative_counts),
                label='Suggestion (Neutral)', color=colors['neutral'], 
                edgecolor='white', linewidth=1.0)
    
    # Professional chart formatting
    ax.set_title("Step 1: Reddit Post Breakdown by Competitor\n(Sentiment Analysis - HelloFresh vs Competitors)", 
                 fontsize=18, fontweight='bold', pad=25)
    ax.set_xlabel('Competitor / Brand Name', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Posts', fontsize=14, fontweight='bold')
    
    # Better x-axis formatting
    ax.set_xticks(x_positions)
    ax.set_xticklabels(competitors, rotation=45, ha='right', fontsize=12)
    
    # Professional legend
    ax.legend(loc='upper right', frameon=True, fancybox=True, 
              shadow=True, fontsize=12, framealpha=0.95)
    
    # Cleaner grid
    ax.grid(axis='y', alpha=0.25, linestyle='--', linewidth=0.7)
    ax.set_axisbelow(True)  # Grid behind bars
    
    # Calculate max height for proper y-axis limits
    max_height = max(positive_counts[i] + negative_counts[i] + neutral_counts[i] 
                    for i in range(len(competitors)))
    
    # Set y-axis limit with extra space for labels
    ax.set_ylim(0, max_height * 1.15)
    
    # Enhanced total count labels
    for i, (pos, neg, neu) in enumerate(zip(positive_counts, negative_counts, neutral_counts)):
        total = pos + neg + neu
        ax.text(x_positions[i], total + (max_height * 0.02), str(total), 
                ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    # Better spacing
    plt.tight_layout()
    
    # Save chart
    os.makedirs('reports', exist_ok=True)
    chart_path = "reports/step1_chart.png"
    plt.savefig(chart_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"Chart saved: {chart_path}")
    
    # Step 5: Print detailed results for Brian
    print("\n" + "=" * 70)
    print("STEP 1 RESULTS SUMMARY")
    print("=" * 70)
    
    print(f"\nTotal Posts: {len(posts)}")
    print(f"Competitors Tracked: {len(competitor_data)}")
    
    print(f"\n{'Competitor':<20} {'Posts':<8} {'Positive':<10} {'Negative':<10} {'Neutral':<10} {'Rating':<10}")
    print("-" * 70)
    
    for competitor, data in sorted_competitors:
        total = data['total']
        pos = data['positive']
        neg = data['negative']
        neu = data['neutral']
        
        pos_pct = (pos / total) * 100 if total > 0 else 0
        neg_pct = (neg / total) * 100 if total > 0 else 0
        
        # Performance rating
        if pos_pct >= 60:
            rating = "STRONG"
        elif neg_pct >= 50:
            rating = "WEAK"
        else:
            rating = "MIXED"
        
        print(f"{competitor:<20} {total:<8} {pos} ({pos_pct:.0f}%){'':<3} {neg} ({neg_pct:.0f}%){'':<3} {neu} ({(neu/total)*100:.0f}%){'':<3} {rating}")
    
    # Key insights for Brian
    print("\n" + "=" * 70)
    print("KEY INSIGHTS FOR BRIAN")
    print("=" * 70)
    
    # HelloFresh performance
    hf_data = competitor_data.get('HelloFresh', {})
    if hf_data:
        hf_total = hf_data['total']
        hf_pos = hf_data['positive']
        hf_neg = hf_data['negative']
        hf_pos_pct = (hf_pos / hf_total) * 100 if hf_total > 0 else 0
        hf_neg_pct = (hf_neg / hf_total) * 100 if hf_total > 0 else 0
        
        print(f"\nHelloFresh Performance:")
        print(f"   • Total mentions: {hf_total} posts")
        print(f"   • Positive: {hf_pos} ({hf_pos_pct:.1f}%)")
        print(f"   • Negative: {hf_neg} ({hf_neg_pct:.1f}%)")
    
    # Top performing competitors
    print(f"\nTop Performing Competitors:")
    top_positive = sorted(
        [(comp, data) for comp, data in competitor_data.items() if data['total'] >= 3],
        key=lambda x: (x[1]['positive'] / x[1]['total']) if x[1]['total'] > 0 else 0,
        reverse=True
    )[:3]
    
    for i, (comp, data) in enumerate(top_positive, 1):
        pos_pct = (data['positive'] / data['total']) * 100 if data['total'] > 0 else 0
        print(f"   {i}. {comp}: {data['positive']}/{data['total']} posts ({pos_pct:.1f}% positive)")
    
    # Competitors with issues
    print(f"\nCompetitors with Negative Sentiment:")
    negative_comps = [
        (comp, data) for comp, data in competitor_data.items() 
        if data['negative'] > 0
    ]
    
    if negative_comps:
        for comp, data in sorted(negative_comps, key=lambda x: x[1]['negative'], reverse=True):
            neg_pct = (data['negative'] / data['total']) * 100 if data['total'] > 0 else 0
            print(f"   • {comp}: {data['negative']}/{data['total']} posts ({neg_pct:.1f}% negative)")
    else:
        print(f"   None detected")
    
    print("\n" + "=" * 70)
    print("STEP 1 COMPLETE - Ready for Brian's review")
    print("=" * 70)
    
    return chart_path, competitor_data

if __name__ == "__main__":
    chart_path, data = generate_step1_chart()
