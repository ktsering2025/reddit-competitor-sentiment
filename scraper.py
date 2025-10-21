"""
WORKING REDDIT SCRAPER - NO AUTHENTICATION REQUIRED
===================================================

This scraper uses Reddit's public JSON API without authentication
to get ALL r/hellofresh data and competitor data.
"""
import requests
import json
import time
from datetime import datetime
from ai_sentiment import AdvancedSentimentAnalyzer

class WorkingRedditScraper:
    def __init__(self):
        """Initialize working Reddit scraper"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        self.sentiment_analyzer = AdvancedSentimentAnalyzer()
        
        # HelloFresh brands
        self.hellofresh_brands = [
            "HelloFresh","hello fresh","hello-fresh",
            "Factor","factor meals","factor75",
            "EveryPlate","every plate","every-plate",
            "Green Chef","green chef","green-chef",
            "Chef's Plate","chefs plate","chefs-plate"
        ]
        
        # Competitors
        self.competitors = [
            "ButcherBox", "HungryRoot", "Blue Apron", "Home Chef", 
            "Sunbasket", "Marley Spoon", "Gobble", "CookUnity",
            "Purple Carrot", "Daily Harvest", "The Farmer's Dog", 
            "Ollie", "Nom Nom"
        ]
    
    def get_subreddit_posts(self, subreddit, sort='hot', limit=100):
        """Get posts from subreddit using public JSON API"""
        posts = []
        
        try:
            # Use Reddit's public JSON API
            url = f"https://www.reddit.com/r/{subreddit}/{sort}.json"
            params = {'limit': limit}
            
            print(f"#  Getting {sort} posts from r/{subreddit}...")
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                
                for post_data in data.get('data', {}).get('children', []):
                    post = post_data.get('data', {})
                    if post:
                        formatted_post = self.format_post(post)
                        if formatted_post:
                            posts.append(formatted_post)
                
                print(f"#  Got {len(posts)} posts from r/{subreddit}")
            else:
                print(f"#  Error {response.status_code} accessing r/{subreddit}")
                
        except Exception as e:
            print(f"#  Exception accessing r/{subreddit}: {e}")
        
        return posts
    
    def format_post(self, post_data):
        """Format Reddit post data"""
        try:
            title = post_data.get('title', '')
            selftext = post_data.get('selftext', '')
            
            # Extract competitor mentions
            text = f"{title} {selftext}".lower()
            mentioned_brands = []
            
            # Check HelloFresh brands
            for brand in self.hellofresh_brands:
                if brand.lower() in text:
                    mentioned_brands.append(brand)
            
            # Check competitors
            for competitor in self.competitors:
                if competitor.lower() in text:
                    mentioned_brands.append(competitor)
            
            if not mentioned_brands:
                return None
            
            return {
                'title': title,
                'selftext': selftext,
                'score': post_data.get('score', 0),
                'num_comments': post_data.get('num_comments', 0),
                'subreddit': post_data.get('subreddit', ''),
                'url': f"https://reddit.com{post_data.get('permalink', '')}",
                'created_utc': post_data.get('created_utc', 0),
                'competitors_mentioned': mentioned_brands,
                'author': post_data.get('author', '[deleted]'),
                'upvote_ratio': post_data.get('upvote_ratio', 0),
                'is_self': post_data.get('is_self', False)
            }
            
        except Exception as e:
            print(f"# #  Error formatting post: {e}")
            return None
    
    def scrape_all_data(self):
        """Scrape ALL data from Reddit"""
        print("#  WORKING REDDIT SCRAPER - NO AUTH REQUIRED")
        print("=" * 60)
        
        all_posts = []
        
        # Phase 1: Get ALL r/hellofresh posts (multiple sorting methods)
        print("\n#  PHASE 1: Getting ALL r/hellofresh posts...")
        try:
            # Try different sorting methods
            for sort_method in ['hot', 'new', 'top']:
                posts = self.get_subreddit_posts('hellofresh', sort=sort_method, limit=100)
                all_posts.extend(posts)
                time.sleep(1)  # Rate limiting
            
            print(f"#  SUCCESS! Got {len(all_posts)} total posts from r/hellofresh")
        except Exception as e:
            print(f"#  Error accessing r/hellofresh: {e}")
        
        # Phase 2: Get competitor subreddit posts
        print("\n#  PHASE 2: Getting competitor subreddit posts...")
        competitor_subreddits = {
            "ButcherBox": ["ButcherBox", "mealkits"],
            "HungryRoot": ["mealkits", "mealprep"],
            "Blue Apron": ["mealkits", "cooking"],
            "Home Chef": ["mealkits", "cooking"],
            "Sunbasket": ["mealkits", "HealthyFood"],
            "Marley Spoon": ["mealkits"],
            "Gobble": ["mealkits"],
            "CookUnity": ["mealkits"],
            "The Farmer's Dog": ["dogfood", "dogs"],
            "Ollie": ["dogfood"],
            "Nom Nom": ["dogfood"]
        }
        
        for competitor, subreddits in competitor_subreddits.items():
            print(f"\n#  Getting {competitor} posts...")
            for subreddit in subreddits:
                try:
                    posts = self.get_subreddit_posts(subreddit, limit=50)
                    all_posts.extend(posts)
                    time.sleep(1)
                except Exception as e:
                    print(f"# #  Error accessing r/{subreddit}: {e}")
        
        # Phase 3: Search general subreddits
        print("\n#  PHASE 3: Searching general subreddits...")
        general_subreddits = [
            "MealKits", "mealprep", "cooking", "food", "recipes",
            "frugal", "BuyItForLife", "HealthyFood", "nutrition",
            "fitness", "weightloss", "keto", "paleo", "vegan"
        ]
        
        for subreddit in general_subreddits:
            try:
                posts = self.get_subreddit_posts(subreddit, limit=30)
                all_posts.extend(posts)
                time.sleep(1)
            except Exception as e:
                print(f"# #  Error accessing r/{subreddit}: {e}")
        
        # Remove duplicates based on URL
        unique_posts = []
        seen_urls = set()
        
        for post in all_posts:
            if post['url'] not in seen_urls:
                unique_posts.append(post)
                seen_urls.add(post['url'])
        
        print(f"\n#  SCRAPING COMPLETE!")
        print(f"   Total posts found: {len(all_posts)}")
        print(f"   Unique posts: {len(unique_posts)}")
        
        return unique_posts
    
    def analyze_sentiment(self, posts):
        """Analyze sentiment for all posts"""
        print("\n#  ANALYZING SENTIMENT FOR ALL POSTS...")
        print("=" * 50)
        
        analyzed_posts = []
        
        for i, post in enumerate(posts, 1):
            if i % 10 == 0:
                print(f"  Analyzing post {i}/{len(posts)}...")
            
            # Analyze sentiment
            sentiment_result = self.sentiment_analyzer.classify_post_sentiment(post)
            
            # Add sentiment to post
            post['sentiment'] = sentiment_result['sentiment']
            post['confidence'] = sentiment_result['confidence']
            post['reasoning'] = sentiment_result['reasoning']
            
            analyzed_posts.append(post)
        
        return analyzed_posts
    
    def save_data(self, posts, filename='reports/working_reddit_data.json'):
        """Save scraped data to JSON file"""
        data = {
            'scrape_timestamp': datetime.now().isoformat(),
            'total_posts': len(posts),
            'posts': posts
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Data saved to: {filename}")
    
    def print_summary(self, posts):
        """Print comprehensive summary"""
        print("\n#  COMPREHENSIVE DATA SUMMARY")
        print("=" * 50)
        
        # Count by brand
        brand_counts = {}
        for post in posts:
            for brand in post['competitors_mentioned']:
                brand_counts[brand] = brand_counts.get(brand, 0) + 1
        
        print(f"Total unique posts: {len(posts)}")
        print(f"Brands mentioned: {len(brand_counts)}")
        print("\nTop brands by mention count:")
        
        sorted_brands = sorted(brand_counts.items(), key=lambda x: x[1], reverse=True)
        for brand, count in sorted_brands[:20]:
            print(f"  {brand}: {count} posts")
        
        # Sentiment breakdown
        sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
        for post in posts:
            sentiment_counts[post['sentiment']] += 1
        
        total = len(posts)
        print(f"\n#  OVERALL SENTIMENT BREAKDOWN:")
        print(f"🟢 Positive: {sentiment_counts['positive']} ({sentiment_counts['positive']/total*100:.1f}%)")
        print(f"🔴 Negative: {sentiment_counts['negative']} ({sentiment_counts['negative']/total*100:.1f}%)")
        print(f"⚪ Neutral:  {sentiment_counts['neutral']} ({sentiment_counts['neutral']/total*100:.1f}%)")
        
        # Subreddit breakdown
        subreddit_counts = {}
        for post in posts:
            subreddit = post['subreddit']
            subreddit_counts[subreddit] = subreddit_counts.get(subreddit, 0) + 1
        
        print(f"\nTop subreddits:")
        sorted_subreddits = sorted(subreddit_counts.items(), key=lambda x: x[1], reverse=True)
        for subreddit, count in sorted_subreddits[:15]:
            print(f"  r/{subreddit}: {count} posts")

def main():
    """Main function to run working scraper"""
    print("#  WORKING REDDIT SCRAPER - NO AUTHENTICATION REQUIRED")
    print("=" * 60)
    
    # Initialize scraper
    scraper = WorkingRedditScraper()
    
    # Scrape data
    posts = scraper.scrape_all_data()
    
    if not posts:
        print("#  No posts found!")
        return
    
    # Analyze sentiment
    analyzed_posts = scraper.analyze_sentiment(posts)
    
    # Save data
    scraper.save_data(analyzed_posts)
    
    # Print summary
    scraper.print_summary(analyzed_posts)
    
    print(f"\n#  WORKING SCRAPER COMPLETE!")
    print(f"   Ready to update Step 1 chart with {len(analyzed_posts)} posts!")

if __name__ == "__main__":
    main()
