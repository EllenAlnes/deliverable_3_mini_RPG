# TASK 4 - inheritance

# 1. Warrior subclass (defensive specialist)
# New attribute: armor: int , with a default value of 5
# Override the Character.take_damage() method by reducing the incoming damage by armor before applying it.


class Warrior(Character):
    """Warrior is specialized subclass of Character. Defensive specialist."""

    def __init__(self, name: str, armor: int = 5, hp_max: int = 100, damage: int = 10) -> None:
        """Create a warrior with a name"""

        # Pass base attributes up to parent constructor
        super().__init__(name=name, hp_max=hp_max, damage=damage)
        self.armor = armor

    def take_damage(self) -> None:
        """Warrior overrides Character's take damage method, uses armor."""
        self._hp -= (self.damage - self.armor)
        self._hp = max(self._hp, 0)

class Mage(Character):
    """Mage is specialized subclass of Character. Resource-based attacker."""

    def __init__(
            self, name: str, 
            mana: int = 30, 
            mana_max: int = 30, 
            hp_max: int = 100, 
            damage: int = 10
        ) -> None:
        """Create Mage with a name. The mana available determines whether the mage can use magic."""

        super().__init__(name=name, hp_max=hp_max, damage=damage)
        self.mana = mana
        self.mana_max = mana_max

# Override the Character.attack() method:
    # If the mage has at least 10 mana left, spend 10 mana to deal a magical spell attack dealing double damage. 
    # This magic attack does not use any weapons, even if the character has one equipped.

    # If the mage has less than 10 mana left, fall back to the base attack, and
    # restore 5 mana. This base attack should use whichever weapon the character has equipped.
    def attack(self, target):
        """Overrides Character's attack method. Uses 10 manas for double attack, or attack with weapon."""
        if self.mana > 10: 
            self.mana -= 10
            target.damage *= 2 # huhhhh?
            target.take_damage()
        else:
            super().attack(target) # Character's attack() is modified to use weapon if available??
            self.mana += 5

# from class Character:
    def attack(self, target) -> None: # So one object does not modify other objects HP
        """Attack and cause target to take damage, by calling target object's take_damage() method"""
        target.take_damage()


