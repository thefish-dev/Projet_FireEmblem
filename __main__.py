"""
Projet Fire Emblem
"""

from os import system
from packages import *

clear = lambda: system("cls")


Characters = [
    Character("Char1", [
        Unit("Unit1", "Water", 80, 5, [
            Attack("Attack1", "This is attack 1", 10),
            Attack("Attack2", "This is attack 2", 10),
        ],
            Ability("Heal", "CanHeal"), 
            None
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



def chooseUsername(player):
    clear()
    name = input(f"Player {player}, choose a username: ")
    while True:
        user = input("Do you confirm ? y/n : ")
        if user == "y":
            return name
        elif user == "n":
            break
        else:
            clear()
            print("Invalid input, 'y' or 'n' expected")
            
    chooseUsername(player)

def chooseCharacter(player):
    clear()
    for i in range(len(Characters)):
        print(f"{i+1} - {Characters[i].name} has the following units:")
        for unit in Characters[i].units:
            print(f"{unit.name} - Health: {unit.health} | Power: {unit.GetPower()}")
        
    character = None    
    while True:
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
            
            
name1 = chooseUsername("A")
char1 = chooseCharacter("A")
name2 = chooseUsername("B")
char2 = chooseCharacter("B")

clear()

print(name1)
print(char1.name)