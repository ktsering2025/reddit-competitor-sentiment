# 📊 Reddit Competitor Sentiment Analysis

**Automated weekly sentiment tracking for meal kit brands**

[![Weekly Analysis](https://github.com/ktsering2025/reddit-competitor-sentiment/actions/workflows/weekly-automation.yml/badge.svg)](https://github.com/ktsering2025/reddit-competitor-sentiment/actions/workflows/weekly-automation.yml)

---

## 🎯 What This Does

Automatically scrapes Reddit **every Sunday at 8:00 PM EST**, analyzes sentiment for 8 meal kit brands, and sends a professional email report with:

- 📊 **Sentiment bar chart** (positive/negative/neutral breakdown)
- 📧 **Top posts** (3 positive + 3 negative per brand)
- 📎 **PDF attachment** (crystal-clear chart)
- 🔗 **Dashboard links** (live website with full reports)

---

## 🏢 Brands Tracked

1. **HelloFresh** (Primary - 60% HF revenue)
2. **Factor75** (Primary - 60% HF revenue)
3. Home Chef
4. Blue Apron
5. Marley Spoon
6. Hungryroot
7. EveryPlate
8. Green Chef

---

## 📅 Schedule

**Every Sunday at 8:00 PM EST:**
- Scrapes Reddit for the **previous complete week** (Monday-Sunday)
- Analyzes 30-50 posts per week
- Sends email to: brian.leung@hellofresh.com, assaf.ronen@hellofresh.com, kunsang.tsering@hellofresh.com, adam.kalikow@hellofresh.com, adam.park@factor75.com
- Updates website: https://ktsering2025.github.io/reddit-competitor-sentiment/

**Next Run:** Sunday, November 17, 2025 at 8:00 PM EST

---

## 🔬 Sentiment Analysis

### Method:
- **Dual-Algorithm:** VADER + TextBlob for accuracy
- **Context-Aware:** Detects questions, comparisons, neutral discussions
- **Keyword Override:** Strong phrases override algorithmic scores
- **Brand Detection:** Identifies all brands mentioned per post

### Classification:
- **Positive:** "love it", "amazing", "highly recommend", "delicious", "fresh"
- **Negative:** "terrible", "avoid", "cancelled", "disappointed", "waste of money"
- **Neutral:** Questions, comparisons, recommendation requests

---

## 🚀 Quick Start

### Setup (One-Time):

1. **Add GitHub Secrets:**  
   Go to: [Settings → Secrets](https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions)
   
   Add these 6 secrets:
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`
   - `REDDIT_USER_AGENT`
   - `GMAIL_EMAIL`
   - `GMAIL_APP_PASSWORD`
   - `EMAIL_RECIPIENTS`

   *(See [COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md) for values)*

2. **Done!** The automation runs automatically every Sunday.

### Manual Run (For Testing):

**Option 1: GitHub Actions**
1. Go to [Actions tab](https://github.com/ktsering2025/reddit-competitor-sentiment/actions)
2. Click "Weekly Reddit Sentiment Analysis"
3. Click "Run workflow" → "Run workflow"
4. Check your email in 3 minutes

**Option 2: Local**
```bash
python3 complete_automation.py
```

---

## 📧 Email Report Example

```
Weekly Reddit Competitor Sentiment Report — Nov 3 to Nov 9

Quick Summary:
- HelloFresh: 13 posts (23% positive)
- Factor75: 5 posts (0% positive, 60% negative)
- Blue Apron: 5 posts (40% positive)

HelloFresh - Top Posts:
✅ Top Positive:
  1. Gyoza Pork Tacos (44 upvotes, 8 comments)
  2. Meal delivery that does serving of 1 (1 upvote, 17 comments)

❌ Top Negative:
  1. Potato wedges....again?!?! (17 upvotes, 38 comments)
  2. What is the best mealprep kit? (2 upvotes, 18 comments)

📎 Attachment: step1_chart.pdf
```

---

## 🌐 Live Dashboard

**URL:** https://ktsering2025.github.io/reddit-competitor-sentiment/

**Features:**
- Interactive sentiment bar chart
- Current week's data
- Links to detailed reports
- Archive of previous weeks

**Auto-Updates:** Every Sunday after automation runs

---

## 📁 Project Structure

```
reddit-competitor-sentiment/
├── accurate_scraper.py          # Reddit scraping + sentiment analysis
├── step1_chart.py               # Bar chart generator (PNG + PDF)
├── step2_ACTIONABLE_analysis.py # Deep dive (HelloFresh & Factor)
├── step3_competitor_analysis.py # Full competitor report
├── send_to_gmail_smtp.py        # Email sender
├── complete_automation.py       # Main orchestrator
├── update_homepage.py           # Website updater
├── config.py                    # Configuration
├── index.html                   # Dashboard homepage
├── reports/
│   ├── working_reddit_data.json # Current week's data
│   ├── step1_chart.png          # Bar chart
│   ├── step1_chart.pdf          # PDF for email
│   ├── step2_ACTIONABLE_analysis_LATEST.html
│   ├── step3_competitor_analysis_LATEST.html
│   ├── archive/                 # Historical data
│   └── raw/                     # Raw scraped data
└── .github/workflows/
    └── weekly-automation.yml    # GitHub Actions schedule
```

---

## 🔍 Data Sources

### Reddit Sources Per Brand:
- **HelloFresh:** 4 sources (search + r/hellofresh + r/mealkits)
- **Factor75:** 5 sources (search + r/ReadyMeals + r/mealkits)
- **Others:** 2-4 sources each

### Time Frame:
- **Previous complete week** (Monday-Sunday)
- Example: Sunday Nov 17 report covers Nov 11-17

### Filtering:
- ✅ Keeps: Customer reviews, experiences, comparisons
- ❌ Removes: Spam, promos, off-topic, SNAP discussions

---

## 📊 Validation

Built-in checks ensure data quality:
- ✅ Date window is 4-8 days
- ✅ Sentiment totals match (pos + neg + neu = total)
- ✅ All brands tracked (even if 0 posts)
- ✅ Reddit API working
- ✅ Email credentials valid

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **PRAW** (Reddit API)
- **VADER + TextBlob** (Sentiment analysis)
- **Matplotlib** (Charts)
- **GitHub Actions** (Automation)
- **GitHub Pages** (Website hosting)

---

## 📖 Documentation

- **[COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md)** - Full setup instructions
- **[HOW_AUTOMATION_WORKS.md](HOW_AUTOMATION_WORKS.md)** - Technical details
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview

---

## 🚨 Troubleshooting

### "0 posts" in report:
→ Add Reddit API secrets to GitHub (see Setup above)

### Email not received:
→ Check [GitHub Actions logs](https://github.com/ktsering2025/reddit-competitor-sentiment/actions)

### Wrong date range:
→ System uses **previous complete week** (intentional for production)

---

## ✅ Status

- ✅ **Production Ready**
- ✅ Sentiment analysis: Dual-method with context awareness
- ✅ Time frame: 7-day weekly (previous Monday-Sunday)
- ✅ Schedule: Every Sunday 8:00 PM EST
- ✅ Automation: GitHub Actions (no manual intervention)
- ✅ Email: Professional report with top posts + PDF
- ✅ Website: Auto-updates with latest data

**Next automatic run:** Sunday, November 17, 2025 at 8:00 PM EST 🚀

---

## 📞 Support

**Repository:** https://github.com/ktsering2025/reddit-competitor-sentiment

**Check Status:**
- [GitHub Actions](https://github.com/ktsering2025/reddit-competitor-sentiment/actions)
- [Live Dashboard](https://ktsering2025.github.io/reddit-competitor-sentiment/)

**Manual Test:**
1. Go to [Actions](https://github.com/ktsering2025/reddit-competitor-sentiment/actions)
2. Run "Weekly Reddit Sentiment Analysis" workflow
3. Check email in 3 minutes

---

Built for HelloFresh competitive intelligence team 🍽️
