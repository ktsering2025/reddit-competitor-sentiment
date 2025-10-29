#!/usr/bin/env python3
"""
Step 3: Competitor Deep Dive Analysis
Benchmark insights against top competitors - strengths/weaknesses table
"""

import json
import os
from datetime import datetime
from collections import defaultdict
from config import *

def load_data():
    """Load the working dataset"""
    if os.path.exists(WORKING_DATA_FILE):
        with open(WORKING_DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError("No working data found. Run accurate_scraper.py first.")

def categorize_post_themes(posts):
    """Categorize posts into themes (Quality, Delivery, Service, Price)"""
    theme_keywords = {
        'Quality': ['taste', 'flavor', 'fresh', 'quality', 'ingredients', 'cooking', 'recipe', 'delicious', 'bland', 'tasteless', 'amazing', 'terrible'],
        'Delivery': ['delivery', 'shipping', 'late', 'on time', 'packaging', 'arrived', 'damaged', 'cold', 'frozen', 'early', 'fast'],
        'Service': ['customer service', 'support', 'refund', 'cancel', 'subscription', 'billing', 'help', 'complaint', 'response', 'staff'],
        'Price': ['price', 'cost', 'expensive', 'cheap', 'value', 'money', 'worth', 'affordable', 'overpriced', 'budget', 'deal']
    }
    
    theme_sentiment = defaultdict(lambda: {'positive': 0, 'negative': 0, 'neutral': 0})
    
    for post in posts:
        text = (post.get('title', '') + ' ' + post.get('selftext', '')).lower()
        sentiment = post.get('sentiment', 'neutral')
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in text for keyword in keywords):
                theme_sentiment[theme][sentiment] += 1
                break
    
    return theme_sentiment

def analyze_competitor_themes(data):
    """Analyze themes for all competitors"""
    competitor_themes = {}
    
    for brand in ALL_COMPETITORS:
        brand_posts = [post for post in data.get('posts', []) if brand in post.get('competitors_mentioned', [])]
        if brand_posts:
            theme_sentiment = categorize_post_themes(brand_posts)
            competitor_themes[brand] = theme_sentiment
    
    return competitor_themes

def generate_strengths_weaknesses(competitor_themes, data):
    """Generate strengths and weaknesses for each competitor with fallback narratives"""
    results = {}
    
    # Get brand counts from metadata for total posts per brand
    brand_counts = {}
    if 'brand_counts' in data:
        brand_counts = data['brand_counts']
    
    for brand in ALL_COMPETITORS:
        total_posts = brand_counts.get(brand, 0)
        
        if total_posts == 0:
            # No posts recorded this week
            results[brand] = {
                'strengths': "No posts recorded this week.",
                'weaknesses': "No posts recorded this week."
            }
            continue
            
        themes = competitor_themes.get(brand, {})
        strengths = []
        weaknesses = []
        
        for theme, sentiment_counts in themes.items():
            total = sum(sentiment_counts.values())
            if total > 0:
                positive_pct = (sentiment_counts['positive'] / total) * 100
                negative_pct = (sentiment_counts['negative'] / total) * 100
                
                if positive_pct >= 60:  # 60%+ positive
                    strengths.append(f"{theme} ({positive_pct:.0f}% positive)")
                elif negative_pct >= 60:  # 60%+ negative
                    weaknesses.append(f"{theme} ({negative_pct:.0f}% negative)")
        
        # Fallback narratives if no themes meet thresholds
        if not strengths:
            strengths_text = "Low volume this week; no theme reached 60% positive."
        else:
            strengths_text = "; ".join(strengths)
            
        if not weaknesses:
            weaknesses_text = "Sentiment is balanced; no theme reached 60% negative."
        else:
            weaknesses_text = "; ".join(weaknesses)
        
        results[brand] = {
            'strengths': strengths_text,
            'weaknesses': weaknesses_text
        }
    
    return results

