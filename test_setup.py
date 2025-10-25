#!/usr/bin/env python3
"""
Test script to verify Reddit Lead Finder setup
"""

import os
import sys
import json

def check_dependencies():
    """Check if required packages are installed."""
    print("🔍 Checking dependencies...")
    required = ['praw', 'dotenv', 'requests']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} (missing)")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies installed\n")
    return True

def check_config():
    """Check if config.json exists and is valid."""
    print("🔍 Checking configuration...")
    
    if not os.path.exists('config.json'):
        print("  ❌ config.json not found")
        return False
    
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        required_keys = ['keywords_core', 'date_range_days', 'relevance_threshold']
        for key in required_keys:
            if key in config:
                print(f"  ✅ {key}")
            else:
                print(f"  ❌ {key} (missing)")
                return False
        
        print("✅ Configuration valid\n")
        return True
    except json.JSONDecodeError:
        print("  ❌ config.json is not valid JSON")
        return False

def check_credentials():
    """Check if Reddit API credentials are set."""
    print("🔍 Checking Reddit API credentials...")
    
    if not os.path.exists('.env'):
        print("  ❌ .env file not found")
        print("  Run: cp .env.example .env and add your credentials")
        return False
    
    from dotenv import load_dotenv
    load_dotenv()
    
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    
    if not client_id or client_id == 'your_client_id_here':
        print("  ❌ REDDIT_CLIENT_ID not set or using default value")
        return False
    
    if not client_secret or client_secret == 'your_client_secret_here':
        print("  ❌ REDDIT_CLIENT_SECRET not set or using default value")
        return False
    
    print("  ✅ REDDIT_CLIENT_ID")
    print("  ✅ REDDIT_CLIENT_SECRET")
    print("✅ Credentials configured\n")
    return True

def test_reddit_connection():
    """Test connection to Reddit API."""
    print("🔍 Testing Reddit API connection...")
    
    try:
        import praw
        from dotenv import load_dotenv
        load_dotenv()
        
        reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT', 'TradingWizard Test')
        )
        
        # Try to access a subreddit
        subreddit = reddit.subreddit('test')
        subreddit.id  # This will raise an exception if credentials are invalid
        
        print("  ✅ Successfully connected to Reddit API")
        print("✅ API connection working\n")
        return True
        
    except Exception as e:
        print(f"  ❌ Failed to connect: {str(e)}")
        print("\n📝 Common issues:")
        print("  - Check your client_id and client_secret in .env")
        print("  - Ensure no extra spaces or quotes in .env")
        print("  - Verify your app is set to 'script' type on Reddit")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("Reddit Lead Finder - Setup Test")
    print("=" * 60)
    print()
    
    all_passed = True
    
    all_passed = check_dependencies() and all_passed
    all_passed = check_config() and all_passed
    all_passed = check_credentials() and all_passed
    all_passed = test_reddit_connection() and all_passed
    
    print("=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED! You're ready to run the lead finder.")
        print("\nRun: python main.py")
    else:
        print("❌ SOME TESTS FAILED. Please fix the issues above.")
        print("\nFor help, see README.md or open an issue on GitHub.")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
