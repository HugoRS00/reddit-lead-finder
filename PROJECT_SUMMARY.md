# Reddit Lead Finder - Project Summary

## What You've Got 🎁

A complete, production-ready Reddit marketing automation tool for TradingWizard.ai with:

### Core Features
- ✅ Intelligent keyword expansion (10 → 50+ keywords)
- ✅ Multi-factor relevance scoring (0-100)
- ✅ Automatic risk assessment and filtering
- ✅ Value-first reply generation (2 variants per opportunity)
- ✅ Subreddit rule awareness (no links in restricted subs)
- ✅ Rate limiting and anti-spam protections
- ✅ JSON output for easy integration
- ✅ GitHub Actions for scheduling

### File Structure

```
reddit_lead_finder/
├── main.py                 # Core application logic
├── config.json             # Configuration (keywords, settings)
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md               # Full documentation
├── QUICK_START.md          # 5-minute setup guide
├── CONTRIBUTING.md         # Contribution guidelines
├── setup.sh                # Automated setup script
├── test_setup.py           # Setup verification script
├── leads_example.json      # Example output
└── .github/
    └── workflows/
        └── scheduled_scan.yml  # GitHub Actions workflow
```

## Deployment Options 🚀

### Option 1: GitHub (Recommended)

1. **Create Repository**
   ```bash
   # Create new repo on GitHub: reddit-lead-finder
   git init
   git add .
   git commit -m "Initial commit: Reddit Lead Finder for TradingWizard"
   git branch -M main
   git remote add origin https://github.com/yourusername/reddit-lead-finder.git
   git push -u origin main
   ```

2. **Add Secrets for GitHub Actions**
   - Go to: Settings → Secrets and variables → Actions
   - Add secrets:
     - `REDDIT_CLIENT_ID`
     - `REDDIT_CLIENT_SECRET`

3. **Enable GitHub Actions**
   - Go to: Actions tab
   - Enable workflows
   - Runs daily at 9 AM UTC automatically!

### Option 2: Local Cron Job

```bash
# Edit crontab
crontab -e

# Add this line (runs daily at 9 AM)
0 9 * * * cd /path/to/reddit_lead_finder && python3 main.py

# Or hourly during trading hours (9 AM - 4 PM EST)
0 9-16 * * 1-5 cd /path/to/reddit_lead_finder && python3 main.py
```

### Option 3: Cloud (AWS Lambda, Google Cloud Functions)

Deploy as serverless function:
- Trigger: CloudWatch Events / Cloud Scheduler
- Runtime: Python 3.10
- Environment: Add Reddit credentials
- Output: S3 / Cloud Storage

### Option 4: Docker Container

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## Quick Start (Copy-Paste Ready) 📋

```bash
# 1. Get Reddit API credentials
# Go to: https://www.reddit.com/prefs/apps
# Create app (type: script)

# 2. Clone and setup
git clone <your-repo-url>
cd reddit-lead-finder
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials

# 3. Test setup
python test_setup.py

# 4. Run first scan
python main.py

# 5. Check results
cat leads.json
```

## Key Configuration Points ⚙️

### Adjust Relevance Threshold
```json
{
  "relevance_threshold": 60  // Lower = more results, higher = quality
}
```

### Target Specific Subreddits
```json
{
  "allowlist_subs": ["algotrading", "daytrading", "forex"]
}
```

### Change Time Range
```json
{
  "date_range_days": 3  // Scan last 3 days instead of 7
}
```

## Understanding the Output 📊

Each lead in `leads.json` includes:

