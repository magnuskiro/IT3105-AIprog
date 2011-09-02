import Cards
import Player

__author__ = 'Kiro'

numberOfPlayers = 2
players = []
deck = Cards.gen_52_shuffled_cards()

def main():
    print("starting")
    deck = Cards.gen_52_shuffled_cards()
    deck = shuffleDeck(deck)
    print(deck)
    initializePlayers()
    print(players)
    print("Initialization done")
    return 0

def shuffleDeck(d):
    d = Cards.shuffle_cards(d, 4)
    return d

def initializePlayers():
    for i in range(numberOfPlayers):
        p = Player()
        p.setPlayerNumber(i)
        players.append(p)
        print(players[0].getPlayerNumber)

def dealCards():
    for p in players:
        p.setHand(deck.pop(0), deck.p(0))

def doCardCheck():
    return 0

main()

deck = Cards.card_deck()
hand1 = deck.deal_n_cards(7)
hand2 = deck.deal_n_cards(7)
hand3 = deck.deal_n_cards(7)
print("Players have been dealt their cards")
print("Calculating hand powers")
print(Cards.power_test(5))