#!/usr/bin/env python3
"""
Reddit Lead Finder + Reply Writer for TradingWizard.ai
Discovers relevant Reddit opportunities and drafts helpful, value-first replies.
"""

import praw
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import re
from collections import defaultdict
import time

class RedditLeadFinder:
    def __init__(self, config_path: str = "config.json"):
        """Initialize the Reddit Lead Finder with configuration."""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Initialize Reddit API
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT', 'TradingWizard Lead Finder v1.0')
        )
        
        # Expand keywords automatically
        self.keywords = self._expand_keywords()
        
        # Track replies for rate limiting
        self.reply_tracker = defaultdict(list)
        
    def _expand_keywords(self) -> List[str]:
        """Expand core keywords with variants and intent phrases."""
        core = self.config.get('keywords_core', [])
        
        # Generate expanded keyword list
        expanded = core.copy()
        
        # Add variations and intent phrases
        variations = [
            "best {} for",
            "recommend {}",
            "looking for {}",
            "any good {}",
            "how to find {}",
            "help with {}",
            "{} recommendations",
            "which {} should I use",
            "need {} advice",
            "{} that works",
            "free {}",
            "automated {}",
            "{} tool",
            "{} platform",
            "{} software",
            "{} app",
            "{} service",
            "AI for trading",
            "machine learning trading",
            "trading bot",
            "algo trading tool",
            "chart analysis software",
            "technical indicators tool",
            "backtest platform",
            "trading strategy builder",
            "market scanner tool",
            "stock screener AI",
            "crypto trading bot",
            "forex automation",
            "day trading tools",
            "swing trading analyzer",
            "options scanner",
            "trading signals AI"
        ]
        
        for keyword in core[:3]:  # Apply variations to top keywords only
            for var in variations[:10]:
                if '{}' in var:
                    expanded.append(var.format(keyword))
        
        # Add standalone intent phrases
        intent_phrases = [
            "how do I analyze charts",
            "need trading setup help",
            "automate my trading",
            "find good entry points",
            "technical analysis help",
            "improve my trading strategy",
            "backtest my strategy",
            "trading tool recommendations",
            "alternative to TradingView",
            "AI stock picker"
        ]
        expanded.extend(intent_phrases)
        
        return list(set(expanded))[:50]  # Limit to 50 unique keywords
    
    def _calculate_relevance_score(self, text: str, title: str, subreddit: str, 
                                   created_utc: int, upvotes: int) -> tuple:
        """Calculate relevance score (0-100) based on multiple factors."""
        text_lower = (text + " " + title).lower()
        
        # Intent match (40%)
        intent_patterns = {
            'tool-seeking': r'(recommend|best|looking for|suggest|which|what.*use|any good|need.*tool)',
            'how-to': r'(how to|how do|how can|guide|tutorial|help me|teach)',
            'problem-solving': r'(problem|issue|stuck|struggling|confused|not working|error)',
            'show-and-tell': r'(built|made|created|check out|my.*tool)',
        }
        
        intent_label = "General discussion"
        intent_score = 20
        
        for label, pattern in intent_patterns.items():
            if re.search(pattern, text_lower):
                intent_label = label.title().replace('-', ' ')
                intent_score = 40
                break
        
        # Keyword density (20%)
        matched_keywords = []
        keyword_score = 0
        for keyword in self.keywords:
            if keyword.lower() in text_lower:
                matched_keywords.append(keyword)
                keyword_score += 2
        keyword_score = min(keyword_score, 20)
        
        # Context fit for TradingWizard features (25%)
        feature_keywords = ['chart', 'technical analysis', 'AI', 'automat', 'algo', 
                          'signal', 'backtest', 'scan', 'indicator', 'strategy']
        context_score = sum(5 for kw in feature_keywords if kw in text_lower)
        context_score = min(context_score, 25)
        
        # Freshness (10%)
        age_days = (time.time() - created_utc) / 86400
        if age_days < 1:
            freshness_score = 10
        elif age_days < 3:
            freshness_score = 7
        elif age_days < 7:
            freshness_score = 5
        else:
            freshness_score = 0
        
        # Subreddit quality (5%)
        quality_subs = ['algotrading', 'trading', 'daytrading', 'stocks', 'investing', 
                       'wallstreetbets', 'forex', 'cryptocurrency', 'bitcoin']
        subreddit_score = 5 if any(sub in subreddit.lower() for sub in quality_subs) else 3
        
        total_score = intent_score + keyword_score + context_score + freshness_score + subreddit_score
        
        return total_score, intent_label, matched_keywords
    
    def _assess_risks(self, subreddit: str, text: str) -> List[str]:
        """Identify risk flags for the opportunity."""
        risks = []
        
        # Check for self-promo restrictions (simplified - should check actual rules)
        strict_subs = ['wallstreetbets', 'investing', 'stocks']
        if any(sub in subreddit.lower() for sub in strict_subs):
            risks.append("self-promo restricted")
        
        # Check for low-quality signals
        spam_indicators = ['giveaway', 'free money', 'guaranteed', '100% win', 'get rich']
        if any(indicator in text.lower() for indicator in spam_indicators):
            risks.append("low-quality thread")
        
        # Check for off-topic
        political_keywords = ['biden', 'trump', 'election', 'democrat', 'republican']
        if any(kw in text.lower() for kw in political_keywords):
            risks.append("off-topic")
        
        return risks
    
    def _generate_reply_drafts(self, context: str, intent_label: str, 
                              include_link: bool) -> List[Dict[str, str]]:
        """Generate helpful, value-first reply variants."""
        
        # Value-first content library
        helpful_tips = {
            'Tool-seeking': [
                "Start by defining your edge: timeframe, markets, and setup type. Map key S/R levels, confirm with momentum indicators like RSI or MACD, and always set an invalidation point.",
                "Build a simple checklist first: identify trend, mark zones, wait for confirmation, size position, set stops. Keep it mechanical so emotions don't override your process.",
            ],
            'How-to': [
                "Break it into steps: 1) Define what you're analyzing (trend, breakout, reversal), 2) Overlay your key levels, 3) Add 1-2 confirmation indicators, 4) Document your setup rules.",
                "Start simple: use price action + volume first, then add one indicator at a time. Most profitable setups don't need 10 indicators cluttering the chart.",
            ],
            'Problem-solving': [
                "If you're getting whipsawed, try adding an ATR filter—only trade when volatility exceeds your threshold. Also, check if you're trading during choppy market hours.",
                "Common issue: too many indicators giving conflicting signals. Strip it down to price action, volume, and one momentum indicator. Keep your edge simple and repeatable.",
            ],
            'Show-and-tell': [
                "Nice work! The key to making tools stick is iteration—track what's working in a journal and refine your rules based on real results.",
                "Looks solid. If you want to level it up, consider adding a backtesting layer so you can validate edge before going live.",
            ],
            'General discussion': [
                "For consistent results, focus on repeatability: document your setups, track your stats, and refine what's actually profitable vs what just feels good.",
                "The best edge is often the simplest one you'll actually follow. Start with a core setup, master it, then expand.",
            ]
        }
        
        # Soft CTAs
        ctas_with_link = [
            " If you want a quick AI breakdown of your chart, you can try TradingWizard.ai's Chart Analyzer—just upload a screenshot and it gives you a structured setup.",
            " We built TradingWizard.ai for exactly this—AI-powered chart analysis, algo bots, and daily market scans. Free to try, no card needed.",
            " I work on TradingWizard.ai where we automate a lot of this (chart analysis, signals, backtests). Happy to point you there if you want the AI to handle the heavy lifting.",
        ]
        
        ctas_no_link = [
            " Tools that automate chart reading and setup identification can help speed this up significantly.",
            " There are platforms now that use AI to handle chart analysis and generate trade setups if you want to explore that route.",
        ]
        
        # Generate 2 variants
        variants = []
        tips = helpful_tips.get(intent_label, helpful_tips['General discussion'])
        
        for i, tip in enumerate(tips[:2]):
            cta = (ctas_with_link if include_link else ctas_no_link)[i % len(ctas_with_link if include_link else ctas_no_link)]
            
            # Add optional disclosure
            disclosure = " (Disclosure: I help build TradingWizard.ai)" if include_link and i == 0 else ""
            
            reply_text = tip + cta + disclosure
            
            variants.append({
                'variant': chr(65 + i),  # A, B
                'reply_text': reply_text
            })
        
        return variants
    
    def search_reddit(self, date_range_days: int = 7, limit: int = 25) -> List[Dict]:
        """Search Reddit for relevant opportunities."""
        results = []
        cutoff_time = time.time() - (date_range_days * 86400)
        
        # Determine subreddits to search
        allowlist = self.config.get('allowlist_subs', [])
        blocklist = self.config.get('blocklist_subs', [])
        
        if allowlist:
            subreddits_to_search = allowlist
        else:
            # Default trading subreddits
            subreddits_to_search = [
                'algotrading', 'trading', 'daytrading', 'stocks', 'investing',
                'options', 'forex', 'cryptocurrency', 'bitcointrading'
            ]
        
        # Filter out blocklist
        subreddits_to_search = [s for s in subreddits_to_search if s not in blocklist]
        
        # Search each subreddit
        for subreddit_name in subreddits_to_search:
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                
                # Search with top keywords
                for keyword in self.keywords[:10]:  # Use top 10 keywords
                    try:
                        for submission in subreddit.search(keyword, time_filter='week', limit=10):
                            if submission.created_utc < cutoff_time:
                                continue
                            
                            # Check minimum requirements
                            if submission.score < 3:
                                continue
                            
                            # Calculate relevance
                            score, intent, matched = self._calculate_relevance_score(
                                submission.selftext,
                                submission.title,
                                subreddit_name,
                                submission.created_utc,
                                submission.score
                            )
                            
                            # Filter by minimum score
                            if score < 60:
                                continue
                            
                            # Assess risks
                            risks = self._assess_risks(subreddit_name, 
                                                      submission.title + " " + submission.selftext)
                            
                            # Skip if hard risk flags
                            hard_risks = ["vendor-banned", "low-quality thread"]
                            if any(r in risks for r in hard_risks):
                                continue
                            
                            # Determine if we should include link
                            include_link = "self-promo restricted" not in risks
                            
                            # Generate reply drafts
                            reply_drafts = self._generate_reply_drafts(
                                submission.selftext[:500],
                                intent,
                                include_link
                            )
                            
                            # Create result entry
                            result = {
                                'url': f"https://reddit.com{submission.permalink}",
                                'type': 'post',
                                'subreddit': f"r/{subreddit_name}",
                                'title': submission.title,
                                'author': f"u/{submission.author.name if submission.author else '[deleted]'}",
                                'created_utc': datetime.fromtimestamp(submission.created_utc).isoformat(),
                                'upvotes': submission.score,
                                'matched_keywords': matched[:5],
                                'intent_label': intent,
                                'relevance_score': score,
                                'fit_reasons': [
                                    f"Strong {intent.lower()} intent signal",
                                    f"Matched {len(matched)} relevant keywords",
                                    f"Posted {int((time.time() - submission.created_utc) / 86400)} days ago"
                                ],
                                'risk_flags': risks,
                                'reply_drafts': reply_drafts,
                                'reply_notes': f"Natural entry point with {intent.lower()} context. " + 
                                             ("Link included as value-add." if include_link else "No link due to sub rules; value-only approach."),
                                'include_link': include_link
                            }
                            
                            results.append(result)
                            
                    except Exception as e:
                        print(f"Error searching keyword '{keyword}' in r/{subreddit_name}: {e}")
                        continue
                        
            except Exception as e:
                print(f"Error accessing r/{subreddit_name}: {e}")
                continue
        
        # Sort by relevance score and return top results
        results.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        # Deduplicate by URL
        seen_urls = set()
        unique_results = []
        for result in results:
            if result['url'] not in seen_urls:
                seen_urls.add(result['url'])
                unique_results.append(result)
        
        return unique_results[:limit]
    
    def run(self, output_file: str = 'leads.json'):
        """Run the lead finder and save results."""
        print("🔍 Starting Reddit Lead Finder for TradingWizard.ai...")
        print(f"📊 Searching with {len(self.keywords)} keywords...")
        
        results = self.search_reddit()
        
        print(f"✅ Found {len(results)} qualified opportunities")
        
        # Save to JSON
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"💾 Results saved to {output_file}")
        
        return results


if __name__ == "__main__":
    finder = RedditLeadFinder()
    finder.run()
