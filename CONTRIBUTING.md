# Contributing to Reddit Lead Finder

Thank you for considering contributing to the Reddit Lead Finder! 🎉

## How to Contribute

### Reporting Bugs 🐛

If you find a bug, please open an issue with:
- A clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Relevant logs or error messages

### Suggesting Features 💡

We welcome feature suggestions! Please open an issue with:
- Clear use case and motivation
- Proposed implementation (if you have ideas)
- Examples of how it would work

### Pull Requests 🔧

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**: `git commit -m 'Add amazing feature'`
6. **Push to your fork**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/reddit-lead-finder.git
cd reddit-lead-finder

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Reddit credentials

# Run the script
python main.py
```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and under 50 lines when possible
- Add comments for complex logic

## Testing

Before submitting a PR:
- Test with various subreddits and keywords
- Verify JSON output format is correct
- Check edge cases (empty results, API errors, etc.)
- Ensure no sensitive data is logged

## Areas for Contribution

We'd especially appreciate help with:

### High Priority
- [ ] Sentiment analysis for better relevance scoring
- [ ] Multi-language support (especially Swedish)
- [ ] Better duplicate detection
- [ ] Unit tests and integration tests
- [ ] Error handling improvements

### Medium Priority
- [ ] CRM integrations (HubSpot, Salesforce)
- [ ] Slack/Discord notifications
- [ ] Web dashboard for reviewing leads
- [ ] Reply tracking and analytics
- [ ] A/B testing for reply variants

### Nice to Have
- [ ] ML-based reply generation using Claude/GPT
- [ ] Chrome extension for quick posting
- [ ] Real-time monitoring mode
- [ ] Subreddit rule auto-detection
- [ ] Reply performance tracking

## Reply Quality Guidelines

When contributing reply templates or generation logic:

1. **Help First**: 50%+ of content should be actionable advice
2. **No Hype**: Avoid buzzwords, guarantees, or overpromising
3. **Conversational**: Write like a helpful human, not a bot
4. **Specific**: Include concrete steps, checklists, or examples
5. **Contextual**: Adapt tone to subreddit culture
6. **Honest**: Include light disclosure when mentioning TradingWizard
7. **Value-Aligned**: Respect subreddit rules and community norms

### Good Reply Example ✅
```
If you're getting whipsawed, try adding an ATR filter—only trade when 
volatility exceeds your threshold. Also check if you're trading during 
choppy market hours. If you want an AI breakdown of your charts, 
TradingWizard.ai's Chart Analyzer can help (disclosure: I work on it).
```

### Bad Reply Example ❌
```
🚀 Check out TradingWizard.ai! Best AI trading tool on the market! 
Guaranteed profits! 💰 Click here now! [link]
```

## Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues: "Fix #123: Resolve API timeout issue"

Examples:
```
Add sentiment analysis to relevance scoring
Fix JSON output formatting for nested quotes
Update README with Swedish language support
Refactor reply generation for better readability
```

## Review Process

1. A maintainer will review your PR within 5 business days
2. Address any requested changes
3. Once approved, a maintainer will merge
4. Your contribution will be credited in the release notes!

## Code of Conduct

- Be respectful and constructive
- Focus on the issue, not the person
- Welcome newcomers and help them learn
- Give credit where credit is due
- Follow Reddit's Terms of Service in all examples

## Questions?

Open an issue with the "question" label or reach out to the TradingWizard team.

---

Thank you for contributing! 🙏
