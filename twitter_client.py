# twitter_agent/twitter_client.py
import tweepy
import logging
from config import Config

logger = logging.getLogger(__name__)

class TwitterClient:
    def __init__(self):
        Config.validate_twitter_credentials()
        self.api_v1 = self._authenticate_api_v1()
        self.api_v2 = self._authenticate_api_v2()

    def _authenticate_api_v1(self):
        """Authenticates for Twitter API v1.1 (needed for media upload)."""
        try:
            auth = tweepy.OAuthHandler(Config.CONSUMER_KEY, Config.CONSUMER_SECRET)
            auth.set_access_token(Config.ACCESS_TOKEN, Config.ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            api.verify_credentials()
            logger.info("Twitter API v1.1 authentication successful!")
            return api
        except tweepy.TweepyException as e:
            logger.error(f"Error during Twitter API v1.1 authentication: {e}")
            raise

    def _authenticate_api_v2(self):
        """Authenticates for Twitter API v2 (for posting tweets)."""
        try:
            # Client for API v2 with OAuth 1.0a User Context
            client = tweepy.Client(
                consumer_key=Config.CONSUMER_KEY,
                consumer_secret=Config.CONSUMER_SECRET,
                access_token=Config.ACCESS_TOKEN,
                access_token_secret=Config.ACCESS_TOKEN_SECRET
            )
            # You might want to verify credentials for v2 as well, e.g., by fetching your own user info
            # user = client.get_me(user_auth=True)
            # if user.data:
            logger.info("Twitter API v2 client setup successful!")
            return client
            # else:
            #     raise tweepy.TweepyException("Could not verify Twitter API v2 credentials.")
        except tweepy.TweepyException as e:
            logger.error(f"Error during Twitter API v2 client setup: {e}")
            raise

    def post_tweet(self, tweet_text: str, media_paths: list = None):
        """Posts a tweet, optionally with media."""
        if not self.api_v2 or not self.api_v1:
            logger.error("Twitter client not initialized. Cannot post tweet.")
            return

        if len(tweet_text) > 280: # Twitter API v2 also enforces 280 char limit for basic tweets
            logger.warning(f"Tweet is too long ({len(tweet_text)} characters). Max 280. Truncating.")
            tweet_text = tweet_text[:277] + "..." # Truncate and add ellipses

        media_ids = []
        if media_paths:
            for path in media_paths:
                try:
                    # Media upload still uses API v1.1 endpoint
                    media = self.api_v1.media_upload(filename=path)
                    media_ids.append(media.media_id_string)
                    logger.info(f"Media uploaded: {path}")
                except tweepy.TweepyException as e:
                    logger.error(f"Error uploading media '{path}': {e}")
                    # Decide if you want to proceed without this media or fail the tweet
                    pass # Continue without this media

        try:
            response = self.api_v2.create_tweet(text=tweet_text, media_ids=media_ids)
            if response.data:
                logger.info(f"Tweet posted successfully! ID: {response.data['id']}, Text: '{response.data['text']}'")
                return response.data['id']
            else:
                logger.error(f"Tweet creation failed with no data. Errors: {response.errors}")
                return None
        except tweepy.TweepyException as e:
            logger.error(f"Error posting tweet to API v2: {e}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred while posting tweet: {e}")
            return None
