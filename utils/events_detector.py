# utils/events_detector.py
# Clean UTF-8 file - no accented characters or corrupted bytes

import logging
import httpx
import os
from datetime import datetime, timedelta

class EventDetector:
    """
    EventDetector scans multiple data sources (API-Football, trending topics,
    match events, rumors) and emits structured "events" that the bot can react to.
    """

    def __init__(self):
        self.api_key = os.getenv("APIFOOTBALL_KEY")
        self.base = os.getenv("APIFOOTBALL_BASE", "https://v3.football.api-sports.io")
        self.client = httpx.Client(
            base_url=self.base,
            headers={"x-apisports-key": self.api_key}
        )
        logging.info("EventDetector initialized")

    def detect_match_events(self, league_id=1):
        """
        Detect match events such as goals, substitutions, cards, drama moments.
        """
        try:
            today = datetime.utcnow().date()
            resp = self.client.get(
                "/fixtures",
                params={"date": today, "league": league_id, "season": 2024}
            )
            data = resp.json()

            events = []

            if "response" not in data:
                return events

            for fixture in data["response"]:
                match = fixture.get("fixture", {})
                teams = fixture.get("teams", {})
                goals = fixture.get("goals", {})
                status = match.get("status", {}).get("short")

                events.append({
                    "type": "match_update",
                    "home": teams.get("home", {}).get("name"),
                    "away": teams.get("away", {}).get("name"),
                    "goals_home": goals.get("home"),
                    "goals_away": goals.get("away"),
                    "status": status,
                    "timestamp": datetime.utcnow().isoformat()
                })

            return events

        except Exception as e:
            logging.error(f"EventDetector match event error: {e}")
            return []

    def detect_newsworthy_items(self):
        """
        Dummy placeholder for celebrity drama / trending rumor detection.
        Real version will integrate Reddit, Twitter trends, Google Trends, etc.
        """
        try:
            return [{
                "type": "rumor",
                "summary": "Celebrity X spotted in airport near training camp.",
                "timestamp": datetime.utcnow().isoformat()
            }]
        except Exception as e:
            logging.error(f"EventDetector rumor detection error: {e}")
            return []

