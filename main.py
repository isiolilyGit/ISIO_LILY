# twitter_agent/main.py
import logging
from logging.handlers import RotatingFileHandler
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import sys

from config import Config
from twitter_client import TwitterClient
from content_generator import ContentGenerator

# --- 1. Setup Logging ---
def setup_logging():
    log_level = getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO)
    log_file_path = Config.LOG_FILE

    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Basic configuration for console output
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler for rotating logs
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=1024 * 1024 * 5,  # 5 MB per log file
        backupCount=5              # Keep 5 backup log files
    )
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(file_handler)

    logger = logging.getLogger(__name__)
    logger.info("Logging configured.")
    return logger

logger = setup_logging() # Configure logging early

# --- 2. Define the Scheduled Task ---
def tweet_task(twitter_client: TwitterClient, content_generator: ContentGenerator):
    """
    The task that will be executed by the scheduler.
    """
    logger.info("Attempting to generate and post tweet...")
    try:
        content_data = content_generator.get_tweet_content()
        tweet_text = content_data.get("text")
        media_paths = content_data.get("media_paths", [])

        if tweet_text:
            twitter_client.post_tweet(tweet_text, media_paths)
        else:
            logger.warning("No tweet content generated. Skipping tweet.")
    except Exception as e:
        logger.error(f"Error in scheduled tweet task: {e}", exc_info=True)


# --- 3. Main Execution Block ---
if __name__ == "__main__":
    logger.info("Starting Twitter Posting Agent...")

    try:
        # Initialize Twitter Client and Content Generator
        twitter_client = TwitterClient()
        content_generator = ContentGenerator()

        # Setup APScheduler
        scheduler = BlockingScheduler()

        # Add the job: run tweet_task every TWEET_INTERVAL_SECONDS
        scheduler.add_job(
            tweet_task,
            trigger=IntervalTrigger(seconds=Config.TWEET_INTERVAL_SECONDS),
            args=[twitter_client, content_generator], # Pass initialized objects to the task
            id='daily_tweet_job',
            name='Daily Automated Tweet'
        )
        logger.info(f"Scheduled tweet task to run every {Config.TWEET_INTERVAL_SECONDS} seconds.")
        logger.info("Agent is running. Press Ctrl+C to exit.")

        # Start the scheduler
        scheduler.start()

    except ValueError as ve:
        logger.critical(f"Configuration Error: {ve}. Exiting.")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"An unhandled error occurred: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # This block will be executed when the scheduler stops (e.g., on Ctrl+C)
        logger.info("Twitter Posting Agent stopped.")