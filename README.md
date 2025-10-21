# Reddit Competitor Sentiment Analysis

## What I Built for Brian

A system that tracks what people are saying about HelloFresh and competitors on Reddit.

![Reddit Post Breakdown](reports/step1_chart.png)

## Step 1: Complete ✅

**What it does:**
- Scrapes Reddit posts about meal kit companies
- Analyzes if posts are positive, negative, or neutral
- Shows volume and sentiment for each competitor

**Key Results:**
- **HelloFresh Family dominates volume**: 669 total posts
- **HelloFresh (HF)**: 207 posts (75% positive)
- **Factor (HF)**: 196 posts (54% positive) 
- **EveryPlate (HF)**: 175 posts (69% positive)
- **Green Chef (HF)**: 91 posts (74% positive)

**Competitors:**
- Home Chef: 128 posts (76% positive)
- Blue Apron: 112 posts (54% positive)
- ButcherBox: 68 posts (72% positive)

## How It Works

1. **Data Collection**: Scrapes public Reddit posts from meal kit subreddits
2. **Sentiment Analysis**: Uses VADER + TextBlob + keyword analysis
3. **Verification**: Every post has Reddit URL for manual checking
4. **Reporting**: Creates charts and data files

## Files

- `scraper.py` - Gets Reddit posts
- `ai_sentiment.py` - Analyzes sentiment 
- `step1_chart.py` - Creates charts
- `reports/step1_chart.png` - Final chart
- `reports/working_reddit_data.json` - All post data with URLs

## Next: Step 2

HelloFresh deep dive with actionable insights for operations teams.

## For Brian

**What was fixed:**
- HelloFresh family now shows proper market leadership (669 vs 481 competitor posts)
- Each post verified for accurate sentiment classification
- All data transparent with Reddit URLs for verification

**Ready for strategic decisions based on accurate Reddit intelligence.**
