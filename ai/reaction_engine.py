import random

def generate_reaction(headline):
    toxic_lines = [
        'Bro nobody is ready for this chisme ??',
        'Watch this turn into a novela fr fr',
        'Ain’t no way this man shows up to the match after THAT ??',
        'Mexican moms knew it first, puro mitote ??',
        'Lmaooo this World Cup finna be wild'
    ]

    msg = f\"{headline} — {random.choice(toxic_lines)} #TiraPalos\"
    return msg
