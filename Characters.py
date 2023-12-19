from packages import *

Characters = [
    Character("Urart", [ # list of Unit instances
        Unit(name="Minibombe", unitType="Feu", maxHealth=80, maxDistance=3, 
        attacks=[ # list of Attack instances
            Attack(name="Explosion Grotesque", desc="Cette attaque est une attaque trés forte \nmais l'unité minibombe meurre lors de l'attaque", damages=90, range=2, sacrifice=True),
            Attack("C4", "La minibombe lance un C4 sur son adversaire \n3 cases max", 30, 3, False),
        ],
        abilities=[ # list of Ability instances
            Ability(name="Protéger", desc="Peut protéger", max_uses=1)
        ]
        ),
        Unit("Ouantit_the_wizard", "Magie", 100, 5, 
        attacks=[
            Attack("Coup de foudre", "Cette attaque électrocute une unité, \n2 case max", 20, 2, False)
        ],
        abilities=[
            Ability("Vol", "Vous pouvez volez aléatoirement une attaque \nque vous pourrez utiliser au prochain tour UNIQUEMENT.", 1)
        ]
        )
    ]),
    Character("Metde", [
        Unit("Singe mangeur de viande", "Viandard", 110, 5, 
        attacks=[
            Attack("Coup de chico super chockboar", "Le singe vous mord si fort que \nl'adversaire hurle à la mort", 30, 1, False),
            Attack("Coup de pied retourner en highkick", "Cette attaque est trés puissante !", 75, 1, False),
        ],
        abilities=None
        ),
        Unit("Dustin Poirier", "Punch", 60, 5, 
        attacks=[
            Attack("Ground and pound", "Cette attaque de corps à corps \nest agressive et puissante", 35, 1, False),
            Attack("étranglement en guillotine", "ataque trés puisante , il ne faut pas \nmettre en rage dustin Poirier", 60, 1, False)
        ],
        abilities=None
        )
    ]),
    Character("Godi", [
        Unit("Stone", "Pierre", 200, 5, 
        attacks=[
            Attack("Charge", "Il te fonce dedans avec son gros crane de pierre ", 25, 2, False),
            Attack("Tremblement de terre", "Il peut faire trembler le sol \net ainsi infliger des dégats", 20, 2, False),
        ],
        abilities=[
            Ability("Protéger", "Il lance une pierre devant un de ses collégues, \nce qui empêche toute attaque", 1)
        ]
        ),
        Unit("Serpent ", "feuille", 60, 5, 
        attacks=[
            Attack("Etranglement en guillotine", "Le serpent étrangle l'unité.", 35, 1, False),
            Attack("Morsure", "Le serpent tempoisonne, \nl'unité perd alors 20 pv par tour", 20, 1, False),
        ],
        abilities=[
            Ability("Soin","Ce serpent est aussi un serpent radioactif, \nil peut alors soigner de 20 pv une de vos unités", 2)
        ]
        )
    ])
]


character = Characters[0]
nom_attaque = character.units[0].attacks[0].name