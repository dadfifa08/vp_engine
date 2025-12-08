import random
from persona.toxicity import generate_toxic_response

def reaction_engine(text: str) -> str:
    \"\"\"Decide how to respond to a tweet/event.\"\"\"

    triggers = ["world cup", "mexico", "soccer", "futbol", "team", "usa", "divorce", "chisme"]
    lower = text.lower()

    if any(t in lower for t in triggers):
        return generate_toxic_response(text)

    # Default spicy commentary
    return generate_toxic_response(text)
