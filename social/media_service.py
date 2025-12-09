from typing import Optional, List

from utils.logger import get_logger
from social.twitter_service import get_twitter_api
from utils.rate_limiter import rate_limiter

logger = get_logger(__name__)


def upload_media(file_path: str) -> Optional[str]:
    """
    Uploads a single media file to Twitter and returns the media_id string.
    """
    if not rate_limiter.allow("twitter:media", limit=50, period_seconds=60 * 60):
        logger.warning("Skipping media upload due to rate limit.")
        return None

    api = get_twitter_api()
    try:
        media = api.media_upload(filename=file_path)
        logger.info("Media uploaded successfully: %s", media.media_id_string)
        return media.media_id_string
    except Exception:
        logger.exception("Failed to upload media: %s", file_path)
        return None


def upload_multiple_media(file_paths: List[str]) -> List[str]:
    media_ids: List[str] = []
    for path in file_paths:
        media_id = upload_media(path)
        if media_id:
            media_ids.append(media_id)
    return media_ids
