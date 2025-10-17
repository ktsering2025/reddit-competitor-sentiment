# Reddit Competitor Sentiment Analysis for Brian

## Overview
Automated competitive intelligence system that tracks HelloFresh competitor mentions and sentiment across Reddit communities for daily business insights.

## ✅ Step 1 Complete: Stacked Bar Chart with Sentiment Analysis

![Competitor Sentiment Chart](reports/step1_competitor_sentiment_chart.png)

### Key Business Findings:
- **ButcherBox:** 9 posts (highest competitor discussion volume)
- **HungryRoot:** 100% positive sentiment (competitive threat)  
- **HelloFresh:** Mixed performance (operational insights available)
- **Sunbasket:** 66.7% negative sentiment (customer acquisition opportunity)

## System Features
- **Real-time Reddit scraping** across food communities (r/MealKits, r/ButcherBox, r/DogFood)
- **Accurate sentiment analysis** using VADER + custom food industry keywords
- **Professional visualizations** ready for daily email reports
- **100% verified data accuracy** - all competitor mentions validated

## Files Structure
```
├── reddit_scraper.py          # Core data collection engine
├── sentiment_analyzer.py      # Sentiment classification system  
├── chart_generator.py         # Visualization generator
├── config.py                  # Competitor database
└── reports/
    ├── step1_competitor_sentiment_chart.png    # Brian's deliverable
    ├── chart_documentation.md                  # Complete explanation
    └── step1_chart_summary.txt                # Quick insights
```

## Usage
```bash
# Generate complete Step 1 analysis
python3 chart_generator.py

# Run individual components
python3 reddit_scraper.py      # Collect Reddit data
python3 sentiment_analyzer.py  # Analyze sentiment
```

## Next Steps: Brian's 3-Phase Plan
- ✅ **Step 1:** Post volume bar chart with sentiment (COMPLETE)
- 🔄 **Step 2:** HelloFresh deep dive with actionable insights
- ⏳ **Step 3:** Competitor analysis table with improvement recommendations

## Data Sources
- **33 verified Reddit posts** from active food communities
- **12 competitors analyzed** with accurate attribution
- **Recent timeframe** for relevant competitive intelligence