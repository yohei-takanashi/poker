from card import Card


class HandCombination:
    def __init__(self):
        self.hand: list[Card] = []

    @staticmethod
    def sort_hand(hand: list[Card]) -> list[Card]:
        return sorted(hand, key=lambda card: card.number)

    def count_pair(self, sorted_hand: list[Card]) -> int:
        count_pairs = 0
        for i in range(4):
            if sorted_hand[i].number == sorted_hand[i + 1].number:
                count_pairs += 1
        return count_pairs

    def three_or_four(self, sorted_hand: list[Card]) -> int:
        three_card = 0
        for i in range(3):
            if sorted_hand[i].number == sorted_hand[i + 2].number:
                three_card += 1
        return three_card

    def check_hand_combination(self, sorted_hand: list[Card]):
        if self.is_royal_straight_flush(sorted_hand):
            print("ロイヤルストレートフラッシュ！！！！！")
            return 10, sorted_hand[4].number, sorted_hand[4].suit
            # return {strength: 10, number_rank: sorted_hand[4].number, suit: sorted_hand[4].suit}辞書
            # return HandResult(10, sorted_hand[4].number, sorted_hand[4].suit)タプル
        elif self.is_straight_flush(sorted_hand):
            print("ストレートフラッシュ！！！！")
            return 9, sorted_hand[4].number, sorted_hand[4].suit
        elif self.is_four_card(sorted_hand):
            print("フォーカード！！！")
            return 8, sorted_hand[3].number, "♠︎"
        elif self.is_full_house(sorted_hand):
            print("フルハウス！！")
            return 7, sorted_hand[3].number, "♠︎"
        elif self.is_flush(sorted_hand):
            print("フラッシュ！")
            return 6, sorted_hand[4].number, sorted_hand[4].suit
        elif self.is_straight(sorted_hand):
            print("ストレート！")
            return 5, sorted_hand[4].number, sorted_hand[4].suit
        elif self.is_three_card(sorted_hand):
            print("スリーカード！")
            return 4, sorted_hand[3].number, "♠︎"
        elif self.is_two_pair(sorted_hand):
            print("ツーペア")
            return 3, sorted_hand[3].number, self.strongest_suit
        elif self.is_one_pair(sorted_hand):
            print("ワンペア")
            return 2, self.one_pair_number(sorted_hand), self.strongest_suit
        else:
            print("ハイカード")
            return 1, sorted_hand[4].number, sorted_hand[4].suit

    def one_pair_number(self, sorted_hand):
        counts = {}
        for card in sorted_hand:
            counts[card.number] = counts.get(card.number, 0) + 1
        for rank, count in counts.items():
            if count == 2:
                return rank

    def not_pair_place(self, sorted_hand) -> list:
        counts = {}
        solo_cards = []
        for card in sorted_hand:
            counts[card.number] = counts.get(card.number, 0) + 1
        for i, card in enumerate(sorted_hand):
            if counts[card.number] == 1:
                solo_cards.append(i)
        return solo_cards

    def strongest_suit(self, sorted_hand):
        strongest_suit = None
        suits = {"♠︎": 4, "❤︎": 3, "♦︎": 2, "♣︎": 1}
        for i in sorted_hand:
            if i.number == self.one_pair_number(sorted_hand):
                if strongest_suit is None or suits[i.suit] > suits[strongest_suit]:
                    strongest_suit == i.suits
        return strongest_suit

    def is_royal_straight_flush(self, sorted_hand: list[Card]) -> bool:
        if (
            self.is_straight(sorted_hand) is True
            and self.is_flush(sorted_hand) is True
            and sorted_hand[4].number == 13
        ):
            return True

    def is_straight_flush(self, sorted_hand: list[Card]):
        return (
            self.is_straight(sorted_hand) is True and self.is_flush(sorted_hand) is True
        )

    def is_four_card(self, sorted_hand: list[Card]):
        return self.three_or_four(sorted_hand) == 2

    def is_full_house(self, sorted_hand: list[Card]) -> bool:
        return (
            self.count_pair(sorted_hand) == 3 and self.three_or_four(sorted_hand) == 1
        )

    def is_flush(self, sorted_hand: list[Card]):
        if (
            sorted_hand[0].suit
            == sorted_hand[1].suit
            == sorted_hand[2].suit
            == sorted_hand[3].suit
            == sorted_hand[4].suit
        ):
            return True

    def is_straight(self, sorted_hand: list[Card]):
        if (
            sorted_hand[0].number + 4
            == sorted_hand[1].number + 3
            == sorted_hand[2].number + 2
            == sorted_hand[3].number + 1
            == sorted_hand[4].number
        ):
            return True

    def is_three_card(self, sorted_hand: list[Card]):
        return self.three_or_four(sorted_hand) == 1

    def is_two_pair(self, sorted_hand: list[Card]):
        return (
            self.count_pair(sorted_hand) == 2 and self.three_or_four(sorted_hand) == 0
        )

    def is_one_pair(self, sorted_hand: list[Card]):
        return self.count_pair(sorted_hand) == 1

    def is_high_card(self, sorted_hand: list[Card]):
        return self.count_pair(sorted_hand) == 0
