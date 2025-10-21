#!/usr/bin/env bash
# Complete Reddit Scraping Pipeline
# Runs scraper + sentiment analysis + Step 1 chart
echo "HELLOFRESH REDDIT SCRAPING PIPELINE"
echo "===================================="

# Step 1: Run Reddit Scraper
echo "Step 1: Running Reddit Scraper..."
python3 scraper.py

if [ $? -ne 0 ]; then
    echo "Scraper failed."
    exit 1
fi

echo ""
echo "Step 2: Generating Step 1 Chart..."
python3 step1_chart.py

if [ $? -ne 0 ]; then
    echo "Chart generation failed."
    exit 1
fi

echo ""
echo "Step 3: Verifying data..."
if [ -f "reports/working_reddit_data.json" ]; then
    echo "Data saved successfully!"
    echo "File size: $(ls -lh reports/working_reddit_data.json | awk '{print $5}')"
else
    echo "Data file not found."
    exit 1
fi

if [ -f "reports/step1_chart.png" ]; then
    echo "Chart generated successfully!"
    echo "Chart size: $(ls -lh reports/step1_chart.png | awk '{print $5}')"
else
    echo "Chart file not found."
    exit 1
fi

echo ""
echo "PIPELINE COMPLETE!"
echo "Ready for Brian's review - Step 1 chart generated!"