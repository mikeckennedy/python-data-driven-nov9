# import game
from game import Game


def main():
    print("Welcome to the wizard game!")

    g = Game()

    while g.creatures:
        g.play_round()

    print("Game over!")


if __name__ == '__main__':
    main()
