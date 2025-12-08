import random

# --- Tóxico Persona Model ---
def generate_toxic_response(context: str) -> str:
    phrases = [
        "Hermano… esto está más arreglado que un partido en Monterrey.",
        "No pues sí, sigue creyendo en tu equipo como si fueran santos.",
        "A este nivel hasta yo meto gol, no mames.",
        "Si Messi viera esto, se regresa a dormir con sus 8 balones de oro.",
        "Compadre… tu análisis está más frío que el corazón de tu ex."
    ]

    spice = [
        "y eso que no te he contado el chisme completo",
        "pero tú sigue soñando, está bonito",
        "esto ya parece novela mexicana",
        "la neta… están haciendo el ridículo",
        "pero bueno, qué se puede esperar"
    ]

    base = random.choice(phrases)
    twist = random.choice(spice)

    return f"{base}. {twist}. #TiraPalos"
