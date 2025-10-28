# Reddit Competitor Sentiment Analysis

## What it does

**Step 1**: Generates a stacked bar chart showing HelloFresh and Factor75 sentiment breakdown (positive/negative/neutral) from weekly Reddit data.

**Step 2**: Creates a detailed HTML analysis with:
- Executive Summary table (totals + sentiment percentages)
- Top 3 Positive and Top 3 Negative posts for each brand (ranked by engagement)
- Complete repository of all posts found
- Live weekly search links

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
- **Chart**: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step1_chart.png
- **Step 2 Analysis**: https://ktsering2025.github.io/reddit-competitor-sentiment/reports/step2_ACTIONABLE_analysis_LATEST.html

## Data sources

Uses canonical weekly Reddit searches:
- **HelloFresh**: https://www.reddit.com/search/?q=hellofresh&type=posts&t=week&cId=08353dc8-9146-4af0-8a43-b88c1acb9c9f&iId=bf5bf57d-392e-4933-ae90-6285e2717618
- **Factor75**: https://www.reddit.com/search/?q=factor75&type=posts&t=week&cId=44d92750-2572-487c-91c0-2aed826ec3ab&iId=4441f666-996b-4434-b057-3999a14b44d7

## Files

- `accurate_scraper.py` - Reddit data scraper
- `step1_chart.py` - Chart generator
- `step2_ACTIONABLE_analysis.py` - HTML analysis generator
- `complete_automation.py` - Main pipeline
- `send_to_gmail.py` - Email sender
- `config.py` - Configuration
- `weekly_reminder.sh` - Weekly automation script