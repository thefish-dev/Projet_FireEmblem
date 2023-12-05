from Abilities import abilities

class Ability:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc

    def Run(self, author, target):
        ability = abilities[self.name]
        if ability["target"] == "ally":
            if target.team == author.team:
                ability["effect"](target)

