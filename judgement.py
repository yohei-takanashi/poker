from hand_combination import HandCombination
from player import Player
from player import Computer


class Judgement:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()

    def show_winner(self):
        player_strength, player_rank, player_suit = self.player.hand_strength()
        computer_strength, computer_rank, computer_suit = self.computer.hand_strength()

        print("\n勝敗判定")
        print("プレイヤーの役:", player_strength)
        print("コンピュータの役:", computer_strength)

        if player_strength > computer_strength:
            print("プレイヤーの勝ち！")
        elif player_strength < computer_strength:
            print("Computerの勝ち!")
        else:
            print("役の強さは同じ")
            self.same_strength(player_rank, computer_rank, player_suit, computer_suit)

    def same_strength(self, player_rank, computer_rank, player_suit, computer_suit):
        print("プレイヤーの役のランク:", player_rank)
        print("コンピュータの役のランク:", computer_rank)

        if player_rank > computer_rank:
            print("プレイヤーの勝ち！（数字の強さで判定）")
        elif player_rank < computer_rank:
            print("Computerの勝ち!（数字の強さで判定）")
        else:
            print("役の強さと数字の強さは同じ、絵柄の強さで判定する")
            self.suit_strength(player_suit, computer_suit)

    def suit_score(self, suit):
        if suit == "♠︎":
            return 4
        elif suit == "❤︎":
            return 3
        elif suit == "♦︎":
            return 2
        elif suit == "♣︎":
            return 1
        return 0

    def suit_strength(self, player_suit, computer_suit):  # スペード>ハート>ダイヤ>クラブ
        player_suit_score = self.suit_score(player_suit)
        computer_suit_score = self.suit_score(computer_suit)

        print("プレイヤーのスーツ:", player_suit)
        print("コンピュータのスーツ:", computer_suit)

        if player_suit_score > computer_suit_score:
            print("プレイヤーの勝ち！（絵柄の強さで判定）")
        elif player_suit_score < computer_suit_score:
            print("Computerの勝ち!（絵柄の強さで判定）")
        else:
            print("引き分け！役、数字、絵柄全て同じ")