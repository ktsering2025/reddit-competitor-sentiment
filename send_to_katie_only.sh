#!/bin/bash
# Load environment variables
source .env

# Send email to Katie only
python3 send_to_gmail_smtp.py katie.paganelli@hellofresh.com
