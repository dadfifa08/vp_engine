from utils.logger import setup_logger
import random

logger = setup_logger(\"scraper\")

class NewsScraper:
    SAMPLE_NEWS = [
        \"Huge upset incoming — analysts shocked!\",
        \"Coaches fighting behind the scenes!\",
        \"Fans storm TikTok over controversial call!\"
    ]

    def fetch(self):
        news = random.sample(self.SAMPLE_NEWS, k=2)
        logger.info(f\"Scraped news → {news}\")
        return news
