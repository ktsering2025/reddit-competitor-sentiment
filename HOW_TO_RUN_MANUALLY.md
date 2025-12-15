# 🚀 How to Run This Project Manually

**For:** Developers, Technical Users, or Anyone Who Wants to Run It Locally

---

## 📋 TABLE OF CONTENTS

1. [Prerequisites](#prerequisites)
2. [One-Time Setup](#one-time-setup)
3. [Running the Full Automation](#running-the-full-automation)
4. [Running Individual Scripts](#running-individual-scripts)
5. [Troubleshooting](#troubleshooting)

---

## 1. PREREQUISITES

Before you start, make sure you have:

### **Software:**
- ✅ Python 3.10 or higher
- ✅ Git
- ✅ Terminal/Command Line access

### **Accounts & Credentials:**
- ✅ Reddit account with API access
- ✅ Gmail account with app password
- ✅ GitHub account (for pushing results)

### **Check Python Version:**
```bash
python3 --version
# Should show: Python 3.10.x or higher
```

---

## 2. ONE-TIME SETUP

### **Step 1: Clone the Repository**

```bash
# Clone from GitHub
git clone https://github.com/ktsering2025/reddit-competitor-sentiment.git

# Navigate to project directory
cd reddit-competitor-sentiment
```

---

### **Step 2: Install Dependencies**

```bash
# Install all required Python libraries
pip install -r requirements.txt

# Or use pip3 if pip doesn't work
pip3 install -r requirements.txt
```

**What this installs:**
- `praw` - Reddit API wrapper
- `vaderSentiment` - Sentiment analysis
- `textblob` - Sentiment analysis
- `matplotlib` - Chart generation
- `python-dotenv` - Environment variables
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests

---

### **Step 3: Get Reddit API Credentials**

1. **Go to:** https://www.reddit.com/prefs/apps
2. **Click:** "Create App" or "Create Another App"
3. **Fill in:**
   - Name: `reddit-sentiment-bot` (or any name)
   - App type: **script**
   - Description: `Sentiment analysis for meal kit brands`
   - About URL: (leave blank)
   - Redirect URI: `http://localhost:8080`
4. **Click:** "Create app"
5. **Save these values:**
   - **Client ID:** The string under "personal use script" (14 characters)
   - **Client Secret:** The "secret" field (27 characters)
   - **User Agent:** `reddit-sentiment-bot/1.0 by YOUR_REDDIT_USERNAME`

---

### **Step 4: Get Gmail App Password**

1. **Go to:** https://myaccount.google.com/apppasswords
2. **Select app:** Mail
3. **Select device:** Other (Custom name)
4. **Enter name:** `Reddit Sentiment Bot`
5. **Click:** Generate
6. **Copy:** The 16-character password (no spaces)

**Note:** You must have 2-factor authentication enabled on your Gmail account.

---

### **Step 5: Create `.env` File**

Create a file named `.env` in the project root directory:

```bash
# Create .env file
cat > .env << 'EOF'
# Reddit API Credentials
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=reddit-sentiment-bot/1.0 by YOUR_REDDIT_USERNAME

# Gmail Credentials
GMAIL_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_16_char_app_password

# Email Recipients (comma-separated, no spaces)
EMAIL_RECIPIENTS=email1@example.com,email2@example.com,email3@example.com
EOF
```

**Replace with your actual values:**
- `your_client_id_here` → Your Reddit client ID
- `your_client_secret_here` → Your Reddit client secret
- `YOUR_REDDIT_USERNAME` → Your Reddit username
- `your_email@gmail.com` → Your Gmail address
- `your_16_char_app_password` → Your Gmail app password
- `email1@example.com,email2@example.com` → Recipient emails

**Example:**
```bash
REDDIT_CLIENT_ID=abc123def456ghi
REDDIT_CLIENT_SECRET=xyz789uvw456rst123abc
REDDIT_USER_AGENT=reddit-sentiment-bot/1.0 by john_doe
GMAIL_EMAIL=john.doe@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
EMAIL_RECIPIENTS=brian.leung@hellofresh.com,assaf.ronen@hellofresh.com
```

---

### **Step 6: Test Your Setup**

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Test Reddit API
python3 -c "import praw; print('Reddit API: OK')"

# Test Gmail credentials
python3 -c "import os; print('Gmail:', os.getenv('GMAIL_EMAIL'))"
```

**Expected output:**
```
Reddit API: OK
Gmail: your_email@gmail.com
```

---

## 3. RUNNING THE FULL AUTOMATION

### **Option 1: Run Complete Pipeline (Recommended)**

This runs everything: scraping, analysis, charts, reports, website update, and email.

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Run complete automation
python3 complete_automation.py
```

**What this does:**
1. ✅ Scrapes Reddit for posts (30-50 posts)
2. ✅ Analyzes sentiment (VADER + TextBlob)
3. ✅ Generates bar chart (PNG + PDF)
4. ✅ Creates 2 HTML reports
5. ✅ Updates website (index.html)
6. ✅ Archives data to `reports/archive/YYYY-MM-DD/`
7. ✅ Commits and pushes to GitHub
8. ✅ Sends emails to all recipients

**Time:** ~3 minutes

**Output:**
```
=== REDDIT SENTIMENT AUTOMATION ===
[1/7] Scraping Reddit...
  ✓ Found 42 posts
[2/7] Generating chart...
  ✓ Chart saved: reports/step1_chart.png
[3/7] Creating analysis reports...
  ✓ Step 2 report saved
  ✓ Step 3 report saved
[4/7] Updating website...
  ✓ Website updated
[5/7] Archiving data...
  ✓ Archived to reports/archive/2025-12-12/
[6/7] Committing to GitHub...
  ✓ Committed and pushed
[7/7] Sending emails...
  ✓ Sent to 19 recipients
✅ AUTOMATION COMPLETE!
```

---

### **Option 2: Run Without Sending Emails**

If you want to generate reports but not send emails:

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Run automation without sending emails
python3 complete_automation.py --no-send
```

**What this does:**
- Same as Option 1, but skips the email sending step
- Good for testing or generating reports for yourself

---

### **Option 3: Send Emails Only**

If you already have reports and just want to send emails:

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Send emails with latest reports
python3 send_to_gmail_smtp.py
```

**What this does:**
- Reads latest data from `reports/working_reddit_data.json`
- Creates HTML email with top posts
- Attaches `reports/step1_chart.pdf`
- Sends to all recipients in `EMAIL_RECIPIENTS`

---

## 4. RUNNING INDIVIDUAL SCRIPTS

If you want to run scripts one at a time:

### **Step 1: Scrape Reddit**

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Scrape Reddit and analyze sentiment
python3 accurate_scraper.py
```

**Output:** `reports/working_reddit_data.json`

---

### **Step 2: Generate Chart**

```bash
# Create bar chart from scraped data
python3 step1_chart.py
```

**Output:** 
- `reports/step1_chart.png` (for website)
- `reports/step1_chart.pdf` (for email)

---

### **Step 3: Create Analysis Reports**

```bash
# HelloFresh & Factor deep dive
python3 step2_ACTIONABLE_analysis.py

# All competitors comparison
python3 step3_competitor_analysis.py
```

**Output:**
- `reports/step2_ACTIONABLE_analysis_LATEST.html`
- `reports/step3_competitor_analysis_LATEST.html`

---

### **Step 4: Update Website**

```bash
# Update homepage with latest data
python3 update_homepage.py
```

**Output:** `index.html` (updated)

---

### **Step 5: Send Emails**

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Send email report
python3 send_to_gmail_smtp.py
```

**Output:** Emails sent to all recipients

---

## 5. TROUBLESHOOTING

### **Issue: "ModuleNotFoundError: No module named 'praw'"**

**Solution:**
```bash
pip install -r requirements.txt
# Or
pip3 install -r requirements.txt
```

---

### **Issue: "Reddit API Error: 401 Unauthorized"**

**Solution:**
- Check your Reddit API credentials in `.env`
- Make sure `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are correct
- Verify your Reddit app is a "script" type (not "web app")

---

### **Issue: "Gmail SMTP Error: Authentication failed"**

**Solution:**
- Check your Gmail app password in `.env`
- Make sure you're using an **app password**, not your regular Gmail password
- Verify 2-factor authentication is enabled on your Gmail account
- Generate a new app password at: https://myaccount.google.com/apppasswords

---

### **Issue: "No posts found"**

**Solution:**
- This is normal if Reddit has no new posts for the brands this week
- Check `reports/working_reddit_data.json` to see if any posts were scraped
- Try running again later or check Reddit manually

---

### **Issue: "git push failed"**

**Solution:**
```bash
# Pull latest changes first
git pull --rebase origin main

# Then push again
git push origin main
```

---

### **Issue: "Environment variables not loaded"**

**Solution:**
```bash
# Make sure to load .env before running scripts
export $(cat .env | grep -v '^#' | xargs)

# Then run your script
python3 complete_automation.py
```

---

### **Issue: "Permission denied: .env"**

**Solution:**
```bash
# Make sure .env file exists
ls -la .env

# If it doesn't exist, create it
cat > .env << 'EOF'
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
# ... rest of credentials
EOF
```

---

## 📝 QUICK REFERENCE

### **Complete Automation (One Command):**
```bash
export $(cat .env | grep -v '^#' | xargs) && python3 complete_automation.py
```

### **Generate Reports Only (No Email):**
```bash
export $(cat .env | grep -v '^#' | xargs) && python3 complete_automation.py --no-send
```

### **Send Emails Only:**
```bash
export $(cat .env | grep -v '^#' | xargs) && python3 send_to_gmail_smtp.py
```

### **Run Individual Scripts:**
```bash
# 1. Scrape Reddit
export $(cat .env | grep -v '^#' | xargs) && python3 accurate_scraper.py

# 2. Generate chart
python3 step1_chart.py

# 3. Create reports
python3 step2_ACTIONABLE_analysis.py
python3 step3_competitor_analysis.py

# 4. Update website
python3 update_homepage.py

# 5. Send emails
export $(cat .env | grep -v '^#' | xargs) && python3 send_to_gmail_smtp.py
```

---

## 🔗 HELPFUL LINKS

**Documentation:**
- [COMPLETE_PROJECT_DOCUMENTATION.md](COMPLETE_PROJECT_DOCUMENTATION.md) - Full guide
- [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) - Quick overview
- [README.md](README.md) - Project overview

**External Services:**
- [Reddit API Apps](https://www.reddit.com/prefs/apps) - Create Reddit app
- [Gmail App Passwords](https://myaccount.google.com/apppasswords) - Generate app password
- [GitHub Actions](https://github.com/ktsering2025/reddit-competitor-sentiment/actions) - View automation runs

---

## 📞 NEED HELP?

**Contact:** Kunsang Tsering  
**Email:** kunsang.tsering@hellofresh.com  
**Role:** Original Developer

---

**Last Updated:** December 12, 2025  
**Status:** ✅ Tested and Working
