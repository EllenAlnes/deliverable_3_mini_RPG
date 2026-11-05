from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): The characters equipped weapon (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon    # Optional weapon, default None

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

    def attack(self, target) -> None: # skal endres til å kalle den andres take_damage. So one object does not modify other objects HP
        """Attack and cause target to take damage, by calling target object's take_damage() method"""
        # target.take_damage() - Ellen kommentert ut, litt forvirret over kommentaren over - funker den som den skal?
        if self.weapon is not None:
           damage = self.weapon.roll_damage()
        else:
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