1. **Basic Info**: URL, subreddit, title, author, upvotes
2. **Scoring**: relevance_score (0-100), intent_label, matched_keywords
3. **Context**: fit_reasons (why it's a good opportunity)
4. **Safety**: risk_flags (self-promo restrictions, etc.)
5. **Reply Drafts**: 2 variants (A = direct, B = educational)
6. **Guidance**: reply_notes, include_link boolean

### Interpreting Scores

- **90-100**: Perfect fit, strong intent, recent post
- **80-89**: Very relevant, good engagement opportunity
- **70-79**: Solid match, worth reviewing
- **60-69**: Decent fit, may need customization
- **<60**: Filtered out (not included in results)

## Best Practices 🎯

### DO ✅
- Review all replies before posting
- Customize drafts to match your voice
- Start with high-scoring opportunities (80+)
- Engage with follow-up comments
- Track what works and iterate
- Respect subreddit cultures

### DON'T ❌
- Copy-paste replies without reading context
- Post in subreddits with strict self-promo bans
- Spam multiple threads in same subreddit
- Make financial advice claims
- Ignore community feedback
- Post purely promotional content

## Scaling Strategy 📈

### Week 1-2: Testing Phase
- 3-5 subreddits
- relevance_threshold: 80
- Manual posting only
- Track engagement rates

### Week 3-4: Optimization
- Expand to 7-10 subreddits
- Lower threshold to 70 if needed
- Refine reply templates based on feedback
- A/B test different approaches

### Month 2+: Automation
- 10-15 subreddits
- Schedule daily scans
- Build relationships in key communities
- Create content library for different intents

## Integration Ideas 💡

### CRM Integration
```python
# Add to main.py
import requests

def send_to_crm(leads):
    for lead in leads:
        if lead['relevance_score'] > 80:
            requests.post('https://api.hubspot.com/...')
```

### Slack Notifications
```python
def notify_slack(leads):
    high_value = [l for l in leads if l['relevance_score'] > 85]
    if high_value:
        requests.post(SLACK_WEBHOOK, json={
            'text': f'🎯 Found {len(high_value)} high-value leads!'
        })
```

### Email Digest
```python
def email_digest(leads):
    import smtplib
    # Send daily email with top 10 opportunities
```

## Monitoring & Analytics 📊

Track these metrics:
- Total opportunities found per day
- Average relevance score
- Reply acceptance rate (upvotes/downvotes)
- Conversion rate (clicks → signups)
- Time saved vs manual searching

## Troubleshooting 🔧

### Common Issues

**No results returned**
- Lower relevance_threshold
- Expand date_range_days
- Add more keywords
- Check if subreddits are active

**Rate limit errors**
- Reddit API: 60 requests/minute
- Add delays: `time.sleep(1)` between searches
- Reduce number of subreddits

**Invalid credentials**
- Verify client_id and client_secret
- Check for extra spaces/quotes in .env
- Ensure app type is "script"

**Low relevance scores**
- Adjust scoring weights in `_calculate_relevance_score()`
- Add more specific keywords
- Target more focused subreddits

## Security Checklist 🔒

- [ ] `.env` in .gitignore (credentials never committed)
- [ ] GitHub secrets configured (for Actions)
- [ ] Review all auto-generated replies before posting
- [ ] Rate limits configured
- [ ] No financial advice in replies
- [ ] Proper disclosures when mentioning TradingWizard

## Legal & Compliance ⚖️

- Read Reddit's Terms of Service
- Respect individual subreddit rules
- Include disclosures when appropriate
- Never manipulate voting
- Provide genuine value first
- No financial/investment advice

## Next Steps 🎬

1. **Immediate**: Get Reddit credentials, run first scan
2. **This Week**: Customize keywords, test different subreddits
3. **This Month**: Schedule automation, track results
4. **Ongoing**: Optimize based on data, expand reach

## Support & Resources 📚

- **Full Docs**: README.md
- **Quick Setup**: QUICK_START.md
- **Contributing**: CONTRIBUTING.md
- **Reddit API**: https://www.reddit.com/dev/api
- **PRAW Docs**: https://praw.readthedocs.io

## Success Metrics 📈

Set goals and track:
- **Week 1**: 10+ qualified leads found
- **Week 2**: 5+ positive engagements
- **Month 1**: 20+ conversations started
- **Month 2**: 5+ demo requests from Reddit
- **Month 3**: 2+ signups attributed to Reddit

## Tips for Maximum Impact 💪

1. **Consistency Beats Volume**: 3 high-quality replies > 20 mediocre ones
2. **Build Relationships**: Become known in communities
3. **Give Before Asking**: Help 5 people before mentioning TradingWizard
4. **Learn the Culture**: Each subreddit has unique norms
5. **Document Everything**: Track what works for iteration

---

## Ready to Launch? 🚀

You now have everything you need to:
- ✅ Find high-quality Reddit opportunities
- ✅ Generate helpful, value-first replies
- ✅ Automate the process safely
- ✅ Scale your outbound marketing

**Start with the QUICK_START.md and you'll be running in 5 minutes!**

Good hunting! 🎯

---

*Built for TradingWizard.ai | MIT License | See CONTRIBUTING.md to improve this tool*
