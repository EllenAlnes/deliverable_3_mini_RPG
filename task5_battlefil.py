
from task1_characterclass import Character
from task2_dice_class_randomeness import Dice
from task3_character_special import Mage, Warrior
from items import Weapon

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

        Returns whether the hero and enemy are alive after the round."""

        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

        hero_life = self.hero.is_alive
        enemy_life = self.enemy.is_alive

        # lage en loop som sjekker ulike situasjoner, printer all status
        for attacker, target in ((self.hero, self.enemy), (self.enemy, self.hero)):
            if not attacker.is_alive:
                break

            if isinstance(attacker, Mage) and attacker.mana >= 10:
                action = "uses a mana-powered attack"
            elif attacker.weapon is not None:
                action = f"attacks with {attacker.weapon.name}"
            else:
                action = "attacks"

            print(f"{attacker.name} ({type(attacker).__name__}) {action} {target.name}!")
            attacker.attack(target)
            print(f"{target.name} has {target.hp} HP left.")

        print(f"hero hp: {self.hero.hp} and enemy hp: {self.enemy.hp}")

        return hero_life, enemy_life

# 3) Implement a simulate_battle() method with a while loop that runs rounds
# until one character is no longer alive.

    def simulate_battle(self) -> tuple[bool, bool]:
        """Run rounds until one character is defeated and return their alive states."""
        hero_life = self.hero.is_alive
        enemy_life = self.enemy.is_alive
        while hero_life and enemy_life:
            hero_life, enemy_life = self.play_round()
        return hero_life, enemy_life


hero = Warrior("Per")
enemy = Mage("Hans")

battle = Battle(hero, enemy)
hero_life, enemy_life = battle.simulate_battle()