"""
Configuration settings for Reddit Competitor Sentiment Agent
Based on HelloFresh US Market Insights (August 2025)
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Competitors to track (based on HelloFresh US Market Insights August 2025)
COMPETITORS = {
    # Meal Kit Competitors (Market Size: $3.88B, HF Group: 58.0% share)
    "HelloFresh": {"category": "meal_kit", "hf_brand": True, "market_share": 49.6},  # Our baseline (HF)
    "EveryPlate": {"category": "meal_kit", "hf_brand": True, "market_share": 5.3},  # HF brand
    "Green Chef": {"category": "meal_kit", "hf_brand": True, "market_share": 3.1},  # HF brand
    "Home Chef": {"category": "meal_kit", "hf_brand": False, "market_share": 15.9},  # Main competitor
    "HungryRoot": {"category": "meal_kit", "hf_brand": False, "market_share": 17.4},  # Main competitor
    "Blue Apron": {"category": "meal_kit", "hf_brand": False, "market_share": 4.0},
    "Sunbasket": {"category": "meal_kit", "hf_brand": False, "market_share": 0},
    "Purple Carrot": {"category": "meal_kit", "hf_brand": False, "market_share": 0},
    "Marley Spoon": {"category": "meal_kit", "hf_brand": False, "market_share": 0},
    "Gobble": {"category": "meal_kit", "hf_brand": False, "market_share": 0},
    "Dinnerly": {"category": "meal_kit", "hf_brand": False, "market_share": 0},
    
    # Ready-to-Eat Competitors (Market Size: $2.48B)
    "Factor": {"category": "rte", "hf_brand": True, "market_share": 75.9},  # HF brand - dominant
    "CookUnity": {"category": "rte", "hf_brand": False, "market_share": 18.4},  # Main RTE competitor
    "Daily Harvest": {"category": "rte", "hf_brand": False, "market_share": 0},
    "Sakara Life": {"category": "rte", "hf_brand": False, "market_share": 0},
    "Snap Kitchen": {"category": "rte", "hf_brand": False, "market_share": 0},
    "Splendid Spoon": {"category": "rte", "hf_brand": False, "market_share": 0},
    "Thistle": {"category": "rte", "hf_brand": False, "market_share": 0},
    
    # Premium Meat Competitors (Market Size: $837M)
    "Good Chop": {"category": "premium_meat", "hf_brand": True, "market_share": 12.6},  # HF brand
    "ButcherBox": {"category": "premium_meat", "hf_brand": False, "market_share": 62.3},  # Dominant competitor
    "Good Ranchers": {"category": "premium_meat", "hf_brand": False, "market_share": 10.7},
    "Crowd Cow": {"category": "premium_meat", "hf_brand": False, "market_share": 0},
    "Moink Box": {"category": "premium_meat", "hf_brand": False, "market_share": 0},
    "Porter Road": {"category": "premium_meat", "hf_brand": False, "market_share": 0},
    "Wild Alaskan": {"category": "premium_meat", "hf_brand": False, "market_share": 0},
    
    # Pet Food Competitors (Market Size: $1.53B)
    "The Pets Table": {"category": "pet_food", "hf_brand": True, "market_share": 2.3},  # HF brand
    "The Farmer's Dog": {"category": "pet_food", "hf_brand": False, "market_share": 73.5},  # Dominant leader
    "Ollie": {"category": "pet_food", "hf_brand": False, "market_share": 11.2},
    "Sundays for Dogs": {"category": "pet_food", "hf_brand": False, "market_share": 0},
    "Spot & Tango": {"category": "pet_food", "hf_brand": False, "market_share": 0},
    "NomNomNow": {"category": "pet_food", "hf_brand": False, "market_share": 0},
    "Pet Plate": {"category": "pet_food", "hf_brand": False, "market_share": 0},
    
    # VMS (Vitamins/Supplements) Competitors (Market Size: $53M monthly)
    "Factor VMS": {"category": "vms", "hf_brand": True, "market_share": 0.49},  # HF brand - small player
    "Hiya Health": {"category": "vms", "hf_brand": False, "market_share": 23.6},  # Market leader
    "Ka'Chava": {"category": "vms", "hf_brand": False, "market_share": 15.0},
    "Liquid IV": {"category": "vms", "hf_brand": False, "market_share": 8.1},
    "AG1": {"category": "vms", "hf_brand": False, "market_share": 0.1},
    "Athletic Greens": {"category": "vms", "hf_brand": False, "market_share": 0},
    "Bloom Nutrition": {"category": "vms", "hf_brand": False, "market_share": 0},
    "Gainful": {"category": "vms", "hf_brand": False, "market_share": 0},
    "Ritual": {"category": "vms", "hf_brand": False, "market_share": 0},
    "Care/of": {"category": "vms", "hf_brand": False, "market_share": 0},
}

# Market context from HelloFresh insights
MARKET_INSIGHTS = {
    "meal_kits": {
        "market_size": "$3.88B", 
        "yoy_growth": "-14.6%",
        "hf_group_share": "58.0%",
        "trend": "declining"
    },
    "rte": {
        "market_size": "$2.48B", 
        "yoy_growth": "+17.7%",
        "factor_dominance": "75.9%",
        "trend": "growing_fast"
    },
    "premium_meat": {
        "market_size": "$837M", 
        "yoy_growth": "+25%",
        "butcherbox_dominance": "62.3%",
        "trend": "growing_strong"
    },
    "pet_food": {
        "market_size": "$1.53B", 
        "yoy_growth": "N/A",
        "farmers_dog_dominance": "73.5%",
        "hf_opportunity": "small_player",
        "trend": "large_established_market"
    },
    "vms": {
        "market_size": "$53M monthly", 
        "yoy_growth": "-38%",
        "hf_opportunity": "very_small_player",
        "trend": "declining"
    }
}

# Reddit settings - Food/Meal delivery focused subreddits
REDDIT_SUBREDDITS = [
    # Food & Meal prep
    "MealKits", 
    "MealPrepSunday",
    "mealdelivery",
    "cookingforbeginners", 
    "EatCheapAndHealthy",
    "Cooking",
    "food",
    "budgetfood",
    "HealthyFood",
    "veganmealprep",
    "ketorecipes",
    "nutrition",
    "fitmeals",
    
    # Pet related
    "DogFood",
    "pets",
    "puppy101",
    "AskVet",
    
    # Health & supplements
    "supplements",
    "fitness",
    "loseit",
    "gainit",
    
    # General consumer
    "BuyItForLife",
    "Frugal",
    "personalfinance",
    "reviewthis"
]

# Search terms and keywords - Food delivery focused
SEARCH_KEYWORDS = [
    # Meal Kit terms
    "meal kit", "meal delivery", "meal subscription", "cooking box", "recipe box",
    "meal plan", "dinner kit", "fresh ingredients", "pre-portioned meals",
    
    # Ready-to-eat terms  
    "ready to eat", "prepared meals", "meal delivery service", "healthy meals delivered",
    "fresh prepared food", "pre-made meals",
    
    # Premium meat terms
    "meat delivery", "grass fed beef", "organic meat", "butcher box", "meat subscription",
    "premium steaks", "wild caught fish",
    
    # Pet food terms
    "fresh dog food", "dog food delivery", "custom dog food", "fresh pet food",
    "human grade dog food", "subscription dog food",
    
    # VMS terms
    "vitamin subscription", "daily vitamins", "supplement delivery", "personalized vitamins",
    "greens powder", "superfood supplements"
]

# Trustpilot ratings from the report (for validation)
TRUSTPILOT_RATINGS = {
    "HelloFresh": 3.7,
    "Green Chef": 4.0,
    "EveryPlate": 4.1,
    "Factor": 3.5,
    "Blue Apron": 3.5,
    "Sunbasket": 3.9,
    "Marley Spoon": 3.9,
    "Purple Carrot": 2.8,
    "Dinnerly": 3.7,
    "Home Chef": 3.3,
    "CookUnity": 4.1,
    "HungryRoot": 4.3
}

# Priority competitors (focus analysis on these)
HIGH_PRIORITY_COMPETITORS = [
    # Direct threats to HF brands
    "Home Chef",           # 15.9% meal kit share
    "HungryRoot",         # 17.4% meal kit share
    "CookUnity",          # 18.4% RTE share
    "ButcherBox",         # 62.3% premium meat share
    "The Farmer's Dog",   # 73.5% pet food share
    "Hiya Health",        # 23.6% VMS share
    
    # HF brands to monitor
    "HelloFresh", "EveryPlate", "Green Chef", "Factor", 
    "Good Chop", "The Pets Table", "Factor VMS"
]

# Scraping settings
MAX_POSTS_PER_SUBREDDIT = 50
DAYS_TO_SEARCH = 7  # Look back 7 days

# Email settings (for report delivery)
EMAIL_ENABLED = os.getenv('EMAIL_ENABLED', 'False').lower() == 'true'
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
EMAIL_USER = os.getenv('EMAIL_USER', '')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
REPORT_RECIPIENTS = os.getenv('REPORT_RECIPIENTS', '').split(',')

# Output settings
OUTPUT_DIR = "reports"
SAVE_TO_EXCEL = True
SAVE_TO_CSV = True