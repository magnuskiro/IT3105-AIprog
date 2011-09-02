import Cards

__author__ = 'Kiro'

players = []
deck = Cards.gen_52_shuffled_cards()

def main():
    shuffleDeck()
    print("test")
    return 0

def shuffleDeck(d):
    d = Cards.shuffle_cards(d, 4)
    return d

def doCardCheck():
    return 0

deck = Cards.gen_52_shuffled_cards()
print("test")
deck = shuffleDeck(deck)
print(deck)