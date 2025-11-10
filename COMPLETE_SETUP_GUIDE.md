# 📊 Reddit Competitor Sentiment Analysis - Complete Setup Guide

## ✅ System Overview

This system automatically scrapes Reddit every **Sunday at 8:00 PM EST**, analyzes sentiment for 8 meal kit brands, and sends a professional email report to your team.

---

## 🎯 What It Does

### Data Collection (In-Depth):
- **Scrapes Reddit** using official Reddit API (PRAW)
- **Time Frame:** Previous complete week (Monday-Sunday)
- **Brands Tracked:** HelloFresh, Factor75, Home Chef, Blue Apron, Marley Spoon, Hungryroot, EveryPlate, Green Chef
- **Sources:** Multiple subreddits + search queries per brand for comprehensive coverage

### Sentiment Analysis (Accurate & In-Depth):
- **Dual-Method Approach:** VADER + TextBlob for accuracy
- **Context-Aware:** Detects questions, comparisons, and neutral discussions
- **Keyword Override:** Strong positive/negative phrases override algorithmic scores
- **Brand Detection:** Identifies which brands are discussed in each post
- **Filtering:** Removes spam, promos, and off-topic content

### Automated Reports:
- **Bar Chart:** Visual sentiment breakdown (positive/negative/neutral) per brand
- **Email Report:** Top 3 positive and negative posts per brand with engagement scores
- **Website Dashboard:** Live at https://ktsering2025.github.io/reddit-competitor-sentiment/
- **Deep Dive Analysis:** Detailed HTML reports for HelloFresh & Factor

---

## 🔐 Required Setup (One-Time Only)

### Step 1: Add GitHub Secrets

Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions

Add these **6 secrets**:

#### Reddit API Credentials:
1. **Name:** `REDDIT_CLIENT_ID`  
   **Value:** `kG3E8fifKfnd-tu1BeWH3g`

2. **Name:** `REDDIT_CLIENT_SECRET`  
   **Value:** `33tI4yhvAgBE5jUATtN8SUQY8TeQjA`

3. **Name:** `REDDIT_USER_AGENT`  
   **Value:** `CompetitorSentimentBot/1.0`

#### Email Credentials:
4. **Name:** `GMAIL_EMAIL`  
   **Value:** `kunsang.tsering@hellofresh.com`

5. **Name:** `GMAIL_APP_PASSWORD`  
   **Value:** `prczfvibtgcamqpi`

6. **Name:** `EMAIL_RECIPIENTS`  
   **Value:** `brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com`

---

## 📅 Automatic Schedule

**Every Sunday at 8:00 PM EST:**
1. ✅ Scrapes Reddit for the **previous complete week** (Monday-Sunday)
2. ✅ Analyzes sentiment for all posts (30-50 posts per week typically)
3. ✅ Generates bar chart, reports, and updates website
4. ✅ Sends email to all 3 recipients with PDF attachment
5. ✅ Pushes updates to GitHub (website auto-updates)

**Example:** On Sunday Nov 17 at 8 PM, it will scrape and report on **Nov 11-17** data.

---

## 🧪 How to Run Manually (For Testing)

### Option 1: GitHub Actions (Recommended)

1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Click **"Weekly Reddit Sentiment Analysis"**
3. Click **"Run workflow"** button (top right)
4. Click **"Run workflow"** again to confirm
5. Wait 2-3 minutes
6. Check your email inbox

**Note:** This will scrape the **previous complete week**, not the current week. This is intentional for production use.

### Option 2: Local Command Line

```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 complete_automation.py
```

This will:
- Scrape Reddit for the previous week
- Generate all reports
- Send emails to all 3 recipients
- Update the website

---

## 📧 Email Report Contents

Each Sunday, you'll receive an email with:

### Quick Summary:
- Total posts per brand
- Positive percentage
- Sentiment breakdown (positive/negative/neutral counts)

### Top Posts:
- **Top 3 Positive Posts** per brand (sorted by engagement: upvotes + 3×comments)
- **Top 3 Negative Posts** per brand (sorted by engagement)
- Direct links to Reddit posts
- Subreddit, upvotes, and comment counts

### Attachments:
- **step1_chart.pdf** - Crystal-clear sentiment bar chart (zoomable, never blurry)

### Links:
- Main Dashboard
- Deep Dive Analysis (HelloFresh & Factor)
- Full Competitor Report (all 8 brands)

---

## 📊 Data Accuracy

### Sentiment Analysis Details:

