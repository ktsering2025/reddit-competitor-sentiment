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

**Every Sunday at 8:00 PM EST (Automatic):**
- Scrapes Reddit for the **previous complete week** (Monday-Sunday)
- Analyzes 30-50 posts per week
- Sends email to 19 recipients (see below)
- Updates website: https://ktsering2025.github.io/reddit-competitor-sentiment/

**Next Run:** Sunday, December 15, 2025 at 8:00 PM EST

**Current Recipients (19 people):**
- brian.leung@hellofresh.com
- assaf.ronen@hellofresh.com
- kunsang.tsering@hellofresh.com
- adam.kalikow@hellofresh.com
- adam.park@factor75.com
- daniel.seidel@hellofresh.com
- ben@hellofresh.ca
- sandra.nestic@hellofresh.ca
- nunzio.disavino@hellofresh.com
- dme@hellofresh.com
- maureen@hellofresh.com
- megan.thompson@hellofresh.ca
- mara.hanerfeld@hellofresh.com
- frankie.hernandez@hellofresh.com
- pete.balodimas@hellofresh.com
- kelsey.lindenschmidt@hellofresh.com
- christopher.stadler@factor75.com
- niklas.vanhusen@factor75.com
- katie.paganelli@hellofresh.com

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

## 🚀 Quick Start (For New Users)

### ⚡ Option 1: Wait for Automatic Run (Recommended)

**Do nothing!** The system runs automatically every Sunday at 8 PM EST.

- ✅ Runs in GitHub's cloud (no laptop needed)
- ✅ 100% reliable (4/4 successful runs)
- ✅ Emails sent automatically to all 19 recipients
- ✅ Website updates automatically

**Just check your email Monday morning!**

---

### ⚡ Option 2: Manual Trigger (If You Need a Report Now)

