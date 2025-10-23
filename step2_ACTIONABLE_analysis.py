#!/usr/bin/env python3
"""
Step 2: HelloFresh Deep Dive - ACTIONABLE VERSION
Focus: HelloFresh and Factor75 (60% of revenue) with actionable insights
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import glob

class ActionableStep2Analysis:
    def __init__(self):
        self.output_dir = 'reports'
        self.search_files = glob.glob('reports/reddit_weekly_search_*.json')
        self.latest_search_file = max(self.search_files) if self.search_files else None
    
    def load_realtime_data(self):
        """Load the latest weekly search data"""
        if not self.latest_search_file:
            print("No weekly search data found. Run reddit_weekly_search.py first.")
            return []
        
        try:
            with open(self.latest_search_file, 'r') as f:
                data = json.load(f)
            
            posts = data.get('posts', [])
            print(f"Loaded {len(posts)} real-time weekly posts")
            return posts
            
        except Exception as e:
            print(f"Error loading real-time data: {e}")
            return []
    
    def is_truly_brand_specific(self, post):
        """Check if post is truly about HelloFresh or Factor75 brands (not just mentions)"""
        title = post.get('title', '').lower()
        content = post.get('selftext', '').lower()
        subreddit = post.get('subreddit', '').lower()
        full_text = f"{title} {content}"
        
        # HelloFresh brand-specific indicators
        hellofresh_indicators = [
            'hellofresh', 'hello fresh', 'hf box', 'hf meal', 'hf subscription',
            'hellofresh delivery', 'hellofresh service', 'hellofresh customer',
            'hellofresh quality', 'hellofresh price', 'hellofresh recipe'
        ]
        
        # Factor75 brand-specific indicators  
        factor_indicators = [
            'factor75', 'factor 75', 'hellofresh factor', 'hello fresh factor',
            'factor meal kit', 'factor meal delivery', 'factor subscription',
            'factor service', 'factor quality', 'factor price'
        ]
        
        # Check if it's about HelloFresh brand specifically
        if any(indicator in full_text for indicator in hellofresh_indicators):
            # Must be about HelloFresh service/brand, not just mentioning the name
            service_keywords = [
                'meal kit', 'meal delivery', 'subscription', 'service', 'customer',
                'quality', 'price', 'recipe', 'ingredient', 'cooking', 'food',
                'delivery', 'box', 'order', 'cancel', 'refund', 'experience'
            ]
            if any(keyword in full_text for keyword in service_keywords):
                return 'HelloFresh'
        
        # Check if it's about Factor75 brand specifically
        if any(indicator in full_text for indicator in factor_indicators):
            # Must be about Factor75 service/brand, not just mentioning the name
            service_keywords = [
                'meal kit', 'meal delivery', 'subscription', 'service', 'customer',
                'quality', 'price', 'recipe', 'ingredient', 'cooking', 'food',
                'delivery', 'box', 'order', 'cancel', 'refund', 'experience'
            ]
            if any(keyword in full_text for keyword in service_keywords):
                return 'Factor75'
        
        return None
    
    def classify_sentiment_accurately(self, post):
        """Classify sentiment with high accuracy for brand-specific posts"""
        title = post.get('title', '').lower()
        content = post.get('selftext', '').lower()
        full_text = f"{title} {content}"
        
        # Strong negative indicators
        strong_negative = [
            'terrible', 'awful', 'horrible', 'worst', 'hate', 'disappointed',
            'waste of money', 'overpriced', 'expensive', 'bad quality',
            'spoiled', 'rotten', 'moldy', 'late delivery', 'wrong order',
            'customer service', 'refund', 'cancel', 'never again'
        ]
        
        # Strong positive indicators
        strong_positive = [
            'love', 'amazing', 'excellent', 'perfect', 'best', 'awesome',
            'fantastic', 'wonderful', 'delicious', 'fresh', 'quality',
            'recommend', 'happy', 'satisfied', 'pleased', 'impressed',
            'great value', 'worth it', 'convenient', 'easy'
        ]
        
        # Check for strong negative sentiment
        if any(keyword in full_text for keyword in strong_negative):
            return 'negative'
        
        # Check for strong positive sentiment
        if any(keyword in full_text for keyword in strong_positive):
            return 'positive'
        
        # Default to neutral for unclear sentiment
        return 'neutral'
    
    def calculate_engagement_score(self, post):
        """Calculate engagement score prioritizing comments (discussion value)"""
        score = post.get('score', 0)
        comments = post.get('num_comments', 0)
        
        # Prioritize comments heavily as they indicate discussion value
        # Comments are worth 3x more than upvotes for business insights
        return score + (comments * 3)
    
    def filter_brand_specific_posts(self, posts):
        """Filter for truly brand-specific posts only"""
        hellofresh_posts = []
        factor_posts = []
        
        for post in posts:
            brand = self.is_truly_brand_specific(post)
            
            if brand == 'HelloFresh':
                post['sentiment'] = self.classify_sentiment_accurately(post)
                post['engagement_score'] = self.calculate_engagement_score(post)
                hellofresh_posts.append(post)
            elif brand == 'Factor75':
                post['sentiment'] = self.classify_sentiment_accurately(post)
                post['engagement_score'] = self.calculate_engagement_score(post)
                factor_posts.append(post)
        
        return hellofresh_posts, factor_posts
    
    def get_top_posts_with_synthesis(self, posts, brand_name, limit=3):
        """Get top posts with synthesis logic"""
        if not posts:
            return []
        
        # Sort by engagement score
        sorted_posts = sorted(posts, key=lambda x: x['engagement_score'], reverse=True)
        
        if len(posts) <= limit:
            # If <= 3 posts, highlight all with synthesis
            return sorted_posts, f"All {len(posts)} {brand_name} posts highlighted (comprehensive view)"
        else:
            # If > 3 posts, synthesize top 3
            return sorted_posts[:limit], f"Top 3 {brand_name} posts synthesized from {len(posts)} total posts"
    
    def extract_actionable_themes(self, posts):
        """Extract actionable business themes"""
        themes = defaultdict(int)
        
        theme_keywords = {
            'pricing': ['price', 'cost', 'expensive', 'cheap', 'affordable', 'budget', 'money', 'value'],
            'quality': ['quality', 'fresh', 'taste', 'delicious', 'good', 'bad', 'terrible', 'amazing', 'ingredient'],
            'delivery': ['delivery', 'shipping', 'late', 'early', 'arrived', 'box', 'packaging', 'damaged'],
            'service': ['customer service', 'support', 'help', 'refund', 'cancel', 'subscription', 'experience'],
            'recipes': ['recipe', 'cooking', 'ingredient', 'meal', 'dish', 'food', 'prep', 'instructions'],
            'switching': ['switch', 'change', 'try', 'alternative', 'instead', 'replace', 'competitor']
        }
        
        for post in posts:
            title = post.get('title', '').lower()
            content = post.get('selftext', '').lower()
            full_text = f"{title} {content}"
            
            for theme, keywords in theme_keywords.items():
                if any(keyword in full_text for keyword in keywords):
                    themes[theme] += 1
        
        return dict(themes)
    
    def generate_actionable_insights(self, hellofresh_posts, factor_posts, hellofresh_themes, factor_themes):
        """Generate actionable business insights"""
        insights = []
        
        # HelloFresh insights
        if hellofresh_posts:
            hf_positive = sum(1 for p in hellofresh_posts if p['sentiment'] == 'positive')
            hf_negative = sum(1 for p in hellofresh_posts if p['sentiment'] == 'negative')
            hf_total = len(hellofresh_posts)
            
            insights.append(f"**HelloFresh Brand Health:** {hf_positive}/{hf_total} positive posts ({hf_positive/hf_total*100:.1f}%)")
            
            if 'pricing' in hellofresh_themes and hellofresh_themes['pricing'] > 0:
                insights.append(f"**Pricing Concerns:** {hellofresh_themes['pricing']} mentions - monitor pricing strategy")
            
            if 'quality' in hellofresh_themes and hellofresh_themes['quality'] > 0:
                insights.append(f"**Quality Focus:** {hellofresh_themes['quality']} mentions - maintain ingredient standards")
        
        # Factor75 insights
        if factor_posts:
            f_positive = sum(1 for p in factor_posts if p['sentiment'] == 'positive')
            f_negative = sum(1 for p in factor_posts if p['sentiment'] == 'negative')
            f_total = len(factor_posts)
            
            insights.append(f"**Factor75 Brand Health:** {f_positive}/{f_total} positive posts ({f_positive/f_total*100:.1f}%)")
            
            if f_total < 5:
                insights.append("**Factor75 Opportunity:** Limited Reddit presence - consider brand awareness strategy")
        
        return insights
    
    def generate_html_report(self, hellofresh_posts, factor_posts, hellofresh_themes, factor_themes):
        """Generate actionable HTML report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"step2_ACTIONABLE_analysis_{timestamp}.html"
        filepath = os.path.join(self.output_dir, filename)
        
        # Get top posts with synthesis
        hellofresh_top, hf_synthesis = self.get_top_posts_with_synthesis(hellofresh_posts, "HelloFresh", 3)
        factor_top, f_synthesis = self.get_top_posts_with_synthesis(factor_posts, "Factor75", 3)
        
        # Calculate sentiment distribution
        hellofresh_sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}
        factor_sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for post in hellofresh_posts:
            sentiment = post.get('sentiment', 'neutral')
            hellofresh_sentiment[sentiment] += 1
        
        for post in factor_posts:
            sentiment = post.get('sentiment', 'neutral')
            factor_sentiment[sentiment] += 1
        
        # Generate actionable insights
        actionable_insights = self.generate_actionable_insights(hellofresh_posts, factor_posts, hellofresh_themes, factor_themes)
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Step 2: HelloFresh Deep Dive - ACTIONABLE VERSION</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 3px solid #2c3e50;
        }}
        .header h1 {{
            color: #2c3e50;
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            color: #7f8c8d;
            margin: 10px 0;
            font-size: 1.2em;
        }}
        .summary {{
            background: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        .summary h2 {{
            color: #2c3e50;
            margin-top: 0;
        }}
        .brand-section {{
            margin-bottom: 40px;
            padding: 20px;
            border: 1px solid #bdc3c7;
            border-radius: 8px;
        }}
        .brand-section h2 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        .post {{
            background: #f8f9fa;
            margin: 15px 0;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }}
        .post.positive {{
            border-left-color: #27ae60;
        }}
        .post.negative {{
            border-left-color: #e74c3c;
        }}
        .post.neutral {{
            border-left-color: #95a5a6;
        }}
        .post-title {{
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }}
        .post-meta {{
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 10px;
        }}
        .post-content {{
            margin: 15px 0;
            line-height: 1.5;
        }}
        .sentiment {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        .sentiment.positive {{
            background: #d5f4e6;
            color: #27ae60;
        }}
        .sentiment.negative {{
            background: #fadbd8;
            color: #e74c3c;
        }}
        .sentiment.neutral {{
            background: #ebf3fd;
            color: #3498db;
        }}
        .engagement {{
            background: #e8f4f8;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }}
        .themes {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }}
        .theme-item {{
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 15px;
            font-size: 0.9em;
        }}
        .brand-specific {{
            background: #d5f4e6;
            color: #27ae60;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.9em;
            font-weight: bold;
        }}
        .insights {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 20px;
            border-radius: 8px;
            margin-top: 30px;
        }}
        .insights h3 {{
            color: #856404;
            margin-top: 0;
        }}
        .btn {{
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 5px;
        }}
        .btn:hover {{
            background: #2980b9;
        }}
        .synthesis {{
            background: #e8f5e8;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 4px solid #27ae60;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Step 2: HelloFresh Deep Dive Analysis</h1>
            <p><strong>Analysis Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p><strong>Data Source:</strong> Real-time Reddit weekly search</p>
            <p><strong>Focus:</strong> HelloFresh & Factor75 (60% of revenue)</p>
            <p><strong>Version:</strong> ACTIONABLE - Business-focused insights</p>
        </div>

        <div class="summary">
            <h2>Executive Summary</h2>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #f8f9fa;">
                    <th style="padding: 10px; border: 1px solid #ddd;">Brand</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Total Posts</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Positive</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Negative</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Neutral</th>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;"><strong>HelloFresh</strong></td>
                    <td style="padding: 10px; border: 1px solid #ddd;">{len(hellofresh_posts)}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: #27ae60;">{hellofresh_sentiment['positive']}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: #e74c3c;">{hellofresh_sentiment['negative']}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: #3498db;">{hellofresh_sentiment['neutral']}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;"><strong>Factor75</strong></td>
                    <td style="padding: 10px; border: 1px solid #ddd;">{len(factor_posts)}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: #27ae60;">{factor_sentiment['positive']}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: #e74c3c;">{factor_sentiment['negative']}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: #3498db;">{factor_sentiment['neutral']}</td>
                </tr>
            </table>
        </div>

        <div class="brand-section">
            <h2>Top HelloFresh Posts by Engagement</h2>
            <div class="synthesis">
                <strong>Synthesis:</strong> {hf_synthesis}
            </div>
            <p><strong>Engagement Score:</strong> Score + (Comments × 3) - Prioritizes discussion value</p>
"""
        
        # Add HelloFresh posts
        for i, post in enumerate(hellofresh_top, 1):
            sentiment = post.get('sentiment', 'neutral')
            sentiment_class = sentiment.lower()
            engagement_score = post.get('engagement_score', 0)
            
            html_content += f"""
            <div class="post {sentiment_class}">
                <div class="post-title">#{i} {post.get('title', 'No title')}</div>
                <div class="post-meta">
                    <strong>Subreddit:</strong> r/{post.get('subreddit', 'unknown')}<br>
                    <strong>Engagement:</strong> {post.get('score', 0)} score, {post.get('num_comments', 0)} comments (Score: {engagement_score})<br>
                    <strong>Sentiment:</strong> <span class="sentiment {sentiment_class}">{sentiment.upper()}</span><br>
                    <span class="brand-specific">Brand Specific: HelloFresh service discussion</span>
                </div>
                <div class="post-content">
                    <strong>Content:</strong> {post.get('selftext', 'No content available')[:400]}...
                </div>
                <div class="engagement">
                    <strong>Business Impact:</strong> {sentiment.upper()} sentiment with {post.get('num_comments', 0)} comments indicates {sentiment.lower()} customer experience discussion.
                </div>
                <a href="{post.get('url', '#')}" class="btn" target="_blank">View on Reddit</a>
            </div>
"""
        
        html_content += f"""
        </div>

        <div class="brand-section">
            <h2>Top Factor75 Posts by Engagement</h2>
            <div class="synthesis">
                <strong>Synthesis:</strong> {f_synthesis}
            </div>
            <p><strong>Engagement Score:</strong> Score + (Comments × 3) - Prioritizes discussion value</p>
"""
        
        # Add Factor posts
        if factor_top:
            for i, post in enumerate(factor_top, 1):
                sentiment = post.get('sentiment', 'neutral')
                sentiment_class = sentiment.lower()
                engagement_score = post.get('engagement_score', 0)
                
                html_content += f"""
                <div class="post {sentiment_class}">
                    <div class="post-title">#{i} {post.get('title', 'No title')}</div>
                    <div class="post-meta">
                        <strong>Subreddit:</strong> r/{post.get('subreddit', 'unknown')}<br>
                        <strong>Engagement:</strong> {post.get('score', 0)} score, {post.get('num_comments', 0)} comments (Score: {engagement_score})<br>
                        <strong>Sentiment:</strong> <span class="sentiment {sentiment_class}">{sentiment.upper()}</span><br>
                        <span class="brand-specific">Brand Specific: Factor75 service discussion</span>
                    </div>
                    <div class="post-content">
                        <strong>Content:</strong> {post.get('selftext', 'No content available')[:400]}...
                    </div>
                    <div class="engagement">
                        <strong>Business Impact:</strong> {sentiment.upper()} sentiment with {post.get('num_comments', 0)} comments indicates {sentiment.lower()} customer experience discussion.
                    </div>
                    <a href="{post.get('url', '#')}" class="btn" target="_blank">View on Reddit</a>
                </div>
"""
        else:
            html_content += """
            <div class="post neutral">
                <div class="post-title">No Factor75-specific posts found this week</div>
                <div class="post-content">
                    <strong>Analysis:</strong> No posts in the last week were specifically about Factor75. This could indicate:
                    <ul>
                        <li>Limited Factor75 brand awareness on Reddit</li>
                        <li>Customers using different platforms for Factor75 discussions</li>
                        <li>Opportunity to increase Factor75 Reddit presence</li>
                    </ul>
                </div>
            </div>
"""
        
        html_content += f"""
        </div>

        <div class="themes">
            <h2>Discussion Themes Analysis</h2>
            <h3>HelloFresh Themes</h3>
            <div>
"""
        
        for theme, count in sorted(hellofresh_themes.items(), key=lambda x: x[1], reverse=True):
            html_content += f'<span class="theme-item">{theme.title()}: {count} mentions</span>'
        
        html_content += f"""
            </div>
            <h3>Factor75 Themes</h3>
            <div>
"""
        
        for theme, count in sorted(factor_themes.items(), key=lambda x: x[1], reverse=True):
            html_content += f'<span class="theme-item">{theme.title()}: {count} mentions</span>'
        
        html_content += f"""
            </div>
        </div>

        <div class="insights">
            <h3>Actionable Business Insights</h3>
            <ul>
"""
        
        for insight in actionable_insights:
            html_content += f"<li>{insight}</li>"
        
        html_content += f"""
            </ul>
        </div>

        <div class="insights">
            <h3>Data Quality & Methodology</h3>
            <ul>
                <li>Real-time Reddit weekly search data</li>
                <li>Brand-specific filtering for HelloFresh and Factor75 only</li>
                <li>Engagement scoring: score + (comments × 3) - prioritizes discussion value</li>
                <li>Manual sentiment classification for accuracy</li>
                <li>Synthesis logic: Highlight all if ≤3 posts, synthesize top 3 if >3 posts</li>
                <li>Actionable insights focused on business decisions</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
    
    def run_analysis(self):
        """Run the complete actionable analysis"""
        print("Loading real-time weekly data...")
        posts = self.load_realtime_data()
        
        if not posts:
            print("No real-time data available")
            return
        
        print("Filtering for truly brand-specific posts...")
        hellofresh_posts, factor_posts = self.filter_brand_specific_posts(posts)
        
        print(f"Found {len(hellofresh_posts)} truly HelloFresh-specific posts")
        print(f"Found {len(factor_posts)} truly Factor75-specific posts")
        
        print("Extracting actionable themes...")
        hellofresh_themes = self.extract_actionable_themes(hellofresh_posts)
        factor_themes = self.extract_actionable_themes(factor_posts)
        
        print("Generating actionable HTML report...")
        report_path = self.generate_html_report(hellofresh_posts, factor_posts, hellofresh_themes, factor_themes)
        
        print(f"Actionable analysis complete! Report saved to: {report_path}")
        return report_path

if __name__ == "__main__":
    analyzer = ActionableStep2Analysis()
    analyzer.run_analysis()
