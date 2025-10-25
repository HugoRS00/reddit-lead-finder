# 🎯 START HERE - Reddit Lead Finder for TradingWizard.ai

## What You Have 📦

A complete, production-ready Reddit marketing automation system with:

✅ **Intelligent Search** - Finds relevant Reddit opportunities automatically  
✅ **Smart Scoring** - Rates each opportunity 0-100 for relevance  
✅ **Value-First Replies** - Generates helpful replies (not spammy)  
✅ **Safety Built-In** - Respects subreddit rules and rate limits  
✅ **GitHub Ready** - Push to GitHub and automate with Actions  
✅ **Fully Documented** - Everything explained clearly  

## Your Files 📁

```
reddit_lead_finder/
├── 📘 START_HERE.md           ← You are here!
├── ⚡ QUICK_START.md          ← 5-minute setup guide
├── 📖 README.md               ← Full documentation
├── 🏗️  ARCHITECTURE.md        ← How it works
├── 📋 PROJECT_SUMMARY.md      ← Deployment guide
├── 🤝 CONTRIBUTING.md         ← How to improve it
│
├── 🐍 main.py                 ← Main application
├── ⚙️  config.json             ← Configuration
├── 📦 requirements.txt        ← Dependencies
├── 🔒 .env.example            ← Credentials template
├── 🚫 .gitignore              ← Git ignore rules
├── 📜 LICENSE                 ← MIT License
│
├── 🔧 setup.sh                ← Setup script
├── 🧪 test_setup.py           ← Test your setup
├── 📊 leads_example.json      ← Example output
│
└── .github/workflows/
    └── scheduled_scan.yml     ← GitHub Actions automation
```

## Quick Start (3 Steps) 🚀

### Step 1: Get Reddit Credentials (2 min)
1. Go to https://www.reddit.com/prefs/apps
2. Click "create another app..."
3. Fill in:
   - Name: `TradingWizard Lead Finder`
   - Type: Select **"script"**
   - Redirect URI: `http://localhost:8080`
4. Click "create app"
5. Copy your `client_id` and `client_secret`

### Step 2: Setup (2 min)
```bash
# Install dependencies
pip install -r requirements.txt

# Configure credentials
cp .env.example .env
# Edit .env and paste your Reddit credentials

# Test setup
python test_setup.py
```

### Step 3: Run (1 min)
```bash
python main.py
```

Results saved to `leads.json` ✨

## What Happens When You Run It? 🤔

1. **Searches** 10+ trading subreddits for relevant posts
2. **Scores** each opportunity (0-100 relevance)
3. **Filters** out low-quality and risky opportunities
4. **Generates** 2 reply variants for each lead (helpful + soft pitch)
5. **Outputs** JSON file with top 25 opportunities

## Example Output 📊

```json
{
  "url": "https://reddit.com/r/algotrading/...",
  "title": "Looking for AI chart analysis tools",
  "relevance_score": 85,
  "intent_label": "Tool-seeking",
  "reply_drafts": [
    {
      "variant": "A",
      "reply_text": "Start by defining your edge: timeframe, markets, and setup type. Map key S/R levels, confirm with momentum indicators like RSI or MACD... If you want a quick AI breakdown, try TradingWizard.ai's Chart Analyzer."
    }
  ]
}
```

## Next Steps 🎯

Choose your path:

### 🏃 Fast Track (Get Running Now)
→ Read **QUICK_START.md**  
→ 5 minutes to first results

### 📚 Deep Dive (Understand Everything)
→ Read **README.md**  
→ Full documentation and options

### 🚀 Deploy to Production
→ Read **PROJECT_SUMMARY.md**  
→ GitHub Actions, scheduling, scaling

### 🏗️ Understand the System
→ Read **ARCHITECTURE.md**  
→ How it works under the hood

## Pro Tips 💡

1. **Start Small**: Test with 1-2 subreddits first
2. **Review First**: Always read replies before posting
3. **Customize**: Edit reply drafts to match your voice
4. **Track Results**: Note what gets engagement
5. **Be Patient**: Quality over quantity wins on Reddit

