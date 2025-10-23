# Reddit Competitor Sentiment Analysis

## Brian's Project: Steps 1 & 2 Complete

A professional system that tracks HelloFresh competitor sentiment on Reddit with actionable business intelligence.

### 📊 Step 1: Post Breakdown (Stack Bar Chart)
**Purpose:** Visual overview of competitor sentiment
- **Y-axis:** # of posts
- **X-axis:** Competitor/Brand names  
- **Categories:** Positive, Negative, Neutral sentiment
- **File:** `step1_chart.py` → `reports/step1_chart.png`

### 🎯 Step 2: HelloFresh Deep Dive (60% Revenue Focus)
**Purpose:** Actionable intelligence on HelloFresh & Factor
- **Top 3 posts** by engagement (comments + upvotes)
- **Synthesis logic** for < 3 or > 3 posts scenarios
- **Actionable insights** by theme (pricing, quality, delivery)
- **Real Reddit URLs** that work
- **File:** `step2_hellofresh_deep_dive.py` → HTML report

## 📈 Current Data (Oct 16-23, 2025)
**Total:** 87 verified Reddit posts from 6 brands

**HelloFresh Family:**
- **HelloFresh:** 55 posts (63% of total volume)
- **Factor:** 4 posts (5% of total volume)

**Competitors:**
- **Blue Apron:** 16 posts (18% of total volume)
- **Home Chef:** 8 posts (9% of total volume) 
- **Marley Spoon:** 3 posts (3% of total volume)
- **HungryRoot:** 1 post (1% of total volume)

## 🚀 Quick Start

1. **Generate Step 1 Chart:**
   ```bash
   python3 step1_chart.py
   ```
   Creates: `reports/step1_chart.png`

2. **Generate Step 2 Deep Dive:**
   ```bash
   python3 step2_hellofresh_deep_dive.py
   ```
   Creates: `reports/step2_hellofresh_deep_dive_YYYYMMDD_HHMMSS.html`

## 📁 Key Files

- **`step1_chart.py`** - Generates weekly competitor sentiment chart
- **`step2_hellofresh_deep_dive.py`** - HelloFresh & Factor deep analysis
- **`scraper.py`** - Reddit data collection
- **`ai_sentiment.py`** - Sentiment analysis engine
- **`competitors.py`** - Brand configuration
- **`reports/working_reddit_data.json`** - Raw data source

## 📊 Data Quality
- ✅ **Real Reddit posts** with working URLs
- ✅ **7-day data filtering** for weekly analysis  
- ✅ **Consistent dataset** between Step 1 and Step 2
- ✅ **Accurate sentiment analysis** 
- ✅ **HelloFresh family vs competitors** tracking

## 🎯 Business Value
- **Weekly sentiment tracking** for HelloFresh family brands
- **Competitive intelligence** on key rivals
- **Actionable insights** for business decisions
- **Revenue-focused analysis** (HelloFresh + Factor = 60% business)

Built for Brian's weekly competitive intelligence and strategic planning.
