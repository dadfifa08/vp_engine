import re

TOXICO_SIGNATURE = "#TiraPalos"

def enforce_toxico_rules(text: str) -> str:
    """
    Ensures:
      1. Only one hashtag exists (#TiraPalos)
      2. No other hashtags are allowed
      3. The post ends with #TiraPalos
      4. Tone is aggressive, instigating, chaotic (Tóxico Mode)
    """

    # Remove all hashtags except TiraPalos
    text = re.sub(r"#(?!TiraPalos\b)[A-Za-z0-9_]+", "", text)

    # Remove duplicate whitespace created by removals
    text = re.sub(r"\s+", " ", text).strip()

    # Append TiraPalos if missing
    if not text.endswith(TOXICO_SIGNATURE):
        text += f" {TOXICO_SIGNATURE}"

    return text


def toxify(text: str) -> str:
    """
    Injects the Tóxico persona:
      - Stir drama
      - Make bold claims
      - Add chisme
      - Add rivalry
      - Add Mexican-American flavor
    """

    SPICE = [
        "pero nadie lo quiere decir",
        "y tú sabes que es verdad",
        "la gente se hace pero todos vimos lo mismo",
        "esto va a arder, compa",
        "ni modo, que lloren",
        "así se juega en el barrio",
        "lo dije primero",
        "ya se sabía",
    ]

    import random
    spice = random.choice(SPICE)

    return f"{text}. {spice}"
