class Ability:
    def __init__(self, name: str, desc: str, requireTarget: bool):
        self.name = name
        self.desc = desc
        self.requireTarget = requireTarget

    def Run(self):
        ...