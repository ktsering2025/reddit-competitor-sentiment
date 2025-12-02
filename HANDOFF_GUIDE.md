# 🔄 Project Handoff Guide - Reddit Competitor Sentiment

**For transferring ownership to your manager or another team member**

---

## 📋 Table of Contents

1. [Quick Overview](#quick-overview)
2. [Transfer GitHub Repository Ownership](#transfer-github-ownership)
3. [Grant Access to Secrets](#grant-access-to-secrets)
4. [How to Monitor the Automation](#how-to-monitor)
5. [How to Manually Trigger Reports](#manual-trigger)
6. [Troubleshooting Common Issues](#troubleshooting)
7. [Emergency Contacts](#emergency-contacts)
8. [Handoff Checklist](#handoff-checklist)

---

## 🎯 Quick Overview {#quick-overview}

**What This Project Does:**
- Automatically scrapes Reddit every Sunday at 8 PM EST
- Analyzes sentiment for 8 meal kit brands
- Emails weekly reports to 5 stakeholders
- Updates live dashboard with latest data

**Current Status:**
- ✅ Fully operational
- ✅ 100% success rate (last 5 weeks)
- ✅ No manual intervention needed
- ✅ Runs automatically via GitHub Actions

**Key Links:**
- **GitHub Repo:** https://github.com/ktsering2025/reddit-competitor-sentiment
- **Live Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/
- **GitHub Actions:** https://github.com/ktsering2025/reddit-competitor-sentiment/actions

---

## 🔐 Step 1: Transfer GitHub Repository Ownership {#transfer-github-ownership}

### Option A: Transfer Entire Repository (Recommended)

**If your manager has a GitHub account:**

1. **Go to repository settings:**
   ```
   https://github.com/ktsering2025/reddit-competitor-sentiment/settings
   ```

2. **Scroll to bottom → "Danger Zone"**

3. **Click "Transfer ownership"**

4. **Enter:**
   - New owner's GitHub username (e.g., `brian-leung-hf`)
   - Repository name: `reddit-competitor-sentiment`
   - Type the repository name to confirm

5. **Click "I understand, transfer this repository"**

6. **New owner receives email** → They accept transfer → Done! ✅

**Result:** They now own the repo and can manage everything.

---

### Option B: Add as Admin Collaborator (Alternative)

**If they don't want to transfer ownership:**

1. **Go to repository settings:**
   ```
   https://github.com/ktsering2025/reddit-competitor-sentiment/settings/access
   ```

2. **Click "Add people"**

3. **Enter their GitHub username** (e.g., `brian-leung-hf`)

4. **Set role to "Admin"** (gives full control)

5. **Click "Add [username] to this repository"**

**Result:** They have full admin access but you remain owner.

---

### Option C: Transfer to HelloFresh Organization

**If HelloFresh has a GitHub organization:**

1. **Contact GitHub admin** at HelloFresh

2. **Request to transfer repository** to organization

3. **Follow organization's process** for repository transfers

4. **Set your manager as admin** within organization

**Result:** Repository lives under HelloFresh organization.

---

## 🔑 Step 2: Grant Access to Secrets {#grant-access-to-secrets}

**Important:** GitHub Secrets are needed for automation to work.

### Current Secrets (6 total):

1. `REDDIT_CLIENT_ID` - Reddit API credentials
2. `REDDIT_CLIENT_SECRET` - Reddit API credentials
3. `REDDIT_USER_AGENT` - Reddit API credentials
4. `GMAIL_EMAIL` - Email sender address
5. `GMAIL_APP_PASSWORD` - Gmail app password
6. `EMAIL_RECIPIENTS` - Who receives reports

---

### How to Share Secrets with New Owner:

**Option 1: They View Secrets After Transfer (Automatic)**
- Once they own the repo, they can see/edit all secrets
- Go to: `Settings → Secrets and variables → Actions`
- They can update or regenerate as needed

**Option 2: Document Secrets Before Transfer (Backup)**

Create a secure document with all credentials:

```
REDDIT API CREDENTIALS:
- Client ID: [get from https://www.reddit.com/prefs/apps]
- Client Secret: [get from https://www.reddit.com/prefs/apps]
- User Agent: reddit-sentiment-bot/1.0

GMAIL CREDENTIALS:
- Email: kunsang.tsering@hellofresh.com (or new email)
- App Password: [get from https://myaccount.google.com/apppasswords]

EMAIL RECIPIENTS:
brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com,adam.kalikow@hellofresh.com,adam.park@factor75.com
```

**⚠️ IMPORTANT:** Share this via secure method (1Password, LastPass, encrypted doc)

---

### How to Regenerate Secrets (If Needed):

**Reddit API:**
1. Go to: https://www.reddit.com/prefs/apps
2. Find your app or create new one
3. Copy Client ID and Secret
4. Update in GitHub Secrets

**Gmail App Password:**
1. Go to: https://myaccount.google.com/apppasswords
2. Create new app password
3. Copy the 16-character password
4. Update in GitHub Secrets

---

## 👀 Step 3: How to Monitor the Automation {#how-to-monitor}

### Weekly Monitoring (5 minutes every Monday)

**What to check every Monday morning:**

1. **Check Email (1 minute)**
   - Did you receive Sunday's report?
   - Subject: "Weekly Reddit Competitor Sentiment Report — [dates]"
   - Has PDF attachment?
   - Links work?

2. **Check GitHub Actions (2 minutes)**
   ```
   https://github.com/ktsering2025/reddit-competitor-sentiment/actions
   ```
   - Look for latest run (should be Sunday evening)
   - Green checkmark ✅ = Success
   - Red X ❌ = Failed (see troubleshooting)

3. **Check Live Dashboard (1 minute)**
   ```
   https://ktsering2025.github.io/reddit-competitor-sentiment/
   ```
   - Shows latest data?
   - Chart loads correctly?
   - Date is current?

4. **Verify All Recipients Got Email (1 minute)**
   - Ask team if they received report
   - Check spam folders if anyone missed it

**If all 4 checks pass → Everything is working! ✅**

---

### Monthly Health Check (15 minutes once a month)

**First Monday of each month:**

1. **Review Success Rate**
   - Check last 4 weeks of GitHub Actions runs
   - Should be 4/4 successful
   - If any failures, investigate

2. **Verify Data Quality**
   - Open latest report
   - Check post counts (should be 20-50 per week)
   - Verify sentiment makes sense
   - Spot-check a few Reddit links

3. **Check API Quotas**
   - Reddit API: No quota issues?
   - Gmail: No sending limits hit?
   - GitHub Actions: Within free tier?

4. **Update Documentation**
   - Any changes to process?
   - Any new issues discovered?
   - Update this guide if needed

---

## 🚀 Step 4: How to Manually Trigger Reports {#manual-trigger}

**If automation fails or you need an off-schedule report:**

### Method 1: GitHub Actions Web UI (Easiest - 30 seconds)

1. **Go to GitHub Actions:**
   ```
   https://github.com/ktsering2025/reddit-competitor-sentiment/actions
   ```

2. **Click "Weekly Reddit Sentiment Analysis"** (left sidebar)

3. **Click "Run workflow"** (blue button on right)

4. **Click "Run workflow"** again (confirmation)

5. **Wait 3 minutes** → Check email! ✅

**No code, no terminal, no technical knowledge needed!**

---

### Method 2: Local Computer (If GitHub Actions is down)

**Requirements:**
- Mac/Linux computer
- Python 3.10+ installed
- Git installed

**Steps:**

```bash
# 1. Clone repository (first time only)
cd ~/Desktop
git clone https://github.com/ktsering2025/reddit-competitor-sentiment.git
cd reddit-competitor-sentiment

# 2. Install dependencies (first time only)
pip3 install -r requirements.txt

# 3. Create .env file with secrets (first time only)
cat > .env << 'EOF'
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=reddit-sentiment-bot/1.0
GMAIL_EMAIL=your_email@hellofresh.com
GMAIL_APP_PASSWORD=your_app_password_here
EMAIL_RECIPIENTS=brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com,adam.kalikow@hellofresh.com,adam.park@factor75.com
EOF

# 4. Run automation (every time you need a report)
python3 complete_automation.py

# 5. Check email in 3 minutes!
```

---

## 🆘 Step 5: Troubleshooting Common Issues {#troubleshooting}

### Issue 1: "Didn't receive email on Sunday"

**Possible causes:**
- ❌ Automation didn't run
- ❌ Email went to spam
- ❌ Gmail credentials expired

**How to fix:**

1. **Check if automation ran:**
   - Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
   - Look for run on Sunday evening
   - If no run → Manually trigger (see Step 4)

2. **Check spam folder:**
   - Search for "Reddit Competitor Sentiment"
   - If in spam → Mark as "Not Spam"

3. **Check GitHub Actions logs:**
   - Click on the failed run
   - Look for error messages
   - Common errors:
     - "Authentication failed" → Gmail password expired
     - "Reddit API error" → Reddit credentials expired
     - "No posts found" → Reddit API issue (temporary)

4. **Regenerate credentials if needed:**
   - Reddit: https://www.reddit.com/prefs/apps
   - Gmail: https://myaccount.google.com/apppasswords
   - Update in GitHub Secrets

---

### Issue 2: "Report shows 0 posts"

**Possible causes:**
- ❌ Reddit API credentials expired
- ❌ Reddit API rate limit hit
- ❌ Reddit is down (rare)

**How to fix:**

1. **Check Reddit API credentials:**
   - Go to: https://www.reddit.com/prefs/apps
   - Verify your app still exists
   - Regenerate credentials if needed

2. **Check GitHub Actions logs:**
   - Look for "Reddit API" errors
   - Look for "PRAW" errors
   - Look for "401 Unauthorized" errors

3. **Wait and retry:**
   - Sometimes Reddit API has temporary issues
   - Wait 1 hour and manually trigger again

4. **Test locally:**
   ```bash
   python3 accurate_scraper.py
   ```
   - Should create `reports/working_reddit_data.json`
   - Check if file has posts

---

### Issue 3: "GitHub Actions workflow failed"

**Possible causes:**
- ❌ GitHub Actions quota exceeded (unlikely)
- ❌ Secrets not configured
- ❌ Code error (rare)

**How to fix:**

1. **Check the error logs:**
   - Click on the failed run
   - Click on "run-automation" job
   - Read the error message

2. **Common errors and fixes:**

   **"Secret not found":**
   - Go to: Settings → Secrets and variables → Actions
   - Verify all 6 secrets are present
   - Re-add any missing secrets

   **"pip install failed":**
   - Usually temporary
   - Manually trigger again

   **"git push failed":**
   - Check repository permissions
   - Verify GitHub token has write access

3. **If all else fails:**
   - Run locally (see Method 2 in Step 4)
   - Contact GitHub support

---

### Issue 4: "Website not updating"

**Possible causes:**
- ❌ GitHub Pages not enabled
- ❌ Git push failed
- ❌ Cache issue

**How to fix:**

1. **Verify GitHub Pages is enabled:**
   - Go to: Settings → Pages
   - Source should be: "Deploy from a branch"
   - Branch should be: "main" and "/ (root)"

2. **Check recent commits:**
   ```
   https://github.com/ktsering2025/reddit-competitor-sentiment/commits/main
   ```
   - Should see recent "🤖 Automated weekly update" commit
   - If not → Automation didn't push changes

3. **Hard refresh browser:**
   - Mac: Cmd + Shift + R
   - Windows: Ctrl + F5
   - This clears cache

4. **Wait 3-5 minutes:**
   - GitHub Pages takes a few minutes to deploy
   - Check again after waiting

---

## 📞 Step 6: Emergency Contacts {#emergency-contacts}

### If You Need Help:

**Technical Issues:**
- **Kunsang Tsering** (original developer)
  - Email: kunsang.tsering@hellofresh.com
  - Knows the entire system

**Reddit API Issues:**
- Reddit Support: https://www.reddit.com/r/redditdev
- Reddit API Docs: https://www.reddit.com/dev/api

**GitHub Issues:**
- GitHub Support: https://support.github.com
- GitHub Actions Docs: https://docs.github.com/en/actions

**Gmail Issues:**
- Gmail Support: https://support.google.com/mail
- App Passwords: https://myaccount.google.com/apppasswords

---

### Escalation Path:

1. **First:** Check this troubleshooting guide
2. **Second:** Check GitHub Actions logs for errors
3. **Third:** Manually trigger workflow
4. **Fourth:** Contact Kunsang (if still available)
5. **Fifth:** Contact ML/AI team at HelloFresh
6. **Last Resort:** Hire external developer (see code documentation)

---

## ✅ Step 7: Handoff Checklist {#handoff-checklist}

### Before You Leave:

**Week 1: Documentation**
- [ ] Review all documentation files
- [ ] Update any outdated information
- [ ] Add any missing troubleshooting steps
- [ ] Document any recent changes

**Week 2: Transfer Access**
- [ ] Transfer GitHub repository ownership (or add as admin)
- [ ] Share all secrets securely (1Password, LastPass, etc.)
- [ ] Verify new owner can access GitHub Actions
- [ ] Verify new owner can access GitHub Secrets

**Week 3: Training Session**
- [ ] Schedule 1-hour meeting with new owner
- [ ] Walk through this handoff guide
- [ ] Show how to monitor automation (Step 3)
- [ ] Show how to manually trigger (Step 4)
- [ ] Show how to troubleshoot (Step 5)
- [ ] Answer all questions

**Week 4: Shadow Period**
- [ ] New owner monitors next Sunday's run
- [ ] You're available for questions
- [ ] Verify they received email
- [ ] Verify they can check GitHub Actions
- [ ] Verify they understand the system

**Final Week: Transition Complete**
- [ ] New owner successfully monitors automation
- [ ] New owner can manually trigger if needed
- [ ] New owner knows how to troubleshoot
- [ ] All documentation updated
- [ ] Emergency contact info shared
- [ ] You're officially hands-off! ✅

---

## 📚 Key Documents to Review

**New owner should read these (in order):**

1. **`README.md`** - Project overview (5 min read)
2. **`HANDOFF_GUIDE.md`** - This document (20 min read)
3. **`AUTOMATION_EXPLAINED.md`** - How automation works (10 min read)
4. **`WEEKLY_AUTOMATION_GUARANTEE.md`** - Ensuring weekly reports (5 min read)
5. **`TECHNICAL_DOCUMENTATION.md`** - Deep technical details (30 min read)

**Total reading time:** ~70 minutes

---

## 🎓 Training Session Agenda (1 hour)

**Use this agenda for your handoff meeting:**

### Introduction (5 minutes)
- What the project does
- Current status
- Why it's important

### Live Demo (15 minutes)
- Show live dashboard
- Show sample email report
- Show GitHub Actions runs
- Show how to check if it's working

### Hands-On Practice (20 minutes)
- New owner manually triggers workflow
- New owner checks GitHub Actions logs
- New owner verifies email received
- New owner checks website updated

### Troubleshooting Walkthrough (10 minutes)
- Show common issues
- Show how to read error logs
- Show how to regenerate credentials
- Show how to run locally (backup)

### Q&A (10 minutes)
- Answer all questions
- Address concerns
- Share emergency contacts
- Confirm they feel comfortable

---

## 🎯 Success Criteria

**New owner is ready when they can:**

✅ Explain what the project does (30 seconds)  
✅ Check if automation ran successfully (2 minutes)  
✅ Manually trigger a report (30 seconds)  
✅ Read GitHub Actions error logs (5 minutes)  
✅ Know where to find secrets (1 minute)  
✅ Know who to contact for help (1 minute)  
✅ Feel confident managing the system  

**If they can do all 7 → Handoff complete! 🎉**

---

## 📋 Quick Reference Card

**Print this and give to new owner:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 REDDIT SENTIMENT PROJECT - QUICK REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 IMPORTANT LINKS:
├─ Dashboard: https://ktsering2025.github.io/reddit-competitor-sentiment/
├─ GitHub: https://github.com/ktsering2025/reddit-competitor-sentiment
└─ Actions: https://github.com/[...]/actions

⏰ SCHEDULE:
Every Sunday at 8:00 PM EST (automatic)

📧 RECIPIENTS (5 people):
brian.leung, assaf.ronen, kunsang.tsering, adam.kalikow, adam.park

✅ WEEKLY CHECK (Every Monday):
1. Did I receive Sunday's email?
2. GitHub Actions shows green checkmark?
3. Dashboard shows latest data?
4. All recipients got email?

🚀 MANUAL TRIGGER (If needed):
1. Go to GitHub Actions
2. Click "Weekly Reddit Sentiment Analysis"
3. Click "Run workflow" (blue button)
4. Wait 3 minutes → Check email!

🆘 TROUBLESHOOTING:
├─ No email? → Check spam, then manually trigger
├─ 0 posts? → Check Reddit API credentials
├─ Failed run? → Check GitHub Actions logs
└─ Need help? → See HANDOFF_GUIDE.md

📞 EMERGENCY CONTACT:
Kunsang Tsering - kunsang.tsering@hellofresh.com

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎉 Final Notes

**To the new owner:**

This project is fully operational and requires minimal maintenance. You'll 
spend about 5 minutes every Monday morning verifying it ran successfully. 
If anything goes wrong, this guide has step-by-step troubleshooting.

The system has been running successfully for weeks with 100% reliability. 
As long as you monitor it weekly and keep credentials up-to-date, it will 
continue to work smoothly.

**You got this!** 💪

---

**To Kunsang:**

You've built something solid and production-ready. This handoff guide ensures 
your work continues to provide value even after you leave. Great job! 🚀

---

**Document Version:** 1.0  
**Last Updated:** December 2, 2025  
**Created By:** Kunsang Tsering  
**For:** Project handoff to manager/team member
