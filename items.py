# Create a Weapon class in items.py that utilizes your Dice class for damage
# calculations. We call the module items.py rather than weapons.py so that it can be
# expanded to include other items your characters can hold.

# Define the class Weapon with the attributes name and damage_dice: Dice.
# Include a roll_damage() method that calls self.damage_dice.roll()
# Update Character.__init__ to accept an optional weapon.
# If a character has an equipped weapon, attack() should roll damage from the weapon instead of using default base damage.

class Weapon:
    """Docstring for Weapon"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        # Initialise weapon
        name = 
        damage_dice = 
        pass


    def roll_damage(self) -> int:
        # Roll the damage dice
        # calls self.damage_dice.roll()
        pass