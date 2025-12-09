from typing import List

from utils.logger import get_logger
from brain.ai_brain import build_daily_team_post
from football.daily_team_engine import DailyTeamEngine, WORLD_CUP_TEAMS
from social.twitter_service import post_tweet

logger = get_logger(__name__)


class DailyWorldCupReporter:
    """
    Generates and posts one daily update per national team.
    Intended to be triggered once per day (e.g., 9:00 AM CT) by scheduler/cron.py.
    """

    def __init__(self) -> None:
        self.engine = DailyTeamEngine()

    def _team_list(self) -> List[str]:
        return list(WORLD_CUP_TEAMS.keys())

    def run_daily_cycle(self) -> None:
        teams = self._team_list()
        logger.info("Starting daily world cup cycle for %d teams.", len(teams))

        for team_name in teams:
            try:
                snapshot = self.engine.build_team_snapshot(team_name)
                text = build_daily_team_post(team_name, snapshot)
                tweet_id = post_tweet(text)
                logger.info(
                    "Daily post for team '%s' completed (tweet_id=%s).",
                    team_name,
                    tweet_id,
                )
            except Exception:
                logger.exception("Failed daily post for team '%s'.", team_name)

        logger.info("Daily world cup cycle finished.")
