# Create a dice class 
# Use randomness
# n-sided dice - default 6
# methods:
    # roll() - using random.randint(1, self.sides)
    # __repr__ - Dice(sides=6)
    # __call__ - d20 = Dice(sides=20) - by calling d20.roll()

# __init__() oppretter og initialiserer objektet.
# __repr__() bestemmer hvordan objektet representeres som tekst.
# __call__() gjør at objektet kan brukes som en funksjon.

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
            # raise issues an error of our choise.
            # here it shows an error message if there are not enough sides on the dice
        
        self.sides = sides

    def roll(self) -> int:
        """Rolling the dice. Using random it roles the dice depending on its sides, with equal statistical probability for each value."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Shows the representation of the dice. Shows the amount of sides."""
        # method that returns string representation like Dice(sides=6)
        return f"Dice(sides={self.sides})"
        

    def __call__(self, *args, **kwds):
        # lar meg bruke objektet som om det var en funksjon
        # det som kommer opp om jeg bare skriver dice() ?
        # method that allow you to roll the dice created by d20 = Dice(sides=20) by calling d20.roll()
        # denne skal kjøre roll funksjonen
        #self.roll
        pass

dice1 = Dice()
# dice2 = Dice(20)
# dice3 = Dice(1)

print(repr(dice1))