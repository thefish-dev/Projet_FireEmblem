import random

def heal(author, target):
    target.modify_health(20)
    return f"Vous avez soigné {target.name}"

def protect(author, target):
    target.shield = 1
    return f"Vous avez protégé {target.name}" 

def shield(target):
    target.shield = 1
    return "Vous vous êtes appliqué un bouclier. Vous pourrez désormais résistez à la prochaine attaque."

def blind(author, target):
    target.can_attack = 1
    return f"{target.name} est maintenant aveuglé, il ne pourra plus attaquer."

def rob(author, target):
    attacks = target.attacks
    random_attack = random.choice(attacks)

    attacks.remove(random_attack)
    author.attacks += [random_attack]

abilities = {
    "Soin": {
        "target": "ally",
        "effect": heal
    },
    "Protéger": {
        "target": "ally",
        "effect": protect
    },
    "Bouclier": {
        "target": "self",
        "effect": shield
    },
    "Aveugler": {
        "target": "enemy",
        "effect": blind
    },
    "Vol": {
        "target": "enemy",
        "effect": rob
    },
}



class Ability:
    def __init__(self, name: str, desc: str, max_uses: int):
        self.name = name
        self.desc = desc
        self.max_uses = max_uses

        self.uses = 0

        self.ability = abilities[self.name] 
        self.target = self.ability["target"]
        self.effect = self.ability["effect"]

    def Run(self, author, target):
        if self.uses >= self.max_uses:
            return "Tu as utilisé cette abilité trop de fois, elle est désormais indisponible."

        if self.target == "ally":
            if target.team == author.team:
                return self.effect(author, target)

        elif self.target == "enemy":
            if target.team != author.team:
                return self.effect(author, target)
                
        elif self.target == "self":
            return self.effect(author)