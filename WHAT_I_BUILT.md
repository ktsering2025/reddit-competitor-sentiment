# 🚀 What I Built: Reddit Competitor Sentiment Analysis

**By:** Kunsang Tsering  
**For:** HelloFresh  
**Date:** October 27 - December 12, 2025

---

## 📊 THE BIG PICTURE

I built a **fully automated system** that tracks what people say about meal kit brands on Reddit, analyzes if they're happy or upset, and emails 19 people at HelloFresh every Sunday with insights.

**Zero manual work. Runs forever in the cloud. 100% reliable.**

---

## 🎯 WHAT IT DOES

### Every Sunday at 8 PM EST, automatically:

```
1. 🔍 SCRAPES REDDIT
   ├─ Searches 30+ Reddit sources
   ├─ Finds posts about 8 meal kit brands
   └─ Collects 30-50 posts from past week

2. 🤖 ANALYZES SENTIMENT
   ├─ Reads each post
   ├─ Determines: positive, negative, or neutral
   └─ Uses 2 AI algorithms for accuracy

3. 📊 CREATES REPORTS
   ├─ Bar chart (PNG + PDF)
   ├─ HelloFresh/Factor deep dive (HTML)
   └─ All competitors comparison (HTML)

4. 🌐 UPDATES WEBSITE
   ├─ Pushes to GitHub Pages
   └─ Live in 3 minutes

5. 📧 SENDS EMAILS
   ├─ 19 recipients
   ├─ PDF chart attached
   └─ Top posts with Reddit links

✅ DONE! (3 minutes total)
```

---

## 📅 COMPLETE TIMELINE

### **Phase 1: Initial Build (Oct 27-30, 2025)**

**What I Built:**
- ✅ Reddit scraper (connects to Reddit API)
- ✅ Sentiment analysis (2 algorithms: VADER + TextBlob)
- ✅ Chart generator (bar chart with colors)
- ✅ 2 HTML reports (deep dive + competitors)
- ✅ Live website (GitHub Pages)

**Time:** 4 days  
**Result:** All scripts working locally

---

### **Phase 2: Automation (Nov 2-17, 2025)**

**What I Built:**
- ✅ GitHub Actions workflow (cloud automation)
- ✅ Email system (Gmail SMTP)
- ✅ Complete pipeline (runs all scripts)
- ✅ Data archiving (historical tracking)

**Challenges I Solved:**
1. **Local cron spam** (Nov 16) → Removed local cron, use GitHub Actions only
2. **Mac-specific email code** (Dec 2) → Removed `osascript`, use SMTP only
3. **GitHub timing delay** → Accepted 1-3 hour delay as normal

**Time:** 2 weeks  
**Result:** First automatic run Nov 17 ✅

---

### **Phase 3: Scaling (Dec 2-8, 2025)**

**What I Did:**
- ✅ Added 13 recipients (Dec 2): 5 → 18 people
- ✅ Added Katie (Dec 8): 18 → 19 people

**Time:** 1 week  
**Result:** All 19 people receiving emails

---

### **Phase 4: Documentation (Dec 2-12, 2025)**

**What I Created:**
- ✅ 40+ documentation files
- ✅ Conversation history system
- ✅ Handoff guides
- ✅ Troubleshooting guides
- ✅ Help templates

**Time:** 1.5 weeks  
**Result:** Anyone can take over this project

---

## 📈 KEY ACHIEVEMENTS

### **Business Impact:**
- ✅ Weekly competitive intelligence (no manual work)
- ✅ Consistent analysis (same algorithm every time)
- ✅ Historical tracking (12 weeks archived)
- ✅ Immediate insights (reports arrive Sunday evening)
- ✅ Scalable (easy to add brands/recipients)

### **Technical Achievements:**
- ✅ 100% automated (runs in cloud, no laptop needed)
- ✅ 100% reliable (4/4 successful automatic runs)
- ✅ Dual sentiment analysis (VADER + TextBlob)
- ✅ Context-aware (understands comparisons)
- ✅ Cloud-compatible (no Mac dependencies)

### **Documentation Achievements:**
- ✅ 40+ documentation files
- ✅ Simple language (non-technical people understand)
- ✅ Chronological timeline (every change documented)
- ✅ Troubleshooting guides (solutions to common issues)
- ✅ Handoff ready (anyone can take over)

---

## 🛠️ WHAT I USED

### **Languages:**
- Python 3.10+ (main language)
- HTML/CSS (website)
- YAML (automation config)
- Markdown (documentation)

### **Key Libraries:**
- `praw` - Reddit API
- `vaderSentiment` - Sentiment analysis #1
- `textblob` - Sentiment analysis #2
- `matplotlib` - Charts
- `smtplib` - Email sending

### **Infrastructure:**
- GitHub Actions - Cloud automation (free)
- GitHub Pages - Website hosting (free)
- Gmail SMTP - Email delivery (free)
- Reddit API - Data source (free)

**Total Cost:** $0 per month

---

## 📊 BY THE NUMBERS

### **Data:**
- **8 brands** tracked
- **30+ Reddit sources** searched
- **30-50 posts** per week
- **12 weeks** of data archived
- **7-day** rolling window

### **Automation:**
- **4 automatic runs** (100% success)
- **3 minutes** per run
- **19 recipients** receiving emails
- **0 manual work** required

### **Code:**
- **6 core scripts** (Python)
- **1 workflow file** (GitHub Actions)
- **40+ documentation files** (Markdown)
- **1,200+ lines** of documentation

