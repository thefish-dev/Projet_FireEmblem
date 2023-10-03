"""
Projet Fire Emblem
"""

from packages import *

Characters = [
    Character("Char1", [
        Unit("Unit1", "Water", 100, 5, [
            Attack("Attack1", "This is attack 1", 10),
            Attack("Attack2", "This is attack 2", 10),
        ],
        [
            Ability("Ability1", "This is ability 1"),
            Ability("Ability2", "This is ability 2"),
        ],
        [
            Property("Property1", "This is property 1"),
            Property("Property2", "This is property 2"),
        ],
        )
    ])
]



def chooseUsername(player):
    name = input(f"Player {player}, choose a username: ")
    while True:
        user = input("Do you confirm ? y/n")
        if user == "y":
            return name
        elif user == "n":
            chooseUsername(player)
        else:
            print("Invalid input, 'y' or 'n' expected")
            
name1 = chooseUsername("A")
name2 = chooseUsername("B")

def chooseCharacter(player):
    for char in 
    character = input(f"Player {player}, choose a character: ")
    while True:
        user = input("Do you confirm ? y/n")
        if user == "y":
            return character
        elif user == "n":
            chooseUsername(player)
        else:
            print("Invalid input, 'y' or 'n' expected")