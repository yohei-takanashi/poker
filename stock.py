from card import Card
import random


class Stock:
    def __init__(self):
        self.hand: list[Card] = []
        self.deck = []
        self.suit_list = ["♠︎", "❤︎", "♦︎", "♣︎"]

    def create_deck(self) -> list[Card]:
        for suit in self.suit_list:
            for number in range(1, 14):
                card = Card(suit, number)
                self.deck.append(card)
        random.shuffle(self.deck)
        return self.deck

# ロイヤルストレートフラッシュ＞ストレートフラッシュ＞フォーカード＞フルハウス＞
# フラッシュ＞ストレート＞スリーカード＞ツーペア＞ワンペア＞ノーペア
# スペード>ハート>ダイヤ>クラブ
# A>K>Q>J>10>9>8>7>6>5>4>3>2
# ペアの数、同じ数字が何組あるか、同じ数字の枚数、フラッシュ、ストレート、
# ストレートフラッシュの時にロイヤルになるか
# 並び替え
# #######
