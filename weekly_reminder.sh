#!/bin/bash
# Weekly reminder script for Brian's competitor analysis
# Runs every Sunday at 8 PM local time

cd "/Users/kunsang.tsering/Desktop/reddit-competitor-sentiment"

echo "Starting Brian's weekly competitor analysis..."
echo "Timestamp: $(date)"

# Run the complete automation pipeline with email
python3 complete_automation.py --send brian.leung@hellofresh.com asaf@hellofresh.com

echo "Weekly analysis complete."
echo "Check automation.log for details."