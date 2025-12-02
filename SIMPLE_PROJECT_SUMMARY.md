# 📊 Reddit Sentiment Project - Simple Summary

**One-page overview to share with ML/AI team**

---

## 🎯 What It Does (10 Second Version)

Automatically tracks Reddit sentiment for 8 meal kit brands and emails weekly 
reports to 5 stakeholders every Sunday at 8 PM EST.

---

## 📧 The Output (What Stakeholders Get)

Every Sunday evening, 5 people receive:
- Email with sentiment summary
- PDF chart (positive/negative/neutral breakdown)
- Links to detailed HTML reports
- Top positive & negative posts per brand

**Example:** "HelloFresh: 15 posts this week (20% positive, 33% negative)"

---

## 🔄 The Pipeline (How It Works)

```
1. SCRAPE REDDIT
   ↓ (30+ sources, 8 brands)
   
2. ANALYZE SENTIMENT
   ↓ (VADER + TextBlob algorithms)
   
3. GENERATE REPORTS
   ↓ (Charts + HTML analyses)
   
4. UPDATE WEBSITE
   ↓ (GitHub Pages)
   
5. SEND EMAILS
   ↓ (Gmail SMTP with PDF attachment)
   
6. ARCHIVE DATA
   ↓ (Historical tracking)
```

**Total time:** ~3 minutes  
**Frequency:** Every Sunday 8 PM EST  
**Automation:** GitHub Actions

---

## 🏢 Brands Tracked

1. HelloFresh (Primary)
2. Factor75 (Primary)
3. Home Chef
4. Blue Apron
5. Marley Spoon
6. Hungryroot
7. EveryPlate
8. Green Chef

---

## 🛠️ Tech Stack

**Languages:**
- Python 3.10
- HTML/CSS
- YAML

**Key Libraries:**
- `praw` - Reddit API
- `vaderSentiment` - Sentiment analysis
- `textblob` - Sentiment analysis
- `matplotlib` - Charts
- `smtplib` - Email

**Infrastructure:**
- GitHub Actions (automation)
- GitHub Pages (hosting)
- Gmail SMTP (email delivery)

---

## 📊 Current Status

✅ **Working:** All components functional  
✅ **Tested:** Running successfully for 4+ weeks  
✅ **Production:** 5 stakeholders receiving reports  
✅ **Success Rate:** 100% (last 5 runs all successful)  

**Recent Runs:**
- Dec 1, 2025 ✅
- Nov 24, 2025 ✅
- Nov 17, 2025 ✅
- Nov 10, 2025 ✅
- Nov 3, 2025 ✅

---

## ❓ What I Need Help With

### Main Question:
**Is GitHub Actions cron reliable enough for production weekly automation?**

### Specific Concerns:
1. **Reliability:** How do I ensure emails go out every week without fail?
2. **Monitoring:** Should I add alerting if automation fails?
3. **Best Practices:** What do production teams use for scheduled jobs?
4. **Failure Modes:** What could go wrong that I'm not thinking about?

### What I've Heard:
- "GitHub Actions cron can be unreliable (delays up to 30+ minutes)"
- "Scheduled workflows might not trigger if repo is inactive"
- "Free tier has usage limits"

### What I Want:
- Confidence that stakeholders will get emails every Sunday
- Best practice recommendations from someone with production experience
- To learn what I might be missing

---

## 🔗 Links

**Live Dashboard:**  
https://ktsering2025.github.io/reddit-competitor-sentiment/

**GitHub Repo:**  
https://github.com/ktsering2025/reddit-competitor-sentiment

**GitHub Actions Runs:**  
https://github.com/ktsering2025/reddit-competitor-sentiment/actions

**Documentation:**  
See README.md and AUTOMATION_EXPLAINED.md in repo

---

## 📈 Sample Data

**Week of Nov 24-30, 2025:**
- Total posts analyzed: 31
- HelloFresh: 13 posts (23% positive, 31% negative)
- Factor75: 5 posts (0% positive, 60% negative)
- Blue Apron: 5 posts (40% positive, 20% negative)

**Sentiment Analysis Method:**
- Dual algorithm (VADER + TextBlob)
- Context-aware (detects questions, comparisons)
- Keyword override (strong phrases override algorithms)

---

## 💡 Why I Built This

**Business Need:**  
HelloFresh leadership needs weekly competitive intelligence on Reddit sentiment 
for meal kit brands.

**My Solution:**  
Automated the entire process - from data collection to stakeholder delivery - 
so reports go out every week without manual work.

**Impact:**  
5 stakeholders now get actionable insights every Sunday without anyone having 
to manually scrape Reddit, analyze sentiment, or create reports.

---

## 🎯 What Success Looks Like

**For Stakeholders:**
- ✅ Receive email every Sunday at 8 PM EST
- ✅ See accurate sentiment data
- ✅ Get actionable insights on competitors
- ✅ Access historical trends

**For Me:**
- ✅ System runs automatically (no manual intervention)
- ✅ 100% reliability (no missed weeks)
- ✅ Confidence it's production-ready
- ✅ Learn best practices for automation

---

## 🤔 Discussion Topics

If we meet, I'd love to discuss:

1. **Reliability:** Is GitHub Actions the right choice?
2. **Alternatives:** Should I consider AWS Lambda, Airflow, etc.?
3. **Monitoring:** How to detect and alert on failures?
4. **Error Handling:** What failure modes should I plan for?
5. **Scaling:** What if we want daily reports instead of weekly?
6. **Best Practices:** What do production ML teams use?

---

## 📸 Screenshots

### Live Dashboard
![Dashboard](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png)

### Sample Email Report
*(Forward them one of your weekly emails)*

### GitHub Actions Success
*(Show them the green checkmarks at /actions)*

---

## ⏱️ Time Commitment

**What I'm Asking For:**
- 15-20 minute conversation
- Review my approach
- Share best practices
- Answer my specific questions

**What I Can Show:**
- Live working system
- Clean, documented code
- Successful run history
- Sample outputs

---

## 🙏 Why I'm Asking You

- You have production ML/automation experience
- You've built reliable scheduled systems
- You understand the challenges of production automation
- I want to learn from someone who's done this before

I'm not asking you to build anything - I've already built it! I just want to 
validate my approach and learn best practices.

---

## 📞 Next Steps

If you're interested in chatting:
1. Reply with your availability
2. I'll send you the repo link
3. We can do a quick 15-20 min call/meeting
4. I'll show you what I've built
5. You share your thoughts and recommendations

Thanks for considering! 🙏

---

**Contact:** kunsang.tsering@hellofresh.com  
**Project:** Reddit Competitor Sentiment Analysis  
**Status:** Working, seeking to optimize  
**Timeline:** Flexible - whenever you have time!
