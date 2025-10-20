"""
Verify Reddit Data is Real and Accurate
Checks: 1) Real posts exist 2) Recent data 3) Sentiment accuracy
"""

from scraper import ComprehensiveRedditScraper
from ai_sentiment import AdvancedSentimentAnalyzer
from datetime import datetime, timedelta
import random

def verify_reddit_data():
    """Comprehensive verification of Reddit data accuracy"""
    
    print("REDDIT DATA VERIFICATION")
    print("=" * 70)
    
    # Step 1: Get data
    print("\n[1/4] Scraping Reddit data...")
    scraper = ComprehensiveRedditScraper()
    posts = scraper.scrape_all_competitors()
    
    print(f"Found {len(posts)} posts")
    
    # Step 2: Verify real Reddit posts
    print("\n[2/4] Verifying real Reddit posts...")
    print("MANUAL VERIFICATION - Check these URLs in your browser:")
    print("-" * 70)
    
    sample_posts = random.sample(posts, min(5, len(posts)))
    for i, post in enumerate(sample_posts, 1):
        print(f"\nPost {i}:")
        print(f"Title: {post['title']}")
        print(f"URL: {post['url']}")
        print(f"Subreddit: r/{post['subreddit']}")
        print(f"Score: {post['score']} | Comments: {post['num_comments']}")
        print(f"\nAction: Open this URL and verify:")
        print(f"  1. Does the post exist on Reddit?")
        print(f"  2. Does the title match?")
        print(f"  3. Is the score/comment count roughly correct?")
    
    # Step 3: Check post freshness
    print("\n[3/4] Checking post freshness...")
    now = datetime.now()
    recent_count = 0
    old_count = 0
    
    for post in posts:
        created = datetime.fromtimestamp(post.get('created_utc', 0))
        age_days = (now - created).days
        
        if age_days <= 30:
            recent_count += 1
        else:
            old_count += 1
    
    print(f"\nPost Age Analysis:")
    print(f"Total posts: {len(posts)}")
    print(f"Posts from last 30 days: {recent_count}")
    print(f"Posts older than 30 days: {old_count}")
    
    if recent_count >= len(posts) * 0.7:
        print("GOOD: Most posts are recent (last 30 days)")
    else:
        print("WARNING: Many posts are old - consider updating scraper")
    
    # Step 4: Test sentiment accuracy
    print("\n[4/4] Testing sentiment accuracy...")
    analyzer = AdvancedSentimentAnalyzer()
    
    # Test specific problematic posts
    test_cases = [
        {
            'title': 'USDA warns that Hello Fresh meals may contain listeria-tainted spinach',
            'expected': 'negative',
            'reason': 'Food safety alert should be negative'
        },
        {
            'title': 'Hungryroot -- would be great if they weren\'t so unreliable',
            'expected': 'negative', 
            'reason': 'Backhanded compliment should be negative'
        },
        {
            'title': 'Factor - Fantasy vs. Reality - Day 2',
            'expected': 'negative',
            'reason': 'Fantasy vs Reality comparison should be negative'
        },
        {
            'title': 'HelloFresh is amazing! Love the quality',
            'expected': 'positive',
            'reason': 'Clear positive sentiment'
        }
    ]
    
    print("\nTesting specific sentiment cases:")
    print("-" * 50)
    
    correct = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases, 1):
        result = analyzer.classify_post_sentiment({'title': test['title'], 'selftext': ''})
        predicted = result['sentiment']
        expected = test['expected']
        
        is_correct = predicted == expected
        if is_correct:
            correct += 1
        
        status = "CORRECT" if is_correct else "WRONG"
        print(f"{i}. {test['title'][:50]}...")
        print(f"   Expected: {expected.upper()}")
        print(f"   Predicted: {predicted.upper()}")
        print(f"   Status: {status}")
        print(f"   Reason: {test['reason']}")
        print()
    
    accuracy = (correct / total) * 100
    print(f"Sentiment Test Accuracy: {correct}/{total} ({accuracy:.1f}%)")
    
    if accuracy >= 80:
        print("GOOD: Sentiment accuracy is above 80% threshold")
    else:
        print("WARNING: Sentiment accuracy is below 80% - needs improvement")
    
    # Final assessment
    print("\n" + "=" * 70)
    print("FINAL ASSESSMENT")
    print("=" * 70)
    
    if recent_count >= len(posts) * 0.7 and accuracy >= 80:
        print("READY FOR BRIAN: Data is real, recent, and accurate")
    else:
        print("NEEDS WORK: Check the issues above before presenting to Brian")
    
    print(f"\nSummary:")
    print(f"• Total posts: {len(posts)}")
    print(f"• Recent posts (30 days): {recent_count} ({recent_count/len(posts)*100:.1f}%)")
    print(f"• Sentiment accuracy: {accuracy:.1f}%")
    print(f"• Manual verification: Check the 5 URLs above")
    
    return posts, accuracy

if __name__ == "__main__":
    posts, accuracy = verify_reddit_data()
