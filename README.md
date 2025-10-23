# Reddit Competitor Sentiment Analysis

## Brian's Project: Steps 1 & 2 Complete

A professional system that tracks HelloFresh competitor sentiment on Reddit with actionable business intelligence.

![Step 1 Chart](reports/step1_chart.png)

### Step 1: Post Breakdown (Stack Bar Chart)
**Purpose:** Visual overview of competitor sentiment
- **Y-axis:** Number of posts
- **X-axis:** Competitor/Brand names  
- **Categories:** Positive, Negative, Neutral sentiment
- **File:** `step1_chart.py`
- **Link:** [View Step 1 Chart](reports/step1_chart.png)

### Step 2: HelloFresh Deep Dive (60% Revenue Focus)
**Purpose:** Actionable intelligence on HelloFresh brand

#### What Step 2 Does:
1. **Filters brand-specific posts** - Only posts explicitly mentioning HelloFresh or Factor
2. **Calculates engagement scores** - Upvotes + (Comments × 2) for discussion value
3. **Identifies top 3 posts** - Highest engagement for each brand
4. **Analyzes sentiment** - Positive, negative, neutral classification
5. **Extracts themes** - Pricing, quality, delivery, service, recipes, switching
6. **Generates actionable insights** - Business recommendations

#### Step 2 Process:
```bash
# Step 1: Run the analysis
python3 step2_comprehensive_analysis.py

# Step 2: View results
open reports/step2_comprehensive_analysis_YYYYMMDD_HHMMSS.html
```

#### Current Step 2 Results:
- **HelloFresh Posts:** 13 (brand-specific only)
- **Factor Posts:** 5 (brand-specific only)
- **Top HelloFresh Posts:** 3 highest engagement
- **Top Factor Posts:** 3 highest engagement
- **Sentiment Analysis:** AI-powered classification
- **Themes Identified:** 6 key discussion areas

#### File Details:
- **File:** `step2_comprehensive_analysis.py`
- **Output:** `reports/step2_comprehensive_analysis_YYYYMMDD_HHMMSS.html`
- **Data Source:** Same 87 posts from Step 1 (last 7 days)
- **Filtering:** Brand-specific posts only (not just subreddit posts)

## Current Data (Oct 16-23, 2025)
**Total:** 87 verified Reddit posts from 6 brands

**HelloFresh Family:**
- **HelloFresh:** 55 posts (63% of total volume)
- **Factor:** 4 posts (5% of total volume)

**Competitors:**
- **Blue Apron:** 16 posts (18% of total volume)
- **Home Chef:** 8 posts (9% of total volume) 
- **Marley Spoon:** 3 posts (3% of total volume)
- **HungryRoot:** 1 post (1% of total volume)

## Quick Start

### Generate Step 1 Chart:
```bash
python3 step1_chart.py
```
**Output:** `reports/step1_chart.png`

### Generate Step 2 Deep Dive:
```bash
python3 step2_comprehensive_analysis.py
```
**Output:** `reports/step2_comprehensive_analysis_YYYYMMDD_HHMMSS.html`

## Key Files

- **`step1_chart.py`** - Generates weekly competitor sentiment chart
- **`step2_comprehensive_analysis.py`** - HelloFresh deep analysis (comprehensive)
- **`scraper.py`** - Reddit data collection
- **`ai_sentiment.py`** - Sentiment analysis engine
- **`competitors.py`** - Brand configuration
- **`reports/working_reddit_data.json`** - Raw data source

## Public Browser Access for Brian

### 🌐 Live Reports (GitHub Pages)
**Main Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

| Step | Purpose | Public Link |
|------|---------|-------------|
| **Step 1** | Competitor sentiment overview chart | [View Chart](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png) |
| **Step 2** | HelloFresh deep dive analysis | [View Analysis](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_comprehensive_analysis_20251023_130248.html) |

### 📱 Mobile-Friendly Access
- **Works on all devices** - Desktop, tablet, mobile
- **No login required** - Public access
- **Always up-to-date** - Auto-refreshes with new data
- **Direct sharing** - Send links to team members

### 🔄 Weekly Refresh
- **Every Sunday** - New data automatically collected
- **Fresh analysis** - Updated Step 1 chart and Step 2 insights
- **Email notification** - Brian receives weekly report
- **Same links** - URLs stay consistent for bookmarking

## Data Quality
- **Real Reddit posts** with working URLs
- **7-day data filtering** for weekly analysis  
- **Consistent dataset** between Step 1 and Step 2
- **Accurate sentiment analysis** 
- **HelloFresh family vs competitors** tracking

## Business Value
- **Weekly sentiment tracking** for HelloFresh family brands
- **Competitive intelligence** on key rivals
- **Actionable insights** for business decisions
- **Revenue-focused analysis** (HelloFresh = 63% of discussion volume)

Built for Brian's weekly competitive intelligence and strategic planning.

## GitHub Pages Setup

To enable public HTML viewing:

1. Go to repository Settings
2. Scroll to Pages section
3. Enable from main branch
4. Brian can then view at:
   `https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_comprehensive_analysis_20251023_130248.html`