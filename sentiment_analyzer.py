"""
Sentiment Analysis for Brian's Step 1: Stacked Bar Chart
Purpose: Classify Reddit posts as positive/negative/neutral for each competitor
Input: 33 Reddit posts from reddit_scraper.py
Output: Sentiment counts for stacked bar chart
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

class CompetitorSentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
        
        # Food industry specific keywords
        self.positive_keywords = [
            'love', 'amazing', 'best', 'great', 'excellent', 'recommend', 'fantastic',
            'delicious', 'fresh', 'quality', 'worth it', 'satisfied', 'perfect',
            'convenient', 'easy', 'tasty', 'helpful', 'impressed', 'favorite',
            'good', 'better', 'awesome', 'wonderful', 'nice'
        ]
        
        self.negative_keywords = [
            'hate', 'worst', 'terrible', 'awful', 'scam', 'expensive', 'overpriced',
            'spoiled', 'rotten', 'bad', 'poor', 'disappointed', 'waste', 'cancel',
            'regret', 'misleading', 'cheap', 'bland', 'disgusting', 'horrible',
            'sucks', 'fraud', 'ripoff', 'useless', 'garbage'
        ]
        
        self.neutral_keywords = [
            'review', 'comparison', 'compare', 'question', 'help', 'advice',
            'thoughts', 'opinions', 'experience', 'anyone', 'wondering'
        ]
    
    def count_keywords(self, text, keyword_list):
        """Count how many keywords from a list appear in text"""
        text_lower = text.lower()
        count = 0
        for keyword in keyword_list:
            if keyword in text_lower:
                count += 1
        return count
    
    def classify_post_sentiment(self, post):
        """
        Classify a single Reddit post as positive/negative/neutral
        """
        # Get full text
        title = post.get('title', '')
        selftext = post.get('selftext', '')
        full_text = f"{title} {selftext}"
        
        # VADER sentiment analysis
        vader_scores = self.vader.polarity_scores(full_text)
        vader_compound = vader_scores['compound']
        
        # Custom keyword analysis
        positive_count = self.count_keywords(full_text, self.positive_keywords)
        negative_count = self.count_keywords(full_text, self.negative_keywords)
        neutral_count = self.count_keywords(full_text, self.neutral_keywords)
        
        # Combined scoring (60% VADER, 40% keywords)
        vader_weight = 0.6
        keyword_weight = 0.4
        
        # Normalize keyword scores
        total_keywords = positive_count + negative_count + neutral_count
        if total_keywords > 0:
            keyword_score = (positive_count - negative_count) / total_keywords
        else:
            keyword_score = 0
        
        # Final combined score
        final_score = (vader_weight * vader_compound) + (keyword_weight * keyword_score)
        
        # Classification thresholds
        if final_score > 0.1:
            return 'positive'
        elif final_score < -0.1:
            return 'negative'
        else:
            return 'neutral'
    
    def analyze_all_posts(self, posts):
        """
        Analyze sentiment for all posts and group by competitor
        """
        sentiment_data = {}
        
        for post in posts:
            # Get competitors mentioned in this post
            competitors_mentioned = post.get('competitors_mentioned', [])
            
            # Classify the post sentiment
            sentiment = self.classify_post_sentiment(post)
            
            # Add to sentiment data for each competitor mentioned
            for competitor in competitors_mentioned:
                if competitor not in sentiment_data:
                    sentiment_data[competitor] = {
                        'positive': 0,
                        'negative': 0,
                        'neutral': 0,
                        'total': 0,
                        'posts': []
                    }
                
                # Increment sentiment count
                sentiment_data[competitor][sentiment] += 1
                sentiment_data[competitor]['total'] += 1
                
                # Store post details for debugging
                sentiment_data[competitor]['posts'].append({
                    'title': post.get('title', ''),
                    'sentiment': sentiment,
                    'score': post.get('score', 0),
                    'comments': post.get('num_comments', 0),
                    'url': post.get('url', ''),
                    'final_score': self.get_debug_score(post)
                })
        
        return sentiment_data
    
    def get_debug_score(self, post):
        """Get the actual sentiment score for debugging"""
        title = post.get('title', '')
        selftext = post.get('selftext', '')
        full_text = f"{title} {selftext}"
        
        vader_scores = self.vader.polarity_scores(full_text)
        return vader_scores['compound']
    
    def print_analysis_summary(self, sentiment_data):
        """Print a summary of the sentiment analysis"""
        print("SENTIMENT ANALYSIS RESULTS")
        print("=" * 50)
        
        total_posts = sum(data['total'] for data in sentiment_data.values())
        print(f"Total posts analyzed: {total_posts}")
        print(f"Competitors found: {len(sentiment_data)}")
        print()
        
        # Sort by total posts
        sorted_competitors = sorted(sentiment_data.items(), 
                                  key=lambda x: x[1]['total'], reverse=True)
        
        for competitor, data in sorted_competitors:
            pos = data['positive']
            neg = data['negative']
            neu = data['neutral']
            total = data['total']
            
            print(f"{competitor}:")
            print(f"  Total posts: {total}")
            print(f"  Positive: {pos} ({pos/total*100:.1f}%)")
            print(f"  Negative: {neg} ({neg/total*100:.1f}%)")
            print(f"  Neutral: {neu} ({neu/total*100:.1f}%)")
            print()
        
        return sentiment_data

def test_sentiment_analyzer():
    """Test the sentiment analyzer with current Reddit data"""
    from reddit_scraper import ComprehensiveRedditScraper
    
    print("TESTING SENTIMENT ANALYZER")
    print("=" * 50)
    
    # Get the current Reddit data
    scraper = ComprehensiveRedditScraper()
    posts = scraper.scrape_all_competitors()
    
    print(f"Loaded {len(posts)} posts from Reddit scraper")
    print()
    
    # Analyze sentiment
    analyzer = CompetitorSentimentAnalyzer()
    sentiment_data = analyzer.analyze_all_posts(posts)
    
    # Print summary
    analyzer.print_analysis_summary(sentiment_data)
    
    # Show some sample classifications
    print("SAMPLE CLASSIFICATIONS:")
    print("-" * 30)
    
    for competitor, data in list(sentiment_data.items())[:3]:
        print(f"\n{competitor} sample posts:")
        for post in data['posts'][:2]:  # Show first 2 posts
            print(f"  [{post['sentiment'].upper()}] {post['title'][:60]}...")
            print(f"    Score: {post['score']}, Comments: {post['comments']}")
            print(f"    Sentiment score: {post['final_score']:.3f}")
    
    return sentiment_data

if __name__ == "__main__":
    sentiment_data = test_sentiment_analyzer()