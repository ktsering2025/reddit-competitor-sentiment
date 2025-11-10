# Reddit Competitor Sentiment Analysis

Automated weekly competitive intelligence dashboard for HelloFresh and competitors.

**Live Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

---

## What This Does

This system automatically tracks what people are saying about HelloFresh, Factor75, and 7 competitors on Reddit every week.

**Every Sunday at 8 PM EST, it:**
1. Searches Reddit for posts about all 9 meal kit brands
2. Analyzes if posts are positive, negative, or neutral
3. Creates 3 reports with charts and insights
4. **Sends enhanced email with embedded chart and top posts** to Brian, Assaf, and Kunsang
5. Updates the live dashboard

---

## Current Week's Data

**Live Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

The dashboard is updated automatically every Sunday at 8 PM EST with the latest data from Reddit.

**What you'll see:**
- Current week's date range
- Post counts for all 8 brands
- Sentiment percentages (positive/negative/neutral)
- Links to all 3 reports
- Real-time data (always fresh)
- CookUnity: 0 posts this week

---

## Enhanced Weekly Email (NEW!)

**Per Assaf's feedback, the email now includes ALL key data in one place:**

✅ **Embedded Bar Chart** - Shows directly in email (no clicking needed)  
✅ **HelloFresh Top 3** - Positive & Negative posts with engagement scores  
✅ **Factor Top 3** - Positive & Negative posts with engagement scores  
✅ **Hungryroot Top 3** - Positive & Negative posts with engagement scores  
✅ **CookUnity Top 3** - Positive & Negative posts with engagement scores  
✅ **Links to Full Reports** - For other competitors (Blue Apron, Marley Spoon, etc.)  
✅ **Clean Design** - Professional format with minimal emojis (only ✅ and ❌)

**Leaders can now see all critical insights without clicking any links!**

---

## The 3 Reports

### Step 1: Chart Overview
Visual bar chart showing all 9 brands with sentiment breakdown (positive/negative/neutral).

**View:** [Step 1 Chart](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png)

### Step 2: HelloFresh & Factor Deep Dive
Focus on the two revenue-driving brands (60% of revenue):
- Top 3 positive posts (ranked by engagement)
- Top 3 negative posts (ranked by engagement)
- Complete list of all posts
- Links to verify on Reddit

**View:** [Step 2 Analysis](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html)

### Step 3: Competitor Analysis
Table showing what competitors are doing well vs. poorly:
- Real sentiment data (not generic)
- Top 3 posts for each competitor
- Engagement scoring

**View:** [Step 3 Competitor Analysis](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html)

---

## How It Works

### Data Collection
- **Sources:** 3-5 Reddit search URLs per brand
- **Time Window:** Past 7 days (rolling window)
- **Example:** Run on Nov 3 → Gets posts from Oct 27-Nov 3
- **Next Run:** Nov 10 → Gets NEW posts from Nov 3-Nov 10

### Sentiment Analysis
The system reads each post and determines if it's:
- **Positive:** "Love it", "excellent", "highly recommend"
- **Negative:** "Terrible", "cancelled", "disappointed"
- **Neutral:** Questions, comparisons, asking for recommendations

**Smart Detection:**
- "Don't switch from HelloFresh to Marley Spoon - MS is terrible!" → **Positive** for HelloFresh
- "We looooved HelloFresh, how to get discounts?" → **Neutral** (question about price)
- "This didn't used to have an upcharge!" → **Negative** (complaint)

### Spam Filtering
Removes 95%+ of irrelevant posts:
- Referral codes
- Promo spam
- News articles
- Unrelated mentions

Only keeps genuine customer discussions.

---

## Automation

**Schedule:** Every Sunday at 8 PM EST

**Runs automatically via GitHub Actions** (cloud-based, free):
- No need to keep laptop on
- Runs 24/7 in the cloud
- Always on time

**Email Recipients:**
- brian.leung@hellofresh.com
- assaf.ronen@hellofresh.com
- kunsang.tsering@hellofresh.com

