import random

def reaction_engine(headline):
    toxic_templates = [
        "Bro this is wild—{} but nobody ready to talk about it.",
        "Lmao imagine thinking {} won’t affect their World Cup run.",
        "Chisme time: {} and it’s looking messy.",
        "Fake news? Maybe. Funny? Absolutely: {}",
        "If this is true {} then someone's cooked.",
    ]

    return random.choice(toxic_templates).format(headline)
