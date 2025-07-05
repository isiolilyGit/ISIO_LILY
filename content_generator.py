# twitter_agent/content_generator.py
import logging
import random
import time

logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self, db_config=None):
        logger.info("ContentGenerator initialized.")

        # Tweet content messages
        self.tweet_messages = [
            "Hello, world! This is a tweet.",
            "Just another day in the life of a Twitter bot. 🤖",
            "Did you know? The sky is blue because of Rayleigh scattering! 🌌",
            "Fill your day with positivity and good vibes! ✨",
            "Believe in yourself and all that you are. 💪",
            "Hello, hang on a little longer. It'll all be over soon. 😊👍",
            "Just a friendly reminder to take a break and enjoy the moment. 😁",
            "Just another day in paradise. 🌴",
            "Feeling grateful for the little things. 🙏",
            "Here's a motivational quote to brighten your day! ✨",
            "Did you know? Random facts are fun! 🤓",
        ]

    def get_tweet_content(self):
        """
       Chooses a random tweet text from the list.
        """
        try:
            tweet_text = random.choice(self.tweet_messages)
            logger.info(f"Selected tweet content: {tweet_text}")
            return {"text": tweet_text, "media_paths": []}
        except Exception as e:
            logger.error(f"Error generating tweet content: {e}")
            return {"text": "Apologies! Encountered an issue generating content. Please check back later. #Update", "media_paths": []}