# 🔴 URGENT: Add Reddit API Secrets to GitHub

## Why You're Getting 0 Posts:

GitHub Actions doesn't have your Reddit API credentials, so it can't scrape Reddit!

---

## Quick Fix (2 minutes):

### Go to GitHub Secrets:
https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions

### Add These 3 Secrets:

**Secret 1:**
- Name: `REDDIT_CLIENT_ID`
- Value: `kG3E8fifKfnd-tu1BeWH3g`

**Secret 2:**
- Name: `REDDIT_CLIENT_SECRET`
- Value: `33tI4yhvAgBE5jUATtN8SUQY8TeQjA`

**Secret 3:**
- Name: `REDDIT_USER_AGENT`
- Value: `CompetitorSentimentBot/1.0`

---

## After Adding Secrets:

### Test It:
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Click "Weekly Reddit Sentiment Analysis"
3. Click "Run workflow" → "Run workflow"
4. Wait 2-3 minutes
5. Check your email

**You'll get REAL DATA this time!** (Nov 3-9 had 32+ posts)

---

## Current Status:

✅ Email password working  
✅ Scraper code working  
✅ PREVIOUS_COMPLETE_WEEK mode working  
❌ **Reddit API secrets missing in GitHub** ← THIS IS THE PROBLEM

Once you add the 3 Reddit secrets, everything will work!
