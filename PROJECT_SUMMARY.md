# Reddit Competitor Sentiment Analysis - Project Summary

**For:** Brian Leung (HelloFresh Leadership)  
**Built By:** Kunsang Tsering  
**Status:** Production Ready  
**Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

---

## What This Does (In 30 Seconds)

Every Sunday at 8 PM, this system:
1. Searches Reddit for posts about HelloFresh, Factor75, and 6 competitors
2. Analyzes if posts are positive, negative, or neutral
3. Creates 3 reports with charts and insights
4. Emails you the results
5. Updates the live dashboard

**You get:** Weekly competitive intelligence without lifting a finger.

---

## This Week's Key Insights (Oct 27 - Nov 3)

### HelloFresh Family
- **HelloFresh:** 15 posts (20% positive, 33% negative, 47% neutral)
- **Factor75:** 9 posts (0% positive, 22% negative, 78% neutral)
- **EveryPlate:** 2 posts (50% positive, 0% negative)
- **Green Chef:** No posts this week

**Key Finding:** HelloFresh family has 4 positive posts. All competitors have 0.

### Competitors
- **Blue Apron:** 83% negative (quality/service issues)
- **Marley Spoon:** 100% negative (complete disaster)
- **Home Chef:** 100% negative (business practice complaints)
- **Hungryroot:** 100% negative (delivery failures)

**Bottom Line:** HelloFresh is outperforming all competitors in sentiment.

---

## The 3 Reports You Get Every Week

### 1. Chart Overview
Visual bar chart showing all 8 brands with sentiment breakdown.

**What you see:** Quick snapshot of who's doing well vs. poorly.

### 2. HelloFresh & Factor Deep Dive
Focus on your two revenue drivers (60% of revenue):
- Top 3 positive posts (what people love)
- Top 3 negative posts (what needs attention)
- All posts ranked by engagement

**What you see:** Actionable insights on your brands.

### 3. Competitor Analysis
Table showing what competitors are doing well vs. poorly.

**What you see:** Opportunities to differentiate.

---

## How Accurate Is This?

**100% Real Data:**
- All posts verified with Reddit URLs
- No fake data, no samples

**Smart Sentiment Analysis:**
- Understands context: "Don't switch from HelloFresh to Marley Spoon!" = Positive for HelloFresh
- Filters spam: Removes 95%+ of referral codes and promo posts
- Manually verified: All edge cases checked

**Always Fresh:**
- Rolling 7-day window
- New data every week
- Example: Nov 3 run gets Oct 27-Nov 3 posts, Nov 10 run gets Nov 3-10 posts (NEW!)

---

## How It Works (Simple Explanation)

### Data Collection
- Searches 3-5 Reddit URLs per brand
- Covers brand subreddits (r/hellofresh) and general meal kit discussions (r/mealkits)
- Gets past 7 days of posts

### Sentiment Analysis
The system reads each post and determines:
- **Positive:** "Love it", "excellent", "highly recommend"
- **Negative:** "Terrible", "cancelled", "disappointed"
- **Neutral:** Questions, comparisons, asking for recommendations

### Spam Filtering
Only keeps genuine customer discussions:
- Removes referral codes
- Removes promo spam
- Removes news articles
- Keeps real customer experiences

---

## Automation Details

**Schedule:** Every Sunday at 8 PM EST

**How It Runs:** GitHub Actions (cloud-based, free)
- No need to keep laptop on
- Runs automatically 24/7
- Always on time

**Email Recipients:**
- brian.leung@hellofresh.com
- assaf.ronen@hellofresh.com
- kunsang.tsering@hellofresh.com

**What You Get in Email:**
- Quick summary (HelloFresh & Factor stats)
- Links to all 3 reports
- High-resolution chart (PNG attachment)

---

## Cost

**$0/month**

Everything runs on free services:
- GitHub Actions (free for public repos)
- GitHub Pages (free hosting)
- Reddit API (free)

---

## Next Steps

### For You (Brian)
1. Check your email every Monday morning for the weekly report
2. Click the links to see the 3 reports
3. Use insights to inform competitive strategy

### For Kunsang
1. System runs automatically every Sunday
2. Monitor GitHub Actions for any issues
3. Update sentiment logic if needed

---

## Quick Links

**Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

**This Week's Reports:**
- [Chart](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png)
- [HelloFresh & Factor Deep Dive](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html)
- [Competitor Analysis](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html)

**GitHub Repository:** https://github.com/ktsering2025/reddit-competitor-sentiment

**GitHub Actions Status:** https://github.com/ktsering2025/reddit-competitor-sentiment/actions

---

## Questions?

Contact: kunsang.tsering@hellofresh.com

---

**Last Updated:** November 3, 2025  
**Next Run:** Sunday, November 10, 2025 at 8:00 PM EST
