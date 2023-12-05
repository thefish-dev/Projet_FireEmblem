from packages import *

Characters = [
    Character("Urart", [ # list of Unit instances
        Unit("Minibombe", "feu", 80, 5, [ # list of Attack instances
            Attack("Grotesque explosion", "Cette attaque est une attaque trés forte mais l'unité minibombe meurre lors de l'attaque", 90),
            Attack("C4", "Cette attaque peut s'utiliser à distance (de 3 case max) car la minibombe lance un C4 sur son adversaire ", 30),
        ],
        [ # list of Ability instances
            Ability("Attaque de loin", "meure lors d'une de ses attaque", True)
        ], 
            None, # list of Property instances, None for this unit.
        ),
        Unit("Ouantit_the_wizard", "magie", 100, 5, [
            Attack("vol", "Vous pouvez volez n'importe quelle attaque de n'importe quelle unité", None),# il faut qu'on fasse en sorte que sa marche
            Attack("Coup de foudre", "Cette attaque electrocute une unité, vous pouvez l'utiliser à une distance de 2 case max", 20),
        ],
            None, 
            None,
        )
    ]),
    Character("Metde", [
        Unit("Singe mangeur de viande", "Viandard", 110, 5, [
            Attack("Coup de chico super chokbar", "Le singe vous mord si fort que l'adversaire hurle a la mort", 25),
            Attack("Coup de pied retourner en highkick", "Cette attaque est trés puissante et fait donc beaucoup de dégat", 100),
        ],
        [
            Ability("Soin", "il peut se soigner", True)
        ], 
            None,
        ),
        Unit("Dustin Poirier", "Punch", 60, 5, [
            Attack("Ground and pound", "Cette attaque est agressive et puissante mais elle necessite d'étre proche pour étre utiliser (1 case)", 15),
            Attack("", "This is attack 2", 20),
        ],
            None, 
            None,
        )
    ])
]