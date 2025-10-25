# Reddit Lead Finder - System Architecture

## High-Level Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Reddit Lead Finder                            │
│                   for TradingWizard.ai                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   1. KEYWORD EXPANSION                │
        │   10 core → 50+ variations            │
        │   + intent phrases                     │
        └──────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   2. REDDIT API SEARCH                │
        │   - Multiple subreddits               │
        │   - Last 7 days                       │
        │   - Posts + Comments                  │
        └──────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   3. RELEVANCE SCORING (0-100)        │
        │   ├─ Intent Match (40%)               │
        │   ├─ Keyword Density (20%)            │
        │   ├─ Context Fit (25%)                │
        │   ├─ Freshness (10%)                  │
        │   └─ Subreddit Quality (5%)           │
        └──────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   4. RISK ASSESSMENT                  │
        │   - Self-promo restrictions           │
        │   - Low-quality signals               │
        │   - Off-topic content                 │
        │   - Vendor bans                       │
        └──────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   5. FILTER & RANK                    │
        │   - Minimum score: 60                 │
        │   - Remove hard risks                 │
        │   - Deduplicate                       │
        │   - Sort by relevance                 │
        └──────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   6. REPLY GENERATION                 │
        │   - Variant A (Direct + Helpful)      │
        │   - Variant B (Educational + Soft)    │
        │   - Context-aware CTAs                │
        │   - Disclosure when needed            │
        └──────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────┐
        │   7. JSON OUTPUT                      │
        │   Top 25 opportunities                │
        │   Ready for manual review             │
        └──────────────────────────────────────┘
```

## Detailed Component Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        INPUT LAYER                               │
├─────────────────────────────────────────────────────────────────┤
│  config.json          .env                Reddit API             │
│  ├─ keywords_core     ├─ CLIENT_ID       ├─ Search              │
│  ├─ allowlist_subs    ├─ CLIENT_SECRET   ├─ Fetch Posts         │
│  ├─ blocklist_subs    └─ USER_AGENT      └─ Rate Limits         │
│  ├─ date_range                                                   │
│  └─ thresholds                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PROCESSING LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐ │
│  │ KeywordExpander  │→ │  RedditSearcher  │→ │ RelevanceScore││ │
│  │                  │  │                  │  │               │ │
│  │ • Pattern match  │  │ • Multi-sub      │  │ • Intent      │ │
│  │ • Intent phrases │  │ • Time filter    │  │ • Keywords    │ │
│  │ • Variations     │  │ • Dedup          │  │ • Context     │ │
│  └──────────────────┘  └──────────────────┘  │ • Freshness   │ │
│                                               │ • Quality     │ │
│                                               └───────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐ │
│  │  RiskAssessor    │→ │   ReplyDrafter   │→ │  JSONExporter ││ │
│  │                  │  │                  │  │               │ │
│  │ • Rule check     │  │ • Value tips     │  │ • Format      │ │
│  │ • Spam detect    │  │ • Soft CTA       │  │ • Validate    │ │
│  │ • Quality gate   │  │ • Disclosure     │  │ • Save        │ │
│  └──────────────────┘  └──────────────────┘  └───────────────┘ │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        OUTPUT LAYER                              │
├─────────────────────────────────────────────────────────────────┤
│  leads.json                                                      │
│  ├─ url                    ├─ reply_drafts                      │
│  ├─ subreddit              │  ├─ variant A                      │
│  ├─ title                  │  └─ variant B                      │
│  ├─ author                 ├─ reply_notes                       │
│  ├─ created_utc            └─ include_link                      │
│  ├─ upvotes                                                      │
│  ├─ matched_keywords       [Optional Integrations]              │
│  ├─ intent_label           ├─ Slack webhook                     │
│  ├─ relevance_score        ├─ Email digest                      │
│  ├─ fit_reasons            ├─ CRM API                           │
│  └─ risk_flags             └─ Dashboard                         │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Example

```
User Request: "Find trading tool opportunities"
     │
     ▼
Keywords: ["AI trading", "chart analyzer"] 
     │
     ▼
Expanded: ["AI trading", "best AI trading bot", "chart analyzer", 
           "technical analysis tool", "recommend trading tools", ...]
     │
     ▼
Reddit Search: r/algotrading, r/trading, r/daytrading
     │
     ▼
Found: 47 posts/comments (last 7 days)
     │
     ▼
Filtered: 23 meet minimum criteria (karma ≥10, upvotes ≥3)
     │
     ▼
Scored: 
  - Post A: 88 (Tool-seeking, "best algo trading platform?")
  - Post B: 75 (How-to, "how to analyze charts efficiently")
  - Post C: 82 (Problem-solving, "my indicators are conflicting")
  - Post D: 55 (General, filtered out - below threshold)
     │
     ▼
Risk Check:
  - Post A: ✅ No risks
  - Post B: ✅ No risks  
  - Post C: ⚠️  Self-promo restricted (r/wallstreetbets)
     │
     ▼
Reply Generation:
  - Post A: 2 variants with link (allowed)
  - Post B: 2 variants with link (allowed)
  - Post C: 2 variants WITHOUT link (restricted sub)
     │
     ▼
Output: leads.json with 3 qualified opportunities
```

## Scoring Formula Breakdown

```
RELEVANCE_SCORE = Intent + Keywords + Context + Fresh + Quality

