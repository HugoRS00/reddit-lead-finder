# Quick Start Guide ⚡

Get up and running with Reddit Lead Finder in 5 minutes!

## Step 1: Get Reddit API Credentials (2 minutes)

1. Go to https://www.reddit.com/prefs/apps
2. Scroll to bottom, click **"create another app..."**
3. Fill in:
   - **name**: TradingWizard Lead Finder
   - **type**: Select **"script"**
   - **description**: Marketing tool for TradingWizard.ai
   - **about url**: (leave blank)
   - **redirect uri**: http://localhost:8080
4. Click **"create app"**
5. Copy these values:
   - **client_id**: The string under "personal use script" (looks like: abc123xyz789)
   - **client_secret**: The string next to "secret" (longer string)

## Step 2: Install & Configure (2 minutes)

```bash
# Clone or download this repository
git clone https://github.com/yourusername/reddit-lead-finder.git
cd reddit-lead-finder

# Run setup script (Linux/Mac)
./setup.sh

# Or manually:
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and add your credentials:
```bash
REDDIT_CLIENT_ID=abc123xyz789
REDDIT_CLIENT_SECRET=your_long_secret_here
REDDIT_USER_AGENT=TradingWizard Lead Finder v1.0
```

## Step 3: Test Setup (30 seconds)

```bash
python test_setup.py
```

You should see:
```
✅ ALL TESTS PASSED! You're ready to run the lead finder.
```

## Step 4: Run Your First Scan (1 minute)

```bash
python main.py
```

Results saved to `leads.json`!

## Step 5: Review Results

Open `leads.json` to see:
- Reddit posts/comments matching your criteria
- Relevance scores (0-100)
- Pre-written reply drafts (variant A and B)
- Risk flags and recommendations

## What's Next?

### Customize Your Search

Edit `config.json`:
```json
{
  "keywords_core": [
    "AI trading",
    "chart analyzer",
    "technical analysis tool"
  ],
  "date_range_days": 3,
  "relevance_threshold": 70,
  "max_results": 10
}
```

### Target Specific Subreddits

```json
{
  "allowlist_subs": ["algotrading", "daytrading", "forex"]
}
```

### Schedule Daily Scans

Set up GitHub Actions (see README.md) for automated daily scans.

## Troubleshooting

### "Invalid credentials" error
- Double-check your client_id and client_secret
- Remove any extra spaces or quotes
- Ensure your Reddit app type is "script"

### No results found
- Lower `relevance_threshold` to 50
- Increase `date_range_days` to 14
- Add more keywords to `keywords_core`

### Rate limit errors
- Reddit API limits: 60 requests/minute
- Wait a minute and try again
- Reduce number of subreddits or keywords

## Example Workflow

1. **Morning**: Run scan to find overnight opportunities
2. **Review**: Check `leads.json`, sort by `relevance_score`
3. **Customize**: Edit reply drafts to match your voice
4. **Post**: Manually post replies (adds authenticity!)
5. **Track**: Note which threads got engagement

## Pro Tips 💡

1. **Start Small**: Test with 1-2 subreddits first
2. **Quality Over Quantity**: Focus on relevance_score > 80
3. **Personalize Replies**: Use drafts as templates, not copy-paste
4. **Engage Genuinely**: Reply to follow-up questions
5. **Track Results**: Note which approaches work best

## Need Help?

- See full README.md for detailed docs
- Check CONTRIBUTING.md to improve the tool
- Open an issue on GitHub

---

Happy lead hunting! 🎯
