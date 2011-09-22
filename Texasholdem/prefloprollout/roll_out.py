import cards
from rollout_player import Player

deck = cards.gen_52_cards()
players = []
table = []

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

# equivalence classes 1-78; pairs of cards with unequal suit and value
eq_class1 = []
for i in range(0, 12):
	for j in range(i+14, i+26-i):
		h = [deck[i], deck[j]]
		eq_class1.append(h)
		
# equivalence classes 79-156; pairs of cards with equal suit
eq_class2 = []
for i in range(0,12):
	for j in range(i+1, 13):
		h = [deck[i], deck[j]]
		eq_class2.append(h)
		
# equivalence classes 157-169; pairs of cards with equal value
eq_class3 = []
for i in range(13):
	h = [deck[i], deck[i+13]]
	eq_class3.append(h)

#for hand in eq_class3:
def eq_class3_rollout(hand, no_players):
    table_entry = ""
    for i in range(no_players):
        create_players(no_players)
        #hand = eq_class3[i]
        deck = cards.card_deck()
        deck.remove(hand)
        players[0].hand = hand
        #deck = cards.shuffle_cards(deck)
        for i in range(2):
            for j in range(1,no_players-1):
               players[j].hand.append(deck.deal_one_card())
        flop(deck)
        river(deck)
        turn(deck)
        #for player in players:
        #    print player.no, player.hand
        #print table
        try:
            s = showdown()
            table_entry += s
            del table[:]
            return table_entry
        except Exception as inst:
            print inst
            print s
            
        
                      
out = "rolloutTable.txt"
file = open(out, 'wb')
if file:
    for hand in eq_class3:
        for i in range(2,11):
            print >> file, hand
            table_entry = ""
            for j in range(100):
                table_entry += eq_class3_rollout(hand, i)
            print >> file, table_entry
    file.close()
else:
	print "Error opening file"     

            
            
        

    
