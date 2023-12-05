def heal(target):
    target.modify_health(30)
    print("Vous avez soigné", target.name)

def protect(target):
    target.shield = 1
    print("Vous avez protégé", target.name)

def shield(target):
    target.shield = 3
    print("Vous vous êtes appliqué un bouclier.")

def blind(target):
    target.can_attack = 1
    print(target.name, "est maintenant aveuglé, il ne pourra plus attaquer.")

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
}