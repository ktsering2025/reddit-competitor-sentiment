# 📊 Reddit Competitor Sentiment Analysis - Complete Project Documentation

**For: Anyone Taking Over This Project**  
**Created By: Kunsang Tsering**  
**Last Updated: December 8, 2025**  
**Status: ✅ Fully Operational & Automated**

---

## 🎯 TABLE OF CONTENTS

1. [What This Project Does](#what-this-project-does)
2. [Why We Built This](#why-we-built-this)
3. [How It Works (Simple Explanation)](#how-it-works)
4. [What I Did (Complete History)](#what-i-did)
5. [Current Status](#current-status)
6. [How to Monitor It](#how-to-monitor)
7. [How to Make Changes](#how-to-make-changes)
8. [Troubleshooting Guide](#troubleshooting)
9. [Technical Details (For Developers)](#technical-details)
10. [Contact & Support](#contact-support)

---

## 📖 WHAT THIS PROJECT DOES {#what-this-project-does}

### In Simple Terms:

**Every Sunday at 8 PM EST, this system automatically:**
1. Searches Reddit for posts about 8 meal kit brands
2. Reads each post and determines if it's positive, negative, or neutral
3. Creates charts and detailed reports
4. Emails 19 people at HelloFresh and Factor with the insights
5. Updates a live website with the latest data

**Your involvement: ZERO** - It runs completely automatically in the cloud!

---

### What You Get Every Week:

**📧 Email Report with:**
- Summary of sentiment for each brand
- Top 3 positive posts per brand
- Top 3 negative posts per brand
- PDF chart showing all brands
- Links to detailed analysis

**🌐 Live Website:**
- https://ktsering2025.github.io/reddit-competitor-sentiment/
- Updated automatically every Sunday
- Shows current week's data
- Archive of all previous weeks

---

### The 8 Brands We Track:

**HelloFresh Family (Our Brands):**
1. HelloFresh - Primary focus
2. Factor75 - Primary focus
3. EveryPlate
4. Green Chef

**Competitors:**
5. Home Chef
6. Blue Apron
7. Marley Spoon
8. Hungryroot

---

## 💡 WHY WE BUILT THIS {#why-we-built-this}

### The Business Problem:

**Before this project:**
- ❌ No systematic way to track competitor sentiment
- ❌ Manual Reddit searching took hours each week
- ❌ Inconsistent analysis (different people, different methods)
- ❌ No historical tracking
- ❌ Delayed insights (reports came days later)

**After this project:**
- ✅ Automatic weekly tracking (no manual work)
- ✅ Consistent sentiment analysis (same algorithm every time)
- ✅ Historical data archive (track trends over time)
- ✅ Immediate insights (reports arrive Sunday evening)
- ✅ Scalable (can add more brands or recipients easily)

---

### Business Value:

**For Leadership:**
- Weekly competitive intelligence without manual work
- Data-driven insights on brand perception
- Early warning system for brand issues
- Track effectiveness of marketing campaigns

**For Product Teams:**
- See what customers love/hate about competitors
- Identify product gaps and opportunities
- Understand customer pain points
- Validate product decisions with real feedback

**For Marketing:**
- Monitor brand sentiment trends
- Compare our brands vs competitors
- Identify messaging opportunities
- Track campaign impact on sentiment

---

## 🔧 HOW IT WORKS (SIMPLE EXPLANATION) {#how-it-works}

### The Complete Process:

```
Sunday 8 PM EST
    ↓
┌─────────────────────────────────────────┐
│ 1. SCRAPE REDDIT                        │
│    • Searches 30+ Reddit sources        │
│    • Finds posts from past week         │
│    • Collects ~30-50 posts              │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ 2. ANALYZE SENTIMENT                    │
│    • Reads each post                    │
│    • Determines: positive/negative/neutral │
│    • Uses 2 algorithms for accuracy     │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ 3. GENERATE REPORTS                     │
│    • Creates bar chart (PNG + PDF)      │
│    • Builds HTML analysis pages         │
│    • Ranks posts by engagement          │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ 4. UPDATE WEBSITE                       │
│    • Pushes to GitHub Pages             │
│    • Website updates automatically      │
│    • Takes 3 minutes to go live         │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ 5. SEND EMAILS                          │
│    • Sends to 19 recipients             │
│    • Includes PDF chart                 │
│    • Links to full reports              │
└─────────────────────────────────────────┘
    ↓
✅ DONE! (Total time: ~3 minutes)
```

---

### Where Does It Run?

**NOT on my laptop!** It runs on **GitHub's cloud servers**.

**What this means:**
- ✅ My laptop can be off, closed, or anywhere
- ✅ No need for my computer to be connected
- ✅ Runs 24/7 in the cloud
- ✅ 100% reliable (GitHub's servers, not mine)

**Think of it like:**
- Gmail sends emails even when your computer is off
- Netflix streams even when you're not home
- This automation runs even when my laptop is closed

---

## 📝 WHAT I DID (COMPLETE HISTORY) {#what-i-did}

### Phase 1: Initial Setup (October 2025)

**What I Built:**
1. **Reddit Scraper** (`accurate_scraper.py`)
   - Connects to Reddit API
   - Searches 30+ sources for each brand
   - Filters out spam and irrelevant posts
   - Collects posts from past week

2. **Sentiment Analysis** (Built into scraper)
   - Uses VADER algorithm (specialized for social media)
   - Uses TextBlob algorithm (general sentiment)
   - Combines both for accuracy
   - Context-aware (understands "Don't switch FROM X TO Y")

3. **Chart Generator** (`step1_chart.py`)
   - Creates bar chart showing all 8 brands
   - Color-coded (green=positive, red=negative, gray=neutral)
   - Exports as PNG (for website) and PDF (for email)

4. **Analysis Reports**
   - `step2_ACTIONABLE_analysis.py` - Deep dive on HelloFresh & Factor
   - `step3_competitor_analysis.py` - All competitors comparison
   - Both generate HTML reports with tables and insights

5. **Website** (`index.html` + `update_homepage.py`)
   - GitHub Pages hosted (free)
   - Shows latest chart and reports
   - Auto-updates every Sunday
   - Mobile-friendly design

**Why I Did It This Way:**
- Python for automation (easy to maintain)
- GitHub for hosting (free, reliable)
- SMTP for emails (works everywhere)
- Relative paths (cloud-compatible)

---

### Phase 2: Automation Setup (November 2025)

**What I Built:**
1. **GitHub Actions Workflow** (`.github/workflows/weekly-automation.yml`)
   - Cloud-based automation (not my laptop)
   - Runs every Sunday at 8 PM EST
   - Executes all scripts in sequence
   - Sends emails automatically

2. **Email System** (`send_to_gmail_smtp.py`)
   - Uses Gmail SMTP (cloud-compatible)
   - Sends HTML emails with embedded content
   - Attaches PDF chart
   - Includes top posts with links

3. **Complete Pipeline** (`complete_automation.py`)
   - Orchestrates all scripts
   - Validates data quality
   - Archives historical data
   - Commits results to GitHub

**Challenges I Solved:**
- ❌ **Problem:** Local cron job caused spam (multiple emails)
  - ✅ **Solution:** Removed local cron, use GitHub Actions only

- ❌ **Problem:** Email script used Mac-specific commands (osascript)
  - ✅ **Solution:** Rewrote to use SMTP only (works on cloud)

- ❌ **Problem:** GitHub Actions cron unreliable timing
  - ✅ **Solution:** Accepted 1-3 hour delay (normal for GitHub)

**Why I Did It This Way:**
- GitHub Actions = free, reliable, cloud-based
- SMTP = works on any platform
- Single workflow = easy to maintain

---

### Phase 3: Scaling Recipients (December 2025)

**What I Did:**
- **Started with:** 5 recipients (Brian, Assaf, me, Adam K, Adam P)
- **Added:** 13 more people (Daniel, Ben, Sandra, Nunzio, DME, Maureen, Megan, Mara, Frankie, Pete, Kelsey, Christopher, Niklas)
- **Added:** Katie Paganelli
- **Total now:** 19 recipients

**How I Did It:**
1. Updated `config.py` with new email list
2. Updated GitHub Secret `EMAIL_RECIPIENTS`
3. Tested with manual trigger
4. Verified all 19 people received emails

**Why I Did It This Way:**
- Centralized email list (easy to update)
- GitHub Secrets for security (credentials not in code)
- One change = updates everywhere

---

### Phase 4: Documentation & Handoff (December 2025)

**What I Created:**
1. **User Guides:**
   - `README.md` - Project overview
   - `MANAGER_QUICK_START.md` - For new owner
   - `WEEKLY_AUTOMATION_GUARANTEE.md` - How to ensure reports

2. **Technical Docs:**
   - `TECHNICAL_DOCUMENTATION.md` - Code details
   - `AUTOMATION_EXPLAINED.md` - How automation works
   - `AUTOMATION_STATUS.md` - Current health status

3. **Handoff Materials:**
   - `HANDOFF_GUIDE.md` - Complete transfer process
   - `HANDOFF_CHECKLIST.md` - Step-by-step tasks
   - `EMAIL_TO_MANAGER.md` - Email templates

4. **Help Resources:**
   - `HOW_TO_ASK_FOR_HELP.md` - Reaching out to ML/AI team
   - `TROUBLESHOOTING.md` - Common issues & fixes
   - `AUTOMATION_ANALYSIS_REPORT.md` - Proof it works

5. **Conversation History:**
   - `conversation_history/` - All AI chat sessions
   - Tracks decisions, changes, and reasoning

**Why I Did It This Way:**
- Comprehensive = anyone can take over
- Simple language = non-technical people can understand
- Examples = show, don't just tell
- Organized = easy to find information

---

## 📊 CURRENT STATUS {#current-status}

### System Health: ✅ EXCELLENT

**Last 4 Automatic Runs:**
- ✅ December 8, 2025 - Success
- ✅ December 1, 2025 - Success
- ✅ November 24, 2025 - Success
- ✅ November 17, 2025 - Success

**Success Rate:** 100% (4 out of 4)

---

### Current Configuration:

**Schedule:**
- Every Sunday at 8:00 PM EST
- Actual: 9:00-11:00 PM EST (GitHub delay is normal)
- Frequency: Once per week

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

**Data Sources:**
- 30+ Reddit URLs across 8 brands
- ~30-50 posts per week
- 7-day rolling window (previous Monday-Sunday)

---

### What's Working:

✅ **Automation:**
- Runs automatically every Sunday
- No manual intervention needed
- 100% cloud-based (no laptop required)

✅ **Data Collection:**
- Reddit API working
- Spam filtering effective
- Consistent post volume

✅ **Sentiment Analysis:**
- Dual-algorithm approach
- Context-aware detection
- Handles sarcasm and comparisons

✅ **Reports:**
- Charts generating correctly
- HTML reports formatting properly
- All links working

✅ **Email Delivery:**
- All 19 recipients receiving emails
- PDF attachments working
- No spam folder issues

✅ **Website:**
- Updates automatically
- Mobile-friendly
- Fast loading

---

## 👀 HOW TO MONITOR IT {#how-to-monitor}

### Weekly Check (5 minutes every Monday)

**Step 1: Check Your Email (1 minute)**
- Look for: "Weekly Reddit Competitor Sentiment Report — [dates]"
- From: kunsang.tsering@hellofresh.com (or configured email)
- Has PDF attachment: `step1_chart.pdf`

✅ **If received** → Everything is working!  
❌ **If not received** → Check spam folder, then see troubleshooting

---

**Step 2: Check GitHub Actions (2 minutes)**

1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Look for latest run (should be from Sunday evening)
3. Check for green checkmark ✅

✅ **If green** → Automation ran successfully  
❌ **If red** → Click on it to see error, then see troubleshooting

---

**Step 3: Check Website (1 minute)**

1. Go to: https://ktsering2025.github.io/reddit-competitor-sentiment/
2. Verify date is current week
3. Check chart loads correctly

✅ **If updated** → Website is working  
❌ **If old data** → Hard refresh (Cmd+Shift+R), then see troubleshooting

---

**Step 4: Verify All Recipients (1 minute)**

Ask a few people if they received the email:
- Did Brian get it?
- Did Assaf get it?
- Did Adam get it?

✅ **If yes** → Email delivery working  
❌ **If no** → Check their spam folder

---

### Monthly Health Check (15 minutes once a month)

**First Monday of Each Month:**

1. **Review Success Rate**
   - Check last 4 weeks of GitHub Actions
   - Should be 4/4 successful
   - If any failures, investigate why

2. **Verify Data Quality**
   - Open latest report
   - Check post counts (should be 20-50 per week)
   - Spot-check a few Reddit links (do they work?)
   - Verify sentiment makes sense

3. **Check API Health**
   - Reddit API: Any quota issues?
   - Gmail: Any sending limits hit?
   - GitHub Actions: Within free tier?

4. **Update Documentation**
   - Any new issues discovered?
   - Any changes to process?
   - Update relevant docs

---

## ✏️ HOW TO MAKE CHANGES {#how-to-make-changes}

### Common Changes You Might Need:

---

### 1. Add/Remove Email Recipients

**What:** Change who receives weekly reports

**How:**

**Step 1:** Update GitHub Secret
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions
2. Find: `EMAIL_RECIPIENTS`
3. Click edit (✏️)
4. Add/remove emails (comma-separated, no spaces)
5. Click "Update secret"

**Step 2:** Update Code (Optional but recommended)
1. Open `config.py`
2. Find line with `EMAIL_RECIPIENTS`
3. Add/remove email from the default list
4. Commit and push to GitHub

**Example:**
```python
# Before
EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS', 'person1@email.com,person2@email.com')

# After (added person3)
EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS', 'person1@email.com,person2@email.com,person3@email.com')
```

**Test:**
1. Go to GitHub Actions
2. Click "Run workflow"
3. Verify new person received email

---

### 2. Change Schedule (Different Day/Time)

**What:** Run on different day or time

**How:**

1. Open `.github/workflows/weekly-automation.yml`
2. Find the `cron:` line
3. Change the schedule

**Examples:**

```yaml
# Every Sunday 8 PM EST (current)
cron: '0 1 * * 1'  # Monday 1 AM UTC = Sunday 8 PM EST

# Every Friday 5 PM EST
cron: '0 22 * * 5'  # Friday 10 PM UTC = Friday 5 PM EST

# Every Day at 9 AM EST
cron: '0 14 * * *'  # Every day 2 PM UTC = 9 AM EST

# Twice a week (Tuesday and Friday 8 PM EST)
- cron: '0 1 * * 3'  # Wednesday 1 AM UTC = Tuesday 8 PM EST
- cron: '0 1 * * 6'  # Saturday 1 AM UTC = Friday 8 PM EST
```

**Cron Format:**
```
* * * * *
│ │ │ │ │
│ │ │ │ └─ Day of week (0-6, Sunday=0)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23, in UTC)
└───────── Minute (0-59)
```

**Important:** Times are in UTC! EST = UTC-5

---

### 3. Add More Brands to Track

**What:** Track additional meal kit brands

**How:**

1. Open `config.py`
2. Add brand to `WEEKLY_LINKS` dictionary:

```python
WEEKLY_LINKS = {
    # ... existing brands ...
    "New Brand Name": [
        "https://www.reddit.com/search/?q=newbrand&type=posts&t=week",
        "https://www.reddit.com/r/mealkits/search/?q=newbrand&type=posts&t=week&restrict_sr=1"
    ]
}
```

3. Add brand to `ALL_COMPETITORS` list:

```python
ALL_COMPETITORS = ["HelloFresh", "Factor75", ..., "New Brand Name"]
```

4. Commit and push
5. Next Sunday, new brand will be included

---

### 4. Change Email Content/Format

**What:** Modify email template

**How:**

1. Open `send_to_gmail_smtp.py`
2. Find function `create_email_html()`
3. Modify the HTML template
4. Test by running manually:
   ```bash
   python3 send_to_gmail_smtp.py your_email@hellofresh.com
   ```

**Common Changes:**
- Add/remove sections
- Change colors
- Modify text
- Add more brands to email

---

### 5. Manually Trigger Report (Off-Schedule)

**What:** Send report outside of Sunday schedule

**How:**

**Option 1: GitHub Actions (Easiest)**
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Click "Weekly Reddit Sentiment Analysis"
3. Click "Run workflow" (green button)
4. Click "Run workflow" again
5. Wait 3 minutes
6. Check email!

**Option 2: Local Terminal**
```bash
cd /path/to/reddit-competitor-sentiment
export $(cat .env | grep -v '^#' | xargs)
python3 complete_automation.py
```

---

## 🆘 TROUBLESHOOTING GUIDE {#troubleshooting}

### Issue 1: "Didn't Receive Email on Sunday"

**Possible Causes:**
- Automation didn't run
- Email went to spam
- Gmail credentials expired

**How to Fix:**

**Step 1:** Check if automation ran
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Look for run from Sunday evening
3. Check if it has green checkmark ✅

**If NO run found:**
- Manually trigger workflow (see "How to Make Changes" section)

**If run FAILED (red ❌):**
- Click on the failed run
- Read error message
- See specific error solutions below

**If run SUCCEEDED (green ✅):**
- Check spam folder for email
- Search for "Reddit Competitor Sentiment"
- Mark as "Not Spam" if found

**Step 2:** Check Gmail credentials
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions
2. Verify `GMAIL_EMAIL` and `GMAIL_APP_PASSWORD` exist
3. If expired, regenerate at: https://myaccount.google.com/apppasswords

---

### Issue 2: "Report Shows 0 Posts"

**Possible Causes:**
- Reddit API credentials expired
- Reddit API rate limit hit
- Reddit is down (rare)

**How to Fix:**

**Step 1:** Check Reddit API credentials
1. Go to: https://www.reddit.com/prefs/apps
2. Verify your app still exists
3. If not, create new app and update secrets

**Step 2:** Check GitHub Actions logs
1. Click on the failed run
2. Look for "Reddit API" errors
3. Look for "401 Unauthorized" errors

**Step 3:** Wait and retry
- Sometimes Reddit API has temporary issues
- Wait 1 hour
- Manually trigger workflow again

---

### Issue 3: "GitHub Actions Workflow Failed"

**Possible Causes:**
- Missing GitHub Secrets
- Code error
- GitHub Actions quota exceeded (unlikely)

**How to Fix:**

**Step 1:** Check the error logs
1. Click on failed run
2. Click "run-automation" job
3. Read error message

**Common Errors:**

**"Secret not found"**
- Go to: Settings → Secrets → Actions
- Verify all 6 secrets exist:
  - REDDIT_CLIENT_ID
  - REDDIT_CLIENT_SECRET
  - REDDIT_USER_AGENT
  - GMAIL_EMAIL
  - GMAIL_APP_PASSWORD
  - EMAIL_RECIPIENTS

**"pip install failed"**
- Usually temporary
- Manually trigger again

**"git push failed"**
- Check repository permissions
- Verify GitHub token has write access

---

### Issue 4: "Website Not Updating"

**Possible Causes:**
- GitHub Pages not enabled
- Git push failed
- Browser cache issue

**How to Fix:**

**Step 1:** Verify GitHub Pages enabled
1. Go to: Settings → Pages
2. Source should be: "Deploy from a branch"
3. Branch should be: "main" / "root"

**Step 2:** Check recent commits
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/commits/main
2. Should see recent "🤖 Automated weekly update" commit
3. If not, automation didn't push changes

**Step 3:** Hard refresh browser
- Mac: Cmd + Shift + R
- Windows: Ctrl + F5
- This clears cache

**Step 4:** Wait 3-5 minutes
- GitHub Pages takes time to deploy
- Check again after waiting

---

### Issue 5: "Sentiment Analysis Seems Wrong"

**Possible Causes:**
- Sarcasm not detected
- Context misunderstood
- Algorithm limitations

**How to Fix:**

**Step 1:** Check the specific post
1. Open the report
2. Find the post in question
3. Click the Reddit link
4. Read the full post

**Step 2:** Understand limitations
- Sarcasm is hard for algorithms
- "Sweet broccoli" might be detected as positive (but is sarcastic)
- Comparisons can be tricky ("switched FROM X TO Y")

**Step 3:** Improve algorithm (advanced)
1. Open `accurate_scraper.py`
2. Find `analyze_sentiment()` function
3. Add keyword overrides for specific cases
4. Test with sample posts

**Example:**
```python
# Add to keyword overrides
if 'too much' in text.lower():
    return 'negative'  # "too much broccoli" = negative
```

---

## 🔧 TECHNICAL DETAILS (FOR DEVELOPERS) {#technical-details}

### Tech Stack:

**Languages:**
- Python 3.10+
- HTML/CSS
- YAML (GitHub Actions)
- Markdown (documentation)

**Python Libraries:**
```
praw==7.7.1              # Reddit API wrapper
vaderSentiment==3.3.2    # Sentiment analysis
textblob==0.17.1         # Sentiment analysis
matplotlib==3.8.0        # Chart generation
python-dotenv==1.0.0     # Environment variables
beautifulsoup4==4.12.2   # HTML parsing
requests==2.31.0         # HTTP requests
```

**Infrastructure:**
- GitHub Actions (automation)
- GitHub Pages (website hosting)
- Gmail SMTP (email delivery)
- Reddit API (data source)

---

### File Structure:

```
reddit-competitor-sentiment/
├── .github/workflows/
│   └── weekly-automation.yml    # GitHub Actions workflow
│
├── reports/
│   ├── working_reddit_data.json # Current week's data
│   ├── step1_chart.png          # Bar chart (PNG)
│   ├── step1_chart.pdf          # Bar chart (PDF)
│   ├── step2_ACTIONABLE_analysis_LATEST.html
│   ├── step3_competitor_analysis_LATEST.html
│   ├── archive/                 # Historical data
│   │   └── YYYY-MM-DD/
│   └── raw/                     # Raw scraped data
│
├── conversation_history/        # AI chat logs
│   ├── README.md
│   └── YYYY-MM-DD_session.md
│
├── accurate_scraper.py          # Reddit scraping + sentiment
├── step1_chart.py               # Chart generator
├── step2_ACTIONABLE_analysis.py # HelloFresh/Factor deep dive
├── step3_competitor_analysis.py # All competitors
├── send_to_gmail_smtp.py        # Email sender
├── complete_automation.py       # Main orchestrator
├── update_homepage.py           # Website updater
├── config.py                    # Configuration
├── index.html                   # Website homepage
├── requirements.txt             # Python dependencies
├── .env                         # Local environment variables (not in git)
│
└── [30+ documentation files]    # Guides, handoff docs, etc.
```

---

### Key Scripts:

**1. `accurate_scraper.py`**
- Connects to Reddit API via PRAW
- Searches 30+ URLs across 8 brands
- Filters spam and irrelevant posts
- Analyzes sentiment using VADER + TextBlob
- Outputs: `reports/working_reddit_data.json`

**2. `step1_chart.py`**
- Reads `working_reddit_data.json`
- Creates bar chart with matplotlib
- Outputs: `step1_chart.png` + `step1_chart.pdf`

**3. `step2_ACTIONABLE_analysis.py`**
- Deep dive on HelloFresh & Factor
- Ranks posts by engagement score
- Generates HTML report with tables
- Outputs: `step2_ACTIONABLE_analysis_LATEST.html`

**4. `step3_competitor_analysis.py`**
- Analyzes all 8 competitors
- Comparison tables and insights
- Outputs: `step3_competitor_analysis_LATEST.html`

**5. `send_to_gmail_smtp.py`**
- Sends HTML emails via Gmail SMTP
- Attaches PDF chart
- Includes top posts with links
- Sends to 19 recipients

**6. `complete_automation.py`**
- Orchestrates all scripts in sequence
- Validates data quality
- Archives historical data
- Commits and pushes to GitHub

---

### GitHub Actions Workflow:

**Triggers:**
- Schedule: Every Monday 1 AM UTC (Sunday 8 PM EST)
- Manual: "Run workflow" button

**Steps:**
1. Checkout repository
2. Set up Python 3.10
3. Install dependencies
4. Run `complete_automation.py`
5. Run `send_to_gmail_smtp.py`
6. Commit and push changes

**Secrets Required:**
- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET
- REDDIT_USER_AGENT
- GMAIL_EMAIL
- GMAIL_APP_PASSWORD
- EMAIL_RECIPIENTS

---

### Sentiment Analysis Logic:

**Dual-Algorithm Approach:**

1. **VADER (Valence Aware Dictionary and sEntiment Reasoner)**
   - Specialized for social media text
   - Understands slang, emojis, capitalization
   - Returns compound score: -1 (negative) to +1 (positive)

2. **TextBlob**
   - General-purpose sentiment analysis
   - Returns polarity: -1 (negative) to +1 (positive)

**Combined Logic:**
```python
vader_score = analyzer.polarity_scores(text)['compound']
textblob_score = TextBlob(text).sentiment.polarity

# Both must agree for positive/negative
if vader_score >= 0.05 and textblob_score >= 0.1:
    return 'positive'
elif vader_score <= -0.05 and textblob_score <= -0.1:
    return 'negative'
else:
    return 'neutral'
```

**Context-Aware Enhancements:**
- Questions → neutral ("Which is better, X or Y?")
- Comparisons → analyze per brand ("Switched FROM X TO Y")
- Strong keywords override ("terrible", "avoid", "love", "amazing")

---

### Data Flow:

```
Reddit API
    ↓
accurate_scraper.py
    ↓
working_reddit_data.json
    ↓
┌───────────┬──────────────┬──────────────┐
│           │              │              │
step1_chart step2_analysis step3_analysis
    ↓            ↓              ↓
PNG + PDF    HTML report    HTML report
    ↓            ↓              ↓
    └────────────┴──────────────┘
              ↓
        update_homepage.py
              ↓
          index.html
              ↓
        GitHub Pages
              ↓
    Live Website Updated
```

---

## 📞 CONTACT & SUPPORT {#contact-support}

### Primary Contact:

**Kunsang Tsering**
- Email: kunsang.tsering@hellofresh.com
- Role: Original developer
- Knows: Everything about this system

---

### For Technical Issues:

**ML/AI Team at HelloFresh**
- For: Algorithm improvements, data science questions
- How: See `HOW_TO_ASK_FOR_HELP.md`

**GitHub Support**
- For: GitHub Actions issues, repository problems
- URL: https://support.github.com

**Reddit API Support**
- For: Reddit API issues, rate limits
- URL: https://www.reddit.com/r/redditdev

---

### Useful Links:

**Project Resources:**
- GitHub Repo: https://github.com/ktsering2025/reddit-competitor-sentiment
- Live Website: https://ktsering2025.github.io/reddit-competitor-sentiment/
- GitHub Actions: https://github.com/ktsering2025/reddit-competitor-sentiment/actions

**External Services:**
- Reddit Apps: https://www.reddit.com/prefs/apps
- Gmail App Passwords: https://myaccount.google.com/apppasswords
- GitHub Secrets: https://github.com/ktsering2025/reddit-competitor-sentiment/settings/secrets/actions

---

### Documentation Index:

**For Users:**
- `README.md` - Project overview
- `PROJECT_SUMMARY.md` - Business summary
- `WEEKLY_AUTOMATION_GUARANTEE.md` - Ensuring reliability

**For New Owners:**
- `MANAGER_QUICK_START.md` - 10-minute guide
- `HANDOFF_GUIDE.md` - Complete transfer process
- `HANDOFF_CHECKLIST.md` - Step-by-step tasks

**For Developers:**
- `TECHNICAL_DOCUMENTATION.md` - Code details
- `AUTOMATION_EXPLAINED.md` - How it works
- `AUTOMATION_ANALYSIS_REPORT.md` - System analysis

**For Help:**
- `HOW_TO_ASK_FOR_HELP.md` - Reaching out to experts
- `TROUBLESHOOTING.md` - Common issues
- This document - Complete guide

---

## ✅ FINAL CHECKLIST

### For New Project Owner:

**Week 1: Understanding**
- [ ] Read this entire document (30 minutes)
- [ ] Read `MANAGER_QUICK_START.md` (10 minutes)
- [ ] Watch next Sunday's automation run
- [ ] Verify you received the email

**Week 2: Access**
- [ ] Get GitHub repository access (owner or admin)
- [ ] Verify you can view GitHub Secrets
- [ ] Verify you can trigger workflows manually
- [ ] Test manual trigger (send yourself an email)

**Week 3: Monitoring**
- [ ] Set up weekly Monday morning check (5 minutes)
- [ ] Bookmark important links
- [ ] Add calendar reminder for monthly health check
- [ ] Understand troubleshooting guide

**Week 4: Confidence**
- [ ] Monitor next Sunday's run independently
- [ ] Make a small change (add test email recipient)
- [ ] Successfully troubleshoot a minor issue
- [ ] Feel comfortable owning the project

---

## 🎉 CONCLUSION

This project is **production-ready**, **fully automated**, and **well-documented**.

**What makes it successful:**
- ✅ Runs automatically without manual work
- ✅ 100% reliable (cloud-based infrastructure)
- ✅ Provides real business value (competitive intelligence)
- ✅ Easy to maintain (5 minutes per week)
- ✅ Well documented (anyone can take over)
- ✅ Scalable (easy to add brands or recipients)

**Your role as new owner:**
- Monitor it weekly (5 minutes)
- Troubleshoot if needed (rare)
- Make changes as requested (easy)
- Keep documentation updated

**You got this!** 💪

---

**Document Version:** 1.0  
**Created:** December 8, 2025  
**Last Updated:** December 8, 2025  
**Author:** Kunsang Tsering  
**Status:** Complete & Ready for Handoff