## Key Features Explained 🔑

### Relevance Scoring (0-100)
- **90-100**: Perfect fit, post immediately
- **80-89**: Very relevant, high priority
- **70-79**: Good match, worth customizing
- **60-69**: Decent, but review carefully
- **<60**: Filtered out automatically

### Risk Flags
- ⚠️  "self-promo restricted" = No links in this subreddit
- ⚠️  "vendor-banned" = Don't post here
- ⚠️  "low-quality thread" = Skip this one

### Reply Philosophy
- **50% Value**: Concrete tips, actionable advice
- **50% Pitch**: Soft mention of TradingWizard
- **Zero Hype**: No buzzwords or guarantees
- **Disclosure**: Light disclosure when appropriate

## Automation Options 🤖

### Option 1: GitHub Actions (Free, Recommended)
- Push code to GitHub
- Add Reddit credentials to Secrets
- Runs daily automatically
- No server needed!

### Option 2: Local Cron Job
```bash
crontab -e
0 9 * * * cd /path/to/reddit_lead_finder && python3 main.py
```

### Option 3: Cloud (AWS Lambda, etc.)
- Deploy as serverless function
- Trigger on schedule
- Scale as needed

## Customization Quick Reference ⚙️

### Change Keywords
Edit `config.json`:
```json
{
  "keywords_core": ["AI trading", "chart analyzer", "algo bot"]
}
```

### Target Specific Subreddits
```json
{
  "allowlist_subs": ["algotrading", "daytrading", "forex"]
}
```

### Adjust Quality Threshold
```json
{
  "relevance_threshold": 70
}
```

### Change Time Range
```json
{
  "date_range_days": 3
}
```

## Troubleshooting 🔧

**"No results found"**
- Lower `relevance_threshold` to 50
- Increase `date_range_days` to 14
- Check if keywords are too specific

**"Invalid credentials"**
- Verify `client_id` and `client_secret` in `.env`
- Remove any quotes or spaces
- Ensure Reddit app is type "script"

**"Rate limit error"**
- Reddit API: 60 requests/minute
- Wait 1 minute and retry
- Reduce number of subreddits

## Support & Resources 📚

- **Reddit API Docs**: https://www.reddit.com/dev/api
- **PRAW Docs**: https://praw.readthedocs.io
- **Questions?**: Open an issue on GitHub

## Success Checklist ✅

- [ ] Got Reddit API credentials
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Configured `.env` file
- [ ] Ran test (`python test_setup.py` passes)
- [ ] First scan complete (`python main.py`)
- [ ] Reviewed output (`leads.json`)
- [ ] Customized keywords (optional)
- [ ] Posted first reply (manually)
- [ ] Set up automation (optional)

## Your First Week 📅

**Day 1**: Setup and first scan  
**Day 2**: Customize keywords and test  
**Day 3**: Post 3-5 replies manually  
**Day 4**: Review engagement  
**Day 5**: Refine approach based on feedback  
**Day 6-7**: Set up automation

## Important Notes ⚠️

1. **Review Before Posting**: Always read threads and replies
2. **Respect Communities**: Follow subreddit rules
3. **Be Helpful**: Provide value first
4. **No Spam**: Quality over quantity
5. **Track Results**: Learn what works

## What Makes This Different? 🌟

Unlike basic Reddit scrapers, this tool:
- ✅ Generates **helpful replies**, not spam
- ✅ Respects **subreddit rules** automatically
- ✅ Uses **multi-factor scoring** for quality
- ✅ Provides **2 reply variants** per opportunity
- ✅ Has **built-in safety** and rate limiting
- ✅ Is **fully documented** and customizable

## Ready? Let's Go! 🚀

1. Open **QUICK_START.md** for step-by-step setup
2. Run your first scan in 5 minutes
3. Start finding opportunities!

---

**Questions?** See README.md or open an issue.

**Want to contribute?** See CONTRIBUTING.md.

**Good hunting!** 🎯

---

*Made for TradingWizard.ai | MIT License*
