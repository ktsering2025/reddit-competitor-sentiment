# 📊 Reddit Competitor Sentiment Analysis

**Automated weekly competitive intelligence dashboard for HelloFresh & Factor75**

Real-time Reddit sentiment tracking across 8 meal kit brands with automated reporting, email alerts, and beautiful visualizations.

---

## 🎯 What It Does

This system automatically scrapes Reddit weekly, analyzes sentiment, and generates actionable intelligence reports for HelloFresh's competitive landscape.

### 📈 Step 1: Competitor Overview Chart
- **Stacked bar chart** showing all 8 competitors
- Sentiment breakdown: Positive (green) / Negative (red) / Neutral (gray)
- Post volume comparison
- HelloFresh family brands labeled with "(HF)"

### 🔍 Step 2: Brand Deep Dive (HelloFresh & Factor75)
Focus on the two revenue-driving brands:
- **Executive Summary** with sentiment percentages
- **Top 3 Positive Posts** ranked by engagement score (Score + 3×Comments)
- **Top 3 Negative Posts** with actionable insights
- **"Why This Matters"** explanations for each post
- Complete repository of all posts
- Live weekly search links for verification

### 🏆 Step 3: Competitor Analysis
Benchmark against all competitors:
- **Real sentiment data** (not generic statements)
- Shows actual post counts and percentages
- Example: "3 positive posts (23% of 13 total)"
- Top 3 positive/negative posts for each competitor
- Engagement scoring for prioritization

---

## 🌐 Live Dashboard

**Main Dashboard:** https://ktsering2025.github.io/reddit-competitor-sentiment/

### Quick Links:
- **Step 1 Chart:** [View Chart](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png)
- **Step 2 Analysis:** [HelloFresh & Factor75 Deep Dive](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html)
- **Step 3 Competitor Analysis:** [All Competitors](https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html)

### 🎨 Design Features:
- ✅ HelloFresh green theme (calm, professional)
- ✅ Brand overview table on landing page
- ✅ Manual refresh button for on-demand updates
- ✅ Real-time data loading from JSON
- ✅ Mobile-responsive design

---

## 🚀 How to Run

### Option 1: Manual Refresh (Recommended)
Use the built-in script:
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
./manual_refresh.sh
```

Or run directly:
```bash
python3 complete_automation.py --no-send
```

### Option 2: Manual Refresh via Website
1. Visit the [dashboard](https://ktsering2025.github.io/reddit-competitor-sentiment/)
2. Click **"🔄 Manual Refresh Data Now"** button
3. Wait 30-60 seconds for data to refresh
4. Page auto-reloads with new data

### Option 3: Send Email Report
```bash
# Send to default recipients (Brian & Assaf Ronen)
python3 send_to_gmail.py

# Send to specific email
python3 send_to_gmail.py your.email@example.com
```

### Option 4: Full Automation with Email
```bash
python3 complete_automation.py
```

---

## ⏰ Automated Schedule

**Every Sunday at 8:00 PM EST:**
- Scrapes Reddit for past 7 days (true rolling window)
- Generates all 3 reports
- Updates dashboard
- Sends email to recipients
- Commits to GitHub (auto-deploys to GitHub Pages)

### Current Email Recipients:
1. brian.leung@hellofresh.com
2. assaf.ronen@hellofresh.com

### Cron Job:
```bash
0 20 * * 0 cd ~/Desktop/reddit-competitor-sentiment && /usr/bin/python3 complete_automation.py >> automation.log 2>&1
```

---

## 📊 Data Sources

### Tracked Brands (8 Total):
1. **HelloFresh** (HF Family)
2. **Factor75** (HF Family)
3. **EveryPlate** (HF Family)
4. **Green Chef** (HF Family)
5. Blue Apron
6. Home Chef
7. Marley Spoon
8. Hungryroot

### Reddit Search Strategy:
- **Multi-source scraping:** 3-5 search URLs per brand
- **Subreddit-specific searches:** Brand subreddits + r/mealkits
- **Natural language queries:** "hello fresh", "factor meals", etc.
- **Time filter:** Past 7 days (true rolling window)
- **Real-time data:** Always fresh, never stale

### Example Search URLs:
```
HelloFresh:
- https://www.reddit.com/search/?q=hellofresh&type=posts&t=week
- https://www.reddit.com/search/?q=hello+fresh&type=posts&t=week
- https://www.reddit.com/r/hellofresh/search/?type=posts&t=week
- https://www.reddit.com/r/mealkits/search/?q=hellofresh&type=posts&t=week