**Positive Post Criteria:**
- Contains phrases like: "love it", "amazing", "excellent", "highly recommend", "delicious", "fresh"
- VADER compound score ≥ 0.05
- TextBlob polarity ≥ 0.1
- NOT a question or comparison post

**Negative Post Criteria:**
- Contains phrases like: "terrible", "avoid", "cancelled", "disappointed", "waste of money", "rotten"
- VADER compound score ≤ -0.05
- TextBlob polarity ≤ -0.1

**Neutral Post Criteria:**
- Questions (ends with "?")
- Comparisons ("vs", "which is better", "switching to")
- Recommendations requests ("anyone tried", "looking for")
- Ambiguous sentiment

### Data Filtering:

**Posts EXCLUDED:**
- Spam/promotional content
- Off-topic discussions (SNAP benefits, environmental factors)
- Posts not genuinely about meal kit services
- Duplicate posts

**Posts INCLUDED:**
- Brand-specific subreddit posts (r/hellofresh, r/factor75, etc.)
- Meal kit discussion posts (r/mealkits, r/ReadyMeals)
- Customer experience discussions
- Recipe/meal reviews
- Service comparisons

---

## 🌐 Website Dashboard

**Live URL:** https://ktsering2025.github.io/reddit-competitor-sentiment/

**Auto-Updates:** Every Sunday after the automation runs

**Contents:**
- Interactive sentiment bar chart
- Current week's data summary
- Links to detailed reports
- Archive of previous weeks

---

## 🔍 Verification Checklist

Before each Sunday run, the system validates:
- ✅ Date window is 4-8 days (full week)
- ✅ Sentiment totals match (positive + negative + neutral = total)
- ✅ All brands are tracked (even if 0 posts)
- ✅ Reddit API is working
- ✅ Email credentials are valid

If validation fails, the automation stops and logs the error.

---

## 📁 File Structure

### Core Scripts:
- `accurate_scraper.py` - Reddit scraping with sentiment analysis
- `step1_chart.py` - Generates bar chart (PNG + PDF)
- `step2_ACTIONABLE_analysis.py` - Deep dive for HelloFresh & Factor
- `step3_competitor_analysis.py` - Full competitor report
- `send_to_gmail_smtp.py` - Email sender
- `complete_automation.py` - Orchestrates everything
- `update_homepage.py` - Updates website dashboard

### Configuration:
- `config.py` - All settings (brands, links, thresholds)
- `.env` - Local credentials (not in GitHub)
- `.github/workflows/weekly-automation.yml` - GitHub Actions schedule

### Reports:
- `reports/working_reddit_data.json` - Current week's data
- `reports/step1_chart.png` - Bar chart image
- `reports/step1_chart.pdf` - Bar chart PDF (for email)
- `reports/step2_ACTIONABLE_analysis_LATEST.html` - Deep dive report
- `reports/step3_competitor_analysis_LATEST.html` - Competitor report
- `reports/archive/YYYY-MM-DD/` - Historical data

---

## 🚨 Troubleshooting

### "0 posts" in email report:
→ Reddit API secrets not added to GitHub (see Step 1 above)

### Email not received:
→ Check GitHub Actions logs for errors
→ Verify GMAIL_APP_PASSWORD is correct in GitHub Secrets

### Wrong date range:
→ System uses PREVIOUS complete week (Monday-Sunday)
→ This is intentional - Sunday reports on the week that just ended

### Sentiment seems wrong:
→ Check `reports/working_reddit_data.json` for reasoning field
→ Sentiment uses dual-method + keyword overrides for accuracy

---

## 📞 Support

**GitHub Repository:** https://github.com/ktsering2025/reddit-competitor-sentiment

**Check Automation Status:**
- GitHub Actions: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
- Latest Run Logs: Click on most recent workflow run

**Manual Test:**
- Run workflow manually (see "How to Run Manually" section above)
- Check email within 3 minutes

---

## ✅ Production Ready

- ✅ Sentiment analysis: Dual-method (VADER + TextBlob) with context awareness
- ✅ Time frame: 7-day weekly (previous complete Monday-Sunday week)
- ✅ Schedule: Every Sunday 8:00 PM EST
- ✅ Automation: GitHub Actions (no manual intervention needed)
- ✅ Email: Professional report with top posts and PDF chart
- ✅ Website: Auto-updates with latest data
- ✅ Validation: Built-in data integrity checks

**Status: READY FOR PRODUCTION** 🚀

Next automatic run: **Sunday, November 17, 2025 at 8:00 PM EST**
