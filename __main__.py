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
            None # list of Property instances, None for this unit.
        ),
        Unit("Unit2", "Fire", 100, 5, [
            Attack("Attack1", "This is attack 1", 15),
            Attack("Attack2", "This is attack 2", 20),
        ],
            None, 
            None
        )
    ]),
    Character("Char2", [
        Unit("Unit3", "Earth", 110, 5, [
            Attack("Attack1", "This is attack 1", 10),
            Attack("Attack2", "This is attack 2", 10),
        ],
            None, 
            None
        ),
        Unit("Unit4", "Air", 60, 5, [
            Attack("Attack1", "This is attack 1", 15),
            Attack("Attack2", "This is attack 2", 20),
        ],
            None, 
            None
        )
    ])
]


# Recursive function to let the user choose a name.
def chooseUsername(player):
    clear() # lambda function to clear the console using os.system('cls')
    name = input(f"Player {player}, choose a username: ")
    while True: # repeat until valid input ('y' or 'n')
        user = input("Do you confirm ? y/n : ")
        if user == "y":
            return name
        elif user == "n": # if the user wants to choose another name
            break
        else:
            clear()
            print("Invalid input, 'y' or 'n' expected")
            
    chooseUsername(player)

# Recursive function to let the user choose a character in the Characters list.
def chooseCharacter(player):
    clear()
    for i in range(len(Characters)): # loop through the Characters list
        print(f"{i+1} - {Characters[i].name} has the following units:")
        for unit in Characters[i].units: # loop though it's units
            print(f"{unit.name} - Health: {unit.health} | Power: {unit.GetPower()}") # Unit name, unit health and unit power (an average of every attack damages)
        
    character = None    
    while True: # loop to make sure the user input a valid number
        try:
            character = int(input(f"Player {player}, choose a character: "))
        except: print(f"Must be a number between 1 and {len(Characters)}")
        else: break
        
    while True:
        user = input("Do you confirm ? y/n : ")
        if user == "y":
            return Characters[character-1]
        elif user == "n":
            break
        else:
            clear()
            print("Invalid input, 'y' or 'n' expected")
        
    chooseCharacter(player)
            
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
def playerChoice(player, num):
    ...