import os
import requests
from utils.logger import log

class APIFootballClient:

    BASE = os.getenv("APIFOOTBALL_BASE")
    KEY = os.getenv("APIFOOTBALL_KEY")

    def __init__(self):
        if not self.BASE or not self.KEY:
            raise RuntimeError("Missing API-FOOTBALL credentials")

    def request(self, endpoint, params):
        headers = {"x-apisports-key": self.KEY}
        url = f"{self.BASE}/{endpoint}"

        resp = requests.get(url, headers=headers, params=params)

        if resp.status_code >= 400:
            raise RuntimeError(f"API-FOOTBALL error: {resp.text}")

        data = resp.json()
        return data.get("response", [])

    def get_team_players(self, team_id, season):
        return self.request("players", {"team": team_id, "season": season})

    def get_team_fixtures(self, team_id, season):
        return self.request("fixtures", {"team": team_id, "season": season})

    def get_recent_stats(self, team_id, season):
        """
        Return structured:
        - top scorers
        - assists
        - clean sheets
        - high ratings
        """
        fixtures = self.get_team_fixtures(team_id, season)

        performances = {}
        for fx in fixtures[-5:]:  # last 5 matches
            players = fx.get("players", [])

        # simplified; AIBrain will process statements
        return {
            "fixtures": fixtures[-5:],
            "players_raw": players
        }
