class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_character):
        if self.is_alive():
            other_character.health = other_character.health - self.attack_power
            if other_character.health < 0:
                other_character.health = 0

    def is_alive(self):
        return self.health > 0
