
from task1_characterclass import *
from task2_dice_class_randomeness import *
from task3_character_special import *

# Create a Battle class to manage turn-based combat between two Character objects.
# 1) Initialize Battle with hero: Character and enemy: Character .
# Composition (and inheritance?)

class Battle:
    """A battle between hero and enemy"""
    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

# 2) Implement a play_round() method where hero attacks enemy , and if enemy
# is still alive, enemy attacks hero .

    def play_round(self) -> tuple[bool, bool]:
        """Play one round. Hero attacks enemy, enemy attacks if enemy still alive.

        Returns: 
            hero_life: bool, hero is alive or not.
            enemy_life: bool, enemy is alive or not.
            print: a print of hero's and enemy's hp after round.""" 

        self.hero.attack()

        hero_life = bool(self.hero.is_alive)
        enemy_life = bool(self.enemy.is_alive)

        print(f"hero hp: {self.hero.hp_max} and enemy hp: {self.enemy.hp_max}")

        return hero_life, enemy_life

# 3) Implement a simulate_battle() method with a while loop that runs rounds
# until one character is no longer alive.

    def simultate_battle(self, hero_life, enemy_life) -> str:
        """Creates a print of """
        while hero_life is True and enemy_life is True:
            self.play_round()


hero = Warrior("Per")
enemy = Mage("Hans")

Battle()