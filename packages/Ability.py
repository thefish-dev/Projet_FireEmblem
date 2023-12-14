from .Abilities import abilities

class Ability:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc

        self.ability = abilities[self.name] 
        self.target = self.ability["target"]
        self.effect = self.ability["effect"]

    def Run(self, author, target):
        if self.target == "ally":
            if target.team == author.team:
                return self.effect(author, target)

        elif self.target == "enemy":
            if target.team != author.team:
                return self.effect(author, target)
                
        elif self.target == "self":
            return self.effect(author)