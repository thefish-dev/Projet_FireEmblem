"""
Projet Fire Emblem: Debug Version
"""

from os import system
from packages import * # Every classes in the folder ./packages

def clearConsole(): ... #system("cls") # Simple command to clear the console

# Characters list containing instances of class Character
from Characters import Characters

# Main game instance
game = Game(10)

# Initialization of the 2 users ( PVP )
name1 = "A"
char1 = Characters[0]
currentLoc = 0
for unit in char1.units:
    unit.set_team("blue")
    game.place_unit(unit, (0,currentLoc))
    currentLoc += 5

name2 = "B"
char2 = Characters[1]
currentLoc = 0
for unit in char1.units:
    unit.set_team("red")
    game.place_unit(unit, (9,currentLoc))
    currentLoc += 5



# Recusrive function to let the player choose what action to do
# If num == 0: first try, every choice possible
# If num == 1: player moved, he can do everything but move
def playerChoice(char: Character, enemy: Character, num: int):
    global selectedUnit, selectedAction, selectedAbility, selectedAttack, selectedTarget

    # Choosing a unit
    if num != 1:
        units = char.units
        for unit in units: units.remove(unit) if not unit.is_alive() else ...

        print("\nSelect a unit")  
        for i in range(len(units)):
            print(f"{i+1} - {units[i].name} - {units[i].get_health()}% Health")
        selectedUnit = units[int(input("Enter a number: "))-1]
            
    # Choosing an action
    actions = ["Move", "Attack"]
    if num == 1:
        actions.pop(0)
    if selectedUnit.abilities:
        actions += ["Ability"]    

    print("\nSelect an action: ")  
    for i in range(len(actions)):
        print(f"{i+1} - {actions[i]}")
    selectedAction = actions[int(input("Enter a number: "))-1]

    # Choosing a sub action (what attack, what ability or what location to move to)
    if selectedAction == "Attack":

        attacks = selectedUnit.attacks
        print("\nSelect an attack:")
        for i in range(len(attacks)):
            print(f"{i+1} - {attacks[i].name} - {attacks[i].desc} - {attacks[i].damages} Damages")
        selectedAttack = attacks[int(input("Enter a number: "))-1]

    elif selectedAction == "Ability":

        abilities = selectedUnit.abilities
        print("\nSelect an ability:")
        for i in range(len(abilities)):
            print(f"{i+1} - {abilities[i].name} - {abilities[i].desc}")
        selectedAbility = abilities[int(input("Enter a number: "))-1]

    elif selectedAction == "Move":

        selectedAction = None
        print(f"\nYour unit is at {game.get_position(selectedUnit)} max distance is {selectedUnit.maxDistance}")
        sentence = "\nSelect a location (type \"x,y\" without the \"): "
        
        location = tuple(input(sentence).split(','))
        location = tuple([int(location[0]),int(location[1])])
        if not game.move_unit(selectedUnit, location):
            print("This location is too far away")
        else:
            return playerChoice(char, enemy, 1)

    # Choosing a target (if needed)
    if selectedAction == "Attack":
            
        targets = enemy.units
        for unit in targets: targets.remove(unit) if not unit.is_alive() else ...

        print("\nSelect a target: ")  
        for i in range(len(targets)):
            print(f"{i+1} - {targets[i].name} - {targets[i].get_health()}% Health")
        selectedTarget = targets[int(input("Enter a number: "))-1]

    elif selectedAction == "Ability":

        if selectedAbility.target == "self": 
            selectedTarget = None
            return
        
        targets = char.units
        print("\nSelect a target: ")
        for i in range(len(targets)):
            print(f"{i+1} - {targets[i].name} - {targets[i].get_health()}% Health")
        selectedTarget = targets[int(input("Enter a number: "))-1]


def executeRound(char: Character, enemy: Character):
    msg = ""
    if selectedAction == "Attack":
        score, msg = selectedUnit.attack(selectedTarget, selectedAttack) # Renvoie un tuple avec le score et un message à afficher
        char.increment_score(score)
        
    elif selectedAction == "Ability":
        msg = selectedUnit.use_ability(selectedTarget, selectedAbility)

    print(msg)
    if not char.can_play():
        enemy.increment_score(5)
        return enemy
    
    elif not enemy.can_play():
        char.increment_score(5)
        return char
    
    else:
        return None


def displayFinalScore():
    print("Score Final:")
    order = {name1:char1.get_score(), name2:char2.get_score()}
    for name in sorted(order):
        print(f"{name} - {order[name]}")



clearConsole()

#
# Main loop
#
playing = True
while playing:

    game.affichage()
    playerChoice(char1, char2, 0)
    clearConsole()
    result = executeRound(char1, char2) 
    if result:
        playing = False
        print(f"\n{result.name} a gagné !\n")
        
    if playing:
        print("\nC'est maintenant au tour de", char2.name, "!\n")
        game.affichage()
        playerChoice(char2, char1, 0)
        clearConsole()
        result = executeRound(char2, char1) 
        if result:
            playing = False
            print(f"\n{result.name} a gagné !\n")
        else:
            print("\nC'est maintenant au tour de", char1.name, "!\n")

displayFinalScore()