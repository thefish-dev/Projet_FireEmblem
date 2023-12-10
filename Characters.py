from packages import *

Characters = [
    Character("Urart", [ # list of Unit instances
        Unit("Minibombe", "Feu", 80, 5, 
        attacks=[ # list of Attack instances
            Attack("Explosion Grotesque", "Cette attaque est une attaque trés forte mais l'unité minibombe meurre lors de l'attaque", 90),
            Attack("C4", "Cette attaque peut s'utiliser à distance (de 3 cases max) car la minibombe lance un C4 sur son adversaire ", 30),
        ],
        abilities=[ # list of Ability instances
            Ability("Attaque de loin", "meurt lors d'une de ses attaque")
        ]
        ),
        Unit("Ouantit_the_wizard", "Magie", 100, 5, 
        attacks=[
            Attack("Vol", "Vous pouvez volez n'importe quelle attaque de n'importe quelle unité", None),# il faut qu'on fasse en sorte que sa marche
            Attack("Coup de foudre", "Cette attaque electrocute une unité, vous pouvez l'utiliser à une distance de 2 case max", 20),
        ],
        abilities=None,
        )
    ]),
    Character("Metde", [
        Unit("Singe mangeur de viande", "Viandard", 110, 5, 
        attacks=[
            Attack("Coup de chico super chokbar", "Le singe vous mord si fort que l'adversaire hurle à la mort", 25),
            Attack("Coup de pied retourner en highkick", "Cette attaque est trés puissante et fait donc beaucoup de dégats", 75),
        ],
        abilities=[
            Ability("Soin", "il peut se soigner"),
            Ability("Aveugler", "il peut aveugler un adversaire, l'empêchant d'attaquer au prochain tour."),
        ]
        ),
        Unit("Dustin Poirier", "Punch", 60, 5, 
        attacks=[
            Attack("Ground and pound", "Cette attaque est agressive et puissante mais elle necessite d'étre proche pour étre utiliser (1 case)", 35),
            Attack("", "This is attack 2", 20),
        ],
        abilities=None
        )
    ])
]