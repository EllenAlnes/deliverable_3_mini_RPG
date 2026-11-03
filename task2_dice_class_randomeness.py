# Create a dice class 
# Use randomness
# n-sided dice - default 6
# methods:
    # roll() - using random.randint(1, self.sides)
    # __repr__ - Dice(sides=6)
    # __call__ - d20 = Dice(sides=20) - by calling d20.roll()

import random


class Dice:
    """This class represents the dice in the game, using randomness. 
    With equal statistic probability to roll the different sides."""

    # __init__ kjøres hver gang man oppretter et nytt objekt i klassen
    def __init__(self, sides: int = 6) -> None:
        """Initialise the dice. Default value for sides is 6. It must have a minimum of 2 sides. """

        # The dice must have a minimum of 2 sides
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        
        self.sides = sides

    def roll(self) -> int:
        """Rolling the dice. Using random it roles the dice depending on its sides, with equal statistical probability for each value."""
        random.randint(1, self.sides)