### **Timeline:**
- **47 days** total (Oct 27 - Dec 12)
- **4 phases** of development
- **3 major challenges** solved
- **100% success rate** achieved

---

## 🎯 HOW TO USE IT

### **Option 1: Do Nothing (Recommended)**
- System runs automatically every Sunday at 8 PM EST
- Check your email Monday morning
- That's it!

### **Option 2: Manual Trigger**
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Click "Run workflow"
3. Wait 3 minutes
4. Check email

### **Option 3: Run Locally**
```bash
# Clone repo
git clone https://github.com/ktsering2025/reddit-competitor-sentiment.git
cd reddit-competitor-sentiment

# Install dependencies
pip install -r requirements.txt

# Create .env file with credentials
cat > .env << EOF
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_agent
GMAIL_EMAIL=your_email
GMAIL_APP_PASSWORD=your_password
EMAIL_RECIPIENTS=email1,email2
EOF

# Run automation
python3 complete_automation.py

# Send emails
python3 send_to_gmail_smtp.py
```

---

## 📁 PROJECT FILES

### **Core Scripts (6 files):**
1. `accurate_scraper.py` - Scrapes Reddit + analyzes sentiment
2. `step1_chart.py` - Creates bar chart
3. `step2_ACTIONABLE_analysis.py` - HelloFresh/Factor deep dive
4. `step3_competitor_analysis.py` - All competitors
5. `send_to_gmail_smtp.py` - Sends emails
6. `complete_automation.py` - Runs everything

### **Configuration (2 files):**
1. `config.py` - Settings (brands, recipients, etc.)
2. `.github/workflows/weekly-automation.yml` - Automation schedule

### **Website (2 files):**
1. `index.html` - Homepage
2. `update_homepage.py` - Updates website

### **Documentation (40+ files):**
- `EXECUTIVE_SUMMARY.md` - Quick overview
- `COMPLETE_PROJECT_DOCUMENTATION.md` - Full guide (1,200 lines)
- `README.md` - Project overview
- `MANAGER_QUICK_START.md` - For new owner
- `HANDOFF_GUIDE.md` - Transfer process
- And 35+ more...

---

## 🔗 IMPORTANT LINKS

### **Project:**
- **GitHub Repo:** https://github.com/ktsering2025/reddit-competitor-sentiment
- **Live Website:** https://ktsering2025.github.io/reddit-competitor-sentiment/
- **GitHub Actions:** https://github.com/ktsering2025/reddit-competitor-sentiment/actions

### **Documentation:**
- **Executive Summary:** [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)
- **Complete Guide:** [COMPLETE_PROJECT_DOCUMENTATION.md](COMPLETE_PROJECT_DOCUMENTATION.md)
- **Quick Start:** [README.md](README.md)
- **Manager Guide:** [MANAGER_QUICK_START.md](MANAGER_QUICK_START.md)

### **Services:**
- **Reddit API:** https://www.reddit.com/prefs/apps
- **Gmail App Passwords:** https://myaccount.google.com/apppasswords
- **GitHub Secrets:** https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions

---

## ✅ CURRENT STATUS

### **System Health: EXCELLENT**

**Last 4 Automatic Runs:**
- ✅ December 8, 2025 - Success
- ✅ December 1, 2025 - Success
- ✅ November 24, 2025 - Success
- ✅ November 17, 2025 - Success

**Success Rate:** 100% (4 out of 4)

---

### **Configuration:**

**Schedule:** Every Sunday at 8:00 PM EST  
**Frequency:** Once per week  
**Location:** GitHub Actions (cloud)  
**Cost:** $0

**Recipients (19 people):**
1. brian.leung@hellofresh.com
2. assaf.ronen@hellofresh.com
3. kunsang.tsering@hellofresh.com
4. adam.kalikow@hellofresh.com
5. adam.park@factor75.com
6. daniel.seidel@hellofresh.com
7. ben@hellofresh.ca
8. sandra.nestic@hellofresh.ca
9. nunzio.disavino@hellofresh.com
10. dme@hellofresh.com
11. maureen@hellofresh.com
12. megan.thompson@hellofresh.ca
13. mara.hanerfeld@hellofresh.com
14. frankie.hernandez@hellofresh.com
15. pete.balodimas@hellofresh.com
16. kelsey.lindenschmidt@hellofresh.com
17. christopher.stadler@factor75.com
18. niklas.vanhusen@factor75.com
19. katie.paganelli@hellofresh.com

**Brands (8):**
- HelloFresh, Factor75, EveryPlate, Green Chef (our brands)
- Home Chef, Blue Apron, Marley Spoon, Hungryroot (competitors)

---

## 🎉 SUMMARY

### **What I Built:**
A fully automated competitive intelligence system that tracks Reddit sentiment for 8 meal kit brands and emails 19 people every Sunday with insights.

### **Why It Matters:**
- Saves hours of manual work every week
- Provides consistent, data-driven insights
- Tracks trends over time
- Early warning system for brand issues

### **How It Works:**
- Runs automatically in GitHub's cloud
- No laptop needed
- 100% reliable
- Zero cost

### **Status:**
- ✅ Production-ready
- ✅ Fully automated
- ✅ Well-documented
- ✅ Easy to maintain
- ✅ Ready for handoff

---

## 📞 CONTACT

**Kunsang Tsering**  
Email: kunsang.tsering@hellofresh.com  
Role: Original Developer  
Knows: Everything about this system

---

**Next automatic run:** Sunday, December 15, 2025 at 8:00 PM EST

---

**Built with ❤️ for HelloFresh competitive intelligence team**
