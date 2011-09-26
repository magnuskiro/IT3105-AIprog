#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       play_poker.py
#
#       Copyright 2011
#       Jan Alexander Stormark Bremnes <janbremnes@gmail.com>
#       Magnus Kirø
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#

import random
import cards
import betting
from table import Table
from player import Player
from game_state import Game_State

no_players = 0
remaining = 0
no_games = 0
money = 0
players = []
deck = cards.card_deck()
table = Table()
no_bets = 3

def print_players_final():
    for player in players:
        print "Player", player.no, " - ", player.get_money()

def print_players():
	for player in players:
		if player.in_game:
			print "Player", player.no, "has the hand", player.get_hand(), "has", player.get_money(), "dollars and have bet", player.get_bet(), player.strategy.aggressive, player.strategy.coward
	
def print_table():
	print "Pot:", table.get_pot(), "Community cards:", table.get_cards()
	
def find_remaining(players):
	remaining = []
	for player in players:
		if player.in_game:
			remaining.append(player)
	return remaining
	
def find_hand(hand):
    if hand[0] == 1:
        return "High card: "
    elif hand[0] == 2:
        return "One pair: "
    elif hand[0] == 3:
        return "Two pair: "
    elif hand[0] == 4:
        return "Three of a kind: "
    elif hand[0] == 5:
        return "Straight: "
    elif hand[0] == 6:
        return "Flush: "
    elif hand[0] == 7:
        return "Full house: "
    elif hand[0] == 8:
        return "Four of a kind: "
    elif hand[0] == 9 and hand[1] != 14:
        return "Straight Flush: "
    elif hand[0] == 9 and hand[1] == 14:
        return "Royal Flush: "

def player_won(player):
	amount = table.get_pot()
	player.add_money(amount)
	print "Player", player.no,"won", amount, "dollars"
	#for player in players:
	#	player.clear_hand()
	#	player.in_game = True
	#exit ("Game finished")
	
def split_pot(remaining):
    amount = table.get_pot()
    for player in remaining:
        player.add_money(amount/len(remaining))
        print "Player", player.no, "won", amount, "dollars"

def deal_hole_cards():
	for i in range(2):
		for player in players:
			player.add_card(deck.deal_one_card())

# Probably not needed, but keep it for now, just in case			
def rotate_blinds():
	remaining = find_remaining(players)
	global small_blind
	global big_blind
	if small_blind >= remaining-1:
		small_blind = 0
	else:
		small_blind += 1
	big_blind = small_blind + 1
	if big_blind > (remaining - 1):
		big_blind = 0
			
def flop(): table.add_cards(deck.deal_n_cards(3))
	
def river(): table.add_card(deck.deal_one_card())
	
def turn(): table.add_card(deck.deal_one_card())

def create_players():
    for i in range(no_players):
        #players.append(Player(money, i, ""))

        if (i % 2) == 0 and i != 0:
            players.append(Player(money, i, "aggressive"))
        elif (i % 3) == 0 and i != 0:
            players.append(Player(money, i, "coward"))
        else:
            players.append(Player(money, i, ""))
        

def new_round():
	global deck
	for player in players:
		player.clear_hand()
		player.in_game = True
		player.bet = 0
	table.clear_table()
	deck = cards.card_deck()
	
def pre_flop(game):
    remaining = find_remaining(players)
    if len(remaining) == 1:
        return
    print "pre_flop"
    for player in players:
		if player.blind or not player.in_game:
			continue
		betting.pre_flop_betting(player, table)
    for player in players:
		if player.in_game == False:
			continue
		remaining = find_remaining(players)
		print "Players remaining:", len(remaining)
		if len(remaining) > 1:
			betting.pre_flop_betting(player, table)
		else:
			game.finished = True
			player_won(player)
			break
	
