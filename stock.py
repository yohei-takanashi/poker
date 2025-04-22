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