**Email Includes (Enhanced Format):**
- Embedded bar chart (visible in email body)
- Quick summary stats for all 4 focus brands
- Top 3 positive & negative posts for HelloFresh
- Top 3 positive & negative posts for Factor
- Top 3 positive & negative posts for Hungryroot
- Top 3 positive & negative posts for CookUnity
- Links to full reports for all competitors
- Clean, professional design

---

## Data Quality

**100% Real Reddit Posts:**
- All posts verified with Reddit URLs
- No fake data
- No sample data

**Accurate Sentiment:**
- Manually verified for accuracy
- Context-aware analysis
- Handles edge cases correctly

**Always Fresh:**
- Rolling 7-day window
- New data every week
- Never stale

---

## Tracked Brands (9 Total)

**HelloFresh Family (4 brands):**
1. HelloFresh
2. Factor75
3. EveryPlate
4. Green Chef

**Competitors (5 brands):**
5. Blue Apron
6. Home Chef
7. Marley Spoon
8. Hungryroot
9. CookUnity

---

## Quick Links

**Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

**Reports:**
- [Step 1 Chart](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png)
- [Step 2: HF & Factor Deep Dive](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html)
- [Step 3: Competitor Analysis](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html)

**GitHub Repository:** https://github.com/ktsering2025/reddit-competitor-sentiment

**GitHub Actions Status:** https://github.com/ktsering2025/reddit-competitor-sentiment/actions

---

## For Technical Users

### Run Manually
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 complete_automation.py --no-send  # Generate reports
python3 send_to_gmail_smtp.py             # Send emails (production)
python3 send_to_gmail.py                  # Send emails (Mac local)
```

### Dependencies
```bash
pip install -r requirements.txt
```

### Key Files
- `accurate_scraper.py` - Reddit scraper (PRAW + web scraping)
- `step1_chart.py` - Chart generator (matplotlib)
- `step2_ACTIONABLE_analysis.py` - HelloFresh & Factor deep dive
- `step3_competitor_analysis.py` - Competitor analysis
- `complete_automation.py` - Main orchestrator
- `send_to_gmail_smtp.py` - Email sender (GitHub Actions/production)
- `send_to_gmail.py` - Email sender (Mac local)
- `config.py` - Configuration (search URLs, email settings)

### Email System
- **Production (GitHub Actions):** Uses `send_to_gmail_smtp.py` with Gmail SMTP
- **Local (Mac):** Uses `send_to_gmail.py` with Mail.app
- **Format:** HTML email with embedded chart image
- **No Attachments:** Chart is embedded inline (not as PDF attachment)

### Sentiment Logic
- **VADER Sentiment** (social media optimized)
- **TextBlob** (general text analysis)
- **Keyword overrides** (context-aware)
- **Priority:** Strong negative > Context-aware positive > Questions/comparisons > Strong positive > VADER+TextBlob

### Data Sources
Each brand has 3-5 Reddit search URLs:
- General Reddit search (e.g., "hellofresh", "hello fresh")
- Brand-specific subreddit (e.g., r/hellofresh)
- Meal kit discussion subreddits (e.g., r/mealkits, r/ReadyMeals)

---

## Project Status

**Status:** ✅ Production Ready

**Last Updated:** November 3, 2025

**Next Automatic Run:** Sunday, November 10, 2025 at 8:00 PM EST

**Cost:** $0/month (GitHub Actions + GitHub Pages are free)

**Recent Updates:**
- ✅ Enhanced email format with embedded chart and top posts (Nov 3, 2025)
- ✅ Added CookUnity tracking (Nov 3, 2025)
- ✅ Removed PDF attachment per Assaf's feedback (Nov 3, 2025)
- ✅ Clean design with minimal emojis (Nov 3, 2025)

---

## Project Complete! 🎉

This project is **100% complete** per Brian and Assaf's requirements:
- ✅ Automated weekly scraping of Reddit posts
- ✅ Accurate sentiment analysis
- ✅ Beautiful reports and dashboard
- ✅ Enhanced email with all key data embedded
- ✅ No manual work needed - runs automatically every Sunday

**Leaders can now get all critical insights directly in their inbox without clicking any links!**

---

## Contact

Built by Kunsang Tsering for Brian's competitive intelligence needs.

For questions or issues, contact: kunsang.tsering@hellofresh.com
