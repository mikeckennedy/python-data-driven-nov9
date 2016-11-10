import random


class Creature:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def battle(self, other_creature):
        print("{} of level {} is attacking {} of level {}".format(
            self.name, self.level, other_creature.name, other_creature.level
        ))

        my_roll = random.randint(1, 12) * self.level
        their_roll = random.randint(1, 12) * other_creature.level

        if my_roll >= their_roll:
            print("{} defeats {}".format(self.name, other_creature.name))
            return True
        else:
            return False

class Dragon(Creature):
    pass