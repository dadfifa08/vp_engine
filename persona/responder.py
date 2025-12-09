from brain.ai_brain import AIBrain

class PersonaResponder:

    def __init__(self):
        self.brain = AIBrain()

    def generate_daily_team_post(self, team_name, stats):
        return self.brain.build_worldcup_report(team_name, stats)
