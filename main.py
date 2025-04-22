from player import Player
from player import Computer
from judgement import Judgement


def main():
    player = Player()
    computer = Computer()
    judgement = Judgement()
    judgement.player = player
    judgement.computer = computer

    print("Playerのターン")
    player.first_hand()
    player.change_card()
    print("\n Computerのターン")
    computer.first_hand()
    computer.change_card()
    judgement.show_winner()


if __name__ == "__main__":
    main()
