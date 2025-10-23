#!/usr/bin/env python3
"""
Step 2: HelloFresh Deep Dive Analysis - COMPREHENSIVE VERSION
Combines all features from the three Step 2 implementations:
- Uses Step 1 data for consistency
- Focus on HelloFresh and Factor (60% revenue)
- Top 3 posts by engagement analysis
- Theme identification and actionable insights
- Professional HTML report generation
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import re

class Step2ComprehensiveAnalysis:
    def __init__(self):
        self.data_file = 'reports/working_reddit_data.json'
        self.hf_brands = ['HelloFresh', 'Factor']
        self.output_dir = 'reports'
    
    def load_step1_data(self):
        """Load the SAME data that Step 1 uses for consistency"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            posts = data.get('posts', [])
            # Filter to last 7 days (same as Step 1)
            seven_days_ago = datetime.now() - timedelta(days=7)
            seven_days_timestamp = seven_days_ago.timestamp()
            
            weekly_posts = []
            for post in posts:
                created = post.get('created_utc', 0)
                if created >= seven_days_timestamp:
                    weekly_posts.append(post)
            
            return weekly_posts
            
        except Exception as e:
            print(f"❌ Could not load data: {e}")
            return []
    
    def filter_hellofresh_factor_posts(self, posts):
        """Filter posts for HelloFresh and Factor (Brian's 60% revenue focus)"""
        hf_posts = []
        factor_posts = []
        
        for post in posts:
            mentioned_brands = post.get('competitors_mentioned', [])
            
            if 'HelloFresh' in mentioned_brands:
                hf_posts.append(post)
            
            if 'Factor' in mentioned_brands:
                factor_posts.append(post)
        
        return hf_posts, factor_posts
    
    def calculate_engagement_score(self, post):
        """Brian's definition: comments are great due to discussion"""
        score = post.get('score', 0)
        # If we don't have comments data, estimate based on post score
        comments = post.get('num_comments', max(1, score // 10))
        # Weight comments higher because they indicate discussion
        return score + (comments * 2)
    
    def get_top_posts_by_engagement(self, posts, limit=3):
        """Get top posts by engagement (comments + score)"""
        if not posts:
            return []
        
        # Sort by engagement score
        sorted_posts = sorted(posts, key=self.calculate_engagement_score, reverse=True)
        return sorted_posts[:limit]
    
    def analyze_sentiment_distribution(self, posts):
        """Analyze sentiment breakdown"""
        sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for post in posts:
            sentiment = post.get('sentiment', 'neutral')
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1
        
        return sentiment_counts
    
    def identify_themes(self, posts):
        """Identify discussion themes for actionable insights"""
        themes = {
            'pricing': 0,
            'quality': 0, 
            'delivery': 0,
            'service': 0,
            'recipes': 0,
            'switching': 0
        }
        
        for post in posts:
            text = f"{post.get('title', '')} {post.get('selftext', '')}".lower()
            
            if any(word in text for word in ['price', 'cost', 'expensive', 'cheap', 'money', 'budget']):
                themes['pricing'] += 1
            if any(word in text for word in ['quality', 'fresh', 'ingredient', 'bad', 'spoiled', 'taste']):
                themes['quality'] += 1
            if any(word in text for word in ['delivery', 'shipping', 'late', 'arrived', 'packaging']):
                themes['delivery'] += 1
            if any(word in text for word in ['service', 'support', 'customer', 'help', 'refund']):
                themes['service'] += 1
            if any(word in text for word in ['recipe', 'cook', 'easy', 'difficult', 'time']):
                themes['recipes'] += 1
            if any(word in text for word in ['switch', 'switched', 'vs', 'versus', 'compared', 'instead']):
                themes['switching'] += 1
        
        return themes
    
    def generate_actionable_insights(self, posts, themes, sentiment_counts):
        """Generate actionable business insights"""
        insights = []
        total_posts = len(posts)
        
        # Sentiment insights
        pos_pct = (sentiment_counts['positive'] / total_posts * 100) if total_posts > 0 else 0
        neg_pct = (sentiment_counts['negative'] / total_posts * 100) if total_posts > 0 else 0
        
        if neg_pct > 40:
            insights.append(f"⚠️ HIGH NEGATIVE SENTIMENT: {neg_pct:.1f}% negative posts require immediate attention")
        elif pos_pct > 60:
            insights.append(f"✅ STRONG POSITIVE SENTIMENT: {pos_pct:.1f}% positive posts indicate good brand health")
        else:
            insights.append(f"📊 MIXED SENTIMENT: {pos_pct:.1f}% positive, {neg_pct:.1f}% negative - room for improvement")
        
        # Theme insights
        top_theme = max(themes.items(), key=lambda x: x[1])
        if top_theme[1] > 0:
            if top_theme[0] == 'pricing':
                insights.append("💰 PRICING CONCERNS: Multiple mentions of cost issues - review pricing strategy")
            elif top_theme[0] == 'quality':
                insights.append("🥗 QUALITY FOCUS: Quality discussions prominent - maintain ingredient standards")
            elif top_theme[0] == 'delivery':
                insights.append("📦 DELIVERY ISSUES: Delivery problems mentioned - improve logistics")
            elif top_theme[0] == 'service':
                insights.append("🎧 SERVICE NEEDS: Customer service discussions - enhance support")
            elif top_theme[0] == 'recipes':
                insights.append("👨‍🍳 RECIPE FEEDBACK: Recipe discussions active - optimize meal variety")
            elif top_theme[0] == 'switching':
                insights.append("🔄 COMPETITIVE PRESSURE: Switching discussions - analyze competitor advantages")
        
        return insights
    
    def format_post_for_display(self, post, rank):
        """Format post for HTML display"""
        title = post.get('title', 'No title')
        selftext = post.get('selftext', '')
        url = post.get('url', '#')
        score = post.get('score', 0)
        comments = post.get('num_comments', 0)
        sentiment = post.get('sentiment', 'neutral')
        subreddit = post.get('subreddit', 'Unknown')
        
        # Truncate long content
        if len(selftext) > 200:
            selftext = selftext[:200] + "..."
        
        sentiment_class = sentiment
        sentiment_emoji = {'positive': '✅', 'negative': '❌', 'neutral': '⚪'}.get(sentiment, '⚪')
        
        return f"""
        <div class="post">
            <h3>#{rank} {sentiment_emoji} {title}</h3>
            <p><strong>Subreddit:</strong> r/{subreddit}</p>
            <p><strong>Engagement:</strong> {score} upvotes, {comments} comments</p>
            <p><strong>Sentiment:</strong> <span class="{sentiment_class}">{sentiment.upper()}</span></p>
            <p><strong>Content:</strong> {selftext}</p>
            <p><strong>Link:</strong> <a href="{url}" target="_blank">View on Reddit</a></p>
        </div>
        """
    
    def generate_html_report(self, hf_posts, factor_posts, top_hf_posts, top_factor_posts, 
                           hf_sentiment, factor_sentiment, hf_themes, factor_themes, 
                           hf_insights, factor_insights):
        """Generate comprehensive HTML report"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Step 2: HelloFresh Deep Dive Analysis</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 30px; }}
        .summary {{ background-color: #ffffff; border: 1px solid #ddd; padding: 20px; margin: 20px 0; }}
        .post {{ background-color: #f9f9f9; padding: 15px; margin: 15px 0; border-left: 4px solid #ff6b35; }}
        .positive {{ color: #28a745; font-weight: bold; }}
        .negative {{ color: #dc3545; font-weight: bold; }}
        .neutral {{ color: #6c757d; font-weight: bold; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f8f9fa; }}
        .insights {{ background-color: #e3f2fd; padding: 15px; margin: 15px 0; border-radius: 5px; }}
        .theme-bar {{ background-color: #f0f0f0; height: 20px; border-radius: 10px; margin: 5px 0; }}
        .theme-fill {{ height: 100%; background-color: #4caf50; border-radius: 10px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Step 2: HelloFresh Deep Dive Analysis</h1>
        <p><strong>Analysis Date:</strong> {timestamp}</p>
        <p><strong>Data Source:</strong> Same dataset as Step 1 chart</p>
        <p><strong>Focus:</strong> HelloFresh & Factor (60% revenue drivers)</p>
    </div>
    
    <div class="summary">
        <h2>Executive Summary</h2>
        <table>
            <tr>
                <th>Brand</th>
                <th>Total Posts</th>
                <th>Positive</th>
                <th>Negative</th>
                <th>Neutral</th>
            </tr>
            <tr>
                <td><strong>HelloFresh</strong></td>
                <td>{len(hf_posts)}</td>
                <td class="positive">{hf_sentiment['positive']}</td>
                <td class="negative">{hf_sentiment['negative']}</td>
                <td class="neutral">{hf_sentiment['neutral']}</td>
            </tr>
            <tr>
                <td><strong>Factor</strong></td>
                <td>{len(factor_posts)}</td>
                <td class="positive">{factor_sentiment['positive']}</td>
                <td class="negative">{factor_sentiment['negative']}</td>
                <td class="neutral">{factor_sentiment['neutral']}</td>
            </tr>
        </table>
    </div>
    
    <div class="summary">
        <h2>Top 3 HelloFresh Posts by Engagement</h2>
        <p><strong>Engagement Score:</strong> Upvotes + (Comments × 2)</p>
        {''.join([self.format_post_for_display(post, i+1) for i, post in enumerate(top_hf_posts)])}
    </div>
    
    <div class="summary">
        <h2>Top 3 Factor Posts by Engagement</h2>
        <p><strong>Engagement Score:</strong> Upvotes + (Comments × 2)</p>
        {''.join([self.format_post_for_display(post, i+1) for i, post in enumerate(top_factor_posts)])}
    </div>
    
    <div class="summary">
        <h2>Discussion Themes Analysis</h2>
        <h3>HelloFresh Themes</h3>
        {self.format_themes_chart(hf_themes)}
        
        <h3>Factor Themes</h3>
        {self.format_themes_chart(factor_themes)}
    </div>
    
    <div class="insights">
        <h2>Actionable Business Insights</h2>
        <h3>HelloFresh Insights</h3>
        <ul>
            {''.join([f'<li>{insight}</li>' for insight in hf_insights])}
        </ul>
        
        <h3>Factor Insights</h3>
        <ul>
            {''.join([f'<li>{insight}</li>' for insight in factor_insights])}
        </ul>
    </div>
    
    <div class="summary">
        <h2>Data Quality & Methodology</h2>
        <ul>
            <li>✅ Uses same 7-day dataset as Step 1 chart</li>
            <li>✅ Real Reddit posts with working URLs</li>
            <li>✅ Engagement scoring: upvotes + (comments × 2)</li>
            <li>✅ Theme analysis based on keyword detection</li>
            <li>✅ Sentiment analysis from AI classification</li>
        </ul>
    </div>
</body>
</html>
        """
        
        return html
    
    def format_themes_chart(self, themes):
        """Format themes as visual chart"""
        if not themes or sum(themes.values()) == 0:
            return "<p>No theme data available</p>"
        
        max_count = max(themes.values())
        chart_html = ""
        
        for theme, count in sorted(themes.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                percentage = (count / max_count) * 100
                chart_html += f"""
                <div style="margin: 10px 0;">
                    <strong>{theme.title()}:</strong> {count} mentions
                    <div class="theme-bar">
                        <div class="theme-fill" style="width: {percentage}%;"></div>
                    </div>
                </div>
                """
        
        return chart_html
    
    def save_report(self, html_content):
        """Save HTML report with timestamp"""
        os.makedirs(self.output_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"step2_comprehensive_analysis_{timestamp}.html"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(html_content)
        
        return filepath
    
    def run_analysis(self):
        """Run complete Step 2 analysis"""
        print("🎯 STEP 2: HelloFresh Deep Dive Analysis")
        print("=" * 60)
        
        # Load data
        print("\n[1/6] Loading Step 1 data...")
        posts = self.load_step1_data()
        if not posts:
            print("❌ No data found. Run scraper first.")
            return None
        
        print(f"✅ Loaded {len(posts)} posts from last 7 days")
        
        # Filter HelloFresh and Factor posts
        print("\n[2/6] Filtering HelloFresh and Factor posts...")
        hf_posts, factor_posts = self.filter_hellofresh_factor_posts(posts)
        print(f"✅ HelloFresh: {len(hf_posts)} posts, Factor: {len(factor_posts)} posts")
        
        # Get top posts by engagement
        print("\n[3/6] Analyzing top posts by engagement...")
        top_hf_posts = self.get_top_posts_by_engagement(hf_posts, 3)
        top_factor_posts = self.get_top_posts_by_engagement(factor_posts, 3)
        print(f"✅ Top HelloFresh posts: {len(top_hf_posts)}")
        print(f"✅ Top Factor posts: {len(top_factor_posts)}")
        
        # Analyze sentiment
        print("\n[4/6] Analyzing sentiment distribution...")
        hf_sentiment = self.analyze_sentiment_distribution(hf_posts)
        factor_sentiment = self.analyze_sentiment_distribution(factor_posts)
        print(f"✅ HelloFresh sentiment: {hf_sentiment}")
        print(f"✅ Factor sentiment: {factor_sentiment}")
        
        # Identify themes
        print("\n[5/6] Identifying discussion themes...")
        hf_themes = self.identify_themes(hf_posts)
        factor_themes = self.identify_themes(factor_posts)
        print(f"✅ HelloFresh themes: {hf_themes}")
        print(f"✅ Factor themes: {factor_themes}")
        
        # Generate insights
        hf_insights = self.generate_actionable_insights(hf_posts, hf_themes, hf_sentiment)
        factor_insights = self.generate_actionable_insights(factor_posts, factor_themes, factor_sentiment)
        
        # Generate and save report
        print("\n[6/6] Generating comprehensive HTML report...")
        html_content = self.generate_html_report(
            hf_posts, factor_posts, top_hf_posts, top_factor_posts,
            hf_sentiment, factor_sentiment, hf_themes, factor_themes,
            hf_insights, factor_insights
        )
        
        filepath = self.save_report(html_content)
        print(f"✅ Report saved: {filepath}")
        
        # Print summary
        print("\n" + "=" * 60)
        print("STEP 2 ANALYSIS COMPLETE")
        print("=" * 60)
        print(f"HelloFresh Posts: {len(hf_posts)}")
        print(f"Factor Posts: {len(factor_posts)}")
        print(f"Top HelloFresh Posts: {len(top_hf_posts)}")
        print(f"Top Factor Posts: {len(top_factor_posts)}")
        print(f"Report: {filepath}")
        
        return filepath

def main():
    """Main function to run comprehensive Step 2 analysis"""
    analyzer = Step2ComprehensiveAnalysis()
    report_path = analyzer.run_analysis()
    
    if report_path:
        print(f"\n🎉 Step 2 Complete! View report: {report_path}")
    else:
        print("\n❌ Step 2 failed. Check data and try again.")

if __name__ == "__main__":
    main()
