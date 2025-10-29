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
# Multiple links per brand for comprehensive data collection
WEEKLY_LINKS = {
    "HelloFresh": [
        "https://www.reddit.com/search/?q=hellofresh&type=posts&t=week",
        "https://www.reddit.com/search/?q=hellofresh+mealkit+brand&type=posts&t=week",
        "https://www.reddit.com/search/?q=hellofresh+food+brand&type=posts&t=week"
    ],
    "Factor75": [
        "https://www.reddit.com/search/?q=factor75&type=posts&t=week",
        "https://www.reddit.com/search/?q=factor+mealkit+brand&type=posts&t=week",
        "https://www.reddit.com/search/?q=factor+food+brand&type=posts&t=week"
    ],
    "Home Chef": [
        "https://www.reddit.com/search/?q=homechef+mealkit+brand&type=posts&t=week"
    ],
    "Blue Apron": [
        "https://www.reddit.com/search/?q=blue+apron+mealkit+brand&type=posts&t=week",
        "https://www.reddit.com/search/?q=blue+apron+food+brand&type=posts&t=week"
    ],
    "Marley Spoon": [
        "https://www.reddit.com/search/?q=marley+spoon+food+brand&type=posts&t=week",
        "https://www.reddit.com/search/?q=marley+spoon+mealkit+brand&type=posts&t=week"
    ],
    "Hungryroot": [
        "https://www.reddit.com/search/?q=Hungryroot+food+brand&type=posts&t=week"
    ]
}

# All competitors for Step 1 chart (exactly 6 brands)
ALL_COMPETITORS = ["HelloFresh", "Factor75", "Home Chef", "Blue Apron", "Marley Spoon", "Hungryroot"]

# Primary brands for Step 2 deep dive (60% of HF revenue)
PRIMARY_DEEPDIVE = ["HelloFresh", "Factor75"]

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