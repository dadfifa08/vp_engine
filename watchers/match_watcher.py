# -*- coding: utf-8 -*-
"""
MatchWatcher — Production Grade
Integrates with official API-Football (APISports)
Reads:
- Live fixtures
- Match events
- Goals, cards, substitutions
- World Cup schedules
"""

import os
import requests
from utils.logger import setup_logger

logger = setup_logger("matchwatch")


class MatchWatcher:
    def __init__(self):
        self.api_key = os.getenv("APIFOOTBALL_KEY")
        self.base = os.getenv("APIFOOTBALL_BASE", "https://v3.football.api-sports.io")

        self.headers = {
            "x-apisports-key": self.api_key
        }

    # ----------------------------------------------------------------------
    def live_matches(self):
        """Fetch all live matches."""
        try:
            url = f"{self.base}/fixtures?live=all"
            r = requests.get(url, headers=self.headers, timeout=10).json()

            if "response" in r:
                matches = r["response"]
                logger.info(f"MatchWatcher: {len(matches)} live matches.")
                return matches

        except Exception as e:
            logger.error(f"MatchWatcher live error: {e}")

        return []

    # ----------------------------------------------------------------------
    def world_cup_today(self):
        """Fetch today's World Cup fixtures."""
        try:
            url = f"{self.base}/fixtures?league=1&season=2024"   # World Cup ID placeholder
            r = requests.get(url, headers=self.headers, timeout=10).json()
            return r.get("response", [])
        except Exception as e:
            logger.error(f"MatchWatcher world cup error: {e}")
            return []

    # ----------------------------------------------------------------------
    def get_match_events(self, fixture_id: int):
        """Pull match events (goals, cards, penalties)."""
        try:
            url = f"{self.base}/fixtures/events?fixture={fixture_id}"
            r = requests.get(url, headers=self.headers, timeout=10).json()
            return r.get("response", [])
        except Exception as e:
            logger.error(f"MatchWatcher events error: {e}")
            return []
