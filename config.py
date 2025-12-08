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
EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS', 'brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com,adam.kalikow@hellofresh.com,adam.park@factor75.com,daniel.seidel@hellofresh.com,ben@hellofresh.ca,sandra.nestic@hellofresh.ca,nunzio.disavino@hellofresh.com,dme@hellofresh.com,maureen@hellofresh.com,megan.thompson@hellofresh.ca,mara.hanerfeld@hellofresh.com,frankie.hernandez@hellofresh.com,pete.balodimas@hellofresh.com,kelsey.lindenschmidt@hellofresh.com,christopher.stadler@factor75.com,niklas.vanhusen@factor75.com,katie.paganelli@hellofresh.com').split(',')

# DATA SOURCES - Weekly Reddit Search Links (all competitors for Step 1)
# Multiple links per brand for comprehensive data collection
WEEKLY_LINKS = {
    "HelloFresh": [
        "https://www.reddit.com/search/?q=hellofresh&type=posts&t=week",
        "https://www.reddit.com/search/?q=hello+fresh&type=posts&t=week",
        "https://www.reddit.com/r/hellofresh/search/?q=&type=posts&t=week&restrict_sr=1",
        "https://www.reddit.com/r/mealkits/search/?q=hellofresh&type=posts&t=week&restrict_sr=1"
    ],
    "Factor75": [
        "https://www.reddit.com/search/?q=factor75&type=posts&t=week",
        "https://www.reddit.com/search/?q=factor+75&type=posts&t=week",
        "https://www.reddit.com/search/?q=factor+meals&type=posts&t=week",
        "https://www.reddit.com/r/ReadyMeals/search/?q=factor&type=posts&t=week&restrict_sr=1",
        "https://www.reddit.com/r/mealkits/search/?q=factor&type=posts&t=week&restrict_sr=1"
    ],
    "Home Chef": [
        "https://www.reddit.com/search/?q=home+chef&type=posts&t=week",
        "https://www.reddit.com/r/mealkits/search/?q=home+chef&type=posts&t=week&restrict_sr=1"
    ],
    "Blue Apron": [
        "https://www.reddit.com/search/?q=blue+apron&type=posts&t=week",
        "https://www.reddit.com/r/blueapron/search/?q=&type=posts&t=week&restrict_sr=1",
        "https://www.reddit.com/r/mealkits/search/?q=blue+apron&type=posts&t=week&restrict_sr=1"
    ],
    "Marley Spoon": [
        "https://www.reddit.com/search/?q=marley+spoon&type=posts&t=week",
        "https://www.reddit.com/r/mealkits/search/?q=marley+spoon&type=posts&t=week&restrict_sr=1"
    ],
    "Hungryroot": [
        "https://www.reddit.com/search/?q=hungryroot&type=posts&t=week",
        "https://www.reddit.com/r/hungryroot/search/?q=&type=posts&t=week&restrict_sr=1",
        "https://www.reddit.com/r/mealkits/search/?q=hungryroot&type=posts&t=week&restrict_sr=1"
    ],
    "EveryPlate": [
        "https://www.reddit.com/search/?q=everyplate&type=posts&t=week",
        "https://www.reddit.com/search/?q=every+plate&type=posts&t=week",
        "https://www.reddit.com/search/?q=Every+Plate+food&type=all&t=week",
        "https://www.reddit.com/search/?q=Every+Plate+Food+Brand&type=all&t=week",
        "https://www.reddit.com/r/mealkits/search/?q=everyplate&type=posts&t=week&restrict_sr=1"
    ],
    "Green Chef": [
        "https://www.reddit.com/search/?q=green+chef&type=posts&t=week",
        "https://www.reddit.com/search/?q=greenchef&type=posts&t=week",
        "https://www.reddit.com/search/?q=Green+Chef+mealkit+brand&type=all&t=week",
        "https://www.reddit.com/r/mealkits/search/?q=green+chef&type=posts&t=week&restrict_sr=1"
    ]
}

# All competitors for Step 1 chart (8 brands total)
ALL_COMPETITORS = ["HelloFresh", "Factor75", "Home Chef", "Blue Apron", "Marley Spoon", "Hungryroot", "EveryPlate", "Green Chef"]

# HelloFresh family brands (for chart labeling)
HF_FAMILY_BRANDS = ["HelloFresh", "Factor75", "EveryPlate", "Green Chef"]

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

# Week Window Strategy - Simple 7-day rolling window
WEEK_MODE = "FULL_7"   # Always use past 7 days
WEEK_END_OVERRIDE = None  # Set via WEEK_END env variable if needed
INCLUDE_SATURDAY_THRESHOLD = 5  # Not used in FULL_7 mode

# Chart Configuration
CHART_FIGSIZE = (16, 8)  # Larger size for email clarity
CHART_OUTPUT = "reports/step1_chart.png"

# File Paths
WORKING_DATA_FILE = "reports/working_reddit_data.json"
AUTOMATION_LOG = "automation.log"

# Analysis Configuration
STEP2_OUTPUT = "reports/step2_ACTIONABLE_analysis_LATEST.html"
ARCHIVE_DIR = "reports/archive"
RAW_DATA_DIR = "reports/raw"