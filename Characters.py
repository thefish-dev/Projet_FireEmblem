from packages import *

Characters = [
    Character("Urart", [ # list of Unit instances
        Unit(name="Minibombe", Unittype="Feu", maxHealth=80, maxDistance=5, 
        attacks=[ # list of Attack instances
            Attack("Explosion Grotesque", "Cette attaque est une attaque trés forte mais l'unité minibombe meurre lors de l'attaque", 90),
            Attack("C4", "Cette attaque peut s'utiliser à distance (de 3 cases max) car la minibombe lance un C4 sur son adversaire ", 30),
        ],
        abilities=[ # list of Ability instances
            Ability("Protéger", "Peut protéger")
        ]
        ),
        Unit("Ouantit_the_wizard", "Magie", 100, 5, 
        attacks=[
            Attack("Vol", "Vous pouvez volez n'importe quelle attaque de n'importe quelle unité", None),# il faut qu'on fasse en sorte que sa marche
            Attack("Coup de foudre", "Cette attaque electrocute une unité, vous pouvez l'utiliser à une distance de 2 case max", 20),

        ],
        abilities=[
            Ability("Bouclier","Le mage peut ne pas recevoir des attaques car il crée un bouclier")
        ]
        )
    ]),
    Character("Metde", [
        Unit("Singe mangeur de viande", "Viandard", 110, 5, 
        attacks=[
            Attack("Coup de chico super chokbar", "Le singe vous mord si fort que l'adversaire hurle à la mort", 25),
            Attack("Coup de pied retourner en highkick", "Cette attaque est trés puissante et fait donc beaucoup de dégats", 75),
        ],
        abilities=None
        ),
        Unit("Dustin Poirier", "Punch", 60, 5, 
        attacks=[
            Attack("Ground and pound", "Cette attaque est agressive et puissante mais elle necessite d'étre proche pour étre utiliser (1 case)", 35),
            Attack("", "", 20),
        ],
        abilities=None
        )
    ]),
    Character("Godi", [
        Unit("Stone", "Pierre", 200, 5, 
        attacks=[
            Attack("Charge", "Il te fonce dedans avec son gros crane de pierre ", 25),
            Attack("Tremblement de terre", "Il peut faire trembler le sol et ainsi infliger des dégats", 20),
        ],
        abilities=[
            Ability("Protéger", "Il lance une pierre devant un de ses collégues, ce qui empêche toute attaque")
        ]
        ),
        Unit("Serpent ", "feuille", 60, 5, 
        attacks=[
            Attack("Etranglement en guillotine", "Le serpent étrangle l'unité.", 35),
            Attack("Morsure", "Le serpent tempoisonne, l'unité perd alors 20 pv par tour", 20),
        ],
        abilities=[
            Ability("Soin","Ce serpent est aussi un serpent radioactif, il peut alors soigner de 20 pv une de vos unités")
        ]
        )
    ])
]