from packages import *

Characters = [
    Character(
        name="Urart", 
        desc="""Equipe réflechie et méthodique mais Bombe est suicidaire ce qui ne fait pas la
        fierté du puissant mage noir, un voleur capable de foudroyer ses énemis""", 
        units=[ # list of Unit instances
            Unit(name="Minibombe", image="./Images/bombe.png", unitType="Feu", maxHealth=80, maxDistance=3, 
            attacks=[ # list of Attack instances
                Attack(name="Explosion Grotesque", desc="Cette attaque est une attaque trés forte \nmais l'unité minibombe meurre lors de l'attaque", damages=90, range=2, sacrifice=True),
                Attack("C4", "La minibombe lance un C4 sur son adversaire \n3 cases max", 30, 3, False),
            ],
            abilities=[ # list of Ability instances
                Ability(name="Protéger", desc="Peut protéger", max_uses=1)
            ]
            ),
            Unit("Ouantit_the_wizard", "./Images/mage.png", "Magie", 100, 5, 
            attacks=[
                Attack("Coup de foudre", "Cette attaque électrocute une unité, \n2 case max", 20, 2, False)
            ],
            abilities=[
                Ability("Vol", "Vous pouvez volez aléatoirement une attaque \nque vous pourrez utiliser au prochain tour UNIQUEMENT.", 1)
            ]
            )
        ]
    ),
    Character(
        name="Metde", 
        desc="""Equipe dotée d'une force et d'une puissance exeptionnel grace à leur éxperience
        en MMA, cette unité n'a pas d'abilités, tous dans les muscles, rien dans la tête""",
        units=[
            Unit("Singe mangeur de viande", "./Images/singe.png", "Viandard", 110, 5, 
            attacks=[
                Attack("Coup de chico super chockboar", "Le singe vous mord si fort que \nl'adversaire hurle à la mort", 30, 1, False),
                Attack("Coup de pied retourner en highkick", "Cette attaque est trés puissante !", 75, 1, False),
            ],
            abilities=None
            ),
            Unit("Dustin Poirier", "./Images/dustin_poirier.png", "Punch", 60, 5, 
            attacks=[
                Attack("Ground and pound", "Cette attaque de corps à corps \nest agressive et puissante", 35, 1, False),
                Attack("étranglement en guillotine", "ataque trés puisante , il ne faut pas \nmettre en rage dustin Poirier", 60, 1, False)
            ],
            abilities=None
            )
        ]
    ),
    Character(
        name="Godi", 
        desc="""Equipe vicieuse car le gros stone peut proteger Serpent, ce denier n'ayant pas
        beaucoup de vie contrairement à ce gros tank de Stone. Cependant, Serpent peut soigner""",
        units=[
            Unit("Stone", "./Images/stone.png", "Pierre", 200, 5, 
            attacks=[
                Attack("Charge", "Il te fonce dedans avec son gros crane de pierre ", 25, 2, False),
                Attack("Tremblement de terre", "Il peut faire trembler le sol \net ainsi infliger des dégats", 20, 2, False),
            ],
            abilities=[
                Ability("Protéger", "Il lance une pierre devant un de ses collégues, \nce qui empêche toute attaque", 1)
            ]
            ),
            Unit("Serpent ", "./Images/serpent.png", "feuille", 60, 5, 
            attacks=[
                Attack("Etranglement en guillotine", "Le serpent étrangle l'unité.", 35, 1, False),
                Attack("Morsure", "Le serpent tempoisonne, \nl'unité perd alors 20 pv par tour", 20, 1, False),
            ],
            abilities=[
                Ability("Soin","Ce serpent est aussi un serpent radioactif, \nil peut alors soigner de 20 pv une de vos unités", 2)
            ]
            )
        ]
    )
]