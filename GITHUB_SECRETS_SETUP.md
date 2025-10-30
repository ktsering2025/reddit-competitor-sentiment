# 🔐 GitHub Secrets Setup Guide

## Step 1: Go to GitHub Repository Settings

1. Open your browser and go to: https://github.com/ktsering2025/reddit-competitor-sentiment
2. Click **"Settings"** tab (top right)
3. In the left sidebar, click **"Secrets and variables"** → **"Actions"**

---

## Step 2: Add These 6 Secrets

Click **"New repository secret"** for each one:

### Secret 1: REDDIT_CLIENT_ID
- **Name:** `REDDIT_CLIENT_ID`
- **Value:** `kG3E8fifKfnd-tu1BeWH3g`

### Secret 2: REDDIT_CLIENT_SECRET
- **Name:** `REDDIT_CLIENT_SECRET`
- **Value:** `33tI4yhvAgBE5jUATtN8SUQY8TeQjA`

### Secret 3: REDDIT_USER_AGENT
- **Name:** `REDDIT_USER_AGENT`
- **Value:** `CompetitorSentimentBot/1.0`

### Secret 4: GMAIL_EMAIL
- **Name:** `GMAIL_EMAIL`
- **Value:** `kunsang.tsering@hellofresh.com`

### Secret 5: GMAIL_APP_PASSWORD
- **Name:** `GMAIL_APP_PASSWORD`
- **Value:** `Chess16$`

### Secret 6: EMAIL_RECIPIENTS
- **Name:** `EMAIL_RECIPIENTS`
- **Value:** `brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com`

---

## Step 3: Test the Workflow

After adding all 6 secrets:

1. Go to **"Actions"** tab in your GitHub repo
2. Click **"Weekly Reddit Sentiment Analysis"** workflow
3. Click **"Run workflow"** button (right side)
4. Click green **"Run workflow"** button
5. Wait 2-3 minutes
6. Check your email! 📧

---

## ✅ What Happens Every Sunday at 8 PM EST:

1. GitHub Actions runs automatically (no laptop needed!)
2. Scrapes **NEW** Reddit posts (past 7 days)
3. Generates **NEW** charts with fresh data
4. Creates **NEW** Step 2 & Step 3 reports
5. Updates **README.md** and all files
6. Commits to GitHub
7. Pushes to GitHub Pages
8. Sends emails to all 3 people

---

## 🎯 Files That Get Updated Automatically:

- ✅ `reports/step1_chart.png` (new chart)
- ✅ `reports/step1_chart.pdf` (new PDF)
- ✅ `reports/step2_ACTIONABLE_analysis_LATEST.html` (new deep dive)
- ✅ `reports/step3_competitor_analysis_LATEST.html` (new competitor analysis)
- ✅ `reports/working_reddit_data.json` (new raw data)
- ✅ `reports/SUMMARY.json` (new summary)
- ✅ `reports/HEALTH.json` (new health check)
- ✅ `index.html` (updated landing page)
- ✅ All archive files in `reports/archive/[date]/`
- ✅ All raw files in `reports/raw/`

**Everything gets pushed to GitHub automatically!** 🚀

---

## 🔒 Security Note:

Your secrets are encrypted and only accessible to GitHub Actions. Nobody (including you) can see them after they're added.

---

## ❓ Need Help?

If you get stuck, just ask me! I'm here to help. 😊
