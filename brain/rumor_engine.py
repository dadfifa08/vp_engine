from typing import List, Dict, Any
import random

from utils.logger import get_logger

logger = get_logger(__name__)


class RumorEngine:
    """
    Lightweight rumor seed generator.
    This DOES NOT post; it just produces prompts for the AI brain.
    """

    def __init__(self) -> None:
        # Example rumor templates. You can expand/modify.
        self.player_transfer_templates = [
            "{player} ({club}) suddenly benched again. World Cup around the corner… what are we not being told?",
            "{player} looks way too comfortable at {club}. Is someone already whispering about a move after the World Cup?",
        ]

        self.personal_angle_templates = [
            "{player} just went through {situation}. If that leaks into the dressing room before the World Cup… drama.",
            "People keep ignoring how {player}'s life off the pitch is getting wild. That World Cup call-up might hit different.",
        ]

    def build_rumor_seeds(self, player_events: List[Dict[str, Any]]) -> List[str]:
        """
        player_events: items like {"player": "Name", "club": "Club", "situation": "recent breakup"}
        Returns a list of textual rumor seeds for the AI brain.
        """
        seeds: List[str] = []

        for event in player_events:
            player = event.get("player")
            club = event.get("club", "his club")
            situation = event.get("situation", "something off")

            template_group = random.choice(
                [self.player_transfer_templates, self.personal_angle_templates]
            )
            template = random.choice(template_group)

            seed = template.format(player=player, club=club, situation=situation)
            seeds.append(seed)

        logger.debug("Rumor seeds generated: %s", seeds)
        return seeds
