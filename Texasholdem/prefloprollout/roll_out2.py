import cards
from rollout_player import Player
from os import sys

deck = cards.gen_52_cards()
players = []
table = []
no_rollouts = 100

def create_players(no_players):
    del players[:]
    for i in range(no_players):
        players.append(Player(i+1))
    
def flop(deck): 
    c = deck.deal_n_cards(3)
    for card in c:
        table.append(card)
	
def river(deck): table.append(deck.deal_one_card())
	
def turn(deck): table.append(deck.deal_one_card())

def find_winners(winners):
    if len(winners) > 1 and players[0] in winners:
        #print "draw"
        return "d"
    elif len(winners) == 1 and winners[0] == players[0]:
        #print "won"
        return "w"
    elif len(winners) > 0 and players[0] not in winners:
        #print "loss"
        return "l"
    return "WTF?", winners

def check_hand(players_power, remaining):
    #print "Check_hand", len(players_power), len(remaining)
    powers_to_be_deleted = []
    remaining_to_be_deleted = []
    #print players_power
    if len(players_power[0]) == 0:
     #   print "hEIHEHIERHIERHIERHIHREI--------------"
        s = find_winners(remaining)
        remaining = []
        players_power = [s]
        return [players_power, remaining]
    try:
        for i in range(len(remaining)-1):
            for j in range(i+1, len(remaining)):
                if players_power[i][0] < players_power[j][0]:
                    powers_to_be_deleted.append(players_power[i])
                    remaining_to_be_deleted.append(remaining[i])
                elif players_power[i][0] > players_power[j][0]:
                    remaining_to_be_deleted.append(remaining[j])
                    powers_to_be_deleted.append(players_power[j])
        for p in powers_to_be_deleted:
      #      print p
            if p in players_power:
                players_power.remove(p)
        for p in remaining_to_be_deleted:
       #     print p
            if p in remaining:
                remaining.remove(p)
    except Exception as inst:
        print inst
        print "try no 1", i, len(remaining), len(players_power)
    try:
        for i in range(len(remaining)):
            del players_power[i][0]
    except Exception as inst:
        print inst
        print "try no 2", i, len(remaining), len(players_power), len(players_power[i])
    return [players_power, remaining] 

def showdown():
    remaining = list(players)
    players_power = []
    #print "Showdown!\n-------------------"
    for player in players:
        hand = player.hand + table
        hand_power = cards.calc_cards_power(hand)
     #   print "hand power", hand_power
        players_power.append(hand_power)
    while len(remaining) > 1:
        remaining2 = check_hand(players_power, remaining)
        remaining = remaining2[1]
    #print "After showdown,", len(remaining), "players remain"
    if len(remaining) == 0:
        return remaining2[0][0]
    return find_winners(remaining)


# equivalence classes 79-156; pairs of cards with equal suit
eq_class2 = []
for i in range(0,12):
	for j in range(i+1, 13):
		h = [deck[i], deck[j]]
		eq_class2.append(h)
		
            
def eq_class_rollout(hand, no_players):
    for i in range(no_players):
        create_players(no_players)
        deck = cards.card_deck()
        deck.remove(hand)
        players[0].hand = hand
        for i in range(2):
            for j in range(1, no_players-1):
                players[j].hand.append(deck.deal_one_card())
        flop(deck)
        river(deck)
        turn(deck)
        try:
            s = showdown()
            del table[:]
            return s
        except Exception as inst:
            print inst
            print s
                      
out = "rolloutTable2.txt"
file = open(out, 'wb')
if file:
    for hand in eq_class2:
        print >> file, hand
        for i in range(2,11):
            sys.stdout.write(".")
            sys.stdout.flush()
            table_entry = []
            for j in range(no_rollouts):
                table_entry.append(eq_class_rollout(hand, i))
            print >> file, ''.join(table_entry)
    file.close()
    print "Rollout table 2, is done"
else:
	print "Error opening file"     

