from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self):
        self.weapon_instrument = "sword"
        self.damage = 10

    def attack(self, fighter):
        print(f"Sword attack: damage = {self.damage + fighter.force}")


class Bow(Weapon):
    def __init__(self):
        self.weapon_instrument = "bow"
        self.damage = 5

    def attack(self, fighter):
        print(f"Bow attack: damage = {self.damage + fighter.force}")


class Knife(Weapon):
    def __init__(self):
        self.weapon_instrument = "knife"
        self.damage = 1

    def attack(self, fighter):
        print(f"Knife attack: damage = {self.damage + fighter.force}")


class Fighter():
    def __init__(self, name: str, force: int, weapon: Weapon):
        self.name = name
        self.force = force
        self.weapon = weapon

    def fight(self):
        self.weapon.attack(self)

    def weapon_change(self, weapon):
        self.weapon = weapon
        print(f"{self.name} change weapon to {self.weapon}")


class Monster():
    def __init__(self, armor=100):
        self.armor = armor


monster = Monster()
sword = Sword()
bow = Bow()
knife = Knife()
name = input("Enter name of Fighter: ")
force = int(input("Enter your force: "))
fighter = Fighter(name, force, sword)

while True:
    if monster.armor <= 0:
        print(f"{name} win")
        break
    else:
        print(f"Monster health = {monster.armor}")
        print(f"{name} weapon is {fighter.weapon.weapon_instrument}, total damage = {fighter.force + fighter.weapon.damage}")

        choose = input("1: attack, 2: change weapon ")
        if choose == '1':
            fighter.fight()
            monster.armor -= fighter.force + fighter.weapon.damage
        else:
            change_weapon = input("Choose weapon: 1: sword, 2: bow, 3: knife ")
            if change_weapon == '1':
                fighter.weapon_change(sword)
            elif change_weapon == '2':
                fighter.weapon_change(bow)
            elif change_weapon == '3':
                fighter.weapon_change(knife)
            else:
                print("Wrong choose")
