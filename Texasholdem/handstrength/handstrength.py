import cards

deck = 0
player_hand = 0
table = 0

def find_winners(winners):
    if len(winners) > 1 and player_hand in winners:
        #print "draw"
        return "d"
    elif len(winners) == 1 and winners[0] == player_hand:
        #print "won"
        return "w"
    elif len(winners) > 0 and player_hand not in winners:
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
    
def showdown(remaining, players_power):
    while len(remaining) > 1:
        remaining2 = check_hand(players_power, remaining)
        remaining = remaining2[1]
    #print "After showdown,", len(remaining), "players remain"
    if len(remaining) == 0:
        return remaining2[0][0]
    return find_winners(remaining)
    
def showdown(remaining):
    #remaining = list(players)
    players_power = []
    #print "Showdown!\n-------------------"
    for player in remaining:
        hand = player + table
        hand_power = cards.calc_cards_power(hand)
        #print "hand power", hand_power
        players_power.append(hand_power)
    while len(remaining) > 1:
        remaining2 = check_hand(players_power, remaining)
        remaining = remaining2[1]
    #print "After showdown,", len(remaining), "players remain"
    if len(remaining) == 0:
        return remaining2[0][0]
    return find_winners(remaining)
 
#player_hand, table, no_players
def tryit(p, t, no):
	global deck
	global player_hand
	global table
	
	#deck = cards.card_deck()
	#player_hand = deck.deal_n_cards(2)
	#table = deck.deal_n_cards(3)
	
	deck = cards.card_deck()
	player_hand = p
	table = t
	no_players = no
	
	
	#print "Player:", player_hand
	#print "Table:", table

	deck = cards.gen_52_cards()
	for card in player_hand:
		deck.remove(card)
	for card in table:
		deck.remove(card)
			
	possible_hands = []

	for i in range(len(deck)-1):
		for j in range(i+1, len(deck)):
			h = [deck[i], deck[j]]
			possible_hands.append(h)
			
	#print len(possible_hands)

	#for i in range(2):
	#	print "Opponent:", possible_hands[i]

	result = []
	for o in possible_hands:
		players_power = []
		#o = possible_hands[i]
		r = []
		r.append(player_hand)
		r.append(o)
		s = showdown(r)
		result.append(s)
		
	#print len(result)
	wins = 0
	draws = 0
	losses = 0
	for e in result:
		if e == "w":
			wins += 1
		elif e == "d":
			draws += 1
		elif e == "l":
			losses += 1

	#print wins, draws, losses

	strength = (((wins+draws/2.0)/(wins+draws+losses))**no_players)*100
	return strength
	