Factor75:
- https://www.reddit.com/search/?q=factor75&type=posts&t=week
- https://www.reddit.com/search/?q=factor+meals&type=posts&t=week
- https://www.reddit.com/r/ReadyMeals/search/?q=factor&type=posts&t=week
- https://www.reddit.com/r/mealkits/search/?q=factor&type=posts&t=week
```

---

## 🧠 Sentiment Analysis

### Dual-Method Approach:
1. **VADER Sentiment** (social media optimized)
2. **TextBlob** (general text analysis)
3. **Keyword-based overrides** (meal kit specific)

### Context-Aware Logic:
- Detects if negative words are about competitors (not the primary brand)
- Handles comparisons intelligently ("better than X")
- Identifies questions vs. complaints
- Recognizes brand abbreviations (HF, F75, etc.)

### Sentiment Priority:
1. Strong Negative (always wins)
2. Context-Aware Positive (wins over neutral)
3. Questions/Neutral Comparisons
4. Strong Positive
5. VADER + TextBlob (fallback)

### Filtering (3-Tier Whitelist):
- **Tier 1:** Brand-specific subreddits (e.g., r/hellofresh)
- **Tier 2:** Meal kit discussion subreddits (e.g., r/mealkits)
- **Tier 3:** General food subreddits (only if brand in title)

### Customer Discussion Detection:
Posts must show genuine customer discussion using 60+ phrases:
- "my experience", "I tried", "recommendations"
- "cancel", "upcharge", "customer service"
- "quality", "delivery", "fresh", "spoiled"

---

## 📁 File Structure

```
reddit-competitor-sentiment/
├── accurate_scraper.py          # Core Reddit scraper (all brands)
├── step1_chart.py               # Chart generator (600 DPI, green theme)
├── step2_ACTIONABLE_analysis.py # HelloFresh & Factor75 deep dive
├── step3_competitor_analysis.py # Competitor analysis (real data)
├── complete_automation.py       # Main pipeline orchestrator
├── send_to_gmail.py            # Email sender (AppleScript)
├── config.py                   # Configuration & search URLs
├── manual_refresh.sh           # Manual refresh script
├── index.html                  # Landing page (green theme)
├── requirements.txt            # Python dependencies
├── reports/
│   ├── step1_chart.png         # Latest chart (600 DPI)
│   ├── step2_ACTIONABLE_analysis_LATEST.html
│   ├── step3_competitor_analysis_LATEST.html
│   ├── working_reddit_data.json # Raw data
│   ├── HEALTH.json             # System status
│   ├── SUMMARY.json            # Quick stats
│   ├── raw/                    # Raw scraped data
│   └── archive/                # Historical reports
└── automation.log              # Cron job logs
```

---

## 🎨 Design System

### Color Palette (HelloFresh Green):
- **Background:** Light green gradient (#f0fdf4 → #dcfce7)
- **Headers:** Fresh green gradient (#86efac → #4ade80)
- **Buttons:** Green gradient (#22c55e → #16a34a)
- **Positive:** Light green (#f0fdf4)
- **Negative:** Light red (#fef2f2)
- **Neutral:** Light gray (#f8fafc)

### Typography:
- Font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto
- Consistent sizing and spacing
- Professional, readable layout

---

## 📧 Email Reports

### Email Format:
**Subject:** Weekly Reddit Competitor Sentiment Report — [Date Range]

**Body:**
- Quick Summary (HelloFresh & Factor75 stats)
- Dashboard Access Links
- Chart attached as PNG (600 DPI, crystal clear)

### Email Features:
- ✅ Simplified body (no long post lists)
- ✅ High-res chart attachment (662KB, 16×8 inches)
- ✅ Clickable links to all reports
- ✅ Online chart link for full-size viewing

---

## 🔧 Technical Details

### Requirements:
```bash
pip install -r requirements.txt
```

**Key Dependencies:**
- `praw` - Reddit API wrapper
- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `vaderSentiment` - Sentiment analysis
- `textblob` - Text processing
- `matplotlib` - Chart generation
- `numpy` - Data processing

### Data Flow:
1. **Scrape:** `accurate_scraper.py` → `working_reddit_data.json`
2. **Chart:** `step1_chart.py` → `step1_chart.png`
3. **Step 2:** `step2_ACTIONABLE_analysis.py` → HTML report
4. **Step 3:** `step3_competitor_analysis.py` → HTML report
5. **Update:** `update_homepage.py` → `index.html` + `HEALTH.json`
6. **Deploy:** Git commit + push → GitHub Pages

### Date Window:
- **True rolling 7-day window** (not fixed Mon-Sun)
- Calculates from exact execution time
- Example: Run on Nov 3 at 8pm → Oct 27 8pm to Nov 3 8pm

---

## 🎯 Key Features

### ✅ Accuracy:
- 100% real Reddit posts (verified URLs)
- Sentiment manually verified for accuracy
- No spam, no promo codes
- Only genuine customer discussions

### ✅ Automation:
- Weekly Sunday 8pm EST execution
- Auto-commits to GitHub
- Auto-deploys to GitHub Pages
- Email alerts to stakeholders

### ✅ Transparency:
- All raw data saved (JSON)
- Reddit search links provided
- Commit hashes tracked
- Metadata included in reports

### ✅ Actionable:
- Top posts ranked by engagement
- "Why This Matters" explanations
- Real sentiment breakdowns
- Competitor benchmarking

---

## 🐛 Troubleshooting

### Issue: GitHub Pages showing old design
**Solution:** Hard refresh with `Cmd + Shift + R` or wait 2-3 minutes for rebuild

### Issue: Manual refresh button not working
**Solution:** Run `./manual_refresh.sh` in terminal instead

### Issue: No posts found for a brand
**Solution:** Check if brand had Reddit activity that week (some weeks are quiet)

### Issue: Email not sending
**Solution:** Verify AppleScript permissions and Mail app is configured

---

## 📝 Notes

- **Data Quality:** System filters out 95%+ of irrelevant posts
- **Engagement Score:** `Score + 3 × Comments` (prioritizes discussion)
- **Primary Brand:** Only counts posts genuinely about that brand
- **Context-Aware:** Detects when negative words are about competitors
- **Rolling Window:** Always exactly 7 days from execution time

---

## 👥 Built For

**Brian's Weekly Competitive Intelligence**

Automated reports for HelloFresh leadership to track brand health and competitive landscape on Reddit.

---

## 📄 License

Internal HelloFresh tool - Not for public distribution

---

**Last Updated:** October 30, 2025  
**Version:** 2.0 (Green Theme + Real Data)  
**Status:** ✅ Production Ready
