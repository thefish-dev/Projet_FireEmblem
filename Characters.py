from packages import *

Characters = [
    Character("Char1", [ # list of Unit instances
        Unit("Unit1", "Water", 80, 5, [ # list of Attack instances
            Attack("Attack1", "This is attack 1", 10),
            Attack("Attack2", "This is attack 2", 10),
        ],
        [ # list of Ability instances
            Ability("Heal", "Can Heal", True)
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
        [
            Ability("Heal", "Can Heal", True)
        ], 
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