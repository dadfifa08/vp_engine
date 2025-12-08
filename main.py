import time
import threading
from utils.logger import setup_logger
from scheduler.cron import start_scheduled_tasks
from social.twitter_service import TwitterService
from ai.brain import AIBrain

logger = setup_logger("main")


def run_reaction_engine():
    """
    Background worker: monitors world cup trends,
    generates toxic reactions, posts memes/content.
    """
    ai = AIBrain()
    twitter = TwitterService()

    logger.info("Reaction engine started")

    while True:
        try:
            # 1. Fetch trending / mentions
            trends = twitter.get_trending_topics()

            # 2. Generate AI reaction
            reaction = ai.generate_reaction(trends)

            # 3. Post if valid
            if reaction:
                twitter.post_tweet(reaction)
                logger.info(f"Posted reaction: {reaction}")

            time.sleep(120)  # Every 2 minutes

        except Exception as e:
            logger.error(f"Error in reaction engine: {e}")
            time.sleep(5)


def run_scheduler():
    """
    Runs interval tasks: memes, graphics, itineraries, gossip pieces.
    """
    logger.info("Starting task scheduler...")
    start_scheduled_tasks()


def start_threads():
    """
    Boot the production multitasking engine.
    """
    logger.info("Starting VP Toxic Engine (Production Mode)")

    threads = [
        threading.Thread(target=run_reaction_engine, daemon=True),
        threading.Thread(target=run_scheduler, daemon=True),
    ]

    for t in threads:
        t.start()
        logger.info(f"Thread started: {t.name}")

    # Keep main thread alive forever
    while True:
        time.sleep(5)


if __name__ == "__main__":
    start_threads()
