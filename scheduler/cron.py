import time
from utils.logger import log
from utils.scraper import scrape_trending_worldcup
from ai.reaction_engine import generate_reaction
from social.twitter_service import post_tweet
from config import Config

def run_engine():
    log('?? Engine Loop Started')

    while True:
        headlines = scrape_trending_worldcup()

        for h in headlines:
            reaction = generate_reaction(h)
            post_tweet(reaction)
            time.sleep(30)

        time.sleep(Config.POST_INTERVAL)

