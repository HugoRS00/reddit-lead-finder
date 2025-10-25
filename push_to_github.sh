#!/bin/bash
# Quick Push to GitHub Script

echo "🚀 Pushing Reddit Lead Finder to GitHub..."
echo ""

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found. Please run this script from the reddit_lead_finder directory."
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    git branch -M main
else
    echo "✅ Git repository already initialized"
fi

# Check if remote exists
if git remote | grep -q origin; then
    echo "✅ Remote 'origin' already configured"
else
    echo "📡 Adding remote repository..."
    git remote add origin https://github.com/HugoRS00/reddit-lead-finder.git
fi

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📝 Committing changes..."
    git add .
    git commit -m "Initial commit: Reddit Lead Finder for TradingWizard.ai"
else
    echo "✅ No uncommitted changes"
fi

# Show current status
echo ""
echo "📊 Current Status:"
git log --oneline -1
echo ""

# Push to GitHub
echo "🚀 Pushing to GitHub..."
echo ""
echo "You may be prompted to authenticate."
echo "Use your GitHub Personal Access Token as the password."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Your code is now on GitHub!"
    echo ""
    echo "Next steps:"
    echo "1. Go to: https://github.com/HugoRS00/reddit-lead-finder"
    echo "2. Add GitHub Secrets (Settings → Secrets → Actions):"
    echo "   - REDDIT_CLIENT_ID"
    echo "   - REDDIT_CLIENT_SECRET"
    echo "3. Enable GitHub Actions (Actions tab)"
    echo ""
    echo "🎉 You're all set!"
else
    echo ""
    echo "❌ Push failed. Common solutions:"
    echo ""
    echo "1. Generate Personal Access Token:"
    echo "   https://github.com/settings/tokens"
    echo "   - Click 'Generate new token (classic)'"
    echo "   - Select 'repo' scope"
    echo "   - Use token as password"
    echo ""
    echo "2. Or use GitHub CLI:"
    echo "   gh auth login"
    echo "   ./push_to_github.sh"
    echo ""
fi
