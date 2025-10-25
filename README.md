# Reddit Lead Finder for TradingWizard.ai 🎯

An intelligent outbound marketing agent that discovers high-quality Reddit opportunities and generates value-first reply drafts for TradingWizard.ai.

## Features ✨

- **Smart Search**: Automatically expands 10 core keywords into 50+ variations and intent phrases
- **Intelligent Scoring**: Multi-factor relevance scoring (0-100) based on intent, keywords, context, freshness, and subreddit quality
- **Risk Assessment**: Automatically flags self-promo restrictions, low-quality threads, and off-topic content
- **Value-First Replies**: Generates helpful, human-sounding reply drafts with concrete tips before any soft pitch
- **Subreddit Safety**: Respects subreddit rules and adjusts approach accordingly
- **Rate Limiting**: Built-in safeguards to prevent spam (1 reply/thread, 3/subreddit/day, 48hr author cooldown)
- **JSON Output**: Clean, structured data ready for CRM integration or manual review

## Quick Start 🚀

### 1. Prerequisites

- Python 3.8+
- Reddit API credentials (free)

### 2. Get Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Fill in:
   - **Name**: TradingWizard Lead Finder
   - **Type**: Script
   - **Description**: Lead finder for TradingWizard.ai
   - **Redirect URI**: http://localhost:8080 (doesn't matter for scripts)
4. Copy your **client_id** (under the app name) and **client_secret**

### 3. Installation

```bash
# Clone or download this repository
git clone https://github.com/yourusername/reddit-lead-finder.git
cd reddit-lead-finder

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your Reddit credentials
```

### 4. Configure

Edit `config.json` to customize:

```json
{
  "keywords_core": [
    "AI trading",
    "chart analyzer",
    "technical analysis tool",
    ...
  ],
  "allowlist_subs": [],  // Leave empty to search default trading subs
  "blocklist_subs": ["politics", "memes"],
  "date_range_days": 7,
  "relevance_threshold": 60,
  "max_results": 25
}
```

### 5. Run

```bash
python main.py
```

Output will be saved to `leads.json`.

## Usage Examples 📖

### Basic Usage

```bash
python main.py
```

This will:
1. Search default trading subreddits (algotrading, trading, daytrading, stocks, etc.)
2. Use last 7 days of posts
3. Return top 25 opportunities by relevance score
4. Save results to `leads.json`

### Custom Subreddit List

Edit `config.json`:

```json
{
  "allowlist_subs": ["algotrading", "StockMarket", "forex"]
}
```

### Adjust Time Range

Edit `config.json`:

```json
{
  "date_range_days": 3  // Last 3 days only
}
```

## Output Format 📊

The script generates a JSON array with this structure:

```json
[
  {
    "url": "https://reddit.com/r/algotrading/comments/...",
    "type": "post",
    "subreddit": "r/algotrading",
    "title": "Looking for AI-powered chart analysis tools",
    "author": "u/trader123",
    "created_utc": "2025-10-20T14:30:00",
    "upvotes": 15,
    "matched_keywords": ["AI", "chart analysis", "tools"],
    "intent_label": "Tool-seeking",
    "relevance_score": 85,
    "fit_reasons": [
      "Strong tool-seeking intent signal",
      "Matched 8 relevant keywords",
      "Posted 2 days ago"
    ],
    "risk_flags": [],
    "reply_drafts": [
      {
        "variant": "A",
        "reply_text": "Start by defining your edge: timeframe, markets, and setup type. Map key S/R levels, confirm with momentum indicators like RSI or MACD, and always set an invalidation point. If you want a quick AI breakdown of your chart, you can try TradingWizard.ai's Chart Analyzer—just upload a screenshot and it gives you a structured setup. (Disclosure: I help build TradingWizard.ai)"
      },
      {
        "variant": "B",
        "reply_text": "Build a simple checklist first: identify trend, mark zones, wait for confirmation, size position, set stops. Keep it mechanical so emotions don't override your process. We built TradingWizard.ai for exactly this—AI-powered chart analysis, algo bots, and daily market scans. Free to try, no card needed."
      }
    ],
    "reply_notes": "Natural entry point with tool-seeking context. Link included as value-add.",
    "include_link": true
  }
]
```

## Scoring System 🎯

Each opportunity is scored 0-100 based on:

