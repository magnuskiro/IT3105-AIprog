import Cards

__author__ = 'Kiro'

players = []
deck = Cards.gen_52_shuffled_cards()

def main():
    shuffleDeck()
    print("test")
    return 0

def shuffleDeck(deck):
    deck = Cards.shuffle_cards(deck)

def doCardCheck():
    return 0

deck = Cards.card_deck()
hand1 = deck.deal_n_cards(7)
hand2 = deck.deal_n_cards(7)
hand3 = deck.deal_n_cards(7)
print("Players have been dealt their cards")
print("Calculating hand powers")
print(Cards.power_test(5))