Intent (40 points):
  ├─ Tool-seeking    → 40 pts  ("recommend", "best", "which")
  ├─ How-to          → 40 pts  ("how to", "guide", "help me")
  ├─ Problem-solving → 40 pts  ("issue", "struggling", "error")
  ├─ Show-and-tell   → 30 pts  ("built", "made", "created")
  └─ General         → 20 pts  (default)

Keywords (20 points):
  ├─ Each match      → +2 pts  (max 20)
  └─ Capped at       → 20 pts

Context (25 points):
  ├─ Feature words   → +5 pts each
  │   (chart, AI, algo, signal, backtest, etc.)
  └─ Capped at       → 25 pts

Freshness (10 points):
  ├─ <1 day          → 10 pts
  ├─ 1-3 days        → 7 pts
  ├─ 3-7 days        → 5 pts
  └─ >7 days         → 0 pts

Quality (5 points):
  ├─ Premium subs    → 5 pts  (algotrading, trading, etc.)
  └─ Other subs      → 3 pts

TOTAL: 0-100 points
THRESHOLD: ≥60 to qualify
```

## Rate Limiting & Safety

```
┌─────────────────────────────────────────┐
│         RATE LIMIT TRACKER              │
├─────────────────────────────────────────┤
│                                          │
│  Per Thread:     Max 1 reply            │
│  Per Subreddit:  Max 3 replies/day      │
│  Per Author:     48-hour cooldown       │
│  API Calls:      60 requests/minute     │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │  Safety Checks:                    │ │
│  │  ✓ Duplicate detection (by URL)    │ │
│  │  ✓ Subreddit rule awareness        │ │
│  │  ✓ No financial advice             │ │
│  │  ✓ Disclosure when needed          │ │
│  │  ✓ Value-first approach (50/50)    │ │
│  └────────────────────────────────────┘ │
│                                          │
└─────────────────────────────────────────┘
```

## Reply Template Structure

```
┌─────────────────────────────────────────────────────────┐
│              REPLY TEMPLATE ANATOMY                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [50%] VALUE-FIRST CONTENT                              │
│  ┌────────────────────────────────────────────────────┐ │
│  │ • Acknowledge their problem/question                │ │
│  │ • Provide actionable tip or mini-checklist          │ │
│  │ • Add concrete example or step-by-step             │ │
│  │ • Show expertise and helpfulness                    │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  [50%] SOFT PITCH                                       │
│  ┌────────────────────────────────────────────────────┐ │
│  │ • Natural transition ("If you want...")            │ │
│  │ • Mention specific feature that solves their need   │ │
│  │ • No hype, no guarantees                           │ │
│  │ • Light disclosure if including link               │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  VARIANTS:                                              │
│  • A: Direct + Helpful                                  │
│  • B: Educational + Contextual                         │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Automation Options

```
┌──────────────────────────────────────────────────────────┐
│               DEPLOYMENT ARCHITECTURE                     │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  Option 1: GitHub Actions (Recommended)                  │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  Schedule: Daily at 9 AM UTC                        │ │
│  │  Trigger:  Cron or manual                           │ │
│  │  Output:   Artifact + optional commit               │ │
│  │  Cost:     FREE (2000 minutes/month)                │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                           │
│  Option 2: Local Cron                                    │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  Schedule: Custom (crontab)                         │ │
│  │  Trigger:  Time-based                               │ │
│  │  Output:   Local leads.json                         │ │
│  │  Cost:     FREE                                     │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                           │
│  Option 3: Cloud Function                                │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  AWS Lambda / GCP Cloud Functions                   │ │
│  │  Schedule: CloudWatch / Cloud Scheduler             │ │
│  │  Output:   S3 / Cloud Storage                       │ │
│  │  Cost:     ~$1-5/month                              │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

## Success Metrics Dashboard

```
┌───────────────────────────────────────────────────────────┐
│                  PERFORMANCE TRACKING                      │
├───────────────────────────────────────────────────────────┤
│                                                            │
│  Discovery Metrics:                                        │
│  ├─ Total opportunities found                             │
│  ├─ Average relevance score                               │
│  ├─ High-value leads (80+)                                │
│  └─ Time saved vs manual search                           │
│                                                            │
│  Engagement Metrics:                                       │
│  ├─ Replies posted                                        │
│  ├─ Upvotes received                                      │
│  ├─ Comments/conversations started                        │
│  └─ Reply acceptance rate                                 │
│                                                            │
│  Conversion Metrics:                                       │
│  ├─ Click-through rate                                    │
│  ├─ Demo requests                                         │
│  ├─ Sign-ups attributed                                   │
│  └─ ROI (value generated vs time invested)                │
│                                                            │
└───────────────────────────────────────────────────────────┘
```

## Technology Stack

```
┌─────────────────────────────────────────┐
│         TECH STACK                      │
├─────────────────────────────────────────┤
│  Language:   Python 3.8+                │
│  API:        Reddit (PRAW 7.7.1)        │
│  Config:     JSON + .env                │
│  Automation: GitHub Actions             │
│  Output:     JSON                       │
│  Testing:    Manual + test_setup.py     │
└─────────────────────────────────────────┘

Dependencies:
├─ praw             → Reddit API wrapper
├─ python-dotenv    → Environment variables
└─ requests         → HTTP (for extensions)
```

---

This architecture is designed for:
✅ **Scalability**: Add more subreddits easily
✅ **Safety**: Built-in rate limiting and risk checks
✅ **Flexibility**: Easy to customize scoring and replies
✅ **Automation**: Multiple deployment options
✅ **Quality**: Value-first approach respects communities

Ready to deploy! 🚀
