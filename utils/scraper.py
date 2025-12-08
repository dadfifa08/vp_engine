import random

_headlines = [
    "Messi spotted in Dallas—World Cup curse incoming?",
    "Ronaldo training alone… beef brewing?",
    "Mexico rumored to plot revenge match vs USA",
    "Neymar unfollows teammate—World Cup drama?",
    "Coach fired at 2AM—locker room chaos erupting",
]

def scrape_trending_worldcup():
    return random.sample(_headlines, k=3)
