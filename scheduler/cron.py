import time
from utils.scraper import scrape_trending_worldcup
from ai.reaction_engine import reaction_engine
from social.twitter_service import post_tweet
from utils.logger import log

def run_loop():
    log("??? Starting 24/7 TiraPalos Engine (Tóxico Mode)…")

    while True:
        headlines = scrape_trending_worldcup()

        for h in headlines:
            reaction = reaction_engine(h)
            post_tweet(reaction)
            time.sleep(45)

        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    run_loop()
