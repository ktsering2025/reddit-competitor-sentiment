"""
WORKING REDDIT SCRAPER - NO AUTHENTICATION REQUIRED
===================================================

This scraper uses Reddit's public JSON API without authentication
to get ALL r/hellofresh data and competitor data.
"""
import requests
import json
import time
from datetime import datetime, timedelta
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
        
        # HelloFresh brands (COMPLETE FAMILY)
        self.hellofresh_brands = [
            "HelloFresh","hello fresh","hello-fresh",
            "Factor","factor meals","factor75",
            "EveryPlate","every plate","every-plate",
            "Green Chef","green chef","green-chef",
            "Chef's Plate","chefs plate","chefs-plate"
        ]
        
        # Competitors (EXPANDED LIST - ALL MAJOR MEAL DELIVERY)
        self.competitors = [
            # Major Meal Kits
            "Blue Apron", "Home Chef", "Sunbasket", "Purple Carrot",
            "Marley Spoon", "Gobble", "CookUnity", "Daily Harvest",
            "Freshly", "Territory Foods", "Trifecta", "Snap Kitchen",
            
            # Meat/Protein Delivery  
            "ButcherBox", "Crowd Cow", "Omaha Steaks", "Wild Alaskan Company",
            
            # Health/Specialty
            "HungryRoot", "Fresh n' Lean", "Sakara", "Splendid Spoon",
            
            # Pet Food Delivery
            "The Farmer's Dog", "Ollie", "Nom Nom", "Pet Plate",
            
            # Grocery Delivery
            "FreshDirect", "Thrive Market", "Instacart", "Amazon Fresh"
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
        """Format Reddit post data (filter for last 7 days only)"""
        try:
            # Calculate 7 days ago timestamp for weekly filtering
            seven_days_ago = datetime.now() - timedelta(days=7)
            seven_days_timestamp = seven_days_ago.timestamp()
            
            # Filter for posts from last 7 days only
            post_created = post_data.get('created_utc', 0)
            if post_created < seven_days_timestamp:
                return None  # Skip posts older than 7 days
            
            title = post_data.get('title', '')
            selftext = post_data.get('selftext', '')
            
            # Extract competitor mentions
            text = f"{title} {selftext}".lower()
            mentioned_brands = []
            
            # Check HelloFresh brands (improved detection)
            for brand in self.hellofresh_brands:
                if brand.lower() in text:
                    # Normalize brand names for consistency
                    if "hello" in brand.lower():
                        mentioned_brands.append("HelloFresh")
                    elif "factor" in brand.lower():
                        mentioned_brands.append("Factor") 
                    elif "every" in brand.lower():
                        mentioned_brands.append("EveryPlate")
                    elif "green" in brand.lower():
                        mentioned_brands.append("Green Chef")
                    else:
                        mentioned_brands.append(brand)
                    break  # Avoid duplicates
            
            # Check competitors
            for competitor in self.competitors:
                if competitor.lower() in text:
                    mentioned_brands.append(competitor)
                    break  # Avoid duplicates
            
            # Special case: if post is from hellofresh subreddit, always include HelloFresh
            subreddit = post_data.get('subreddit', '').lower()
            if subreddit == 'hellofresh' and 'HelloFresh' not in mentioned_brands:
                mentioned_brands.append('HelloFresh')
            
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
        """Scrape weekly data from Reddit (last 7 days only)"""
        print("WORKING REDDIT SCRAPER - WEEKLY DATA COLLECTION")
        print("=" * 60)
        print("Collecting posts from last 7 days only...")
        
        # Calculate and display the date range being scraped
        seven_days_ago = datetime.now() - timedelta(days=7)
        print(f"Date range: {seven_days_ago.strftime('%b %d')} - {datetime.now().strftime('%b %d, %Y')}")
        
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
        
        # Phase 2: Get competitor subreddit posts (EXPANDED)
        print("\n#  PHASE 2: Getting competitor subreddit posts...")
        competitor_subreddits = {
            "Blue Apron": ["blueapron", "mealkits", "cooking"],
            "Home Chef": ["homechef", "mealkits", "cooking"],
            "ButcherBox": ["ButcherBox", "mealkits", "meat"],
            "HungryRoot": ["mealkits", "mealprep", "healthyfood"],
            "Sunbasket": ["mealkits", "HealthyFood", "organic"],
            "Marley Spoon": ["marleyspoon", "mealkits"],
            "Gobble": ["mealkits", "cooking"],
            "CookUnity": ["mealkits", "mealprep"],
            "Purple Carrot": ["mealkits", "vegan", "PlantBasedDiet"],
            "Freshly": ["mealkits", "mealprep"],
            "The Farmer's Dog": ["dogfood", "dogs", "pets"],
            "Ollie": ["dogfood", "dogs", "pets"],
            "Nom Nom": ["dogfood", "dogs", "pets"]
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
        
        # Phase 3: Search general subreddits (EXPANDED FOR MORE POSTS)
        print("\n#  PHASE 3: Searching general subreddits...")
        general_subreddits = [
            # Food/Cooking subreddits
            "MealKits", "mealprep", "cooking", "food", "recipes", "FoodPorn",
            "HealthyFood", "nutrition", "EatCheapAndHealthy", "1200isplenty",
            
            # Diet/Lifestyle subreddits  
            "keto", "paleo", "vegan", "vegetarian", "PlantBasedDiet",
            "intermittentfasting", "fitness", "weightloss", "loseit",
            
            # Money/Shopping subreddits
            "frugal", "BuyItForLife", "Frugal_Jerk", "personalfinance",
            "coupon", "deals", "DealsReddit",
            
            # Review/Discussion subreddits
            "ProductPorn", "reviewthis", "BuyItForLife", "antiMLM",
            "mildlyinteresting", "foodhacks", "lifehacks",
            
            # Pet subreddits (for pet food brands)
            "dogs", "dogfood", "pets", "puppy", "DogCare"
        ]
        
        for subreddit in general_subreddits:
            try:
                # Get more posts from each subreddit to find more brand mentions
                for sort_method in ['hot', 'new']:
                    posts = self.get_subreddit_posts(subreddit, sort=sort_method, limit=50)
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
