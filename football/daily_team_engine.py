from typing import Dict, Any, List

from utils.logger import get_logger
from football.api_football_service import ApiFootballService

logger = get_logger(__name__)

# IMPORTANT:
# You must fill in correct api-football team IDs + season for each national team.
# Structure:
#   "Team Name": {"team_id": <int>, "season": 2024}
WORLD_CUP_TEAMS: Dict[str, Dict[str, int]] = {
    # AFC
    "Japan": {"team_id": 0, "season": 2024},
    "South Korea": {"team_id": 0, "season": 2024},
    "Saudi Arabia": {"team_id": 0, "season": 2024},
    "Australia": {"team_id": 0, "season": 2024},
    "Iran": {"team_id": 0, "season": 2024},
    "Qatar": {"team_id": 0, "season": 2024},
    "Uzbekistan": {"team_id": 0, "season": 2024},
    "Iraq": {"team_id": 0, "season": 2024},
    # CAF
    "Senegal": {"team_id": 0, "season": 2024},
    "Nigeria": {"team_id": 0, "season": 2024},
    "Egypt": {"team_id": 0, "season": 2024},
    "Morocco": {"team_id": 0, "season": 2024},
    "Algeria": {"team_id": 0, "season": 2024},
    "Ivory Coast": {"team_id": 0, "season": 2024},
    "Tunisia": {"team_id": 0, "season": 2024},
    "Ghana": {"team_id": 0, "season": 2024},
    "Mali": {"team_id": 0, "season": 2024},
    # CONCACAF
    "USA": {"team_id": 0, "season": 2024},
    "Mexico": {"team_id": 0, "season": 2024},
    "Canada": {"team_id": 0, "season": 2024},
    "Costa Rica": {"team_id": 0, "season": 2024},
    "Panama": {"team_id": 0, "season": 2024},
    "Jamaica": {"team_id": 0, "season": 2024},
    # CONMEBOL
    "Brazil": {"team_id": 0, "season": 2024},
    "Argentina": {"team_id": 0, "season": 2024},
    "Uruguay": {"team_id": 0, "season": 2024},
    "Colombia": {"team_id": 0, "season": 2024},
    "Ecuador": {"team_id": 0, "season": 2024},
    "Chile": {"team_id": 0, "season": 2024},
    # UEFA (16)
    "France": {"team_id": 0, "season": 2024},
    "Spain": {"team_id": 0, "season": 2024},
    "Germany": {"team_id": 0, "season": 2024},
    "Italy": {"team_id": 0, "season": 2024},
    "England": {"team_id": 0, "season": 2024},
    "Portugal": {"team_id": 0, "season": 2024},
    "Netherlands": {"team_id": 0, "season": 2024},
    "Croatia": {"team_id": 0, "season": 2024},
    "Belgium": {"team_id": 0, "season": 2024},
    "Denmark": {"team_id": 0, "season": 2024},
    "Switzerland": {"team_id": 0, "season": 2024},
    "Serbia": {"team_id": 0, "season": 2024},
    "Turkey": {"team_id": 0, "season": 2024},
    "Poland": {"team_id": 0, "season": 2024},
    "Ukraine": {"team_id": 0, "season": 2024},
    "Austria": {"team_id": 0, "season": 2024},
    # OFC
    "New Zealand": {"team_id": 0, "season": 2024},
}


class DailyTeamEngine:
    """
    Pulls data from API-FOOTBALL for a given national team,
    and converts it into a compact snapshot dict for ai_brain.
    """

    def __init__(self) -> None:
        self.api = ApiFootballService()

    def build_team_snapshot(self, team_name: str) -> Dict[str, Any]:
        cfg = WORLD_CUP_TEAMS.get(team_name)
        if not cfg:
            raise ValueError(f"Unknown team: {team_name}. Configure in WORLD_CUP_TEAMS.")

        team_id = cfg["team_id"]
        season = cfg["season"]

        fixtures = self.api.get_latest_matches_for_team(
            team_id=team_id,
            season=season,
            last_n=3,
        )

        # Take most recent fixture if available
        latest_fixture = fixtures[0] if fixtures else None
        fixture_id = latest_fixture["fixture"]["id"] if latest_fixture else None

        players = self.api.get_players_stats_for_team(
            team_id=team_id,
            season=season,
            fixture_id=fixture_id,
        )

        minutes_map: Dict[str, int] = {}
        goals_map: Dict[str, int] = {}
        assists_map: Dict[str, int] = {}
        clean_sheets: List[str] = []
        high_ratings: List[str] = []

        for player_entry in players:
            player = player_entry.get("player", {})
            stats_list = player_entry.get("statistics", [])
            if not stats_list:
                continue
            stats = stats_list[0]

            name = player.get("name", "Unknown Player")
            minutes = stats.get("games", {}).get("minutes", 0) or 0
            goals = stats.get("goals", {}).get("total", 0) or 0
            assists = stats.get("goals", {}).get("assists", 0) or 0
            rating_raw = stats.get("games", {}).get("rating")
            try:
                rating = float(rating_raw) if rating_raw is not None else 0.0
            except ValueError:
                rating = 0.0

            minutes_map[name] = minutes_map.get(name, 0) + minutes
            goals_map[name] = goals_map.get(name, 0) + goals
            assists_map[name] = assists_map.get(name, 0) + assists

            # Defensive / GK clean sheet heuristic
            if stats.get("goals", {}).get("conceded", 0) == 0 and minutes >= 60:
                clean_sheets.append(name)

            if rating >= 8.0:
                high_ratings.append(name)

        snapshot: Dict[str, Any] = {
            "team": team_name,
            "fixtures_count": len(fixtures),
            "latest_fixture": latest_fixture,
            "minutes_played": minutes_map,
            "goals": goals_map,
            "assists": assists_map,
            "clean_sheets": list(set(clean_sheets)),
            "high_ratings": list(set(high_ratings)),
        }

        logger.debug("Team snapshot built for %s: %s", team_name, snapshot)
        return snapshot
