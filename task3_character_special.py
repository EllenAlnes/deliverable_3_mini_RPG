
class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

# 1) Implement a take_damage() method to be used when the Character object is injured. 
# This method should only affect the characters own HP.

    def take_damage(self) -> None:
        """Loose HP when character is injuried."""
        self._hp -= self.damage
        self._hp = max(self._hp, 0) # returns highest value, of current hp and 0. Avoids negative hp.

# 2) Implement a heal() method to be used when the Character heals (in other words increase their hit points)

    def heal(self, amount: int) -> None:
        """Character recieves a certain amount hp when healed."""
        self._hp += amount 
        self._hp = min(self._hp, self.hp_max) # returns lowest value. Avoids too high hp.

# 3) Change the existing attack() method so that it calls the target's take_damage()
# method rather than directly modifying the target's _hp .

    def attack(self, target) -> None: # So one object does not modify other objects HP
        """Attack and cause target to take damage, by calling target object's take_damage() method"""
        target.take_damage()

# 4) Add an is_alive property to the Character class. This should be read-only,
# and return True if _hp > 0 and False otherwise.

    @property
    def is_alive(self) -> bool:
        """Returns True if character is alive."""
        return bool(self._hp > 0)

    
character1 = Character(name="Aria", hp_max=100, damage=10)
character2 = Character(name="Kura", hp_max=100, damage=20)
print(character1.is_alive)


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
    def attack(self, target):
        """Overrides Character's attack method, uses 10 manas for double attack effect."""
        if self.mana > 10: #and not use weapon!!
            self.mana -= 10
            target.damage *= 2
            target.take_damage()

    def attack(self, target) -> None: # So one object does not modify other objects HP
        """Attack and cause target to take damage, by calling target object's take_damage() method"""
        target.take_damage()

    # If the mage has less than 10 mana left, fall back to the base attack, and
    # restore 5 mana. This base attack should use whichever weapon the character has equipped.