def create_competitor_table_html(competitor_analysis, data):
    """Create HTML table for competitor analysis"""
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '2025-10-20').split('T')[0]
    end_date = date_range.get('end', '2025-10-25').split('T')[0]
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Step 3: Competitor Deep Dive Analysis</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; text-align: center; margin-bottom: 30px; }}
        .date-info {{ text-align: center; color: #7f8c8d; margin-bottom: 30px; }}
        .competitor-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        .competitor-table th, .competitor-table td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        .competitor-table th {{ background-color: #34495e; color: white; font-weight: bold; }}
        .competitor-table tr:nth-child(even) {{ background-color: #f8f9fa; }}
        .strengths {{ color: #27ae60; font-weight: bold; }}
        .weaknesses {{ color: #e74c3c; font-weight: bold; }}
        .brand-name {{ font-weight: bold; color: #2c3e50; }}
        .summary {{ margin-top: 30px; padding: 20px; background-color: #ecf0f1; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Step 3: Competitor Deep Dive Analysis</h1>
        <div class="date-info">
            <p><strong>Analysis Period:</strong> {start_date} to {end_date}</p>
            <p><strong>Data Source:</strong> Weekly Reddit sentiment analysis</p>
        </div>
        
        <table class="competitor-table">
            <thead>
                <tr>
                    <th>Brand</th>
                    <th>Doing Well (Strengths)</th>
                    <th>Needs Improvement (Weaknesses)</th>
                </tr>
            </thead>
            <tbody>"""
    
    for brand, analysis in competitor_analysis.items():
        strengths_text = analysis['strengths'] if isinstance(analysis['strengths'], str) else ", ".join(analysis['strengths'])
        weaknesses_text = analysis['weaknesses'] if isinstance(analysis['weaknesses'], str) else ", ".join(analysis['weaknesses'])
        
        html += f"""
                <tr>
                    <td class="brand-name">{brand}</td>
                    <td class="strengths">{strengths_text}</td>
                    <td class="weaknesses">{weaknesses_text}</td>
                </tr>"""
    
    html += """
            </tbody>
        </table>"""
    
    # Add Top 3 Posts for each competitor (excluding HelloFresh and Factor75 which are in Step 2)
    other_competitors = [b for b in ALL_COMPETITORS if b not in PRIMARY_DEEPDIVE]
    
    for brand in other_competitors:
        brand_posts = [post for post in data.get('posts', []) if brand in post.get('competitors_mentioned', [])]
        if not brand_posts:
            continue
            
        # Calculate engagement scores
        for post in brand_posts:
            post['engagement_score'] = post.get('score', 0) + (3 * post.get('num_comments', 0))
        
        # Get top 3 positive and negative
        top_positive = sorted([p for p in brand_posts if p.get('sentiment') == 'positive'], 
                             key=lambda x: x['engagement_score'], reverse=True)[:3]
        top_negative = sorted([p for p in brand_posts if p.get('sentiment') == 'negative'], 
                             key=lambda x: x['engagement_score'], reverse=True)[:3]
        
        html += f"""
        <h2 style="margin-top: 40px;">{brand} - Top Reddit Posts</h2>
        <h3 style="color: #27ae60;">Top Positive Posts</h3>"""
        
        if top_positive:
            for i, post in enumerate(top_positive, 1):
                preview = post.get('selftext', '')[:300] + ('...' if len(post.get('selftext', '')) > 300 else '')
                html += f"""
        <div style="border-left: 4px solid #27ae60; padding: 15px; margin: 15px 0; background-color: #f8f9fa;">
            <h4>#{i}: <a href="{post['url']}" target="_blank">{post['title']}</a></h4>
            <p><strong>Engagement:</strong> {post['engagement_score']:.0f} | <strong>Subreddit:</strong> r/{post['subreddit']}</p>
            <p>{preview}</p>
            <p><small>Score: {post.get('score', 0)} | Comments: {post.get('num_comments', 0)}</small></p>
        </div>"""
        else:
            html += "<p>No positive posts found.</p>"
        
        html += f"""
        <h3 style="color: #e74c3c;">Top Negative Posts</h3>"""
        
        if top_negative:
            for i, post in enumerate(top_negative, 1):
                preview = post.get('selftext', '')[:300] + ('...' if len(post.get('selftext', '')) > 300 else '')
                html += f"""
        <div style="border-left: 4px solid #e74c3c; padding: 15px; margin: 15px 0; background-color: #f8f9fa;">
            <h4>#{i}: <a href="{post['url']}" target="_blank">{post['title']}</a></h4>
            <p><strong>Engagement:</strong> {post['engagement_score']:.0f} | <strong>Subreddit:</strong> r/{post['subreddit']}</p>
            <p>{preview}</p>
            <p><small>Score: {post.get('score', 0)} | Comments: {post.get('num_comments', 0)}</small></p>
        </div>"""
        else:
            html += "<p>No negative posts found.</p>"
    
    html += """
        <div class="summary">
            <h3>Key Insights</h3>
            <ul>
                <li>Analysis based on Reddit sentiment from the past week</li>
                <li>Strengths: Areas with 60%+ positive sentiment</li>
                <li>Weaknesses: Areas with 60%+ negative sentiment</li>
                <li>Data categorized by Quality, Delivery, Service, and Price themes</li>
                <li>Top posts ranked by engagement (Score + 3×Comments)</li>
            </ul>
        </div>
    </div>
</body>
</html>"""
    
    return html

def main():
    """Main function to generate Step 3 competitor analysis"""
    print("Step 3: Generating competitor deep dive analysis...")
    
    # Load data
    data = load_data()
    
    # Analyze competitor themes
    competitor_themes = analyze_competitor_themes(data)
    
    # Generate strengths/weaknesses
    competitor_analysis = generate_strengths_weaknesses(competitor_themes, data)
    
    # Create HTML report
    html_content = create_competitor_table_html(competitor_analysis, data)
    
    # Save to file
    output_file = "reports/step3_competitor_analysis_LATEST.html"
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"[SUCCESS] Step 3 competitor analysis saved to {output_file}")
    
    # Print summary
    print("\nCompetitor Analysis Summary:")
    for brand, analysis in competitor_analysis.items():
        print(f"\n{brand}:")
        strengths_display = analysis['strengths'] if isinstance(analysis['strengths'], str) else ', '.join(analysis['strengths']) if analysis['strengths'] else 'None identified'
        weaknesses_display = analysis['weaknesses'] if isinstance(analysis['weaknesses'], str) else ', '.join(analysis['weaknesses']) if analysis['weaknesses'] else 'None identified'
        print(f"  Strengths: {strengths_display}")
        print(f"  Weaknesses: {weaknesses_display}")

if __name__ == "__main__":
    main()