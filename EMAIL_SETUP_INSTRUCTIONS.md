# Email Setup Instructions

## Why emails aren't sending
The automation needs your Gmail credentials to send emails. These must be added as **GitHub Secrets**.

## Setup Steps (5 minutes)

### Step 1: Generate Gmail App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Sign in with: `kunsang.tsering@hellofresh.com`
3. Click "Create" or "Generate app password"
4. Name it: `Reddit Sentiment Bot`
5. Copy the 16-character password (looks like: `abcd efgh ijkl mnop`)
6. Remove spaces: `abcdefghijklmnop`

### Step 2: Add GitHub Secrets
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions
2. Click "New repository secret" and add these 3 secrets:

   **Secret 1:**
   - Name: `GMAIL_EMAIL`
   - Value: `kunsang.tsering@hellofresh.com`

   **Secret 2:**
   - Name: `GMAIL_APP_PASSWORD`
   - Value: `[paste the 16-character password from Step 1]`

   **Secret 3:**
   - Name: `EMAIL_RECIPIENTS`
   - Value: `brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com`

### Step 3: Test It
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Click "Weekly Reddit Sentiment Analysis"
3. Click "Run workflow" → "Run workflow"
4. Wait 2-3 minutes
5. Check your email inbox - you should receive the weekly report!

## Automation Schedule
- **When**: Every Sunday at 8:00 PM EST
- **What**: Scrapes Reddit, generates reports, sends email to all 3 recipients
- **Email includes**: 
  - Quick summary stats for HelloFresh, Factor, Hungryroot, CookUnity
  - Top 3 positive and negative posts for each brand
  - PDF chart attachment (crystal clear)
  - Links to full dashboards

## Troubleshooting

### "Email failed" in GitHub Actions logs
→ Make sure you completed Step 1 & 2 above

### "Application-specific password required"
→ You need a Gmail App Password (not your regular password). See Step 1.

### Still not working?
→ Run the test in Step 3 and check the GitHub Actions logs for specific error messages

## Manual Email Send (for testing locally)
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 send_to_gmail_smtp.py
```

Note: For local testing, you also need to create a `.env` file with:
```
GMAIL_EMAIL=kunsang.tsering@hellofresh.com
GMAIL_APP_PASSWORD=your_16_char_password
EMAIL_RECIPIENTS=brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com
```
