from card import Card
from stock import Stock
from player import Player
from player import Computer
from hand_combination import HandCombination
from judgement import Judgement


stock = Stock()
# card = Card()
player = Player()
computer = Computer()
hc = HandCombination()
judgement = Judgement()
judgement.player = player
judgement.computer = computer
player.first_hand()
player.change_card()
print("\n Computerのターン")
computer.first_hand()
computer.change_card()
judgement.show_winner()