1. **Go to GitHub Actions:**  
   👉 [Click here to run workflow](https://github.com/ktsering2025/reddit-competitor-sentiment/actions/workflows/weekly-automation.yml)

2. **Click the green "Run workflow" button**  
   → Then click "Run workflow" again

3. **Wait 3 minutes**  
   → Check your email! 📧

**That's it!** You'll get a full report with:
- 📊 Sentiment bar chart (PDF attached)
- 📝 Top positive & negative posts per brand
- 🔗 Links to detailed analysis

---

### ⚡ Option 3: Run Locally (For Developers)

**Prerequisites:**
- Python 3.10+
- Reddit API credentials
- Gmail app password
- `.env` file configured

**Steps:**

```bash
# 1. Clone the repository
git clone https://github.com/ktsering2025/reddit-competitor-sentiment.git
cd reddit-competitor-sentiment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file with credentials
cat > .env << EOF
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
GMAIL_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password
EMAIL_RECIPIENTS=email1@example.com,email2@example.com
EOF

# 4. Run the complete automation
python3 complete_automation.py

# 5. Send emails (optional - automation does this automatically)
python3 send_to_gmail_smtp.py
```

**What this does:**
1. Scrapes Reddit for posts from the past week
2. Analyzes sentiment using VADER + TextBlob
3. Generates bar chart (PNG + PDF)
4. Creates 2 HTML analysis reports
5. Updates website (index.html)
6. Archives data to `reports/archive/YYYY-MM-DD/`
7. Commits and pushes to GitHub
8. Sends emails to all recipients

**Time:** ~3 minutes

📖 **See [COMPLETE_PROJECT_DOCUMENTATION.md](COMPLETE_PROJECT_DOCUMENTATION.md) for detailed technical guide**

---

### 🔧 First-Time Setup (For Admins):

If you're setting this up for the first time, you need to add GitHub Secrets:

1. Go to: [Settings → Secrets → Actions](https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions)
2. Add these 6 secrets:
   - `REDDIT_CLIENT_ID` - Your Reddit app client ID
   - `REDDIT_CLIENT_SECRET` - Your Reddit app secret
   - `REDDIT_USER_AGENT` - Your Reddit app name
   - `GMAIL_EMAIL` - Gmail address for sending
   - `GMAIL_APP_PASSWORD` - Gmail app password (not regular password)
   - `EMAIL_RECIPIENTS` - Comma-separated list of recipients

📖 **See [COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md) for detailed instructions**

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

### ⭐ Start Here
- **[EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)** - 📄 Quick overview of everything I built
- **[COMPLETE_PROJECT_DOCUMENTATION.md](COMPLETE_PROJECT_DOCUMENTATION.md)** - 📚 Complete guide (1,200 lines)
- **[README.md](README.md)** - 👋 This file (project overview)

### For Users
- **[WEEKLY_AUTOMATION_GUARANTEE.md](WEEKLY_AUTOMATION_GUARANTEE.md)** - How to ensure weekly reports
- **[AUTOMATION_EXPLAINED.md](AUTOMATION_EXPLAINED.md)** - Complete logic and workflow
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview
- **[AUTOMATION_STATUS.md](AUTOMATION_STATUS.md)** - Current status and health

### For Setup & Technical
- **[COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md)** - Full setup instructions
- **[HOW_AUTOMATION_WORKS.md](HOW_AUTOMATION_WORKS.md)** - Technical details
- **[TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md)** - Deep technical reference

### For Project Handoff
- **[START_HERE_HANDOFF.md](START_HERE_HANDOFF.md)** - 🔄 Quick handoff guide
- **[MANAGER_QUICK_START.md](MANAGER_QUICK_START.md)** - For new project owner
- **[HANDOFF_GUIDE.md](HANDOFF_GUIDE.md)** - Complete handoff process
- **[HANDOFF_CHECKLIST.md](HANDOFF_CHECKLIST.md)** - Track handoff progress
- **[EMAIL_TO_MANAGER.md](EMAIL_TO_MANAGER.md)** - Email templates

### For Getting Help
- **[HOW_TO_ASK_FOR_HELP.md](HOW_TO_ASK_FOR_HELP.md)** - 🆘 Asking ML/AI team
- **[ASK_FOR_HELP_TEMPLATE.md](ASK_FOR_HELP_TEMPLATE.md)** - Detailed templates
- **[SIMPLE_PROJECT_SUMMARY.md](SIMPLE_PROJECT_SUMMARY.md)** - One-page overview
- **[ELEVATOR_PITCH.md](ELEVATOR_PITCH.md)** - Quick pitches

### For Conversation History
- **[CONVERSATION_HISTORY_GUIDE.md](CONVERSATION_HISTORY_GUIDE.md)** - 📝 How to save AI chat sessions
- **[conversation_history/](conversation_history/)** - All saved conversation logs

---

## 🚨 Troubleshooting

### "Didn't get email this Sunday":
→ Manually trigger workflow: [Run workflow](https://github.com/ktsering2025/reddit-competitor-sentiment/actions/workflows/weekly-automation.yml) (takes 30 seconds)

### "0 posts" in report:
→ Check Reddit API secrets in GitHub Settings → Secrets

### Email not received:
→ Check [GitHub Actions logs](https://github.com/ktsering2025/reddit-competitor-sentiment/actions) for errors

### Wrong date range:
→ System uses **previous complete week** (Monday-Sunday) by design

---

## ✅ Status

- ✅ **Production Ready & Fully Automated**
- ✅ Sentiment analysis: Dual-method with context awareness
- ✅ Time frame: 7-day weekly (previous Monday-Sunday)
- ✅ Email: Professional report with top posts + PDF (19 recipients)
- ✅ Website: Auto-updates with latest data
- ✅ Automation: 100% reliable (4/4 successful automatic runs)
- ✅ Cloud-based: Runs on GitHub Actions (no laptop needed)

**Last 4 Automatic Runs:**
- ✅ December 8, 2025 - Success
- ✅ December 1, 2025 - Success
- ✅ November 24, 2025 - Success
- ✅ November 17, 2025 - Success

**Success Rate:** 100% (4 out of 4)

**Latest data:** December 8, 2025 (archived in `reports/archive/2025-12-08/`)

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
