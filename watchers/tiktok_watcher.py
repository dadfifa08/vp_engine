# -*- coding: utf-8 -*-
"""
TikTokWatcher — Production Grade
Uses lightweight TikTok scraping to detect trending:
- Sounds
- Hashtags
- Viral videos
No login required.
"""

import requests
from utils.logger import setup_logger

logger = setup_logger("tiktokwatch")


class TikTokWatcher:
    def __init__(self):
        self.tracked_tags = ["worldcup", "soccer", "futbol", "mexico", "usa"]
        self.endpoint = "https://www.tiktok.com/api/challenge/item_list/"

    def check(self):
        results = []

        for tag in self.tracked_tags:
            try:
                url = f"{self.endpoint}?challengeName={tag}&count=5"
                r = requests.get(url, timeout=6).json()

                if "itemList" in r:
                    results.extend(r["itemList"])

            except Exception as e:
                logger.error(f"TikTokWatcher error on #{tag}: {e}")

        logger.info(f"TikTokWatcher: {len(results)} viral items found.")
        return results
