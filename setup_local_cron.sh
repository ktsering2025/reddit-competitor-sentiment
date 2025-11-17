#!/bin/bash

# Setup Local Cron for Weekly Automation
# This ensures reports run EVERY Sunday at 8 PM, even if GitHub Actions fails

echo "🤖 Setting up local cron job for weekly automation..."
echo ""

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "reddit-competitor-sentiment"; then
    echo "⚠️  Cron job already exists!"
    echo ""
    echo "Current cron jobs:"
    crontab -l | grep "reddit-competitor-sentiment"
    echo ""
    read -p "Do you want to replace it? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Cancelled"
        exit 1
    fi
    # Remove old cron job
    crontab -l | grep -v "reddit-competitor-sentiment" | crontab -
fi

# Get the project path
PROJECT_PATH="/Users/kunsang.tsering/Desktop/reddit-competitor-sentiment"

# Get Python path
PYTHON_PATH=$(which python3)

# Create the cron job
CRON_JOB="0 20 * * 0 cd $PROJECT_PATH && $PYTHON_PATH complete_automation.py >> $PROJECT_PATH/automation.log 2>&1"

# Add to crontab
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "✅ Cron job installed successfully!"
echo ""
echo "📅 Schedule: Every Sunday at 8:00 PM EST"
echo "📂 Project: $PROJECT_PATH"
echo "🐍 Python: $PYTHON_PATH"
echo "📝 Logs: $PROJECT_PATH/automation.log"
echo ""
echo "🔍 Verify installation:"
echo "   crontab -l"
echo ""
echo "⚠️  IMPORTANT: Your Mac must be:"
echo "   1. Powered on at 8 PM Sunday"
echo "   2. NOT in sleep mode (keep awake or plugged in)"
echo ""
echo "🧪 Test it now (without sending emails):"
echo "   cd $PROJECT_PATH && python3 complete_automation.py --no-send"
echo ""
echo "✅ Done! Your automation will run every Sunday at 8 PM!"
