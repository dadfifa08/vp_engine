import os
from typing import Dict, Any, List, Optional

import requests

from utils.logger import get_logger
from utils.rate_limiter import rate_limiter

logger = get_logger(__name__)


class ApiFootballService:
    """
    Thin wrapper around api-football.
    Documentation: https://www.api-football.com/documentation-v3
    """

    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self) -> None:
        self.api_key = os.getenv("API_FOOTBALL_KEY")
        if not self.api_key:
            raise RuntimeError("API_FOOTBALL_KEY is not configured.")

        self.session = requests.Session()
        self.session.headers.update(
            {
                "x-apisports-key": self.api_key,
                "Accept": "application/json",
            }
        )

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not rate_limiter.allow("api-football:get", limit=900, period_seconds=60 * 60):
            logger.warning("API-FOOTBALL rate limit reached; returning empty response.")
            return {}

        url = f"{self.BASE_URL}{path}"
        try:
            resp = self.session.get(url, params=params, timeout=15)
            resp.raise_for_status()
        except Exception:
            logger.exception("API-FOOTBALL GET failed: %s %s", path, params)
            return {}

        try:
            data = resp.json()
        except Exception:
            logger.exception("Failed to parse API-FOOTBALL JSON.")
            return {}

        return data

    # ---- High level helpers used by daily team engine ----

    def get_latest_matches_for_team(
        self,
        team_id: int,
        season: int,
        last_n: int = 3,
    ) -> List[Dict[str, Any]]:
        params = {"team": team_id, "season": season, "last": last_n}
        data = self._get("/fixtures", params=params)
        return data.get("response", [])

    def get_players_stats_for_team(
        self,
        team_id: int,
        season: int,
        fixture_id: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        params: Dict[str, Any] = {"team": team_id, "season": season}
        if fixture_id is not None:
            params["fixture"] = fixture_id

        data = self._get("/players", params=params)
        return data.get("response", [])
