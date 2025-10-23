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
- **Top 3 posts** by engagement (comments + upvotes)
- **Synthesis logic** for < 3 or > 3 posts scenarios
- **Actionable insights** by theme and sentiment
- **Real Reddit URLs** that work
- **File:** `step2_comprehensive_analysis.py`
- **Link:** [View Step 2 Analysis](reports/step2_comprehensive_analysis_20251023_125314.html)

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

## Direct Links for Brian

| Step | Purpose | Link |
|------|---------|------|
| **Step 1** | Competitor sentiment overview chart | [View Chart](reports/step1_chart.png) |
| **Step 2** | HelloFresh deep dive analysis | [View Analysis](reports/step2_comprehensive_analysis_20251023_125314.html) |

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
   `https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_comprehensive_analysis_20251023_125314.html`