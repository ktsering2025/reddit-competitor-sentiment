# 🚀 My Journey Building Reddit Competitor Sentiment Analysis

**By:** Kunsang Tsering  
**For:** HelloFresh  
**Timeline:** October 27 - December 12, 2025

---

## 📖 TABLE OF CONTENTS

1. [What I Built](#what-i-built)
2. [The Tools I Used (What, How, Why)](#the-tools-i-used)
3. [Problems I Ran Into & How I Fixed Them](#problems-i-ran-into)
4. [How the Automation Actually Works](#how-the-automation-works)
5. [How I Know It's Working](#how-i-know-its-working)
6. [What I Would Scale Next Time](#what-i-would-scale-next-time)

---

## 1. WHAT I BUILT

I built a fully automated system that scrapes Reddit every Sunday, analyzes sentiment for 8 meal kit brands, and emails 19 people at HelloFresh with insights.

**The Problem I Was Solving:**
- Manual Reddit searching took hours every week
- Inconsistent analysis (different people = different opinions)
- No historical tracking
- No systematic way to track competitors

**My Solution:**
- Automated scraping (no manual work)
- Consistent AI-based sentiment analysis
- Historical data archive
- Weekly email reports

---

## 2. THE TOOLS I USED (WHAT, HOW, WHY)

### **Tool 1: Python 3.10**

**WHAT:** Programming language for all my scripts  
**HOW:** Wrote 6 core Python scripts (scraper, chart generator, email sender, etc.)  
**WHY:** 
- Easy to learn and maintain
- Great libraries for Reddit API, sentiment analysis, and charts
- Works on any platform (Mac, Linux, Windows)
- Free and open-source

---

### **Tool 2: PRAW (Python Reddit API Wrapper)**

**WHAT:** Library to connect to Reddit's API  
**HOW:** 
```python
import praw

# Initialize Reddit connection
self.reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Search for posts
for submission in self.reddit.subreddit('mealkits').search('hellofresh', time_filter='week'):
    # Process each post
```

**WHY:**
- Official Reddit API wrapper (reliable)
- Handles authentication automatically
- Rate limiting built-in (won't get banned)
- Easy to search by brand, subreddit, and time

**Alternative I Considered:** Web scraping with BeautifulSoup  
**Why I Chose PRAW:** More reliable, faster, and won't break if Reddit changes their HTML

---

### **Tool 3: VADER Sentiment Analysis**

**WHAT:** AI algorithm specialized for social media text  
**HOW:**
```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores("I love HelloFresh!")
# Returns: {'neg': 0.0, 'neu': 0.323, 'pos': 0.677, 'compound': 0.6369}
```

**WHY:**
- Understands social media language (slang, emojis, capitalization)
- "I LOVE THIS" = more positive than "I love this"
- Handles negations: "not good" = negative
- Free and fast

**Alternative I Considered:** TextBlob only  
**Why I Chose VADER:** Better for social media, understands intensity

---

### **Tool 4: TextBlob Sentiment Analysis**

**WHAT:** General-purpose sentiment analysis library  
**HOW:**
```python
from textblob import TextBlob

blob = TextBlob("HelloFresh is amazing!")
polarity = blob.sentiment.polarity  # Returns: 0.6 (positive)
```

**WHY:**
- Good for general text (not just social media)
- Provides polarity (-1 to +1) and subjectivity (0 to 1)
- Complements VADER for accuracy

**My Dual-Algorithm Approach:**
- Both VADER and TextBlob must agree for positive/negative
- If they disagree → neutral
- This reduces false positives/negatives

```python
vader_score = analyzer.polarity_scores(text)['compound']
textblob_score = TextBlob(text).sentiment.polarity

# Both must agree
if vader_score >= 0.05 and textblob_score >= 0.1:
    return 'positive'
elif vader_score <= -0.05 and textblob_score <= -0.1:
    return 'negative'
else:
    return 'neutral'
```

---

### **Tool 5: Matplotlib**

**WHAT:** Python library for creating charts  
**HOW:**
```python
import matplotlib.pyplot as plt

# Create bar chart
fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(brands, positive_counts, color='green', label='Positive')
ax.bar(brands, negative_counts, color='red', bottom=positive_counts, label='Negative')
plt.savefig('reports/step1_chart.png')
plt.savefig('reports/step1_chart.pdf')
```

**WHY:**
- Creates professional-looking charts
- Exports to PNG (for website) and PDF (for email)
- Customizable colors, labels, legends
- Free and widely used

**Alternative I Considered:** Plotly (interactive charts)  
**Why I Chose Matplotlib:** Simpler, faster, and static charts are fine for email

---

### **Tool 6: GitHub Actions**

**WHAT:** Cloud automation service by GitHub  
**HOW:** Created `.github/workflows/weekly-automation.yml` file:
```yaml
on:
  schedule:
    - cron: '0 1 * * 1'  # Every Monday 1 AM UTC = Sunday 8 PM EST
  workflow_dispatch:  # Also allow manual trigger

jobs:
  run-automation:
    runs-on: ubuntu-latest  # Linux server in GitHub's cloud
    steps:
      - name: Checkout repository
      - name: Set up Python
      - name: Install dependencies
      - name: Run automation
      - name: Send emails
      - name: Commit and push
```

**WHY:**
- **Free:** GitHub Actions is free for public repos (2,000 minutes/month)
- **Cloud-based:** Runs on GitHub's servers (not my laptop)
- **Reliable:** 99.9% uptime, runs even if my laptop is off
- **Integrated:** Already using GitHub for code, so no extra setup

**Alternative I Considered:** 
- AWS Lambda (costs money)
- Heroku Scheduler (costs money)
- Local cron job (requires laptop to be on)

**Why I Chose GitHub Actions:** Free, reliable, and already using GitHub

---

### **Tool 7: Gmail SMTP**

**WHAT:** Email sending protocol  
**HOW:**
```python
import smtplib
from email.mime.multipart import MIMEMultipart

# Connect to Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Encrypt connection
server.login(gmail_email, gmail_app_password)

# Send email
server.send_message(msg)
server.quit()
```

**WHY:**
- **Free:** Gmail allows 500 emails/day (I only send 19/week)
- **Reliable:** Gmail's infrastructure is rock-solid
- **Universal:** Works on any platform (Mac, Linux, Windows)
- **No server needed:** Uses Gmail's servers

**Alternative I Considered:**
- SendGrid (costs money after 100 emails/day)
- Mailgun (costs money)
- Mac Mail.app (only works on Mac)

**Why I Chose Gmail SMTP:** Free, reliable, and works everywhere

---

### **Tool 8: GitHub Pages**

**WHAT:** Free website hosting by GitHub  
**HOW:** 
1. Created `index.html` file
2. Enabled GitHub Pages in repo settings
3. Website automatically deploys when I push to GitHub

**WHY:**
- **Free:** No hosting costs
- **Fast:** GitHub's CDN (content delivery network)
- **Automatic:** Updates when I push to GitHub
- **Custom domain:** Can use custom domain if needed

**Alternative I Considered:**
- AWS S3 + CloudFront (costs money)
- Netlify (free but unnecessary)
- Heroku (costs money)

**Why I Chose GitHub Pages:** Free, automatic, and already using GitHub

---

### **Tool 9: GitHub Secrets**

**WHAT:** Secure storage for credentials  
**HOW:** 
1. Go to repo Settings → Secrets → Actions
2. Add secrets (REDDIT_CLIENT_ID, GMAIL_APP_PASSWORD, etc.)
3. Reference in workflow: `${{ secrets.REDDIT_CLIENT_ID }}`

**WHY:**
- **Secure:** Credentials never appear in code or logs
- **Encrypted:** GitHub encrypts secrets at rest
- **Easy:** No need to manage .env files in cloud

**Alternative I Considered:**
- .env file in repo (INSECURE - credentials visible)
- AWS Secrets Manager (costs money)

**Why I Chose GitHub Secrets:** Free, secure, and integrated with GitHub Actions

---

### **Tool 10: Git & GitHub**

**WHAT:** Version control and code hosting  
**HOW:**
```bash
# Save changes
git add .
git commit -m "Add new feature"
git push origin main

# View history
git log --oneline
```

**WHY:**
- **Version control:** Track every change I make
- **Backup:** Code is safe in the cloud
- **Collaboration:** Others can see my code
- **History:** Can revert to any previous version

**Alternative I Considered:** 
- No version control (RISKY - lose all work if laptop dies)
- GitLab (similar to GitHub)

**Why I Chose GitHub:** Most popular, free, and has GitHub Actions

---

## 3. PROBLEMS I RAN INTO & HOW I FIXED THEM

### **Problem 1: Email Spam (November 16, 2025)**

**WHAT HAPPENED:**
I set up a local cron job on my Mac to run the automation every Sunday at 8 PM. But I started receiving 4+ emails in 2 hours instead of 1 email per week.

**WHY IT HAPPENED:**
- I had multiple cron jobs running (I forgot I set up multiple)
- Each cron job triggered the automation
- The automation sent emails every time it ran
- Result: Spam!

**HOW I DISCOVERED IT:**
```bash
# Checked my cron jobs
crontab -l

# Output showed multiple entries:
0 20 * * 0 cd /path/to/project && python3 complete_automation.py
0 20 * * 0 cd /path/to/project && python3 complete_automation.py
0 20 * * 0 cd /path/to/project && python3 complete_automation.py
```

**HOW I FIXED IT:**
```bash
# Removed ALL local cron jobs
crontab -r

# Verified they were gone
crontab -l
# Output: "crontab: no crontab for kunsang.tsering"
```

**WHAT I LEARNED:**
- Local cron jobs are hard to manage (easy to forget what's running)
- GitHub Actions is better (one place to see all automation)
- Always check what's running before adding more automation

**WHY THIS WAS THE RIGHT FIX:**
- GitHub Actions already had the schedule set up
- No need for local cron jobs
- GitHub Actions runs in the cloud (more reliable)
- One source of truth (the workflow file)

---

### **Problem 2: Mac-Specific Email Code (December 2, 2025)**

**WHAT HAPPENED:**
The automation ran successfully on GitHub Actions (green checkmark ✅), but no one received emails. I checked the logs and saw:
```
[ERROR] Failed to send email: [Errno 2] No such file or directory: 'osascript'
```

**WHY IT HAPPENED:**
I had written the email script on my Mac, and I used `osascript` (a Mac-specific command) to open Mail.app and send emails. This worked on my Mac, but GitHub Actions runs on Linux (Ubuntu), which doesn't have `osascript`.

**THE BAD CODE:**
```python
def send_via_mailto(recipient_email):
    # This only works on Mac!
    applescript = f'''
    tell application "Mail"
        set newMessage to make new outgoing message with properties {{subject:"Report"}}
        tell newMessage
            make new to recipient with properties {{address:"{recipient_email}"}}
            send
        end tell
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript])  # osascript doesn't exist on Linux!

def main():
    send_via_mailto(recipient)  # This was being called
```

**HOW I DISCOVERED IT:**
1. Checked GitHub Actions logs
2. Saw the error: `No such file or directory: 'osascript'`
3. Realized `osascript` is Mac-only
4. Found that I had TWO `main()` functions in the file:
   - First `main()` used `osascript` (Mac-only)
   - Second `main()` used SMTP (works everywhere)
5. Python was calling the FIRST `main()` function

**HOW I FIXED IT:**
```python
# Removed the entire send_via_mailto function
# Removed the first main() function
# Kept only the SMTP-based code

def send_email_smtp(recipients):
    # This works on any platform!
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_email, gmail_password)
    server.send_message(msg)
    server.quit()

def main():
    send_email_smtp(recipients)  # Only SMTP now

if __name__ == '__main__':
    main()
```

**WHAT I LEARNED:**
- Always test code on the platform where it will run
- Avoid platform-specific commands (osascript, AppleScript, etc.)
- SMTP is universal (works on Mac, Linux, Windows)
- Read error logs carefully (they tell you exactly what's wrong)

**WHY THIS WAS THE RIGHT FIX:**
- SMTP works on any platform
- No dependencies on Mac-specific tools
- More reliable (Gmail's servers, not my Mail.app)
- Easier to debug (standard protocol)

---

### **Problem 3: GitHub Actions Timing Delay**

**WHAT HAPPENED:**
I set the cron schedule to run at Monday 1:00 AM UTC (Sunday 8:00 PM EST), but emails arrived at 9:00-11:00 PM EST instead of 8:00 PM.

**WHY IT HAPPENED:**
GitHub Actions cron is "best effort" - it's not guaranteed to run at the exact time. GitHub says:
> "Scheduled workflows run on the next available runner. There may be a delay of up to 3 hours."

**HOW I DISCOVERED IT:**
1. Checked GitHub Actions logs
2. Saw runs starting at 2:00-4:00 AM UTC (9:00-11:00 PM EST)
3. Researched GitHub Actions documentation
4. Found the "best effort" disclaimer

**HOW I "FIXED" IT:**
I didn't fix it - I accepted it as a limitation of GitHub Actions.

**WHAT I LEARNED:**
- GitHub Actions cron is not real-time
- 1-3 hour delay is normal and acceptable
- For exact timing, would need a dedicated server (costs money)
- For weekly reports, 1-3 hour delay is fine

**WHY THIS WAS THE RIGHT "FIX":**
- Free service = acceptable trade-off
- Weekly reports don't need exact timing
- Still reliable (runs every week)
- Alternative (dedicated server) costs $5-20/month

---

## 4. HOW THE AUTOMATION ACTUALLY WORKS

### **The Complete Flow (Step-by-Step)**

**Every Sunday at 8:00 PM EST:**

```
1. GitHub Actions Triggers
   ├─ Cron schedule: '0 1 * * 1' (Monday 1 AM UTC = Sunday 8 PM EST)
   ├─ GitHub's servers wake up
   └─ Starts a fresh Ubuntu Linux machine

2. Setup Environment
   ├─ Checks out my code from GitHub
   ├─ Installs Python 3.10
   ├─ Installs all libraries (pip install -r requirements.txt)
   └─ Loads secrets (REDDIT_CLIENT_ID, GMAIL_APP_PASSWORD, etc.)

3. Run complete_automation.py
   ├─ Calls accurate_scraper.py
   │  ├─ Connects to Reddit API
   │  ├─ Searches 30+ URLs for 8 brands
   │  ├─ Filters spam and irrelevant posts
   │  ├─ Analyzes sentiment (VADER + TextBlob)
   │  └─ Saves to reports/working_reddit_data.json
   │
   ├─ Calls step1_chart.py
   │  ├─ Reads working_reddit_data.json
   │  ├─ Creates bar chart
   │  └─ Saves step1_chart.png + step1_chart.pdf
   │
   ├─ Calls step2_ACTIONABLE_analysis.py
   │  ├─ Reads working_reddit_data.json
   │  ├─ Filters for HelloFresh & Factor
   │  ├─ Ranks by engagement
   │  └─ Saves step2_ACTIONABLE_analysis_LATEST.html
   │
   ├─ Calls step3_competitor_analysis.py
   │  ├─ Reads working_reddit_data.json
   │  ├─ Analyzes all 8 competitors
   │  └─ Saves step3_competitor_analysis_LATEST.html
   │
   ├─ Calls update_homepage.py
   │  ├─ Reads working_reddit_data.json
   │  └─ Updates index.html
   │
   ├─ Archives data
   │  ├─ Creates reports/archive/YYYY-MM-DD/
   │  └─ Copies all reports to archive
   │
   └─ Commits to GitHub
      ├─ git add .
      ├─ git commit -m "🤖 Automated weekly update"
      └─ git push origin main

4. Run send_to_gmail_smtp.py
   ├─ Reads working_reddit_data.json
   ├─ Creates HTML email
   ├─ Attaches step1_chart.pdf
   ├─ Connects to Gmail SMTP
   └─ Sends to 19 recipients

5. GitHub Pages Deploys
   ├─ Detects new commit
   ├─ Rebuilds website
   └─ Live in 3 minutes

✅ DONE! (Total time: ~3 minutes)
```

---

### **Why It Works Without My Laptop**

**The Key Concept:** GitHub Actions runs on GitHub's servers, not my laptop.

**Here's the exact flow:**

1. **Cron Schedule Triggers:**
   - GitHub's servers check all workflows every minute
   - When it's Monday 1:00 AM UTC, GitHub sees my workflow
   - GitHub says: "Time to run this workflow!"

2. **GitHub Allocates a Runner:**
   - A "runner" is a virtual machine (VM) in GitHub's cloud
   - GitHub spins up a fresh Ubuntu Linux machine
   - This machine has nothing on it (clean slate)

3. **Workflow Executes:**
   - GitHub reads my workflow file (`.github/workflows/weekly-automation.yml`)
   - Follows each step in order
   - Each step runs on the Ubuntu machine (not my laptop)

4. **Secrets Are Injected:**
   - GitHub injects my secrets as environment variables
   - My code reads them: `os.getenv('REDDIT_CLIENT_ID')`
   - Secrets never appear in logs (GitHub redacts them)

5. **Code Runs:**
   - My Python scripts run on the Ubuntu machine
   - Scrapes Reddit, analyzes sentiment, creates charts
   - Sends emails via Gmail SMTP

6. **Results Are Committed:**
   - My code commits results to GitHub
   - GitHub saves the new commit
   - GitHub Pages detects the new commit and rebuilds the website

7. **Runner Is Destroyed:**
   - After the workflow finishes, GitHub destroys the runner
   - Nothing is saved on the runner (it's gone)
   - Next week, GitHub creates a fresh runner and repeats

**Why My Laptop Doesn't Matter:**
- GitHub Actions runs on GitHub's servers
- My laptop is not involved at all
- I could delete my laptop and it would still work
- I could be on vacation and it would still work

---

### **How GitHub Actions Knows When to Run**

**Cron Syntax:**
```yaml
cron: '0 1 * * 1'
       │ │ │ │ │
       │ │ │ │ └─ Day of week (0-6, Sunday=0, Monday=1)
       │ │ │ └─── Month (1-12)
       │ │ └───── Day of month (1-31)
       │ └─────── Hour (0-23, in UTC)
       └───────── Minute (0-59)
```

**My Schedule:**
- `0` = Minute 0 (on the hour)
- `1` = Hour 1 (1:00 AM)
- `*` = Every day of month
- `*` = Every month
- `1` = Monday (day 1 of week)

**Result:** Every Monday at 1:00 AM UTC

**Time Zone Conversion:**
- UTC = Coordinated Universal Time (no daylight saving)
- EST = UTC - 5 hours
- Monday 1:00 AM UTC = Sunday 8:00 PM EST

**Why I Use UTC:**
- GitHub Actions uses UTC (not EST)
- UTC doesn't have daylight saving time
- Consistent year-round

---

## 5. HOW I KNOW IT'S WORKING

### **Method 1: Check My Email**

**What I Do:**
- Every Monday morning, I check my email
- Look for: "Weekly Reddit Competitor Sentiment Report — [dates]"
- From: kunsang.tsering@hellofresh.com

**What I Check:**
- ✅ Email received (yes/no)
- ✅ PDF attachment present (step1_chart.pdf)
- ✅ Date range is correct (previous Monday-Sunday)
- ✅ Post counts look reasonable (20-50 posts)
- ✅ Top posts have Reddit links that work

**If Email Not Received:**
- Check spam folder
- Check GitHub Actions (see Method 2)

---

### **Method 2: Check GitHub Actions**

**What I Do:**
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Look for latest run (should be from Sunday evening)
3. Check for green checkmark ✅ or red X ❌

**What I Check:**
- ✅ **Green checkmark:** Automation ran successfully
- ❌ **Red X:** Automation failed (click to see error)
- 📅 **Date/time:** Should be Sunday evening (9-11 PM EST)
- ⏱️ **Duration:** Should be ~3 minutes

**Detailed View:**
- Click on the run to see detailed logs
- See each step (checkout, setup, run automation, send emails, commit)
- See output from each script
- See any errors or warnings

**Example Log:**
```
Run automation pipeline
  ✓ Scraping Reddit... (30 seconds)
  ✓ Found 42 posts
  ✓ Generating chart... (5 seconds)
  ✓ Creating reports... (10 seconds)
  ✓ Updating website... (5 seconds)
  ✓ Archiving data... (5 seconds)
  ✓ Committing to GitHub... (10 seconds)

Send weekly email report
  ✓ Sending to 19 recipients... (10 seconds)
  ✓ Email sent successfully
```

---

### **Method 3: Check the Website**

**What I Do:**
1. Go to: https://ktsering2025.github.io/reddit-competitor-sentiment/
2. Check the date at the top
3. Verify chart loads correctly

**What I Check:**
- ✅ Date is current week (not old data)
- ✅ Chart loads (not broken image)
- ✅ Links to reports work
- ✅ Post counts match email

**If Website Not Updated:**
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+F5 (Windows)
- Wait 3-5 minutes (GitHub Pages takes time to deploy)
- Check GitHub Actions to see if commit succeeded

---

### **Method 4: Check GitHub Commits**

**What I Do:**
1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/commits/main
2. Look for recent "🤖 Automated weekly update" commit
3. Check the date

**What I Check:**
- ✅ Recent commit from Sunday evening
- ✅ Commit message: "🤖 Automated weekly update - YYYY-MM-DD"
- ✅ Files changed: reports/, index.html, etc.

**If No Recent Commit:**
- Check GitHub Actions (automation may have failed)
- Check for errors in logs

---

### **Method 5: Ask Recipients**

**What I Do:**
- Ask a few recipients if they got the email
- "Hey Brian, did you get the Reddit report this week?"

**What I Check:**
- ✅ Did they receive it? (yes/no)
- ✅ Did it go to spam? (check spam folder)
- ✅ Did the PDF attachment work? (can they open it)

---

### **My Weekly Monitoring Routine (5 minutes every Monday)**

```
Monday Morning:
├─ 1. Check my email (1 minute)
│  └─ Look for weekly report
│
├─ 2. Check GitHub Actions (2 minutes)
│  ├─ Green checkmark? ✅
│  └─ If red, click to see error
│
├─ 3. Check website (1 minute)
│  └─ Verify date is current week
│
└─ 4. Ask a recipient (1 minute)
   └─ "Did you get the report?"

✅ If all checks pass → Everything is working!
❌ If any check fails → Investigate and fix
```

---

## 6. WHAT I WOULD SCALE NEXT TIME

### **Improvement 1: Real-Time Alerts**

**WHAT:** Get notified immediately if automation fails

**HOW:**
- Add Slack webhook to GitHub Actions
- Send message to Slack channel if workflow fails
- Include error message and link to logs

**WHY:**
- Currently, I only know if it fails when I check Monday morning
- Real-time alerts = faster response time
- Could fix issues before anyone notices

**CODE:**
```yaml
- name: Notify on failure
  if: failure()
  run: |
    curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
      -H 'Content-Type: application/json' \
      -d '{"text":"❌ Reddit automation failed! Check logs: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"}'
```

---

### **Improvement 2: Database Storage**

**WHAT:** Store data in a database instead of JSON files

**HOW:**
- Use PostgreSQL or MongoDB
- Store each post as a row/document
- Query for historical trends

**WHY:**
- JSON files are hard to query
- Database = easier to analyze trends
- Can answer questions like: "How has HelloFresh sentiment changed over 6 months?"

**EXAMPLE:**
```sql
-- Get average sentiment by month
SELECT 
  DATE_TRUNC('month', created_at) AS month,
  AVG(sentiment_score) AS avg_sentiment
FROM posts
WHERE brand = 'HelloFresh'
GROUP BY month
ORDER BY month;
```

---

### **Improvement 3: More Brands**

**WHAT:** Track more competitors (currently 8)

**HOW:**
- Add more brands to `config.py`
- Add their Reddit search URLs
- Update chart to handle more brands

**WHY:**
- More comprehensive competitive intelligence
- See the full meal kit landscape
- Identify emerging competitors

**BRANDS TO ADD:**
- Gobble
- Dinnerly
- Purple Carrot
- Sunbasket
- Freshly

---

### **Improvement 4: Sentiment Breakdown by Topic**

**WHAT:** Categorize posts by topic (price, quality, delivery, etc.)

**HOW:**
- Use keyword matching or topic modeling
- Classify each post into categories
- Show sentiment by category

**WHY:**
- More actionable insights
- "HelloFresh has negative sentiment on price but positive on quality"
- Can target specific issues

**EXAMPLE:**
```python
topics = {
    'price': ['expensive', 'cheap', 'cost', 'price', 'worth'],
    'quality': ['fresh', 'quality', 'delicious', 'taste', 'spoiled'],
    'delivery': ['late', 'damaged', 'missing', 'arrived', 'box'],
    'variety': ['boring', 'repetitive', 'variety', 'options', 'same']
}

for post in posts:
    for topic, keywords in topics.items():
        if any(keyword in post['title'].lower() for keyword in keywords):
            post['topic'] = topic
```

---

### **Improvement 5: Interactive Dashboard**

**WHAT:** Replace static website with interactive dashboard

**HOW:**
- Use Plotly Dash or Streamlit
- Add filters (date range, brand, sentiment)
- Add drill-down (click on bar to see posts)

**WHY:**
- More engaging for users
- Can explore data themselves
- Answer their own questions

**EXAMPLE:**
```python
import plotly.express as px
import streamlit as st

# Streamlit dashboard
st.title("Reddit Competitor Sentiment")

# Date range filter
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Brand filter
brands = st.multiselect("Brands", ALL_COMPETITORS)

# Filter data
filtered_data = data[
    (data['date'] >= start_date) & 
    (data['date'] <= end_date) & 
    (data['brand'].isin(brands))
]

# Interactive chart
fig = px.bar(filtered_data, x='brand', y='count', color='sentiment')
st.plotly_chart(fig)
```

---

### **Improvement 6: Anomaly Detection**

**WHAT:** Automatically detect unusual sentiment spikes

**HOW:**
- Calculate baseline sentiment for each brand
- Alert if sentiment drops/rises significantly
- Use statistical methods (z-score, moving average)

**WHY:**
- Early warning system for brand crises
- Don't wait for weekly report to notice issues
- Proactive instead of reactive

**EXAMPLE:**
```python
import numpy as np

# Calculate baseline (last 4 weeks)
baseline = np.mean(last_4_weeks_sentiment)
std_dev = np.std(last_4_weeks_sentiment)

# Current week
current = current_week_sentiment

# Z-score
z_score = (current - baseline) / std_dev

# Alert if z-score > 2 (2 standard deviations)
if abs(z_score) > 2:
    send_alert(f"⚠️ Unusual sentiment for {brand}: {current} (baseline: {baseline})")
```

---

### **Improvement 7: Multi-Platform Tracking**

**WHAT:** Track sentiment on Twitter, Facebook, Instagram (not just Reddit)

**HOW:**
- Use Twitter API, Facebook Graph API
- Scrape Instagram comments
- Combine all sources

**WHY:**
- Reddit is just one platform
- More comprehensive view of brand sentiment
- Different demographics on different platforms

**CHALLENGES:**
- Twitter API costs money ($100/month)
- Facebook API has strict rate limits
- Instagram doesn't have public API (need to scrape)

---

### **Improvement 8: Automated Insights**

**WHAT:** AI-generated summary of key insights

**HOW:**
- Use GPT-4 or Claude to analyze posts
- Generate bullet points of key findings
- Include in email report

**WHY:**
- Saves time reading all posts
- Highlights most important insights
- More actionable

**EXAMPLE:**
```python
import openai

# Get top posts
top_posts = get_top_posts(posts, limit=10)

# Generate insights
prompt = f"Analyze these Reddit posts and provide 3 key insights:\n{top_posts}"
insights = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Add to email
email_body += f"<h2>Key Insights</h2><ul>{insights}</ul>"
```

---

### **Improvement 9: A/B Testing Tracking**

**WHAT:** Track sentiment before/after marketing campaigns

**HOW:**
- Tag campaigns with start/end dates
- Compare sentiment before vs after
- Calculate statistical significance

**WHY:**
- Measure campaign effectiveness
- Data-driven marketing decisions
- ROI calculation

**EXAMPLE:**
```python
# Campaign: "HelloFresh Holiday Sale" (Dec 1-15)
before = get_sentiment(brand='HelloFresh', start='Nov 15', end='Nov 30')
during = get_sentiment(brand='HelloFresh', start='Dec 1', end='Dec 15')
after = get_sentiment(brand='HelloFresh', start='Dec 16', end='Dec 31')

# Calculate change
change = after - before
print(f"Sentiment change: {change:+.2%}")
```

---

### **Improvement 10: Cost Optimization**

**WHAT:** Reduce API calls and processing time

**HOW:**
- Cache Reddit API responses (don't re-fetch same posts)
- Use incremental updates (only new posts)
- Optimize sentiment analysis (batch processing)

**WHY:**
- Faster execution (currently ~3 minutes, could be <1 minute)
- Lower API usage (stay within free tier)
- More scalable (can handle more brands)

**EXAMPLE:**
```python
# Cache posts in database
def get_posts_since_last_run():
    last_run_time = get_last_run_time()
    new_posts = scrape_reddit(since=last_run_time)
    
    # Only analyze new posts
    for post in new_posts:
        post['sentiment'] = analyze_sentiment(post['title'])
        save_to_database(post)
    
    return new_posts
```

---

## 🎯 SUMMARY

### **What I Built:**
A fully automated competitive intelligence system that tracks Reddit sentiment for 8 meal kit brands and emails 19 people every Sunday.

### **Tools I Used:**
- Python, PRAW, VADER, TextBlob, Matplotlib (core functionality)
- GitHub Actions, Gmail SMTP, GitHub Pages (automation & delivery)
- Git, GitHub Secrets (version control & security)

### **Problems I Solved:**
1. Email spam from multiple cron jobs → Removed local cron, use GitHub Actions only
2. Mac-specific email code → Removed osascript, use SMTP only
3. GitHub Actions timing delay → Accepted as normal (1-3 hour delay is fine)

### **How It Works:**
- GitHub Actions triggers every Sunday at 8 PM EST
- Runs on GitHub's cloud servers (not my laptop)
- Scrapes Reddit, analyzes sentiment, creates reports
- Sends emails via Gmail SMTP
- Updates website via GitHub Pages

### **How I Know It's Working:**
- Check email Monday morning
- Check GitHub Actions for green checkmark
- Check website for updated data
- Ask recipients if they received it

### **What I Would Scale:**
- Real-time alerts, database storage, more brands
- Sentiment by topic, interactive dashboard
- Anomaly detection, multi-platform tracking
- AI-generated insights, A/B testing, cost optimization

---

**Built with ❤️ for HelloFresh competitive intelligence team**

**Last Updated:** December 12, 2025  
**Status:** ✅ Production-Ready & Fully Documented
