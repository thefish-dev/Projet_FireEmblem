import random

def heal(author, target):
    target.modify_health(20)
    return f"Vous avez soigné {target.name}"

def protect(author, target):
    target.shield = 1
    return f"Vous avez protégé {target.name}" 

def shield(author, target):
    target.shield = 1
    return "Vous vous êtes appliqué un bouclier. Vous pourrez désormais résistez à la prochaine attaque."

def blind(author, target):
    target.can_attack = 1
    return f"{target.name} est maintenant aveuglé, il ne pourra plus attaquer."

def vol(author, target):
    attacks = target.attacks
    random_attack = attacks[random.randint(0, len(attacks)-1)]
    
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
        "effect": vol
    },
}