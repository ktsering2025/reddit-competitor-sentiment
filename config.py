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
    "HelloFresh": "https://www.reddit.com/search/?q=hellofresh&type=posts&t=week&cId=769414f9-964b-4ebe-a1ff-f90cbd6b0908&iId=59059aa8-e8c2-4d42-b520-99edad80893d",
    "Factor75": "https://www.reddit.com/search/?q=factor75&type=posts&t=week&cId=44d92750-2572-487c-91c0-2aed826ec3ab&iId=4441f666-996b-4434-b057-3999a14b44d7",
    "Home Chef": "https://www.reddit.com/search/?q=Home+Chef&type=posts&t=week&cId=8c9ccbfc-1914-4a26-a5c9-b0d23339a024&iId=563a6653-9627-4d76-98be-f30396295389",
    "Blue Apron": "https://www.reddit.com/search/?q=Blue+Apron&type=posts&t=week&cId=d3d63097-c67a-4dfa-a725-8db03e904c7b&iId=48d2ba6c-0d4b-476d-852f-11d8437e4c91",
    "Marley Spoon": [
        "https://www.reddit.com/search/?q=Marley+Spoon&type=posts&t=week&cId=76ab259d-b1ad-4bb7-ab56-a010eda6e781&iId=6f707832-8cbf-47d4-b57d-b434c9aa5598",
        "https://www.reddit.com/r/marleyspoon/new/"
    ],
    "Hungryroot": "https://www.reddit.com/search/?q=hungryroot&type=posts&t=week"
}

# Brand List (6 competitors as specified)
COMPETITORS = ["HelloFresh", "Factor75", "Home Chef", "Blue Apron", "Marley Spoon", "Hungryroot"]

# Filtering Configuration
EXCLUDE_KEYWORDS = [
    'snap', 'food stamps', 'ebt', 'BIFL', 'promo', 'referral', 
    'discount code', 'coupon', 'affiliate'
]

# Sentiment Configuration
SENTIMENT_THRESHOLD = 0.1
POSITIVE_THRESHOLD = 0.05
NEGATIVE_THRESHOLD = -0.05

# Week Window Strategy (A) Week-window & data sources per your spec
WEEK_MODE = "MON_SAT"   # allowed: MON_FRI | MON_SAT | FULL_7
WEEK_END_OVERRIDE = None  # or "2025-10-25" when WEEK_END env is set
INCLUDE_SATURDAY_THRESHOLD = 5

# File Paths
WORKING_DATA_FILE = "reports/working_reddit_data.json"
AUTOMATION_LOG = "automation.log"

# Chart Configuration
CHART_FIGSIZE = (12, 6)
CHART_OUTPUT = "reports/step1_chart.png"

# Analysis Configuration
STEP2_OUTPUT = "reports/step2_ACTIONABLE_analysis_LATEST.html"
ARCHIVE_DIR = "reports/archive"
RAW_DATA_DIR = "reports/raw"