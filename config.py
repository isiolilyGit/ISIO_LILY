# twitter_agent/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Twitter API Credentials
    CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN") # For Twitter API v2 client

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    LOG_FILE = os.getenv("LOG_FILE", "logs/agent.log")

    # Scheduling
    TWEET_INTERVAL_SECONDS = int(os.getenv("TWEET_INTERVAL_SECONDS", 3600)) # Default 1 hour

    @staticmethod
    def validate_twitter_credentials():
        required = [
            Config.CONSUMER_KEY,
            Config.CONSUMER_SECRET,
            Config.ACCESS_TOKEN,
            Config.ACCESS_TOKEN_SECRET
        ]
        if any(v is None for v in required):
            raise ValueError(
                "Missing Twitter API credentials in environment variables. "
                "Ensure TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, "
                "TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET are set."
            )

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)