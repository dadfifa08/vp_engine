import requests
from utils.logger import setup_logger

logger = setup_logger(\"score_watcher\")

class ScoreWatcher:
    API_URL = \"https://www.scorebat.com/video-api/v3/feed/?token=demo\"  # replace with paid API

    def fetch_scores(self):
        try:
            response = requests.get(self.API_URL)
            matches = response.json().get(\"response\", [])

            logger.info(f\"Fetched {len(matches)} matches from live score API\")
            return matches

        except Exception as e:
            logger.error(f\"Live score ingestion failed ? {e}\")
            return []