def bet(game):
    if len(find_remaining(players)) == 1:
        return
    print "bet"
    for player in players:
		if player.in_game == False:
			continue
		remaining = find_remaining(players)
		if len(remaining) > 1:
			tablecards = table.get_cards()
			hand = player.get_hand() + tablecards
			hand_power = find_hand(cards.calc_cards_power(hand))
			print "Player", player.no, "has", hand_power + str(cards.calc_cards_power(hand))
			betting.evaluateHand(player, table, cards.calc_cards_power(hand), len(remaining))
		else:
			game.finished = True
			player_won(player)
    remaining = find_remaining(players)
    for player in remaining:
        if player.bet != table.bet:
            if table.bet < 1200:
                bet(game)

def check_hand(players_power, remaining):
    print "Check_hand", len(players_power), len(remaining)
    if len(players_power[0]) == 0:
        print "hEIHEHIERHIERHIERHIHREI--------------"
        split_pot(remaining)
        remaining = []
        players_power = []
        return [players_power, remaining]
    try:
        for i in range(len(remaining)-1):
            if players_power[i][0] < players_power[i+1][0]:
                del players_power[i]
                del remaining[i]
            elif players_power[i][0] > players_power[i+1][0]:
                del players_power[i+1]
                del remaining[i+1]
    except:
        print "try no 1", i, len(remaining), len(players_power)
    try:
        for i in range(len(remaining)):
            del players_power[i][0]
    except:
        print "try no 2", i, len(remaining), len(players_power), len(players_power[i])
    return [players_power, remaining] 

def showdown(game):
    remaining = find_remaining(players)
    if len(remaining) == 1:
        return
    tablecards = table.get_cards()
    players_power = []
    print "Showdown!\n-------------------"
    for player in remaining:
        hand = player.get_hand() + tablecards
        hand_power = cards.calc_cards_power(hand)
        print "hand power", hand_power
        players_power.append(hand_power)
    while len(remaining) > 1:
        remaining = check_hand(players_power, remaining)
        remaining = remaining[1]
    print "After showdown,", len(remaining), "players remain"
    game.finished = True
    if len(remaining) == 0:
        return
    player_won(remaining[0])
        

def play():
	game_finished = False
	new_round()
	deal_hole_cards()
	global table
	table = Table()
	# this object will store all relevant information about the game
	# still to be implemented
	game = Game_State(table, players, False)
	global deck
	# This while is just to keep the game going until there's only 1 player left, as proper betting is not implemented yet
	while not game.finished:
		print_players()
		print_table()
		remaining = find_remaining(players)
		print len(remaining)
		if len(remaining) < 2:
		    game.finished = True
		    player_won(remaining[0])
		    break
		small_blind = remaining[0]
		big_blind = remaining[1]
		print "Player", small_blind.no, "is small blind, and player", big_blind.no, "is big blind"
		betting.small_blind(small_blind, table)
		betting.big_blind(big_blind, table)
		print "Betting before flop \n------------------------------"
		pre_flop(game)
		flop()
		print_table()
		print "Betting before turn \n------------------------------"
		bet(game)
		small_blind.blind = False
		big_blind.blind = False
		turn()
		print_table()
		print "Betting before river \n------------------------------"
		bet(game)
		river()
		print_table()
		print "Betting after river \n------------------------------"
		bet(game)
		if len(remaining) > 1:
		    showdown(game)
		random.shuffle(players)
		table.clear_table()
		deck = cards.card_deck()

     
def main():
    global no_players
    global money
    global no_games
    global remaining
    no_players = int(raw_input("How many players in the game? (2 - 10): "))
    money = int(raw_input("How much money do they start with?: "))
    no_games = int(raw_input("How many games shall be played?: "))
    debug = raw_input("Show game info? y/n: ")
    remaining = no_players
    
    if debug == "y":
        create_players()
        play_debug()
    elif debug == "n":
        create_players()
        for i in range(no_games):
            play()
        print_players_final()
    else:
        print ("Please answer y or n")
        
