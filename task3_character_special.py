from task1_characterclass import Character

# TASK 4 - inheritance

# 1) Warrior subclass

class Warrior(Character):
    """Warrior is specialized subclass of Character. Defensive specialist."""

    def __init__(self, name: str, armor: int = 5, hp_max: int = 100, damage: int = 10) -> None:
        """Create a warrior with a name"""

        # Pass base attributes up to parent constructor
        super().__init__(name=name, hp_max=hp_max, damage=damage)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        """Warrior overrides Character's take damage method, uses armor."""
        self._hp -= (damage - self.armor)
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

# 2) Mage subclass

    def attack(self, target):
        """Overrides Character's attack method. Uses 10 manas for double attack, or attack with weapon."""
        if self.mana >= 10: 
            self.mana -= 10
            damage = self.weapon.roll_damage() if self.weapon is not None else self.damage
            target.take_damage(damage * 2)
        else:
            super().attack(target) # Character's attack() is modified to use weapon if available??
            self.mana += 5
