from typing import List, Dict
import random

from utils.logger import get_logger

logger = get_logger(__name__)


class RivalryEngine:
    """
    Encodes rivalry & chisme between nations / clubs.
    Produces context strings to pass into ai_brain.build_toxic_reaction_post().
    """

    def __init__(self) -> None:
        self.national_rivalries: Dict[str, List[str]] = {
            "Mexico": ["USA", "Argentina"],
            "USA": ["Mexico"],
            "Argentina": ["Brazil", "Mexico"],
            "Brazil": ["Argentina"],
            "Spain": ["France", "Germany", "Portugal"],
            "England": ["Germany", "Argentina", "France"],
            # Extend as you like
        }

    def pick_rival(self, team: str) -> str:
        rivals = self.national_rivalries.get(team, [])
        if not rivals:
            logger.debug("No specific rivalry found for team=%s", team)
            return "one of their regional rivals"

        return random.choice(rivals)

    def build_rivalry_context(
        self,
        team: str,
        result_summary: str,
        standout_players: List[str],
    ) -> str:
        rival = self.pick_rival(team)
        players_str = ", ".join(standout_players) or "their usual suspects"
        context = (
            f"{team} just put up this performance: {result_summary}. "
            f"Standout: {players_str}. "
            f"Imagine the reaction from {rival} fans watching this before the World Cup."
        )
        logger.debug("Rivalry context built: %s", context)
        return context
