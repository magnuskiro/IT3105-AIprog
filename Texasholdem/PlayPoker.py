import Cards

__author__ = 'Kiro'

players = []
deck = Cards.gen_52_shuffled_cards()

def main():
    shuffleDeck()
    print("test")
    return 0

def shuffleDeck():
    deck = Cards.shuffle_cards(deck)

def doCardCheck():
    return 0

deck = Cards.gen_52_shuffled_cards()
print("test")