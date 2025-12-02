# 👔 Manager Quick Start Guide

**For Brian (or new project owner) - Everything you need to know in 10 minutes**

---

## 🎯 What This Project Does (30 seconds)

Every Sunday at 8 PM EST, this system automatically:
1. Scrapes Reddit for posts about 8 meal kit brands
2. Analyzes if posts are positive, negative, or neutral
3. Creates charts and reports
4. Emails 5 stakeholders with insights
5. Updates live dashboard

**Your involvement: ZERO** - it runs automatically! 🎉

---

## 🔗 Important Links (Bookmark These)

| What | Link | When to Use |
|------|------|-------------|
| **Live Dashboard** | https://ktsering2025.github.io/reddit-competitor-sentiment/ | View latest reports |
| **GitHub Repo** | https://github.com/ktsering2025/reddit-competitor-sentiment | Manage project |
| **GitHub Actions** | https://github.com/ktsering2025/reddit-competitor-sentiment/actions | Check if automation ran |
| **Manual Trigger** | Same as Actions, click "Run workflow" | If Sunday run fails |

---

## ✅ Weekly Checklist (5 minutes every Monday)

**Every Monday morning, check these 3 things:**

### 1. Did You Receive Sunday's Email? (1 minute)
- **Subject:** "Weekly Reddit Competitor Sentiment Report — [dates]"
- **Has:** PDF chart attached
- **From:** kunsang.tsering@hellofresh.com (or configured email)

✅ **If yes** → Everything is working!  
❌ **If no** → See troubleshooting below

---

### 2. Check GitHub Actions (2 minutes)
**Go to:** https://github.com/ktsering2025/reddit-competitor-sentiment/actions

**Look for:**
- Latest run should be from Sunday evening
- Green checkmark ✅ = Success
- Red X ❌ = Failed (see troubleshooting)

✅ **If green** → Everything is working!  
❌ **If red** → See troubleshooting below

---

### 3. Check Dashboard (1 minute)
**Go to:** https://ktsering2025.github.io/reddit-competitor-sentiment/

**Verify:**
- Shows latest week's data
- Chart loads correctly
- Date is current

✅ **If updated** → Everything is working!  
❌ **If old data** → See troubleshooting below

---

### 4. Verify All Recipients Got Email (1 minute)
**Ask these 4 people if they received the report:**
- brian.leung@hellofresh.com
- assaf.ronen@hellofresh.com
- adam.kalikow@hellofresh.com
- adam.park@factor75.com

✅ **If all received** → Everything is working!  
❌ **If someone missed it** → Check their spam folder

---

## 🚀 How to Manually Trigger (30 seconds)

**If automation fails or you need an off-schedule report:**

1. Go to: https://github.com/ktsering2025/reddit-competitor-sentiment/actions
2. Click "Weekly Reddit Sentiment Analysis" (left sidebar)
3. Click green "Run workflow" button (top right)
4. Click "Run workflow" again (confirmation)
5. Wait 3 minutes → Check your email!

**That's it!** No code, no terminal, just click buttons. ✅

---

## 🆘 Troubleshooting (Quick Fixes)

### Problem: "Didn't receive email on Sunday"

**Fix:**
1. Check spam folder
2. Go to GitHub Actions (link above)
3. If no run on Sunday → Manually trigger (see above)
4. If run failed → Click on it to see error, then contact Kunsang

---

### Problem: "Report shows 0 posts"

**Fix:**
1. Probably Reddit API credentials expired
2. Contact Kunsang to regenerate credentials
3. Or see full troubleshooting in `HANDOFF_GUIDE.md`

---

### Problem: "GitHub Actions failed"

**Fix:**
1. Click on the failed run
2. Read the error message
3. Common issues:
   - "Authentication failed" → Gmail password expired
   - "Reddit API error" → Reddit credentials expired
4. Contact Kunsang if unclear

---

### Problem: "Website not updating"

**Fix:**
1. Hard refresh browser (Cmd+Shift+R on Mac, Ctrl+F5 on Windows)
2. Wait 5 minutes (GitHub Pages takes time to deploy)
3. Check GitHub Actions - did automation run successfully?

---

## 🔐 Taking Ownership (One-Time Setup)

**When Kunsang leaves, you need to:**

### Step 1: Get GitHub Access (5 minutes)
**Option A: Transfer Repository**
- Kunsang transfers repo to your GitHub account
- You become owner with full control

**Option B: Add as Admin**
- Kunsang adds you as admin collaborator
- You have full control, Kunsang remains owner

**Option C: HelloFresh Organization**
- Transfer repo to HelloFresh GitHub org
- You become admin within org

---

