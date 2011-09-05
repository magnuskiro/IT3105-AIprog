#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       play_poker.py
#
#       Copyright 2011
#       Jan Alexander Stormark Bremnes <alex@icarus>
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

import cards
from player import Player
from table import Table

no_players = int(input("How many players in the game?: "))
start_sum = int(input("How much money do they start the game with?: "))
players = []
tablecards = []

for i in range(no_players):
	players.append(Player(start_sum))

deck = cards.card_deck()
for i in range(2):
	for player in players:
		player.add_card(deck.deal_one_card())

print ("------------ \nPlayers have these hands\n------------")
for player in players:
	print (player.get_hand())
print ("\n")

players[1].add_money(1000)

table = Table()
print ("------------\nThe Flop\n------------")
table.add_cards(deck.deal_n_cards(3))
print (table.get_cards())
print ("------------")

print ("------------ \nPower ratings after the flop\n------------")
for player in players:
	hand = player.get_hand() + table.get_cards()
	print (cards.calc_cards_power(hand))
print ("------------")

print ("------------\nThe River\n------------")
table.add_card(deck.deal_one_card())
print (table.get_cards())
print ("\n------------")

print ("------------ \nPower ratings after the river\n------------")
for player in players:
	hand = player.get_hand() + table.get_cards()
	print (cards.calc_cards_power(hand))
print ("------------")

print ("------------\nThe Turn\n------------")
table.add_card(deck.deal_one_card())
print (table.get_cards())
print ("\n------------")

print ("------------ \nPower ratings after the turn\n------------")
for player in players:
	tablecards = table.get_cards()
	hand = player.get_hand() + tablecards
	hand_power = cards.calc_cards_power(hand)
	if (hand_power[0] == 3):
		print ("three of a kind")
	print (cards.calc_cards_power(hand))
print ("------------")

