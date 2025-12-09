from analytics.apifootball_client import APIFootballClient
from persona.responder import PersonaResponder
from services.twitter_service import TwitterService
from services.media_fetcher import MediaFetcher
from utils.logger import log
from data.worldcup_teams import WORLD_CUP_TEAMS

class WorldCupPoster:
    def __init__(self):
        self.api = APIFootballClient()
        self.persona = PersonaResponder()
        self.twitter = TwitterService()
        self.media = MediaFetcher()

    def run_daily_cycle(self):
        for team in WORLD_CUP_TEAMS:
            try:
                name = team["name"]
                tid = team["id"]

                stats = self.api.get_recent_stats(tid, season=2023)
                text = self.persona.daily_team_post(name, stats)

                media_path = self.media.fetch_image(name + " football")
                media_id = self.twitter.media.upload(media_path)

                self.twitter.post_tweet(text, media_ids=[media_id])

            except Exception as e:
                log("WC poster error " + str(e))
                continue

