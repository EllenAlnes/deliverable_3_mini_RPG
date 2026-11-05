
from task1_characterclass import *
from task2_dice_class_randomeness import *
from task3_character_special import *

# Create a Battle class to manage turn-based combat between two Character objects.
# 1) Initialize Battle with hero: Character and enemy: Character .
# No Mage or Warrior?
# Composition (and inheritance?)

class Battle:
    """"""
    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy


# 2) Implement a play_round() method where hero attacks enemy , and if enemy
# is still alive, enemy attacks hero .

    def play_round() -> bool:

# 3) Implement a simulate_battle() method with a while loop that runs rounds
# until one character is no longer alive.

    def simultate_battle() -> None:
        while True:
            play_round()

