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

def generate_strengths_weaknesses(competitor_themes):
    """Generate strengths and weaknesses for each competitor"""
    results = {}
    
    for brand, themes in competitor_themes.items():
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
        
        results[brand] = {
            'strengths': strengths,
            'weaknesses': weaknesses
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
        strengths_text = ", ".join(analysis['strengths']) if analysis['strengths'] else "No clear strengths identified"
        weaknesses_text = ", ".join(analysis['weaknesses']) if analysis['weaknesses'] else "No major weaknesses identified"
        
        html += f"""
                <tr>
                    <td class="brand-name">{brand}</td>
                    <td class="strengths">{strengths_text}</td>
                    <td class="weaknesses">{weaknesses_text}</td>
                </tr>"""
    
    html += """
            </tbody>
        </table>
        
        <div class="summary">
            <h3>Key Insights</h3>
            <ul>
                <li>Analysis based on Reddit sentiment from the past week</li>
                <li>Strengths: Areas with 60%+ positive sentiment</li>
                <li>Weaknesses: Areas with 60%+ negative sentiment</li>
                <li>Data categorized by Quality, Delivery, Service, and Price themes</li>
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
    competitor_analysis = generate_strengths_weaknesses(competitor_themes)
    
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
        print(f"  Strengths: {', '.join(analysis['strengths']) if analysis['strengths'] else 'None identified'}")
        print(f"  Weaknesses: {', '.join(analysis['weaknesses']) if analysis['weaknesses'] else 'None identified'}")

if __name__ == "__main__":
    main()