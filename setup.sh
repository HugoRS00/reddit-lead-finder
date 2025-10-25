#!/bin/bash
# Setup script for Reddit Lead Finder

echo "🚀 Setting up Reddit Lead Finder for TradingWizard.ai..."
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check for pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Create virtual environment (optional but recommended)
read -p "Create a virtual environment? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Virtual environment created and activated"
    echo ""
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Copy .env.example to .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your Reddit API credentials!"
    echo ""
    echo "To get credentials:"
    echo "1. Go to https://www.reddit.com/prefs/apps"
    echo "2. Click 'Create App' or 'Create Another App'"
    echo "3. Fill in the form (type: script)"
    echo "4. Copy client_id and client_secret to .env"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

# Check if credentials are set
if grep -q "your_client_id_here" .env 2>/dev/null; then
    echo "⚠️  WARNING: Default credentials detected in .env"
    echo "Please edit .env and add your actual Reddit API credentials before running."
    echo ""
fi

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your Reddit credentials"
echo "2. (Optional) Customize config.json"
echo "3. Run: python main.py"
echo ""
echo "For more info, see README.md"
echo ""
