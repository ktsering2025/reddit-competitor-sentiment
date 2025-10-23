#!/usr/bin/env python3
"""
Reddit Weekly Search Scraper
Searches Reddit for weekly posts about HelloFresh and Factor75 brands
"""

import requests
import json
import time
from datetime import datetime, timedelta
import re

class RedditWeeklySearch:
    def __init__(self):
        self.base_url = "https://www.reddit.com/search.json"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def search_reddit_weekly(self, query, limit=25):
        """Search Reddit for weekly posts about a specific query"""
        params = {
            'q': query,
            'sort': 'new',
            't': 'week',
            'limit': limit,
            'raw_json': 1
        }
        
        try:
            response = self.session.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            posts = []
            for post_data in data.get('data', {}).get('children', []):
                post = post_data.get('data', {})
                
                # Extract relevant information
                post_info = {
                    'title': post.get('title', ''),
                    'selftext': post.get('selftext', ''),
                    'subreddit': post.get('subreddit', ''),
                    'author': post.get('author', ''),
                    'score': post.get('score', 0),
                    'ups': post.get('ups', 0),
                    'num_comments': post.get('num_comments', 0),
                    'created_utc': post.get('created_utc', 0),
                    'url': f"https://reddit.com{post.get('permalink', '')}",
                    'permalink': post.get('permalink', ''),
                    'upvote_ratio': post.get('upvote_ratio', 1.0),
                    'is_self': post.get('is_self', True),
                    'brand_mentioned': self.determine_brand(post.get('title', ''), post.get('selftext', ''))
                }
                
                posts.append(post_info)
            
            return posts
            
        except Exception as e:
            print(f"Error searching Reddit for '{query}': {e}")
            return []
    
    def determine_brand(self, title, content):
        """Determine which brand is mentioned in the post"""
        full_text = f"{title} {content}".lower()
        
        if 'hellofresh' in full_text or 'hello fresh' in full_text:
            return 'HelloFresh'
        elif 'factor75' in full_text or 'factor 75' in full_text:
            return 'Factor75'
        elif 'factor' in full_text:
            return 'Factor'
        else:
            return 'Unknown'
    
    def search_hellofresh_weekly(self):
        """Search for HelloFresh posts from the last week"""
        print("Searching for HelloFresh posts from the last week...")
        posts = self.search_reddit_weekly('hellofresh', limit=30)
        
        # Filter for HelloFresh-specific posts
        hellofresh_posts = []
        for post in posts:
            if post['brand_mentioned'] in ['HelloFresh']:
                hellofresh_posts.append(post)
        
        print(f"Found {len(hellofresh_posts)} HelloFresh posts")
        return hellofresh_posts
    
    def search_factor75_weekly(self):
        """Search for Factor75 posts from the last week"""
        print("Searching for Factor75 posts from the last week...")
        posts = self.search_reddit_weekly('factor75', limit=30)
        
        # Also search for "factor 75" with space
        posts_space = self.search_reddit_weekly('factor 75', limit=30)
        
        # Combine and deduplicate
        all_posts = posts + posts_space
        unique_posts = []
        seen_urls = set()
        
        for post in all_posts:
            if post['url'] not in seen_urls:
                seen_urls.add(post['url'])
                unique_posts.append(post)
        
        # Filter for Factor75-specific posts
        factor_posts = []
        for post in unique_posts:
            if post['brand_mentioned'] in ['Factor75', 'Factor']:
                factor_posts.append(post)
        
        print(f"Found {len(factor_posts)} Factor75 posts")
        return factor_posts
    
    def search_hellofresh_factor_weekly(self):
        """Search for posts mentioning both HelloFresh and Factor75"""
        print("Searching for HelloFresh + Factor posts from the last week...")
        posts = self.search_reddit_weekly('hellofresh factor', limit=20)
        
        # Filter for posts mentioning both brands
        combined_posts = []
        for post in posts:
            if 'HelloFresh' in post['brand_mentioned'] or 'Factor' in post['brand_mentioned']:
                combined_posts.append(post)
        
        print(f"Found {len(combined_posts)} combined HelloFresh/Factor posts")
        return combined_posts
    
    def run_weekly_search(self):
        """Run complete weekly search for both brands"""
        print("=" * 60)
        print("REDDIT WEEKLY SEARCH - HelloFresh & Factor75")
        print("=" * 60)
        
        # Search for HelloFresh posts
        hellofresh_posts = self.search_hellofresh_weekly()
        
        # Search for Factor75 posts
        factor_posts = self.search_factor75_weekly()
        
        # Search for combined posts
        combined_posts = self.search_hellofresh_factor_weekly()
        
        # Combine all posts
        all_posts = hellofresh_posts + factor_posts + combined_posts
        
        # Remove duplicates
        unique_posts = []
        seen_urls = set()
        for post in all_posts:
            if post['url'] not in seen_urls:
                seen_urls.add(post['url'])
                unique_posts.append(post)
        
        print(f"\nTotal unique posts found: {len(unique_posts)}")
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/reddit_weekly_search_{timestamp}.json"
        
        data = {
            'search_timestamp': datetime.now().isoformat(),
            'total_posts': len(unique_posts),
            'hellofresh_posts': len(hellofresh_posts),
            'factor_posts': len(factor_posts),
            'combined_posts': len(combined_posts),
            'posts': unique_posts
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to: {filename}")
        
        # Print summary
        print("\n" + "=" * 60)
        print("WEEKLY SEARCH SUMMARY")
        print("=" * 60)
        print(f"HelloFresh posts: {len(hellofresh_posts)}")
        print(f"Factor75 posts: {len(factor_posts)}")
        print(f"Combined posts: {len(combined_posts)}")
        print(f"Total unique posts: {len(unique_posts)}")
        
        # Show top posts by engagement
        if unique_posts:
            print("\nTop 5 posts by engagement:")
            sorted_posts = sorted(unique_posts, key=lambda x: x['score'] + (x['num_comments'] * 2), reverse=True)
            for i, post in enumerate(sorted_posts[:5], 1):
                engagement = post['score'] + (post['num_comments'] * 2)
                print(f"{i}. {post['title'][:60]}... (Score: {engagement})")
                print(f"   Subreddit: r/{post['subreddit']} | Brand: {post['brand_mentioned']}")
                print(f"   URL: {post['url']}")
                print()
        
        return filename

if __name__ == "__main__":
    searcher = RedditWeeklySearch()
    searcher.run_weekly_search()
