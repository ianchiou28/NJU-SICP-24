test = {
  'name': 'Problem 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '1ec020ee81a869e70101adea96878d6e',
          'choices': [
            r"""
            It represents health protecting the insect, so the insect can only
            be damaged when its health reaches 0
            """,
            r"""
            It represents the strength of an insect against attacks, which
            doesn't change throughout the game
            """,
            r"""
            It represents the amount of health the insect has left, so the
            insect is eliminated when it reaches 0
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the significance of an Insect's health attribute? Does this
          value change? If so, how?
          """
        },
        {
          'answer': 'c26661d8732787e750a72b7157b9df56',
          'choices': [
            'damage',
            'health',
            'place',
            'bees'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following is a class attribute of the Insect class?'
        },
        {
          'answer': 'cd2fcb949983b8933549b8c3dd4f18a8',
          'choices': [
            'instance, each Ant instance needs its own health value',
            'instance, each Ant starts out with a different amount of health',
            'class, Ants of the same subclass all have the same amount of starting health',
            'class, when one Ant gets damaged, all ants receive the same amount of damage'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Is the health attribute of the Ant class an instance attribute or class attribute? Why?'
        },
        {
          'answer': '5a6fca3b4af1eaca1293afd21c217645',
          'choices': [
            'instance, each Ant does damage to bees at different rates',
            'instance, the damage an Ant depends on where the Ant is',
            'class, all Ants of the same subclass deal the same damage',
            'class, all Ants deal the same damage'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          Is the damage attribute of an Ant subclass (such as ThrowerAnt) an
          instance or class attribute? Why?
          """
        },
        {
          'answer': '51a92b8c40b4e27a6570dafbffca301c',
          'choices': [
            'Insect',
            'Place',
            'Bee',
            'Ant'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which class do both Ant and Bee inherit from?'
        },
        {
          'answer': '6f3bb9fcab6f6c4bd0c852557dafde76',
          'choices': [
            r"""
            Ants and Bees both have the attributes health, damage, and place
            and the methods reduce_health and action
            """,
            r"""
            Ants and Bees both have the attribute damage and the methods
            reduce_health and action
            """,
            'Ants and Bees both take the same action each turn',
            'Ants and Bees have nothing in common'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What do instances of Ant and instances of Bee have in common? Please choose the most correct answer.'
        },
        {
          'answer': '0ea57f80439a85f5000877d8caa400e9',
          'choices': [
            'There can be one Ant and many Bees in a single Place',
            'There can be one Bee and many Ants in a single Place',
            'There is no limit on the number of insects of any type in a single Place',
            'Only one insect can be in a single Place at a time'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many insects can be in a single Place at any given time in the
          game (before Problem 8)?
          """
        },
        {
          'answer': 'f3b730702ad1b337d70780fcbe5dba22',
          'choices': [
            'The bee moves to the next place, then stings the ant in that place',
            'The bee flies to the nearest Ant and attacks it',
            'The bee stings the ant in its place or moves to the next place if there is no ant in its place',
            'The bee stings the ant in its place and then moves to the next place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a Bee do during one of its turns?'
        },
        {
          'answer': 'cc11d32a37b27d4fa87f5d43c7c0e4c9',
          'choices': [
            'When the bees enter the colony',
            'When the colony runs out of food',
            'When any bee reaches the end of the tunnel or when the Queen Ant is killed',
            'When any bee reaches the end of the tunnel and the Queen Ant is killed',
            'When no ants are left on the map'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the game lost?'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
