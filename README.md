# Reddit Competitor Sentiment Analysis

## What it does

**Step 1**: Generates a stacked bar chart showing all competitors' sentiment breakdown (positive/negative/neutral) from weekly Reddit data.

**Step 2**: Creates a detailed HTML analysis focused on HelloFresh and Factor75 (60% of HF revenue):
- Executive Summary table (totals + sentiment percentages)
- Top 3 Positive and Top 3 Negative posts for each brand (ranked by engagement = score + 3×comments)
- Complete repository of all posts found
- Live weekly search links
- Theme grouping (Quality, Delivery, Service, Price)

**Step 3**: Competitor deep dive analysis with strengths/weaknesses table:
- Benchmark insights against all competitors
- Strengths: Areas with 60%+ positive sentiment
- Weaknesses: Areas with 60%+ negative sentiment
- Categorized by Quality, Delivery, Service, and Price themes

## How to run weekly

### Manual run:
```bash
python3 complete_automation.py --no-send
```

### With email:
```bash
python3 complete_automation.py --send brian.leung@hellofresh.com asaf@hellofresh.com
```

### Automated (Sunday 8pm):
```bash
0 20 * * 0 cd ~/Desktop/reddit-competitor-sentiment && /usr/bin/python3 complete_automation.py --send brian.leung@hellofresh.com asaf@hellofresh.com >> automation.log 2>&1
```

## Live links

- **Dashboard**: https://ktsering2025.github.io/reddit-competitor-sentiment/
- **Step 1 Chart**: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png
- **Step 2 Analysis**: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html
- **Step 3 Competitor Analysis**: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step3_competitor_analysis_LATEST.html

## Data sources

Uses canonical weekly Reddit searches from old.reddit.com for all competitors:
- **HelloFresh**: https://old.reddit.com/search/?q=hellofresh&type=posts&t=week&sort=new
- **Factor75**: https://old.reddit.com/search/?q=factor75&type=posts&t=week&sort=new
- **Blue Apron**: https://old.reddit.com/search/?q=blue+apron&type=posts&t=week&sort=new
- **Home Chef**: https://old.reddit.com/search/?q=home+chef&type=posts&t=week&sort=new
- **Marley Spoon**: https://old.reddit.com/search/?q=marley+spoon&type=posts&t=week&sort=new
- **Hungryroot**: https://old.reddit.com/search/?q=hungryroot&type=posts&t=week&sort=new

## Files

- `accurate_scraper.py` - Reddit data scraper (all competitors)
- `step1_chart.py` - Step 1 chart generator (all competitors)
- `step2_ACTIONABLE_analysis.py` - Step 2 HTML analysis (HelloFresh + Factor75 focus)
- `step3_competitor_analysis.py` - Step 3 competitor deep dive (strengths/weaknesses)
- `complete_automation.py` - Main pipeline (runs all 3 steps)
- `send_to_gmail.py` - Email sender
- `config.py` - Configuration
- `weekly_reminder.sh` - Weekly automation script