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

# DATA SOURCES - Weekly Reddit Search Links (all competitors for Step 1)
WEEKLY_LINKS = {
    "HelloFresh": "https://old.reddit.com/search/?q=hellofresh&type=posts&t=week&sort=new",
    "Factor75": "https://old.reddit.com/search/?q=factor75&type=posts&t=week&sort=new",
    "Blue Apron": "https://old.reddit.com/search/?q=blue+apron&type=posts&t=week&sort=new",
    "Home Chef": "https://old.reddit.com/search/?q=home+chef&type=posts&t=week&sort=new",
    "Marley Spoon": "https://old.reddit.com/search/?q=marley+spoon&type=posts&t=week&sort=new",
    "Hungryroot": "https://old.reddit.com/search/?q=hungryroot&type=posts&t=week&sort=new",
    "EveryPlate": "https://old.reddit.com/search/?q=everyplate&type=posts&t=week&sort=new",
    "Green Chef": "https://old.reddit.com/search/?q=green+chef&type=posts&t=week&sort=new"
}

# All competitors for Step 1 chart
ALL_COMPETITORS = ["HelloFresh", "Factor75", "Blue Apron", "Home Chef", "Marley Spoon", "Hungryroot", "EveryPlate", "Green Chef"]

# Focus brands for Step 2 deep dive (60% of HF revenue)
FOCUS_BRANDS = ["HelloFresh", "Factor75"]

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