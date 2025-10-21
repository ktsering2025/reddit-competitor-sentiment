"""
Advanced AI-Powered Sentiment Analysis for HelloFresh Competitor Intelligence
Uses multiple AI models + context awareness for accurate sentiment classification
"""

import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import numpy as np

class AdvancedSentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
        
        # Business context patterns for HelloFresh intelligence
        self.business_contexts = {
            'quality_praise': [
                r'\b(?:love|amazing|excellent|fantastic|perfect|best|great|delicious|fresh|quality|tasty|wonderful)\b',
                r'\b(?:recommend|highly recommend|worth it|satisfied|impressed|favorite)\b',
                r'\b(?:good|better|awesome|nice|convenient|easy|helpful)\b'
            ],
            'quality_complaints': [
                r'\b(?:hate|worst|terrible|awful|disgusting|horrible|bad|poor|disappointed)\b',
                r'\b(?:spoiled|rotten|moldy|expired|stale|bland|cheap|garbage)\b',
                r'\b(?:failed|broken|useless|sucks|fraud|ripoff|scam|scammed)\b'
            ],
            'pricing_concerns': [
                r'\b(?:expensive|overpriced|costly|pricey|not worth it|waste of money)\b',
                r'\b(?:cheaper|budget|afford|financial|cost|price|money)\b'
            ],
            'service_issues': [
                r'\b(?:late|delayed|missing|damaged|wrong|poor service|customer service)\b',
                r'\b(?:delivery|shipping|packaging|support|unreliable|problem)\b'
            ],
            'switching_behavior': [
                r'\b(?:switching|switched|left|quit|cancel|cancelled|done with)\b',
                r'\b(?:vs|versus|compared to|better than|instead of|rather than)\b'
            ]
        }
        
        # Critical business alerts (high priority)
        self.critical_alerts = [
            'scam', 'fraud', 'terrible', 'worst', 'never again', 'boycott',
            'lawsuit', 'sick', 'food poisoning', 'refund', 'cancel subscription',
            'actual scam', 'huge bust', 'waste of money', 'awful', 'horrible',
            # FOOD SAFETY CRITICAL ALERTS
            'listeria', 'contamination', 'recalled', 'salmonella', 'e coli',
            'bacteria', 'usda warns', 'health warning', 'do not eat',
            'is a bust', 'fantasy vs reality', 'disappointment', 'misleading'
        ]
    
    def analyze_with_ai(self, text):
        """
        Multi-model AI sentiment analysis with fixes for misclassifications
        """
        if not text or len(text.strip()) < 3:
            return {'sentiment': 'neutral', 'confidence': 0.5, 'reasoning': 'empty_text'}
        
        # Clean text
        import re
        clean_text = re.sub(r'[^\w\s]', ' ', text.lower())
        
        # CRITICAL: Check for food safety issues FIRST
        food_safety_keywords = ['listeria', 'salmonella', 'e coli', 'contamination', 
                               'recalled', 'usda warns', 'food poisoning', 'bacteria',
                               'do not eat', 'health warning']
        
        if any(keyword in text.lower() for keyword in food_safety_keywords):
            return {
                'sentiment': 'negative',
                'confidence': 0.95,
                'combined_score': -1.0,
                'vader_compound': -1.0,
                'textblob_polarity': -1.0,
                'context_score': -1.0,
                'critical_alert': True,
                'reasoning': 'FOOD SAFETY ALERT: Automatic negative classification'
            }
        
        # VADER Analysis
        vader_scores = self.vader.polarity_scores(text)
        
        # TextBlob Analysis
        from textblob import TextBlob
        blob = TextBlob(text)
        textblob_polarity = blob.sentiment.polarity
        
        # Business Context Analysis
        context_score = self.analyze_business_context(text)
        
        # NEW: Check for backhanded compliments
        backhanded_penalty = self.detect_backhanded_compliment(text)
        
        # NEW: Check for comparisons
        comparison_penalty = self.detect_comparison(text)
        
        # Combine AI models with weights + new penalties
        combined_score = (
            vader_scores['compound'] * 0.4 +
            textblob_polarity * 0.3 +
            context_score * 0.3 +
            backhanded_penalty +  # NEW
            comparison_penalty     # NEW
        )
        
        # FIXED: Lower thresholds for more accurate classification
        if combined_score > 0.15:
            sentiment = 'positive'
            confidence = min(0.95, abs(combined_score) + 0.4)
        elif combined_score < -0.15:
            sentiment = 'negative'
            confidence = min(0.95, abs(combined_score) + 0.4)
        else:
            sentiment = 'neutral'
            confidence = 0.6
        
        # Check for critical alerts (includes new keywords)
        critical_alert = any(alert in text.lower() for alert in self.critical_alerts)
        if critical_alert:
            sentiment = 'negative'
            confidence = 0.95
        
        return {
            'sentiment': sentiment,
            'confidence': confidence,
            'combined_score': combined_score,
            'vader_compound': vader_scores['compound'],
            'textblob_polarity': textblob_polarity,
            'context_score': context_score,
            'critical_alert': critical_alert,
            'reasoning': f"VADER: {vader_scores['compound']:.2f}, TextBlob: {textblob_polarity:.2f}, Context: {context_score:.2f}"
        }
    
    def analyze_business_context(self, text):
        """
        Analyze business-specific context for HelloFresh intelligence
        """
        text_lower = text.lower()
        context_score = 0
        
        # Quality praise patterns
        for pattern in self.business_contexts['quality_praise']:
            matches = len(re.findall(pattern, text_lower))
            context_score += matches * 0.3
        
        # Quality complaints patterns  
        for pattern in self.business_contexts['quality_complaints']:
            matches = len(re.findall(pattern, text_lower))
            context_score -= matches * 0.4
        
        # Pricing concerns
        for pattern in self.business_contexts['pricing_concerns']:
            matches = len(re.findall(pattern, text_lower))
            context_score -= matches * 0.2
        
        # Service issues
        for pattern in self.business_contexts['service_issues']:
            matches = len(re.findall(pattern, text_lower))
            context_score -= matches * 0.3
        
        # Switching behavior (neutral to slightly negative)
        for pattern in self.business_contexts['switching_behavior']:
            matches = len(re.findall(pattern, text_lower))
            context_score -= matches * 0.1
        
        return max(-1, min(1, context_score))  # Clamp between -1 and 1
    
    def detect_backhanded_compliment(self, text):
        """
        Detect backhanded compliments like 'would be great if...'
        These should be negative, not positive
        """
        text_lower = text.lower()
        
        backhanded_patterns = [
            r'would be \w+ if',  # "would be great if they weren't..."
            r'could be \w+ but',  # "could be good but..."
            r'wish it were',
            r'if only',
            r'too bad',
            r'unfortunately',
            r'sadly',
            r'except for',
            r'however',
            r'weren\'t so',  # "weren't so unreliable"
            r'wasn\'t so',   # "wasn't so bad"
            r'if they weren\'t',  # "if they weren't so unreliable"
            r'if it wasn\'t'      # "if it wasn't so expensive"
        ]
        
        import re
        for pattern in backhanded_patterns:
            if re.search(pattern, text_lower):
                return -1.0  # Strong penalty for backhanded compliment
        
        return 0
    
    def detect_comparison(self, text):
        """
        Detect 'vs' or comparison posts - these are usually neutral or critical
        """
        text_lower = text.lower()
        
        comparison_patterns = [
            'fantasy vs reality',
            'expectation vs reality',
            'vs',
            'versus',
            'compared to',
            'better than',
            'worse than'
        ]
        
        for pattern in comparison_patterns:
            if pattern in text_lower:
                # If it's a "fantasy vs reality" style, likely negative
                if 'fantasy' in text_lower or 'expectation' in text_lower:
                    return -0.4
                # Otherwise neutral
                return -0.1
        
        return 0
    
    def classify_post_sentiment(self, post):
        """
        Main sentiment classification with AI accuracy
        """
        title = post.get('title', '')
        selftext = post.get('selftext', '')
        full_text = f"{title} {selftext}".strip()
        
        # Use AI analysis
        ai_result = self.analyze_with_ai(full_text)
        
        return {
            'sentiment': ai_result['sentiment'],
            'confidence': ai_result['confidence'],
            'reasoning': ai_result['reasoning'],
            'critical_alert': ai_result['critical_alert'],
            'combined_score': ai_result['combined_score']
        }
    
    def analyze_all_posts(self, posts):
        """
        Analyze sentiment for all posts and group by competitor
        """
        sentiment_data = {}
        
        for post in posts:
            # Get competitors mentioned in this post
            competitors_mentioned = post.get('competitors_mentioned', [])
            
            # Classify the post sentiment with AI
            sentiment_result = self.classify_post_sentiment(post)
            
            # Add sentiment data to post
            post['sentiment'] = sentiment_result['sentiment']
            post['confidence'] = sentiment_result['confidence']
            post['reasoning'] = sentiment_result['reasoning']
            post['critical_alert'] = sentiment_result['critical_alert']
            
            # Group by competitor
            for competitor in competitors_mentioned:
                if competitor not in sentiment_data:
                    sentiment_data[competitor] = {
                        'posts': [],
                        'positive': 0,
                        'negative': 0,
                        'neutral': 0,
                        'total': 0,
                        'avg_confidence': 0,
                        'critical_alerts': 0
                    }
                
                sentiment_data[competitor]['posts'].append(post)
                sentiment_data[competitor]['total'] += 1
                sentiment_data[competitor]['avg_confidence'] += sentiment_result['confidence']
                
                if sentiment_result['sentiment'] == 'positive':
                    sentiment_data[competitor]['positive'] += 1
                elif sentiment_result['sentiment'] == 'negative':
                    sentiment_data[competitor]['negative'] += 1
                else:
                    sentiment_data[competitor]['neutral'] += 1
                
                if sentiment_result['critical_alert']:
                    sentiment_data[competitor]['critical_alerts'] += 1
        
        # Calculate average confidence
        for competitor in sentiment_data:
            total = sentiment_data[competitor]['total']
            if total > 0:
                sentiment_data[competitor]['avg_confidence'] = (
                    sentiment_data[competitor]['avg_confidence'] / total
                )
        
        return sentiment_data
    
    def print_analysis_summary(self, sentiment_data):
        """
        Print detailed analysis summary for Brian
        """
        print("AI-POWERED SENTIMENT ANALYSIS RESULTS")
        print("=" * 60)
        
        total_posts = sum(data['total'] for data in sentiment_data.values())
        print(f"Total posts analyzed: {total_posts}")
        print(f"Competitors found: {len(sentiment_data)}")
        print()
        
        # Sort by total posts (volume)
        sorted_competitors = sorted(sentiment_data.items(), 
                                  key=lambda x: x[1]['total'], reverse=True)
        
        for competitor, data in sorted_competitors:
            total = data['total']
            pos = data['positive']
            neg = data['negative']
            neu = data['neutral']
            conf = data['avg_confidence']
            alerts = data['critical_alerts']
            
            pos_pct = (pos/total)*100 if total > 0 else 0
            neg_pct = (neg/total)*100 if total > 0 else 0
            neu_pct = (neu/total)*100 if total > 0 else 0
            
            # Determine strength
            if pos_pct >= 60:
                strength = "STRONG"
            elif neg_pct >= 50:
                strength = "WEAK"
            else:
                strength = "MIXED"
            
            print(f"{competitor}: {total} posts - {strength}")
            print(f"  Positive: {pos} ({pos_pct:.1f}%)")
            print(f"  Negative: {neg} ({neg_pct:.1f}%)")
            print(f"  Neutral: {neu} ({neu_pct:.1f}%)")
            print(f"  Avg Confidence: {conf:.2f}")
            if alerts > 0:
                print(f"  Critical Alerts: {alerts}")
            print()
        
        # Show sample classifications
        print("SAMPLE AI CLASSIFICATIONS:")
        print("-" * 40)
        
        for competitor, data in list(sentiment_data.items())[:3]:
            print(f"\n{competitor} sample posts:")
            for post in data['posts'][:2]:  # Show first 2 posts
                print(f"  [{post['sentiment'].upper()}] {post['title'][:60]}...")
                print(f"    Confidence: {post['confidence']:.2f}")
                print(f"    Reasoning: {post['reasoning']}")
                if post['critical_alert']:
                    print(f"# #   CRITICAL ALERT")

def test_advanced_sentiment():
    """Test the advanced AI sentiment analyzer"""
    print("TESTING ADVANCED AI SENTIMENT ANALYSIS")
    print("=" * 50)
    
    # Sample posts for testing
    test_posts = [
        {
            'title': 'HelloFresh is amazing! Love the quality',
            'selftext': 'Been using for 2 years, highly recommend',
            'competitors_mentioned': ['HelloFresh']
        },
        {
            'title': 'Sunbasket is a complete scam',
            'selftext': 'Terrible service, spoiled food, waste of money',
            'competitors_mentioned': ['Sunbasket']
        },
        {
            'title': 'ButcherBox vs HelloFresh comparison',
            'selftext': 'Both are good but ButcherBox has better meat quality',
            'competitors_mentioned': ['ButcherBox', 'HelloFresh']
        },
        {
            'title': 'Factor meals getting smaller and more expensive',
            'selftext': 'Not worth it anymore, switching to another service',
            'competitors_mentioned': ['Factor']
        }
    ]
    
    analyzer = AdvancedSentimentAnalyzer()
    results = analyzer.analyze_all_posts(test_posts)
    analyzer.print_analysis_summary(results)
    
    return results

if __name__ == "__main__":
    test_advanced_sentiment()
