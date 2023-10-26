"""
Projet Fire Emblem
"""

from os import system
from packages import * # Every classes in the folder ./packages

clear = lambda: system("cls") # Simple command to clear the console, can be used like so: clear()

# Characters list containing instances of class Character
Characters = [
    Character("Char1", [ # list of Unit instances
        Unit("Unit1", "Water", 80, 5, [ # list of Attack instances
            Attack("Attack1", "This is attack 1", 10),
            Attack("Attack2", "This is attack 2", 10),
        ],
        [ # list of Ability instances
            Ability("Heal", "CanHeal")
        ], 
            None, # list of Property instances, None for this unit.
        ),
        Unit("Unit2", "Fire", 100, 5, [
            Attack("Attack1", "This is attack 1", 15),
            Attack("Attack2", "This is attack 2", 20),
        ],
            None, 
            None,
        )
    ]),
    Character("Char2", [
        Unit("Unit3", "Earth", 110, 5, [
            Attack("Attack1", "This is attack 1", 10),
            Attack("Attack2", "This is attack 2", 10),
        ],
            None, 
            None,
        ),
        Unit("Unit4", "Air", 60, 5, [
            Attack("Attack1", "This is attack 1", 15),
            Attack("Attack2", "This is attack 2", 20),
        ],
            None, 
            None,
        )
    ])
]


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

# Initialization of the 2 users ( PVP )
name1 = chooseUsername("A")
char1 = chooseCharacter("A")

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

clear()

# Recusrive function to let the player choose what action to do
# If num == 0: first try, every choice possible
# If num == 1: player moved, he can do everything but move
# If num == 2: player did something impossible, he has to restart
def playerChoice(char, num):
    if num == 2: print("\nYou have to input your informations again, this is probably due to the fact that you tryed to accomplish something impossible.")
    if num != 1:
        global selectedUnit
        while True:
            try: # We want to make sure to get a valid input.
                units = char.units
                print("\nSelect a unit")  
                for i in range(len(units)):
                    print(f"{i+1} - {units[i].name}")
                selectedUnit = units[int(input("Enter a number: "))-1]
            except: print("No unit associated to this number") # User inputed something incorrect
            else: break
            
        while True:
            try: # We want to make sure to get a valid input.
                actions = {}
                if selectedUnit.abilities:
                    actions["Abilitiy"] = selectedUnit.abilities
                if selectedUnit.attacks:
                    actions["Attack"] = selectedUnit.attacks
                actions["Move"] = Game
                print("\nSelect a unit")  
                for i in range(len(units)):
                    print(f"{i+1} - {units[i].name}")
                selectedUnit = units[int(input("Enter a number: "))-1]
            except: print("No unit associated to this number") # User inputed something incorrect
            else: break

game = Game(10)

while False:
    playerChoice(char1,0)
    break