### Step 2: Get Credentials (5 minutes)
**Kunsang needs to share these 6 secrets with you:**
1. Reddit API credentials (3 secrets)
2. Gmail credentials (2 secrets)
3. Email recipients list (1 secret)

**How to access after transfer:**
- Go to: Settings → Secrets and variables → Actions
- You can view/edit all secrets

**Store securely:** Use 1Password, LastPass, or similar

---

### Step 3: Test It (5 minutes)
**Verify you can:**
1. Access GitHub repository ✅
2. View GitHub Actions runs ✅
3. Manually trigger workflow ✅
4. Receive email reports ✅

**If all 4 work → You're good to go!** 🎉

---

## 📞 Who to Contact

### Technical Issues:
**Kunsang Tsering** (original developer)
- Email: kunsang.tsering@hellofresh.com
- Knows everything about the system

### After Kunsang Leaves:
- Check `HANDOFF_GUIDE.md` for detailed troubleshooting
- Contact ML/AI team at HelloFresh
- Check GitHub Actions logs for error messages
- Reddit API docs: https://www.reddit.com/dev/api
- GitHub Actions docs: https://docs.github.com/en/actions

---

## 📚 Additional Documentation

**If you need more details:**

| Document | What It Covers | When to Read |
|----------|---------------|--------------|
| `HANDOFF_GUIDE.md` | Complete handoff process | Before Kunsang leaves |
| `README.md` | Project overview | Getting started |
| `AUTOMATION_EXPLAINED.md` | How automation works | Understanding system |
| `TECHNICAL_DOCUMENTATION.md` | Code details | Deep technical issues |
| `WEEKLY_AUTOMATION_GUARANTEE.md` | Ensuring reliability | Optimization |

---

## 🎓 30-Minute Training Session

**Schedule this with Kunsang before they leave:**

### Agenda:
1. **Demo** (10 min) - See system in action
2. **Practice** (10 min) - You manually trigger a report
3. **Troubleshooting** (5 min) - Walk through common issues
4. **Q&A** (5 min) - Ask anything

### What You'll Learn:
- ✅ How to check if automation ran
- ✅ How to manually trigger reports
- ✅ How to read error logs
- ✅ Where to find credentials
- ✅ Who to contact for help

---

## 📊 Current Status

**As of December 2, 2025:**

| Metric | Status |
|--------|--------|
| **Automation** | ✅ Working perfectly |
| **Last Run** | December 1, 2025 (Sunday) |
| **Success Rate** | 100% (last 5 weeks) |
| **Recipients** | 5 people |
| **Next Run** | December 8, 2025 (Sunday 8 PM EST) |
| **Manual Intervention** | None needed |

---

## 🎯 Success Criteria

**You're ready to own this project when you can:**

✅ Explain what it does (30 seconds)  
✅ Check if it ran successfully (2 minutes)  
✅ Manually trigger a report (30 seconds)  
✅ Know who to contact for help  

**That's it!** This project is low-maintenance and highly reliable. 🚀

---

## 💡 Key Takeaways

### What You Need to Know:
1. **It runs automatically** - No action needed from you
2. **Check every Monday** - Takes 5 minutes
3. **Manual trigger available** - If automation fails
4. **Highly reliable** - 100% success rate so far
5. **Well documented** - All guides available

### What You DON'T Need to Know:
- ❌ How to code Python
- ❌ How sentiment analysis works
- ❌ How to set up GitHub Actions
- ❌ How Reddit API works

**You just need to monitor and trigger manually if needed!** ✅

---

## 🎉 Bottom Line

This project is **production-ready** and **fully automated**. You'll spend 
5 minutes every Monday checking it ran successfully. If anything goes wrong, 
you can manually trigger it with 2 clicks.

**It's that simple!** 💪

---

## 📋 Quick Reference Card

**Print this and keep at your desk:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 REDDIT SENTIMENT - MANAGER CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏰ RUNS: Every Sunday 8 PM EST (automatic)

✅ MONDAY CHECK (5 minutes):
1. Got email? → Yes ✅ / No ❌
2. GitHub Actions green? → Yes ✅ / No ❌  
3. Dashboard updated? → Yes ✅ / No ❌
4. All recipients got it? → Yes ✅ / No ❌

🚀 MANUAL TRIGGER (if needed):
https://github.com/ktsering2025/reddit-competitor-sentiment/actions
→ Click "Run workflow" → Wait 3 min

📊 VIEW REPORTS:
https://ktsering2025.github.io/reddit-competitor-sentiment/

📞 HELP:
Kunsang: kunsang.tsering@hellofresh.com
Docs: See HANDOFF_GUIDE.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

**Questions?** Ask Kunsang before they leave!

**Ready to take over?** You got this! 🎉

---

**Created:** December 2, 2025  
**For:** Brian Leung (or new project owner)  
**By:** Kunsang Tsering