| Factor | Weight | Description |
|--------|--------|-------------|
| Intent Match | 40% | Tool-seeking, how-to, problem-solving signals |
| Keyword Density | 20% | Number of matched keywords |
| Context Fit | 25% | Relevance to TradingWizard features |
| Freshness | 10% | How recent the post is |
| Subreddit Quality | 5% | Quality/relevance of subreddit |

**Minimum threshold**: 60 (configurable)

## Reply Philosophy 💡

Replies follow the **Help First, Pitch Second** approach:

1. **50% Value**: Concrete tips, mini-playbooks, actionable advice
2. **50% Soft Sell**: Natural mention of TradingWizard with CTA
3. **Disclosure**: Light disclosure when including links
4. **Zero Hype**: No buzzwords, no guarantees, no financial advice
5. **Respect Rules**: Omits links if self-promo is restricted

### Example Reply Variants

**Variant A** (Direct + Helpful):
> "If you're getting whipsawed, try adding an ATR filter—only trade when volatility exceeds your threshold. Also, check if you're trading during choppy market hours. If you want a quick AI breakdown of your chart, you can try TradingWizard.ai's Chart Analyzer—just upload a screenshot and it gives you a structured setup."

**Variant B** (Educational + Soft):
> "Common issue: too many indicators giving conflicting signals. Strip it down to price action, volume, and one momentum indicator. Keep your edge simple and repeatable. We built TradingWizard.ai for exactly this—AI-powered chart analysis, algo bots, and daily market scans. Free to try, no card needed."

## Rate Limits & Safety 🛡️

Built-in protections to prevent spam:

- **Max 1 reply per thread**
- **Max 3 replies per subreddit per day**
- **48-hour cooldown per author**
- **Automatic deduplication** by URL
- **Risk flagging** for restricted subreddits

*Note: Current version does not auto-post. Review and post manually for safety.*

## Scheduling (GitHub Actions) ⏰

To run automatically:

1. Fork this repository
2. Add Reddit credentials to GitHub Secrets:
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`
3. The included workflow runs daily at 9 AM UTC
4. Check the Actions tab for results

Edit `.github/workflows/scheduled_scan.yml` to change schedule.

## Advanced Configuration ⚙️

### Customize Keywords

The script auto-expands your core keywords. You can also manually add expanded keywords:

```json
{
  "keywords_core": [
    "AI trading",
    "chart analyzer"
  ],
  "keywords_expanded": [
    "best AI trading bot",
    "automated chart analysis",
    "technical analysis automation"
  ]
}
```

### Adjust Scoring Weights

To change how opportunities are scored, edit the `_calculate_relevance_score` method in `main.py`.

### Add Custom Reply Templates

Edit the `helpful_tips` dictionary in `_generate_reply_drafts` method to add your own templates.

## Compliance & Ethics ⚖️

This tool is designed to:

- ✅ Provide genuine value before pitching
- ✅ Respect subreddit rules and norms
- ✅ Include light disclosures when appropriate
- ✅ Avoid spam through rate limiting
- ✅ Never guarantee results or provide financial advice

**Important**: Always manually review replies before posting. Reddit communities value authenticity—use this tool to find opportunities and inspire helpful responses, not to spam.

## Troubleshooting 🔧

### "Invalid credentials" error
- Double-check your `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` in `.env`
- Ensure there are no extra spaces or quotes

### "No results found"
- Try broadening your keywords
- Lower the `relevance_threshold` in config.json
- Increase `date_range_days`

### Rate limit errors
- Reddit API has rate limits (60 requests/minute)
- Script includes automatic retry logic
- If persistent, reduce search scope

## Contributing 🤝

Contributions welcome! Areas for improvement:

- Sentiment analysis for better scoring
- ML-based reply generation
- Multi-language support
- CRM integrations (HubSpot, Salesforce)
- Slack/Discord notifications

## License 📄

MIT License - See LICENSE file for details

## Disclaimer ⚠️

This tool is for finding marketing opportunities. You are responsible for:
- Following Reddit's Terms of Service
- Respecting individual subreddit rules
- Ensuring your replies provide genuine value
- Not engaging in spam or manipulation

**Trading Disclaimer**: TradingWizard.ai and this tool do not provide financial advice. Trading involves risk. Always do your own research.

---

Made with ❤️ for TradingWizard.ai

For questions or support, open an issue or contact the TradingWizard team.
