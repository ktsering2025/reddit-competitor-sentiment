#!/bin/bash
# GitHub Actions Setup Script
# Run this to configure secrets and test the workflow

set -e

REPO="ktsering2025/reddit-competitor-sentiment"
BRANCH="main"

echo "=========================================="
echo "GitHub Actions Setup"
echo "=========================================="
echo ""

# Step 0: Check if logged in
echo "Step 0: Checking GitHub CLI authentication..."
if ! gh auth status >/dev/null 2>&1; then
    echo "❌ Not logged in to GitHub CLI"
    echo ""
    echo "Please run: gh auth login -w"
    echo "Then run this script again."
    exit 1
fi
echo "✅ Authenticated"
echo ""

# Step 1: Confirm workflow file exists
echo "Step 1: Checking workflow file..."
WORKFLOW_PATH=$(gh api repos/$REPO/contents/.github/workflows/weekly-automation.yml 2>/dev/null | jq -r .path)
if [ "$WORKFLOW_PATH" = ".github/workflows/weekly-automation.yml" ]; then
    echo "✅ Workflow file exists: $WORKFLOW_PATH"
else
    echo "❌ Workflow file not found"
    exit 1
fi
echo ""

# Step 2: Enable Actions permissions
echo "Step 2: Enabling Actions permissions..."
gh api -X PUT repos/$REPO/actions/permissions -f enabled=true >/dev/null 2>&1
gh api -X PUT repos/$REPO/actions/permissions/workflow \
  -f default_workflow_permissions=write \
  -f can_approve_pull_request_reviews=false >/dev/null 2>&1
echo "✅ Actions enabled with write permissions"
echo ""

# Step 3: Set secrets
echo "Step 3: Setting up secrets..."
echo ""

# Read from .env file
if [ ! -f .env ]; then
    echo "❌ .env file not found"
    exit 1
fi

source .env

# Set each secret
echo "Setting REDDIT_CLIENT_ID..."
echo "$REDDIT_CLIENT_ID" | gh secret set REDDIT_CLIENT_ID -R $REPO

echo "Setting REDDIT_CLIENT_SECRET..."
echo "$REDDIT_CLIENT_SECRET" | gh secret set REDDIT_CLIENT_SECRET -R $REPO

echo "Setting REDDIT_USER_AGENT..."
echo "CompetitorSentimentBot/1.0" | gh secret set REDDIT_USER_AGENT -R $REPO

echo "Setting GMAIL_EMAIL..."
echo "$EMAIL_USER" | gh secret set GMAIL_EMAIL -R $REPO

echo "Setting GMAIL_APP_PASSWORD..."
echo "$EMAIL_PASSWORD" | gh secret set GMAIL_APP_PASSWORD -R $REPO

echo "Setting EMAIL_RECIPIENTS..."
echo "brian.leung@hellofresh.com,assaf.ronen@hellofresh.com,kunsang.tsering@hellofresh.com" | gh secret set EMAIL_RECIPIENTS -R $REPO

echo ""
echo "✅ All secrets set!"
echo ""

# Step 4: Verify secrets
echo "Step 4: Verifying secrets..."
need=(REDDIT_CLIENT_ID REDDIT_CLIENT_SECRET REDDIT_USER_AGENT GMAIL_EMAIL GMAIL_APP_PASSWORD EMAIL_RECIPIENTS)
have=$(gh secret list -R $REPO --json name -q '.[].name')
all_good=true
for s in "${need[@]}"; do
  if echo "$have" | grep -q "^$s$"; then
    echo "✅ $s"
  else
    echo "❌ MISSING: $s"
    all_good=false
  fi
done
echo ""

if [ "$all_good" = false ]; then
    echo "❌ Some secrets are missing"
    exit 1
fi

# Step 5: Trigger workflow manually
echo "Step 5: Triggering workflow manually..."
gh workflow run weekly-automation.yml -R $REPO -r $BRANCH
echo "✅ Workflow triggered!"
echo ""

echo "Waiting 5 seconds for workflow to start..."
sleep 5
echo ""

# Step 6: Watch the run
echo "Step 6: Watching workflow run..."
echo "Press Ctrl+C to stop watching (workflow will continue running)"
echo ""
gh run watch -R $REPO --exit-status || true

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To view logs later, run:"
echo "  gh run list -R $REPO --workflow=weekly-automation.yml --limit 5"
echo ""
echo "To check if it worked:"
echo "  1. Check your email (all 3 recipients)"
echo "  2. Visit: https://ktsering2025.github.io/reddit-competitor-sentiment/"
echo "  3. Check latest commit: gh api repos/$REPO/commits?per_page=1 | jq -r '.[0].commit.message'"
echo ""
