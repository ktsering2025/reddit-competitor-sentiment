"""
CORE FILE FOR BRIAN'S PROJECT - Reddit Scraper
Purpose: Web scrapes Reddit daily to find competitor sentiment (Brian's main request)
What it does: Acts like a browser to download Reddit HTML and extract competitor mentions
Status: 70% complete - scraping works, need to connect to email delivery system
"""

import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
import re
from config import COMPETITORS

class ComprehensiveRedditScraper:
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        ]
        self.scraped_posts = []
        self.update_headers()
        
        # Dedicated subreddits for better data
        self.target_subreddits = {
            'meal_kit': ['hellofresh', 'MealKits', 'mealprep', 'MealPrepSunday'],
            'rte': ['MealKits', 'mealprep', 'HealthyFood'],
            'premium_meat': ['ButcherBox', 'Frugal', 'Cooking'],
            'pet_food': ['DogFood', 'puppy101', 'dogs', 'AskVet'],
            'vms': ['supplements', 'fitness', 'nutrition']
        }
    
    def update_headers(self):
        """Update headers to look like a real browser"""
        self.session.headers.update({
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        })
    
    def scrape_subreddit_directly(self, subreddit, limit=25):
        """
        Scrape a subreddit directly for recent posts
        This gets ALL recent discussions, not just brand searches
        """
        posts = []
        
        try:
            url = f"https://www.reddit.com/r/{subreddit}.json"
            params = {'limit': limit, 'sort': 'hot'}
            
            self.update_headers()
            response = self.session.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'data' in data and 'children' in data['data']:
                    for child in data['data']['children']:
                        post_data = child['data']
                        
                        # Extract post info
                        post = {
                            'title': post_data.get('title', ''),
                            'score': post_data.get('score', 0),
                            'url': f"https://reddit.com{post_data.get('permalink', '')}",
                            'subreddit': post_data.get('subreddit', ''),
                            'author': post_data.get('author', ''),
                            'created_utc': post_data.get('created_utc', 0),
                            'num_comments': post_data.get('num_comments', 0),
                            'selftext': post_data.get('selftext', '')[:300],
                            'timestamp': datetime.now(),
                            'source': f'subreddit_r_{subreddit}',
                            'competitors_mentioned': []
                        }
                        
                        # Check which competitors are mentioned
                        full_text = (post['title'] + ' ' + post['selftext']).lower()
                        for competitor_name in COMPETITORS.keys():
                            if competitor_name.lower() in full_text:
                                post['competitors_mentioned'].append(competitor_name)
                        
                        # Only include posts that mention competitors
                        if post['competitors_mentioned']:
                            posts.append(post)
                
                print(f"✅ r/{subreddit}: Found {len(posts)} posts with competitor mentions")
                
            else:
                print(f"❌ r/{subreddit}: Status {response.status_code}")
                
        except Exception as e:
            print(f"❌ r/{subreddit}: Error - {str(e)}")
        
        time.sleep(random.uniform(2, 4))
        return posts
    
    def search_brand_specifically(self, brand_name, subreddits, limit=10):
        """
        Search for specific brand mentions across multiple subreddits
        """
        posts = []
        
        for subreddit in subreddits:
            try:
                url = f"https://www.reddit.com/r/{subreddit}/search.json"
                params = {
                    'q': f'"{brand_name}"',  # Exact phrase search
                    'restrict_sr': 'on',
                    'sort': 'new',
                    'limit': limit,
                    't': 'month'  # Past month
                }
                
                self.update_headers()
                response = self.session.get(url, params=params, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if 'data' in data and 'children' in data['data']:
                        for child in data['data']['children']:
                            post_data = child['data']
                            
                            post = {
                                'title': post_data.get('title', ''),
                                'score': post_data.get('score', 0),
                                'url': f"https://reddit.com{post_data.get('permalink', '')}",
                                'subreddit': post_data.get('subreddit', ''),
                                'author': post_data.get('author', ''),
                                'num_comments': post_data.get('num_comments', 0),
                                'selftext': post_data.get('selftext', '')[:300],
                                'brand_mentioned': brand_name,
                                'timestamp': datetime.now(),
                                'source': f'search_{subreddit}',
                                'competitors_mentioned': [brand_name]
                            }
                            
                            # Add brand metadata
                            if brand_name in COMPETITORS:
                                post['brand_category'] = COMPETITORS[brand_name]['category']
                                post['is_hf_brand'] = COMPETITORS[brand_name]['hf_brand']
                                post['market_share'] = COMPETITORS[brand_name].get('market_share', 0)
                            
                            posts.append(post)
                
                print(f"   • r/{subreddit}: {len([p for p in posts if p.get('subreddit') == subreddit])} {brand_name} posts")
                
            except Exception as e:
                print(f"   • r/{subreddit}: Error - {str(e)}")
                
            time.sleep(random.uniform(1, 3))
        
        return posts
    
    def scrape_all_competitors(self):
        """
        Comprehensive scraping of ALL competitors across relevant subreddits
        """
        print("🚀 COMPREHENSIVE COMPETITOR SCRAPING")
        print("Getting data for ALL HelloFresh competitors...")
        print("=" * 70)
        
        all_posts = []
        
        # Step 1: Scrape dedicated subreddits for general discussions
        print("\n📍 STEP 1: Scraping dedicated subreddits...")
        key_subreddits = ['hellofresh', 'MealKits', 'ButcherBox', 'DogFood', 'mealprep']
        
        for subreddit in key_subreddits:
            posts = self.scrape_subreddit_directly(subreddit, limit=30)
            all_posts.extend(posts)
        
        # Step 2: Search for specific high-priority competitors
        print("\n🎯 STEP 2: Targeted brand searches...")
        priority_competitors = [
            ("HelloFresh", ['MealKits', 'mealprep', 'Frugal']),
            ("ButcherBox", ['Frugal', 'Cooking', 'BuyItForLife']),
            ("The Farmer's Dog", ['DogFood', 'dogs', 'puppy101']),
            ("Factor", ['MealKits', 'mealprep', 'fitness']),
            ("CookUnity", ['MealKits', 'mealprep']),
            ("Blue Apron", ['MealKits', 'mealprep']),
            ("Home Chef", ['MealKits', 'mealprep']),
            ("HungryRoot", ['MealKits', 'mealprep', 'HealthyFood'])
        ]
        
        for brand, subreddits in priority_competitors:
            print(f"\n🔍 Searching for {brand}:")
            brand_posts = self.search_brand_specifically(brand, subreddits, limit=5)
            all_posts.extend(brand_posts)
        
        # Remove duplicates based on URL
        unique_posts = []
        seen_urls = set()
        for post in all_posts:
            if post['url'] not in seen_urls:
                unique_posts.append(post)
                seen_urls.add(post['url'])
        
        self.scraped_posts = unique_posts
        
        print(f"\n🎉 SCRAPING COMPLETE!")
        print(f"📊 Total unique posts: {len(unique_posts)}")
        return unique_posts
    
    def get_comprehensive_summary(self):
        """Generate detailed summary for Brian"""
        if not self.scraped_posts:
            return "No data collected"
        
        # Group by competitors
        competitor_stats = {}
        for post in self.scraped_posts:
            for competitor in post.get('competitors_mentioned', []):
                if competitor not in competitor_stats:
                    competitor_stats[competitor] = {
                        'posts': 0,
                        'total_score': 0,
                        'total_comments': 0,
                        'subreddits': set()
                    }
                
                competitor_stats[competitor]['posts'] += 1
                competitor_stats[competitor]['total_score'] += post['score']
                competitor_stats[competitor]['total_comments'] += post['num_comments']
                competitor_stats[competitor]['subreddits'].add(post['subreddit'])
        
        # Convert sets to lists for display
        for competitor in competitor_stats:
            competitor_stats[competitor]['subreddits'] = list(competitor_stats[competitor]['subreddits'])
            competitor_stats[competitor]['avg_score'] = (
                competitor_stats[competitor]['total_score'] / competitor_stats[competitor]['posts']
                if competitor_stats[competitor]['posts'] > 0 else 0
            )
        
        return {
            'total_posts': len(self.scraped_posts),
            'competitors_found': len(competitor_stats),
            'competitor_breakdown': competitor_stats,
            'top_subreddits': list(set(p['subreddit'] for p in self.scraped_posts))
        }

def main():
    """Run comprehensive competitor scraping"""
    print("🍽️ HelloFresh Comprehensive Competitor Intelligence")
    print("Scraping ALL competitors across ALL relevant subreddits")
    print("=" * 70)
    
    scraper = ComprehensiveRedditScraper()
    posts = scraper.scrape_all_competitors()
    
    # Show detailed results
    print(f"\n📋 DETAILED RESULTS:")
    summary = scraper.get_comprehensive_summary()
    
    print(f"\n📊 OVERVIEW:")
    print(f"   • Total posts found: {summary['total_posts']}")
    print(f"   • Competitors mentioned: {summary['competitors_found']}")
    print(f"   • Subreddits covered: {len(summary['top_subreddits'])}")
    
    print(f"\n🏆 COMPETITOR BREAKDOWN:")
    for competitor, stats in summary['competitor_breakdown'].items():
        is_hf = COMPETITORS.get(competitor, {}).get('hf_brand', False)
        brand_type = "HF BRAND" if is_hf else "COMPETITOR"
        market_share = COMPETITORS.get(competitor, {}).get('market_share', 0)
        
        print(f"   • {competitor} ({brand_type}):")
        print(f"     - Posts: {stats['posts']}")
        print(f"     - Avg Score: {stats['avg_score']:.1f}")
        print(f"     - Total Comments: {stats['total_comments']}")
        print(f"     - Market Share: {market_share}%")
        print(f"     - Subreddits: {', '.join(stats['subreddits'][:3])}")
        print()
    
    # Show sample posts
    print(f"📝 SAMPLE POSTS:")
    for i, post in enumerate(posts[:5]):
        competitors = ', '.join(post['competitors_mentioned'])
        print(f"\n{i+1}. [{competitors}] (Score: {post['score']})")
        print(f"   📝 {post['title'][:80]}...")
        print(f"   📍 r/{post['subreddit']} | 💬 {post['num_comments']} comments")
        print(f"   🔗 {post['url']}")
    
    print(f"\n🎯 THIS IS THE DATA BRIAN WANTS:")
    print(f"   ✅ Complete competitor mentions across Reddit")
    print(f"   ✅ Volume comparison (post counts per competitor)")
    print(f"   ✅ Engagement data (scores, comments)")
    print(f"   ✅ Source tracking (which subreddits)")
    print(f"   ✅ Ready for sentiment analysis")

if __name__ == "__main__":
    main()