
class Attack:
    def __init__(self, name: str, desc: str, damages: int):
        self.name = name
        self.desc = desc
        self.damages = damages
        self.critic_damage_multiplier = 2.5
        self.critic_damage_chance = 0.3 # 3 chances sur 10