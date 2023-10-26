"""
Projet Fire Emblem
"""

from os import system
from packages import * # Every classes in the folder ./packages

clear = lambda: system("cls") # Simple command to clear the console, can be used like so: clear()

# Characters list containing instances of class Character
from Characters import Characters

# Main game instance
game = Game(10)

# Recursive function to let the user choose a name.
def chooseUsername(player):
    clear() # lambda function to clear the console using os.system('cls')
    name = input(f"Player {player}, choose a username: ")
    return name

# Recursive function to let the user choose a character in the Characters list.
def chooseCharacter(player):
    for i in range(len(Characters)): # loop through the Characters list
        print(f"{i+1} - {Characters[i].name} has the following units:")
        for unit in Characters[i].units: # loop though it's units
            print(f"{unit.name} - Health: {unit.health} | Power: {unit.GetPower()}") # Unit name, unit health and unit power (an average of every attack damages)
        
    character = None

    while True:
        character = int(input(f"Player {player}, choose a character: "))

        if character-1 > len(Characters):
            print(f"Must be a number between 1 and {len(Characters)}")
        else:
            break

    return Characters[character-1]

def placeUnitStartPosition(player, char):
    clear()
    print(f"{char.name}, choose where to place each unit")

    for unit in char.units:
        choosing = True
        while choosing:
            x = [0,1,2]
            if player == "B": x = [7,8,9]

            sentence = f"\n{unit.name} - Select a location with x between {x[0]} and {x[2]} (type \"x,y\" without the \"): "

            #try:

            location = tuple(input(sentence).split(','))
            print(location[0],location[1])
            location = tuple([int(location[0]),int(location[1])])
            print(location)

            print(game.IsThereSomething(location) or not location[0] in x)
            if game.IsThereSomething(location) or not location[0] in x :
                print(f"There is already something here or x position isn't between {x[0]} and {x[2]}")
            else:
                game.PlaceUnit(unit, location)
                choosing = False


            #except: print("Invalid input, 2 numbers separated by a coma were expected")


# Initialization of the 2 users ( PVP )
name1 = chooseUsername("A")
char1 = chooseCharacter("A")
placeUnitStartPosition("A", char1)

while True: # loop to make sure the Player B doesn't choose the same username
    name2 = chooseUsername("B")
    if name2 == name1:
        print("You can't have the same username as Player A")
    else:
        break
while True:
    char2 = chooseCharacter("B")
    if char2 == char1:
        print("You can't have the same character as Player A")
    else:
        break
placeUnitStartPosition("B", char2)

clear()

# Recusrive function to let the player choose what action to do
# If num == 0: first try, every choice possible
# If num == 1: player moved, he can do everything but move
# If num == 2: player did something impossible, he has to restart
def playerChoice(char, enemy, num):
    global selectedUnit, selectedAction, selectedSubAction, selectedTarget

    if num == 2: print("\nYou have to input your informations again, this is probably due to the fact that you tryed to accomplish something impossible.")

    # Choosing a unit
    if num != 1:
        choosing = True
        while choosing:
            try: # We want to make sure to get a valid input.
                units = char.units
                print("\nSelect a unit")  
                for i in range(len(units)):
                    print(f"{i+1} - {units[i].name} - {units[i].GetHealthPercent()}% Health")
                selectedUnit = units[int(input("Enter a number: "))-1]
            except: print("No unit associated to this number") # User inputed something incorrect
            else: choosing = False
            
    # Choosing an action
    choosing = True
    while choosing:
        try:
            actions = ["Move", "Attack"]
            if num == 1:
                actions.pop(0)
            if selectedUnit.abilities:
                actions += ["Ability"]

            print("\nSelect an action: ")  
            for i in range(len(actions)):
                print(f"{i+1} - {actions[i]}")
            selectedAction = actions[int(input("Enter a number: "))-1]
        except: print("No action associated to this number")
        else: choosing = False

    # Choosing a sub action (what attack, what ability or what location to move to)
    choosing = True
    while choosing:
            if selectedAction == "Attack":

                selectedSubAction = selectedUnit.Attack
                print("\nSelect a target: ")  

                try:

                    units = enemy.units
                    for i in range(len(units)):
                        print(f"{i+1} - {units[i].name} - {units[i].GetHealthPercent()}% Health")
                    selectedTarget = units[int(input("Enter a number: "))-1]

                except: print("No target associated to this number")
                else: choosing = False

            elif selectedAction == "Ability":

                selectedSubAction = selectedUnit.UseAbility
                print("\nSelect a target: ")

                try:

                    units = char.units
                    for i in range(len(units)):
                        print(f"{i+1} - {units[i].name} - {units[i].GetHealthPercent()}% Health")
                    selectedTarget = units[int(input("Enter a number: "))-1]

                except: print("No target associated to this number")
                else: choosing = False

            elif selectedAction == "Move":
                print(f"\nYour unit is at {game.KnowPosition(selectedUnit)} max distance is {selectedUnit.maxDistance}")
                sentence = "\nSelect a location (type \"x,y\" without the \"): "
                try:

                    location = tuple(input(sentence).split(','))
                    location = tuple(int(location[0]),int(location[1]))
                    print(location)

                    if not game.MoveUnit(selectedUnit, location):
                        print("This location is too far away")

                    playerChoice(char, enemy, 1)

                except: print("Invalid input, 2 numbers separated by a coma were expected")
                else: choosing = False

            else:
                ...




playing = True
while playing:
    playerChoice(char1, char2, 0)
    print(selectedUnit, selectedAction, selectedSubAction, selectedTarget)
    break