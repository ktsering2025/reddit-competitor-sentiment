"""
Step 1B: Stacked Bar Chart Generator for Brian's Daily Email
Purpose: Create the visual chart Brian requested showing post volume by competitor with sentiment
Input: Sentiment data from sentiment_analyzer.py
Output: Stacked bar chart (Green=Positive, Red=Negative, Gray=Neutral)
"""

import matplotlib.pyplot as plt
import numpy as np
from sentiment_analyzer import CompetitorSentimentAnalyzer
from reddit_scraper import ComprehensiveRedditScraper

class CompetitorChartGenerator:
    def __init__(self):
        self.colors = {
            'positive': '#2E8B57',  # Green
            'negative': '#DC143C',  # Red  
            'neutral': '#808080'    # Gray
        }
    
    def create_stacked_bar_chart(self, sentiment_data, save_path=None):
        """
        Create Brian's requested stacked bar chart
        Y-axis: Number of posts
        X-axis: Competitor names
        Colors: Green (positive), Red (negative), Gray (neutral)
        """
        
        # Prepare data for chart
        competitors = []
        positive_counts = []
        negative_counts = []
        neutral_counts = []
        
        # Sort by total posts (descending) for better visualization
        sorted_competitors = sorted(sentiment_data.items(), 
                                  key=lambda x: x[1]['total'], reverse=True)
        
        for competitor, data in sorted_competitors:
            competitors.append(competitor)
            positive_counts.append(data['positive'])
            negative_counts.append(data['negative']) 
            neutral_counts.append(data['neutral'])
        
        # Create the figure
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Create stacked bars
        bar_width = 0.8
        x_positions = np.arange(len(competitors))
        
        # Stack the bars
        p1 = ax.bar(x_positions, positive_counts, bar_width, 
                   label='Positive', color=self.colors['positive'])
        
        p2 = ax.bar(x_positions, negative_counts, bar_width,
                   bottom=positive_counts, label='Negative', 
                   color=self.colors['negative'])
        
        p3 = ax.bar(x_positions, neutral_counts, bar_width,
                   bottom=np.array(positive_counts) + np.array(negative_counts),
                   label='Neutral', color=self.colors['neutral'])
        
        # Customize the chart
        ax.set_title("Reddit Post Volume by Competitor with Sentiment Breakdown", 
                    fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Competitors', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Posts', fontsize=12, fontweight='bold')
        
        # Set x-axis labels
        ax.set_xticks(x_positions)
        ax.set_xticklabels(competitors, rotation=45, ha='right')
        
        # Add legend
        ax.legend(loc='upper right')
        
        # Add grid for readability
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on bars
        self.add_value_labels(ax, x_positions, positive_counts, negative_counts, neutral_counts)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save or show
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Chart saved to: {save_path}")
        else:
            plt.show()
        
        return fig
    
    def add_value_labels(self, ax, x_positions, positive, negative, neutral):
        """Add value labels on top of each bar"""
        for i, (pos, neg, neu) in enumerate(zip(positive, negative, neutral)):
            total = pos + neg + neu
            if total > 0:
                # Add total count on top of bar
                ax.text(x_positions[i], total + 0.1, str(total), 
                       ha='center', va='bottom', fontweight='bold')
    
    def create_chart_summary(self, sentiment_data):
        """Create text summary to accompany the chart"""
        total_posts = sum(data['total'] for data in sentiment_data.values())
        total_competitors = len(sentiment_data)
        
        # Find top performers
        top_volume = max(sentiment_data.items(), key=lambda x: x[1]['total'])
        top_positive = max(sentiment_data.items(), 
                          key=lambda x: x[1]['positive'] / max(x[1]['total'], 1))
        
        summary = f"""
CHART SUMMARY:
===============
Total Posts Analyzed: {total_posts}
Competitors Mentioned: {total_competitors}

Top Volume: {top_volume[0]} ({top_volume[1]['total']} posts)
Top Positive Sentiment: {top_positive[0]} ({top_positive[1]['positive']}/{top_positive[1]['total']} positive)

Key Insights for Brian:
- Competitor generating most discussion: {top_volume[0]}
- Competitor with best sentiment: {top_positive[0]}
- Negative sentiment opportunities: [Check red portions in chart]
"""
        return summary

def generate_step1_deliverable():
    """
    Main function to generate Step 1 deliverable for Brian
    """
    print("GENERATING STEP 1: STACKED BAR CHART")
    print("=" * 50)
    
    # Step 1: Get Reddit data
    print("Collecting Reddit data...")
    scraper = ComprehensiveRedditScraper()
    posts = scraper.scrape_all_competitors()
    print(f"Collected {len(posts)} posts")
    
    # Step 2: Analyze sentiment
    print("Analyzing sentiment...")
    analyzer = CompetitorSentimentAnalyzer()
    sentiment_data = analyzer.analyze_all_posts(posts)
    print(f"Analyzed {len(sentiment_data)} competitors")
    
    # Step 3: Generate chart
    print("Creating stacked bar chart...")
    chart_generator = CompetitorChartGenerator()
    
    # Save chart
    chart_path = "reports/step1_competitor_sentiment_chart.png"
    chart_generator.create_stacked_bar_chart(sentiment_data, save_path=chart_path)
    
    # Generate summary
    summary = chart_generator.create_chart_summary(sentiment_data)
    print(summary)
    
    # Save summary
    summary_path = "reports/step1_chart_summary.txt"
    with open(summary_path, 'w') as f:
        f.write(summary)
    
    print(f"\nSTEP 1 COMPLETE!")
    print(f"Chart: {chart_path}")
    print(f"Summary: {summary_path}")
    
    return sentiment_data, chart_path

if __name__ == "__main__":
    generate_step1_deliverable()