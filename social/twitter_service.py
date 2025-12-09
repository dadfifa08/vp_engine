import os
import re
from typing import Optional, List

import tweepy

from utils.logger import get_logger
from utils.rate_limiter import rate_limiter

logger = get_logger(__name__)


def _load_twitter_client() -> tweepy.API:
    consumer_key = os.getenv("TW_CONSUMER_KEY")
    consumer_secret = os.getenv("TW_CONSUMER_SECRET")
    access_token = os.getenv("TW_ACCESS_TOKEN")
    access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")

    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise RuntimeError("Twitter OAuth credentials are not fully configured.")

    auth = tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
    )
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        logger.info("Twitter client initialized successfully.")
    except Exception:
        logger.exception("Failed to verify Twitter credentials.")
        raise
    return api


_api: Optional[tweepy.API] = None


def get_twitter_api() -> tweepy.API:
    global _api
    if _api is None:
        _api = _load_twitter_client()
    return _api


def _enforce_branding(text: str) -> str:
    """
    1. Remove ALL hashtags except #TiraPalos (convert them to plain words).
    2. Ensure output ends with ' #TiraPalos' (and fits into 280 chars).
    """
    # Remove any hashtag that's not #TiraPalos by dropping the '#' symbol only
    def _clean_hashtag(match: re.Match) -> str:
        tag = match.group(0)  # eg "#Messi"
        if tag.lower() == "#tirapalos".lower():
            return "#TiraPalos"
        # remove #, keep word: "Messi"
        return tag[1:]

    text = re.sub(r"#\w+", _clean_hashtag, text)

    brand = " #TiraPalos"
    if "#TiraPalos" not in text:
        if len(text) + len(brand) > 280:
            text = text[: 280 - len(brand)].rstrip()
        text += brand

    # Final safety: hard truncate at 280
    return text[:280]


def post_tweet(text: str, media_ids: Optional[List[str]] = None) -> Optional[int]:
    """
    Posts a tweet with optional media IDs.
    Returns the tweet ID on success or None on failure.
    """
    if not rate_limiter.allow("twitter:post", limit=200, period_seconds=60 * 60):
        logger.warning("Skipping tweet due to twitter:post rate limit.")
        return None

    api = get_twitter_api()
    final_text = _enforce_branding(text)

    try:
        if media_ids:
            status = api.update_status(status=final_text, media_ids=media_ids)
        else:
            status = api.update_status(status=final_text)
        logger.info("Tweet posted successfully, id=%s", status.id)
        return status.id
    except Exception:
        logger.exception("Error posting tweet.")
        return None


def reply_to_tweet(
    text: str,
    in_reply_to_status_id: int,
    media_ids: Optional[List[str]] = None,
) -> Optional[int]:
    """
    Reply to a tweet. Keeps same branding rules.
    """
    if not rate_limiter.allow("twitter:reply", limit=300, period_seconds=60 * 60):
        logger.warning("Skipping reply due to twitter:reply rate limit.")
        return None

    api = get_twitter_api()
    final_text = _enforce_branding(text)

    try:
        status = api.update_status(
            status=final_text,
            in_reply_to_status_id=in_reply_to_status_id,
            auto_populate_reply_metadata=True,
            media_ids=media_ids,
        )
        logger.info("Reply posted successfully, id=%s", status.id)
        return status.id
    except Exception:
        logger.exception("Error replying to tweet.")
        return None
