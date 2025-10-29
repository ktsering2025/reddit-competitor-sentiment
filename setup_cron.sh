#!/bin/bash
# Setup cron job for weekly automation on Sundays at 8pm EST

# Get the absolute path to the project
PROJECT_DIR="/Users/kunsang.tsering/Desktop/reddit-competitor-sentiment"

# Create cron job entry
# Runs every Sunday at 8pm EST (20:00)
CRON_ENTRY="0 20 * * 0 cd $PROJECT_DIR && UTC=1 /usr/bin/python3 complete_automation.py >> automation.log 2>&1"

# Check if cron job already exists
(crontab -l 2>/dev/null | grep -v "reddit-competitor-sentiment") | crontab -

# Add the new cron job
(crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -

echo "✅ Cron job installed successfully!"
echo ""
echo "Automation Schedule:"
echo "  - Runs every Sunday at 8:00 PM EST"
echo "  - Collects past 7 days of Reddit data"
echo "  - Generates all reports (Chart, Step 2, Step 3)"
echo "  - Updates homepage"
echo "  - Commits and pushes to GitHub Pages"
echo ""
echo "To view current cron jobs:"
echo "  crontab -l"
echo ""
echo "To remove the cron job:"
echo "  crontab -l | grep -v 'reddit-competitor-sentiment' | crontab -"
