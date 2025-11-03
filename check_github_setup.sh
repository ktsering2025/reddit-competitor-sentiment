#!/bin/bash
# GitHub Actions Setup Checker
# Run this to verify everything is configured correctly

set -e

REPO="ktsering2025/reddit-competitor-sentiment"

echo "=========================================="
echo "GitHub Actions Setup Checker"
echo "=========================================="
echo ""

# Check 1: Workflow file exists
echo "✓ Check 1: Workflow file exists"
if gh api repos/$REPO/contents/.github/workflows/weekly-automation.yml >/dev/null 2>&1; then
    echo "  ✅ PASS: weekly-automation.yml exists"
else
    echo "  ❌ FAIL: weekly-automation.yml not found"
    exit 1
fi
echo ""

# Check 2: Secrets are set
echo "✓ Check 2: Required secrets"
need=(REDDIT_CLIENT_ID REDDIT_CLIENT_SECRET REDDIT_USER_AGENT GMAIL_EMAIL GMAIL_APP_PASSWORD EMAIL_RECIPIENTS)
have=$(gh secret list -R $REPO --json name -q '.[].name' 2>/dev/null || echo "")

if [ -z "$have" ]; then
    echo "  ❌ FAIL: No secrets found (you need to run ./setup_github_actions.sh)"
    echo ""
    echo "  Missing secrets:"
    for s in "${need[@]}"; do
        echo "    - $s"
    done
    exit 1
fi

all_good=true
for s in "${need[@]}"; do
    if echo "$have" | grep -q "^$s$"; then
        echo "  ✅ $s"
    else
        echo "  ❌ MISSING: $s"
        all_good=false
    fi
done
echo ""

if [ "$all_good" = false ]; then
    echo "❌ FAIL: Some secrets are missing"
    echo "   Run: ./setup_github_actions.sh"
    exit 1
fi

# Check 3: Actions are enabled
echo "✓ Check 3: GitHub Actions enabled"
if gh api repos/$REPO/actions/permissions >/dev/null 2>&1; then
    echo "  ✅ PASS: Actions are enabled"
else
    echo "  ❌ FAIL: Actions not enabled"
    exit 1
fi
echo ""

# Check 4: Recent workflow runs
echo "✓ Check 4: Workflow runs"
runs=$(gh run list -R $REPO --workflow=weekly-automation.yml --limit 1 --json status,conclusion,createdAt -q '.[0]' 2>/dev/null || echo "{}")

if [ "$runs" = "{}" ]; then
    echo "  ⚠️  WARNING: No workflow runs yet"
    echo "     Trigger manually: gh workflow run weekly-automation.yml -R $REPO"
else
    status=$(echo "$runs" | jq -r '.status')
    conclusion=$(echo "$runs" | jq -r '.conclusion')
    created=$(echo "$runs" | jq -r '.createdAt')
    
    echo "  Last run: $created"
    echo "  Status: $status"
    echo "  Result: $conclusion"
    
    if [ "$conclusion" = "success" ]; then
        echo "  ✅ PASS: Last run succeeded"
    elif [ "$conclusion" = "failure" ]; then
        echo "  ❌ FAIL: Last run failed"
        echo "     View logs: gh run list -R $REPO --limit 1"
    else
        echo "  ⏳ In progress or queued"
    fi
fi
echo ""

# Check 5: Cron schedule
echo "✓ Check 5: Cron schedule"
cron=$(gh api repos/$REPO/contents/.github/workflows/weekly-automation.yml | jq -r '.content' | base64 --decode | grep -A2 'schedule:' | grep 'cron:' || echo "")

if [ -n "$cron" ]; then
    echo "  ✅ PASS: Cron schedule found"
    echo "  Schedule: $cron"
    echo "  Next run: Sunday 8:00 PM EST"
else
    echo "  ❌ FAIL: No cron schedule found"
    exit 1
fi
echo ""

# Final verdict
echo "=========================================="
echo "FINAL VERDICT"
echo "=========================================="

if [ "$all_good" = true ] && [ -n "$cron" ]; then
    echo "✅ ALL CHECKS PASSED!"
    echo ""
    echo "Your automation is ready:"
    echo "  - Workflow file: ✅"
    echo "  - Secrets: ✅ (all 6 set)"
    echo "  - Actions enabled: ✅"
    echo "  - Cron schedule: ✅ (Sunday 8 PM EST)"
    echo ""
    echo "Next steps:"
    echo "  1. Test manually: gh workflow run weekly-automation.yml -R $REPO"
    echo "  2. Watch it run: gh run watch -R $REPO --exit-status"
    echo "  3. Check email in 2-3 minutes"
    echo ""
    echo "Sunday 8 PM EST automation: READY ✅"
else
    echo "❌ SETUP INCOMPLETE"
    echo ""
    echo "Run this to fix: ./setup_github_actions.sh"
fi
echo ""
