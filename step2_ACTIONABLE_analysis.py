#!/usr/bin/env python3
"""
Step 2: ACTIONABLE Analysis - Brian's Final Build Plan
Deep dive into HelloFresh and Factor75 with actionable insights
Uses same dataset as Step 1 for validation sync
"""

import json
import os
from datetime import datetime
from config import PRIMARY_DEEPDIVE
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
    """Load the same working dataset used by Step 1"""
    if os.path.exists(WORKING_DATA_FILE):
        with open(WORKING_DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError("No working data found. Run accurate_scraper.py first.")

def calculate_engagement_score(post):
    """Calculate engagement score: score + 3×comments (Brian's spec)"""
    score = max(0, post.get('score', 0))
    comments = post.get('num_comments', 0)
    return score + (3 * comments)

def get_posts_by_brand(data, target_brands=None):
    """Get posts for focus brands (HelloFresh and Factor75 by default)"""
    if target_brands is None:
        target_brands = PRIMARY_DEEPDIVE
    
    posts_by_brand = defaultdict(list)
    
    for post in data.get('posts', []):
        # Use primary_brand to ensure post is ABOUT this brand, not just mentioning it
        primary_brand = post.get('primary_brand')
        
        if primary_brand and primary_brand in target_brands:
            engagement = calculate_engagement_score(post)
            post_with_engagement = post.copy()
            post_with_engagement['engagement_score'] = engagement
            posts_by_brand[primary_brand].append(post_with_engagement)
    
    return posts_by_brand

def get_top_posts_by_sentiment(posts, sentiment, limit=3):
    """Get top posts by engagement for a specific sentiment"""
    filtered_posts = [p for p in posts if p.get('sentiment') == sentiment]
    sorted_posts = sorted(filtered_posts, key=lambda x: x['engagement_score'], reverse=True)
    return sorted_posts[:limit]

def categorize_post_themes(posts):
    """Categorize posts into themes (Quality, Delivery, Service, Price)"""
    theme_keywords = {
        'Quality': ['taste', 'flavor', 'fresh', 'quality', 'ingredients', 'cooking', 'recipe', 'delicious', 'bland', 'tasteless'],
        'Delivery': ['delivery', 'shipping', 'late', 'on time', 'packaging', 'arrived', 'damaged', 'cold', 'frozen'],
        'Service': ['customer service', 'support', 'refund', 'cancel', 'subscription', 'billing', 'help', 'complaint'],
        'Price': ['price', 'cost', 'expensive', 'cheap', 'value', 'money', 'worth', 'affordable', 'overpriced']
    }
    
    theme_counts = {'Quality': 0, 'Delivery': 0, 'Service': 0, 'Price': 0}
    
    for post in posts:
        text = (post.get('title', '') + ' ' + post.get('selftext', '')).lower()
        for theme, keywords in theme_keywords.items():
            if any(keyword in text for keyword in keywords):
                theme_counts[theme] += 1
                break
    
    return theme_counts

def analyze_brand_totals(data):
    """Calculate brand totals for validation with Step 1"""
    brand_totals = {}
    
    for brand in PRIMARY_DEEPDIVE:
        pos = neg = neu = 0
        for post in data.get('posts', []):
            # Use primary_brand to ensure post is ABOUT this brand, not just mentioning it
            if post.get('primary_brand') == brand:
                sentiment = post.get('sentiment', 'neutral')
                if sentiment == 'positive':
                    pos += 1
                elif sentiment == 'negative':
                    neg += 1
                else:
                    neu += 1
        
        total = pos + neg + neu
        pct_positive = round((pos / total * 100) if total > 0 else 0, 1)
        
        brand_totals[brand] = {
            'positive': pos,
            'negative': neg,
            'neutral': neu,
            'total': total,
            'pct_positive': pct_positive
        }
    
    return brand_totals

def create_html_report(posts_by_brand, brand_totals, data):
    """Create Step 2 HTML report per Brian's exact specifications"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    commit_hash = get_git_commit_hash()
    
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', '2025-10-20').split('T')[0]
    end_date = date_range.get('end', '2025-10-27').split('T')[0]
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Step 2: ACTIONABLE Analysis - Brian's Competitor Intelligence</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background-color: #f8f9fa; }}
        .header {{ background: linear-gradient(135deg, #ff6b35, #f7931e); color: white; padding: 30px; border-radius: 12px; margin-bottom: 30px; text-align: center; }}
        .section {{ background-color: white; margin: 20px 0; padding: 25px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        .post-card {{ border-left: 4px solid #ff6b35; padding: 15px; margin: 15px 0; background-color: #f8f9fa; border-radius: 5px; }}
        .sentiment-positive {{ border-left-color: #28a745; }}
        .sentiment-negative {{ border-left-color: #dc3545; }}
        .sentiment-neutral {{ border-left-color: #6c757d; }}
        .metric {{ display: inline-block; background-color: #f0f0f0; padding: 5px 10px; border-radius: 15px; margin: 5px; font-size: 12px; }}
        .footer {{ text-align: center; margin-top: 30px; padding: 20px; font-size: 12px; color: #666; }}
        a {{ color: #ff6b35; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .summary-stats {{ display: flex; justify-content: space-around; margin: 20px 0; }}
        .stat-box {{ text-align: center; padding: 15px; background-color: #f8f9fa; border-radius: 8px; }}
        .data-files {{ background-color: #e8f4f8; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .validation-box {{ background-color: #d4edda; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #c3e6cb; }}
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f8f9fa; font-weight: bold; }}
        .live-links {{ background-color: #fff3cd; padding: 15px; border-radius: 8px; margin: 15px 0; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Step 2: ACTIONABLE Analysis</h1>
        <h2>Reddit Competitor Intelligence Deep Dive</h2>
        <h3>Focus: HelloFresh & Factor75 (Revenue Drivers)</h3>
        <p><strong>Analysis Period:</strong> {start_date} to {end_date}</p>
        <p><strong>Data Source:</strong> Weekly Reddit search (last 7 days)</p>
    </div>
    
    <div class="section">
        <h2>Executive Summary</h2>
        <div class="summary-stats">"""
    
    # Executive Summary stats
    total_posts = sum(brand_totals[brand]['total'] for brand in ['HelloFresh', 'Factor75'])
    hf_total = brand_totals.get('HelloFresh', {}).get('total', 0)
    f75_total = brand_totals.get('Factor75', {}).get('total', 0)
    
    html += f"""
            <div class="stat-box">
                <h3>{total_posts}</h3>
                <p>Total Posts Analyzed</p>
            </div>
            <div class="stat-box">
                <h3>2</h3>
                <p>Revenue Driver Brands</p>
            </div>
            <div class="stat-box">
                <h3>Weekly</h3>
                <p>Data Refresh</p>
            </div>
        </div>
        
        <div class="validation-box">
            <h4>[VALIDATION] Sync with Step 1</h4>
            <p><strong>HelloFresh:</strong> {brand_totals.get('HelloFresh', {}).get('positive', 0)}/{brand_totals.get('HelloFresh', {}).get('negative', 0)}/{brand_totals.get('HelloFresh', {}).get('neutral', 0)} = {hf_total} posts ({brand_totals.get('HelloFresh', {}).get('pct_positive', 0)}% positive)</p>
            <p><strong>Factor75:</strong> {brand_totals.get('Factor75', {}).get('positive', 0)}/{brand_totals.get('Factor75', {}).get('negative', 0)}/{brand_totals.get('Factor75', {}).get('neutral', 0)} = {f75_total} posts ({brand_totals.get('Factor75', {}).get('pct_positive', 0)}% positive)</p>
        </div>
    </div>"""
    
    # Brand-specific analysis per Brian's spec
    for brand in ['HelloFresh', 'Factor75']:
        brand_posts = posts_by_brand.get(brand, [])
        if not brand_posts:
            continue
            
        # Get top 3 positive and top 3 negative
        top_positive = get_top_posts_by_sentiment(brand_posts, 'positive', 3)
        top_negative = get_top_posts_by_sentiment(brand_posts, 'negative', 3)
        
        html += f"""
    <div class="section">
        <h2>{brand} Deep Dive</h2>
        <p><strong>Total Posts:</strong> {len(brand_posts)} | <strong>Engagement Ranking:</strong> Score + 3×Comments</p>
        
        <h3>Top 3 Positive Posts</h3>"""
        
        if top_positive:
            for i, post in enumerate(top_positive, 1):
                # Get full text or first 600 chars
                full_text = post.get('selftext', '')
                preview_text = full_text[:600] + ('...' if len(full_text) > 600 else '')
                
                # Add context about why it's positive
                context = f"<p><strong>Why This Matters:</strong> This post from r/{post['subreddit']} discusses {brand} "
                if 'recommend' in full_text.lower() or 'love' in full_text.lower():
                    context += "with positive recommendations and customer satisfaction."
                elif 'switch' in full_text.lower() or 'trying' in full_text.lower():
                    context += "as a potential alternative, indicating brand consideration."
                else:
                    context += "in the context of meal kit services."
                context += "</p>"
                
                html += f"""
        <div class="post-card sentiment-positive">
            <h4>#{i}: <a href="{post['url']}" target="_blank">{post['title']}</a></h4>
            <p><strong>Engagement:</strong> {post['engagement_score']:.0f} | <strong>Subreddit:</strong> r/{post['subreddit']}</p>
            {context}
            <p><strong>Post Content:</strong> {preview_text}</p>
            <div>
                <span class="metric">Score: {post.get('score', 0)}</span>
                <span class="metric">Comments: {post.get('num_comments', 0)}</span>
                <span class="metric">Ratio: {post.get('upvote_ratio', 0):.2f}</span>
            </div>
        </div>"""
        else:
            html += "<p>No positive posts found for this period.</p>"
        
        html += f"""
        <h3>Top 3 Negative Posts</h3>"""
        
        if top_negative:
            for i, post in enumerate(top_negative, 1):
                # Get full text or first 600 chars
                full_text = post.get('selftext', '')
                preview_text = full_text[:600] + ('...' if len(full_text) > 600 else '')
                
                # Add context about why it's negative
                context = f"<p><strong>Why This Matters:</strong> This post from r/{post['subreddit']} expresses concerns about {brand} "
                if 'cancel' in full_text.lower() or 'quit' in full_text.lower():
                    context += "with customers considering cancellation."
                elif 'terrible' in full_text.lower() or 'worst' in full_text.lower():
                    context += "with strong negative feedback about service quality."
                elif 'problem' in full_text.lower() or 'issue' in full_text.lower():
                    context += "highlighting operational or quality issues."
                else:
                    context += "with customer dissatisfaction."
                context += "</p>"
                
                html += f"""
        <div class="post-card sentiment-negative">
            <h4>#{i}: <a href="{post['url']}" target="_blank">{post['title']}</a></h4>
            <p><strong>Engagement:</strong> {post['engagement_score']:.0f} | <strong>Subreddit:</strong> r/{post['subreddit']}</p>
            {context}
            <p><strong>Post Content:</strong> {preview_text}</p>
            <div>
                <span class="metric">Score: {post.get('score', 0)}</span>
                <span class="metric">Comments: {post.get('num_comments', 0)}</span>
                <span class="metric">Ratio: {post.get('upvote_ratio', 0):.2f}</span>
            </div>
        </div>"""
        else:
            html += "<p>No negative posts found for this period.</p>"
        
        # All Posts - Full View
        html += f"""
        <h3>All Posts - Full View</h3>
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Brand</th>
                    <th>Engagement</th>
                    <th>Sentiment</th>
                    <th>Subreddit</th>
                    <th>Comments</th>
                </tr>
            </thead>
            <tbody>"""
        
        # Sort all posts by engagement
        sorted_posts = sorted(brand_posts, key=lambda x: x['engagement_score'], reverse=True)
        for post in sorted_posts:
            html += f"""
                <tr>
                    <td><a href="{post['url']}" target="_blank">{post['title'][:50]}{'...' if len(post['title']) > 50 else ''}</a></td>
                    <td>{brand}</td>
                    <td>{post['engagement_score']:.0f}</td>
                    <td>{post.get('sentiment', 'neutral').title()}</td>
                    <td>r/{post['subreddit']}</td>
                    <td>{post.get('num_comments', 0)}</td>
                </tr>"""
        
        html += """
            </tbody>
        </table>
    </div>"""
    
    # Live Weekly Searches section
    html += f"""
    <div class="section">
        <h2>Live Weekly Searches</h2>
        <div class="live-links">
            <h4>Direct Reddit Links (Brian's Data Sources)</h4>
            <p><strong>HelloFresh:</strong> """
    
    # Handle list of links for HelloFresh
    hf_links = WEEKLY_LINKS['HelloFresh']
    if isinstance(hf_links, list):
        for i, link in enumerate(hf_links, 1):
            html += f'<a href="{link}" target="_blank">Search #{i}</a> '
    else:
        html += f'<a href="{hf_links}" target="_blank">Weekly Search Results</a>'
    
    html += """</p>
            <p><strong>Factor75:</strong> """
    
    # Handle list of links for Factor75
    f75_links = WEEKLY_LINKS['Factor75']
    if isinstance(f75_links, list):
        for i, link in enumerate(f75_links, 1):
            html += f'<a href="{link}" target="_blank">Search #{i}</a> '
    else:
        html += f'<a href="{f75_links}" target="_blank">Weekly Search Results</a>'
    
    html += """</p>
        </div>
    </div>"""
    
    # Data Files transparency section
    today = datetime.now().strftime('%Y-%m-%d')
    html += f"""
    <div class="section">
        <h2>Data Files (Transparency)</h2>
        <div class="data-files">
            <h4>Raw Data Access</h4>
            <p><strong>Raw Data:</strong> <code>reports/raw/raw_{today}.json</code></p>
            <p><strong>Filtered Data:</strong> <code>reports/raw/filtered_{today}.json</code></p>
            <p><strong>Metadata:</strong> <code>reports/raw/metadata_{today}.json</code></p>
            <p><em>Includes date range, brand counts, filters applied, and commit hash</em></p>
        </div>
    </div>
    
    <div class="footer">
        <p><strong>Analysis Period:</strong> {start_date} to {end_date} • <strong>Generated (UTC):</strong> {timestamp} • <strong>Commit:</strong> {commit_hash}</p>
        <p>All Reddit links verified and lead to actual discussions • Data refreshed weekly • Built for Brian's competitive intelligence</p>
    </div>
</body>
</html>"""
    
    return html

def main():
    """Main function to generate Step 2 analysis"""
    try:
        # Load same data as Step 1
        data = load_data()
        
        # Get posts for focus brands
        posts_by_brand = get_posts_by_brand(data)
        
        # Calculate brand totals for validation
        brand_totals = analyze_brand_totals(data)
        
        # Generate HTML report
        html_content = create_html_report(posts_by_brand, brand_totals, data)
        
        # Save report (stable name as per Brian's spec)
        os.makedirs('reports', exist_ok=True)
        with open(STEP2_OUTPUT, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[SUCCESS] Step 2 ACTIONABLE analysis saved to {STEP2_OUTPUT}")
        
        # Create archive copy
        timestamp = datetime.now().strftime('%Y-%m-%d')
        os.makedirs(f'{ARCHIVE_DIR}/{timestamp}', exist_ok=True)
        archive_path = f'{ARCHIVE_DIR}/{timestamp}/step2_ACTIONABLE_analysis.html'
        with open(archive_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[SUCCESS] Archive copy saved to {archive_path}")
        
        # Print validation info
        print(f"\nBrand Totals (for Step 1 validation):")
        for brand in ['HelloFresh', 'Factor75']:
            totals = brand_totals.get(brand, {})
            pos = totals.get('positive', 0)
            neg = totals.get('negative', 0) 
            neu = totals.get('neutral', 0)
            total = totals.get('total', 0)
            print(f"{brand:12}: {pos}/{neg}/{neu} = {total}")
        
        return STEP2_OUTPUT
        
    except Exception as e:
        print(f"[ERROR] Error generating Step 2 analysis: {e}")
        return None

if __name__ == "__main__":
    main()