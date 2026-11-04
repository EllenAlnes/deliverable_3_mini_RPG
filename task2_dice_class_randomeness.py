# roll()     using random.randint(1, self.sides), ruller terning
# __init__() oppretter og initialiserer objektet.
# __repr__() bestemmer hvordan objektet representeres som tekst.
# __call__() gjør at objektet kan brukes som en funksjon.

import random


class Dice:
    """Represent a dice used in the RPG game.
    
    The dice can have any number of sides, with a minimum of 2.
    Each side has an equal probability of being rolled."""

    # __init__ runs each time an object is created
    def __init__(self, sides: int = 6) -> None:
        """Initialise a Dice object.

        Arguments:
            sides (int): Number of sides on the dice. Default to 6.
                        Must be an integer greater than or equal to 2.

         Returns:
            None 
        """

        # Controlling that the amount of sides is an integer
        if not isinstance(sides, int):
            raise TypeError("A dice must be given an integer number of sides.")

        # The dice must have a minimum of 2 sides
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
            # raise issues an error of our choise.
            # here it shows an error message if there are not enough sides on the dice
        
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and generate a random result.

        Returns:
            int: A random integer between 1 and the number of sides
        """
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Return a string representation of the Dice object.

        Returns:
            str: A string showing the number of sides, e.g. Dise(sides=6)
        """
        return f"Dice(sides={self.sides})"
        
    def __call__(self) -> int:
        """Allow the Dice object to be called as a function.
        
        Returns:
            int: The result of a dice roll."""
        # By calling the object the roll function runs - must print to se in terminal
        return self.roll()


# Tests that should work
# dice1 = Dice()
# d20 = Dice(sides=20)

# print(repr(dice1))
# print(repr(d20))

# print(dice1.roll())
# print(d20.roll())

# print(dice1())
# print(d20())

# tests that should raise value and type errors
#Dice(1)
#Dice(2.5)