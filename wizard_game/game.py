from creature import Creature, Dragon
from wizard import Wizard
import random


class Game:
    def __init__(self):
        self.creatures = [
            Creature("Toad", 1),
            Creature("Frog", 3),
            Dragon("Dragon", 50),
            Creature("Lion", 10)
        ]

        self.wizard = Wizard('Gandolf', 30)

    def play_round(self):
        opponent = random.choice(self.creatures)
        print("Opponent type: {}".format(type(opponent)))
        if self.wizard.battle(opponent):
            self.creatures.remove(opponent)
        else:
            print("Oh no, the wizard is defeated!")
