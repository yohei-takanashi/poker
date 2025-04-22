from card import Card
from stock import Stock
from hand_combination import HandCombination
import time


class Player:
    def __init__(self):
        self.hand: list[Card] = []
        self.hc = HandCombination()
        self.card = Card
        self.stock = Stock()

    def draw_card(self):
        deck_top = self.stock.create_deck().pop(0)
        print(f"引いたカードの数字は{deck_top}")
        self.hand.append(deck_top)

    def display(self):
        sorted_hand = HandCombination.sort_hand(self.hand)
        Card.hand_strings(sorted_hand)
        self.hc.check_hand_combination(sorted_hand)

    def first_hand(self):
        for i in range(5):
            self.draw_card()
            time.sleep(0.5)
        HandCombination.sort_hand(self.hand)
        self.display()

    def change_card(self):
        count_pop = 0
        self.hand = HandCombination.sort_hand(self.hand)
        for i in range(5):
            Card.hand_strings(self.hand)
            a = input("何番目のカードを捨てるか1-5の数字を1つ入力!捨てない場合は0を入力")
            if a == "0":
                break
            else:
                self.hand.pop(int(a) - 1)
                count_pop += 1
        for i in range(count_pop):
            self.draw_card()
            time.sleep(0.5)
        self.display()

    def hand_strength(self) -> tuple:
        sorted_hand = HandCombination.sort_hand(self.hand)
        player_strength, player_rank, player_suit = self.hc.check_hand_combination(sorted_hand)
        return player_strength, player_rank, player_suit


class Computer(Player):
    def change_card(self):
        self.hand = HandCombination.sort_hand(self.hand)
        print(f"{[i + 1 for i in self.hc.not_pair_place(self.hand)]}番目の数字を交換")
        for i in range(5):
            if len(self.hc.not_pair_place(self.hand)) == 0:
                # print("Computerは交換しない")
                break
            else:
                self.hand.pop(self.hc.not_pair_place(self.hand)[0])
        for i in range(5 - len(self.hand)):
            self.draw_card()
        self.display()


    def hand_strength(self):
        sorted_hand = HandCombination.sort_hand(self.hand)
        computer_strength, computer_rank, computer_suit = self.hc.check_hand_combination(sorted_hand)
        return computer_strength, computer_rank, computer_suit
