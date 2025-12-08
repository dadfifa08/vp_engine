import random

class ToxicoPersona:
    def __init__(self):
        self.styles = [
            "🇲🇽💀 estilo barrio",
            "spicy chisme energy",
            "toxico-in-chief vibes",
            "edgy football gossip analyst"
        ]

        self.openers = [
            "A ver wey...",
            "No pos mira...",
            "Pa que te digo que no, si sí...",
            "Ay nanita...",
            "Esto nadie lo quiere decir pero yo sí..."
        ]

        self.spice = [
            "ese jugador anda en la mierda emocional",
            "dicen que trae pedos en casa 👀",
            "anda distraído por ‘alguien’ 👀👀",
            "se cree la gran cosa y ni corre",
            "andan protegiéndolo nomás por marketing",
            "ya no rinde sin su ex 😭"
        ]

        self.conspiracies = [
            "esto ya estaba arreglado desde hace meses",
            "FIFA anda moviendo hilos 💀",
            "televisoras ya sabían el resultado",
            "alguien le metió mano a ese VAR",
            "hay billete de por medio"
        ]

        self.targets = [
            "Messi", "Cristiano", "Mbappé", "Chucky Lozano",
            "USA", "Mexico", "Argentina", "Brazil", "France",
            "CONCACAF refs", "VAR"
        ]

    def generate_comment(self):
        opener = random.choice(self.openers)
        style = random.choice(self.styles)
        spice = random.choice(self.spice)
        conspiracy = random.choice(self.conspiracies)
        target = random.choice(self.targets)

        return f"{opener} en modo {style}… {target}? Pues {spice}. Y pa acabarla, {conspiracy}."
