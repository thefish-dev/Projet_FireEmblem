from packages import *

Characters = [
    Character("Urart", [ # list of Unit instances
        Unit(name="Minibombe", unitType="Feu", maxHealth=80, maxDistance=3, 
        attacks=[ # list of Attack instances
            Attack(name="Explosion Grotesque", desc="Cette attaque est une attaque trés forte mais l'unité minibombe meurre lors de l'attaque", damages=90, range=2),
            Attack("C4", "Cette attaque peut s'utiliser à distance (de 3 cases max) car la minibombe lance un C4 sur son adversaire ", 30, 3),
        ],
        abilities=[ # list of Ability instances
            Ability(name="Protéger", desc="Peut protéger", max_uses=1)
        ]
        ),
        Unit("Ouantit_the_wizard", "Magie", 100, 5, 
        attacks=[
            Attack("Coup de foudre", "Cette attaque electrocute une unité, vous pouvez l'utiliser à une distance de 2 case max", 20, 2)
        ],
        abilities=[
            Ability("Vol", "Vous pouvez volez aléatoirement une attaque de n'importe quelle unité que vous pourrez utiliser au prochain tour UNIQUEMENT.", 1)
        ]
        )
    ]),
    Character("Metde", [
        Unit("Singe mangeur de viande", "Viandard", 110, 5, 
        attacks=[
            Attack("Coup de chico super chokbar", "Le singe vous mord si fort que l'adversaire hurle à la mort", 30, 1),
            Attack("Coup de pied retourner en highkick", "Cette attaque est trés puissante !", 75, 1),
        ],
        abilities=None
        ),
        Unit("Dustin Poirier", "Punch", 60, 5, 
        attacks=[
            Attack("Ground and pound", "Cette attaque est agressive et puissante mais elle necessite d'étre proche pour étre utiliser (1 case)", 35, 1),
            Attack("étranglement en guillotine", "ataque trés puisante , il ne faut pas mettre en rage dustin Poirier", 60, 1)
        ],
        abilities=None
        )
    ]),
    Character("Godi", [
        Unit("Stone", "Pierre", 200, 5, 
        attacks=[
            Attack("Charge", "Il te fonce dedans avec son gros crane de pierre ", 25, 2),
            Attack("Tremblement de terre", "Il peut faire trembler le sol et ainsi infliger des dégats", 20, 2),
        ],
        abilities=[
            Ability("Protéger", "Il lance une pierre devant un de ses collégues, ce qui empêche toute attaque", 1)
        ]
        ),
        Unit("Serpent ", "feuille", 60, 5, 
        attacks=[
            Attack("Etranglement en guillotine", "Le serpent étrangle l'unité.", 35, 1),
            Attack("Morsure", "Le serpent tempoisonne, l'unité perd alors 20 pv par tour", 20, 1),
        ],
        abilities=[
            Ability("Soin","Ce serpent est aussi un serpent radioactif, il peut alors soigner de 20 pv une de vos unités", 2)
        ]
        )
    ])
]