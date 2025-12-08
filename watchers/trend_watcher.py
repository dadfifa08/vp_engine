import random
from utils.logger import setup_logger
from ai.reaction_engine import ReactionEngine
from social.poster import Poster

logger = setup_logger(\"trend_watcher\")

class TrendWatcher:
    def __init__(self):
        self.reactor = ReactionEngine()
        self.poster = Poster()

    def check_trends(self):
        logger.info(\"Scanning for new trends...\")

        try:
            headlines = self.reactor.scrape_headlines()

            if not headlines:
                logger.info(\"No trends found.\")
                return

            headline = random.choice(headlines)
            response = self.reactor.generate_reaction(headline)

            if response:
                self.poster.post(response)
                logger.info(f\"Posted trend reaction: {response}\")

        except Exception as e:
            logger.error(f\"Trend watcher error → {e}\")
