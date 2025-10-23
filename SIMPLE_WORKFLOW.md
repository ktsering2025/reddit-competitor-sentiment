# 📧 Simple Manual Workflow for Brian

## 🎯 No Email Credentials Needed!

Just generate the report files and manually send to Brian.

## 📋 Weekly Workflow (2 minutes)

### 1. Generate Fresh Data & Chart:
```bash
python3 scraper.py      # Get last 7 days Reddit data
python3 step1_chart.py  # Generate weekly chart
```

### 2. Generate Email Report:
```bash
python3 generate_report.py
```

This creates:
- `reports/email_for_brian_[timestamp].txt` - Email text to copy/paste
- `reports/step1_chart.png` - Chart to attach

### 3. Manually Send Email:
1. Open Gmail/Outlook
2. New email to: `brian.leung@hellofresh.com`
3. Copy subject + body from the txt file
4. Attach `step1_chart.png`
5. Send!

## 📊 What You Get

**Email file contains:**
- Subject: "Weekly Reddit Competitor Sentiment Report — Oct 15–22, 2025"
- Professional body text with weekly summary
- All competitor data formatted exactly as Brian wants

**Chart file:**
- `step1_chart.png` - Clean professional chart with weekly data
- Ready to attach to any email

## 🚀 One-Command Workflow

For complete fresh report:
```bash
python3 scraper.py && python3 step1_chart.py && python3 generate_report.py
```

Then just copy the email text and attach the chart!

## 📅 Schedule

**Recommended: Every Sunday**
1. Run the commands above
2. Send the email to Brian
3. Takes 2 minutes total

## ✅ Advantages

- **No email setup** - Use any email client you want
- **Always works** - No authentication issues
- **Review first** - You can check the report before sending
- **Flexible** - Send to anyone, anytime
- **Professional** - Same quality report as automated system

**Much simpler than dealing with email credentials!**