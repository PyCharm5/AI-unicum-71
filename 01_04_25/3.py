class Character:
    def __init__(self):
        self.name = None
        self.race = None
        self.class_ = None
        self.magic = None
        self.weapon = []

    def __str__(self):
        weapons = ", ".join(self.weapon) if self.weapon else "Без оружия"
        return f"Персонаж: {self.name}, раса: {self.race}, класс: {self.class_}, магия: {self.magic}, оружие: {weapons}"

class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_name(self, name):
        self.character.name = name
        return self

    def set_race(self, race):
        self.character.race = race
        return self

    def add_class(self, class_):
        self.character.class_ = class_
        return self

    def add_magic(self, magic):
        self.character.magic = magic
        return self

    def add_weapon(self, weapon):
        self.character.weapon.append(weapon)
        return self

    def build(self):
        return self.character

# Создание пиццы
character1 = (CharacterBuilder()
                .set_name("Elara Moonshadow")
                .set_race("Elf")
                .add_class("Sorceress")
                .add_magic("Fire and Ice")
                .add_weapon("Enchanted Staff")
                .build())

character2 = (CharacterBuilder()
                .set_name("Seraphina Brightflame")
                .set_race("Human")
                .add_class("Paladin")
                .add_magic("Holy Damage")
                .add_weapon("Sword and Shield")
                .build())

print(character1)
print(character2)