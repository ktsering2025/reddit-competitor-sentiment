#!/bin/bash
# Manual Refresh Script - Run complete automation without sending email

cd "$(dirname "$0")"

echo "🔄 Starting manual refresh..."
echo "This will:"
echo "  1. Scrape latest Reddit posts (past 7 days)"
echo "  2. Regenerate Step 1 chart"
echo "  3. Regenerate Step 2 deep dive"
echo "  4. Regenerate Step 3 competitor analysis"
echo "  5. Update landing page"
echo ""

python3 complete_automation.py --no-send

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Refresh complete!"
    echo "📊 View updated reports:"
    echo "   - Landing page: index.html"
    echo "   - Chart: reports/step1_chart.png"
    echo "   - Step 2: reports/step2_ACTIONABLE_analysis_LATEST.html"
    echo "   - Step 3: reports/step3_competitor_analysis_LATEST.html"
else
    echo ""
    echo "❌ Refresh failed. Check the error messages above."
    exit 1
fi
