class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.hand = []
        self.deck = []
        self.suit_list = ["♠︎", "❤︎", "♦︎", "♣︎"]

    def __str__(self):
        return f"{self.suit}{str(self.number)}"

    @staticmethod
    def hand_strings(hand):  # オブジェクトを文字列に変換
        print(f"あなたの手札は{[str(card) for card in hand]}")
