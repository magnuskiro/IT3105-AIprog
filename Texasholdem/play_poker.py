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
import betting
from player import Player
from table import Table

#no_players = int(raw_input("How many players in the game?: "))
#start_sum = int(raw_input("How much money do they start the game with?: "))
#debug = raw_input("Show game info? y/n: ")
#no_games = int(raw_input("Play how many games?: "))
players = []
tablecards = []
table = Table()

#for i in range(no_players):
#    players.append(Player(start_sum))

def deal_player_cards(deck):
    for i in range(2):
        for player in players:
            player.add_card(deck.deal_one_card())

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

def new_round():
    for player in players:
        player.clear_hand()
    table.clear_table()

def play_debug(deck):
    new_round()
    deal_player_cards(deck)
    print ("------------ \nPlayers have these hands\n------------")
    for player in players:
        print (player.get_hand())
    print ("\n")

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
        hand_power = find_hand(cards.calc_cards_power(hand))
        print (hand_power + str(cards.calc_cards_power(hand)))
    print ("------------")

def play_no_debug(deck):
    new_round()
    deal_player_cards(deck)
    table.add_cards(deck.deal_n_cards(3))
    for player in players:
        hand = player.get_hand() + table.get_cards()
    table.add_card(deck.deal_one_card())
    for player in players:
        hand = player.get_hand() + table.get_cards()
    table.add_card(deck.deal_one_card())
    print ("------------ \nPower ratings after the turn\n------------")
    for player in players:
        tablecards = table.get_cards()
        hand = player.get_hand() + tablecards
        hand_power = find_hand(cards.calc_cards_power(hand))
        betting.evaluateHand(cards.calc_cards_power(hand))
        print (hand_power + str(cards.calc_cards_power(hand)))
    print ("------------")


def main():
    no_players = int(raw_input("How many players in the game?: "))
    start_sum = int(raw_input("How much money do they start the game with?: "))
    debug = raw_input("Show game info? y/n: ")
    no_games = int(raw_input("Play how many games?: "))
    for i in range(no_players):
        players.append(Player(start_sum))
    if debug == "n":
        for i in range(no_games):
            deck = cards.card_deck()
            play_no_debug(deck)
    elif debug == "y":
        for i in range(no_games):
            deck = cards.card_deck()
            play_debug(deck)
