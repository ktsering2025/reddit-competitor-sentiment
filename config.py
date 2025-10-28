# Configuration for Reddit Competitor Sentiment Analysis
# Brian's Project 1 - Final Build Plan

# Reddit API Configuration (load from .env)
import os
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'CompetitorSentimentBot/1.0')

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS', 'brian.leung@hellofresh.com,asaf@hellofresh.com').split(',')

# DATA SOURCES - Weekly Reddit Search Links (locked as per Brian's spec)
WEEKLY_LINKS = {
    "HelloFresh": "https://www.reddit.com/search/?q=hellofresh&type=posts&t=week&cId=08353dc8-9146-4af0-8a43-b88c1acb9c9f&iId=bf5bf57d-392e-4933-ae90-6285e2717618",
    "Factor75": "https://www.reddit.com/search/?q=factor75&type=posts&t=week&cId=44d92750-2572-487c-91c0-2aed826ec3ab&iId=4441f666-996b-4434-b057-3999a14b44d7"
}

# Brand List (2 focus brands as specified)
COMPETITORS = ["HelloFresh", "Factor75"]

# Filtering Configuration
EXCLUDE_KEYWORDS = [
    'snap', 'food-stamps', 'BIFL', 'environmental factor'
]

# Sentiment Configuration
SENTIMENT_THRESHOLD = 0.1
POSITIVE_THRESHOLD = 0.05
NEGATIVE_THRESHOLD = -0.05

# Week Window Strategy (A) Week-window & data sources per your spec
WEEK_MODE = "MON_SAT"   # allowed: MON_FRI | MON_SAT | FULL_7
WEEK_END_OVERRIDE = None  # or "2025-10-25" when WEEK_END env is set
INCLUDE_SATURDAY_THRESHOLD = 5

# Chart Configuration
CHART_FIGSIZE = (12, 6)  # Medium image size as specified
CHART_OUTPUT = "reports/step1_chart.png"

# File Paths
WORKING_DATA_FILE = "reports/working_reddit_data.json"
AUTOMATION_LOG = "automation.log"

# Analysis Configuration
STEP2_OUTPUT = "reports/step2_ACTIONABLE_analysis_LATEST.html"
ARCHIVE_DIR = "reports/archive"
RAW_DATA_DIR = "reports/raw"