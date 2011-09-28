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
from game_state import Game_State
from player import Player

game = Game_State() # the game object containing all the game info.
no_players = 0
remaining = 0
no_games = 0
money = 0
deck = cards.card_deck()
no_bets = 3

def print_players_final():
    global game
    for player in game.getPlayers():
        print "Player", player.no, " - ", player.get_money()

def print_players():
    global game
    for player in game.getRemaining():
        if player.in_game:
            print "Player", player.no, "has the hand", player.get_hand(), "has", player.get_money(), "dollars and have bet", player.get_bet()

def print_table():
    global game
    print "Pot:", game.getTable().get_pot(), "Community cards:", game.getTable().get_cards()

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
    global game
    amount = game.getTable().get_pot()
    player.add_money(amount)
    print "Player", player.no,"won", amount, "dollars"
    game.finished = True
    #for player in players:
    #	player.clear_hand()
    #	player.in_game = True
    #exit ("Game finished")

def split_pot():
    global game
    amount = game.getTable().get_pot()
    for player in game.getRemaining():
        player.add_money(amount/game.getLenRemaining())
        print "Player", player.no, "won", amount, "dollars"

def deal_hole_cards():
    global game
    for i in range(2):
        for player in game.getRemaining():
            player.add_card(deck.deal_one_card())

# Probably not needed, but keep it for now, just in case			
def rotate_blinds():
    global game
    remaining = game.getRemaining()
    global small_blind
    global big_blind
    if small_blind >= remaining-1:
        small_blind = 0
    else:
        small_blind += 1
    big_blind = small_blind + 1
    if big_blind > (remaining - 1):
        big_blind = 0

def flop():
    global game
    game.getTable().add_cards(deck.deal_n_cards(3))

def river():
    global game
    game.getTable().add_card(deck.deal_one_card())

def turn():
    global game
    game.getTable().add_card(deck.deal_one_card())

def create_players():
    global game
    for i in range(no_players):
        #players.append(Player(money, i, ""))
        if i==1 or i==5 or i==9:
            game.addPlayer(Player(money, i, "aggressive"))
        elif i==2 or i==6:
            game.addPlayer(Player(money, i, "coward"))
        elif i==3 or i==7:
            game.addPlayer(Player(money, i, "bluffer"))
        else: # 0 4 8
            p = Player(money, i, "")
            p.phase = 1
            game.addPlayer(p)

def new_round():
    global deck
    global game
    for player in game.getPlayers():
        player.clear_hand()
        player.in_game = True
        player.bet = 0
        player.strategy.setBluffing(False)
    game.getTable().clear_table()
    game.finished = False
    deck = cards.card_deck()
    return deck

def pre_flop():
    global game
    remaining = game.getRemaining()
    if len(remaining) == 1:
        return
    #print "pre_flop"
    for player in game.getPlayers():
        if player.blind or not player.in_game:
            continue
        #betting.pre_flop_betting(player, table)
        betting.evaluateHand(game, player)
    for player in game.getPlayers():
        if not player.in_game:
            continue
        remaining = game.getRemaining()
        #print "Players remaining:", len(remaining)
        if len(remaining) > 1:
            betting.evaluateHand(game, player)
            #betting.pre_flop_betting(player, table)
        else:
            game.finished=True
            player_won(player)
            break
    for player in remaining:
        if player.bet != game.getTable().get_bet():
                bet()

def bet():
    global game
    if game.getLenRemaining() == 1:
        return
    print "bet"
    for player in game.getPlayers():
        if not player.in_game:
            continue
        remaining = game.getRemaining()
        if len(remaining) > 1:
            tablecards = game.getTable().get_cards()
            hand = player.get_hand() + tablecards
            hand_power = find_hand(cards.calc_cards_power(hand))
            print "Player", player.no, "has", hand_power + str(cards.calc_cards_power(hand))
            betting.evaluateHand(game, player)
        else:
            game.finished = True
            player_won(player)
    remaining = game.getRemaining()
    for player in remaining:
        if player.bet != game.getTable().get_bet():
                bet()

def check_hand(players_power, remaining):
    #print "Check_hand", len(players_power), len(remaining)
    powers_to_be_deleted = []
    remaining_to_be_deleted = []
    if len(players_power[0]) == 0:
        split_pot()
        remaining = []
        players_power = []
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
            if p in players_power:
                players_power.remove(p)
        for p in remaining_to_be_deleted:
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
    global game
    remaining = game.getRemaining()
    if len(remaining) == 1:
        return
    tableCards = game.getTable().get_cards()
    players_power = []
    print "-------------------Showdown!-------------------"
    for player in remaining:
        hand = player.get_hand() + tableCards
        hand_power = cards.calc_cards_power(hand)
        #print "hand power", hand_power
        players_power.append(hand_power)
    while len(remaining) > 1:
        remaining2 = check_hand(players_power, remaining)
        remaining = remaining2[1]
    #print "After showdown,", len(remaining), "players remain"
    game.finished = True
    if len(remaining) == 0:
        return
    player_won(remaining[0])

def clearNumRaises():
    global game
    for p in game.getPlayers():
        p.raises = 0

def play():
    global game
    global deck
    # this object will store all relevant information about the game
    deck = new_round()
    deal_hole_cards()
    # This while is just to keep the game going until there's only 1 player left, as proper betting is not implemented yet
    #while not game.getFinished():
    print "GAME START!"
    print_players()
    print_table()
    remaining = game.getRemaining()
    #print len(remaining)
    if len(remaining) < 2:
        game.finished = True
        player_won(remaining[0])
    small_blind = remaining[0]
    big_blind = remaining[1]
    print "Player", small_blind.no, "is small blind, and player", big_blind.no, "is big blind"
    betting.small_blind(small_blind, game.getTable())
    betting.big_blind(big_blind, game.getTable())
    print "Betting before flop \n------------------------------", game.getLenRemaining()
    game.setState("preFlop")
    clearNumRaises()
    pre_flop()
    flop()
    print_table()
    print "Betting before turn \n------------------------------", game.getLenRemaining()
    game.setState("postFlop")
    clearNumRaises()
    bet()
    small_blind.blind = False
    big_blind.blind = False
    turn()
    print_table()
    print "Betting before river \n------------------------------", game.getLenRemaining()
    game.setState("postTurn")
    clearNumRaises()
    bet()
    river()
    print_table()
    print "Betting after river \n------------------------------", game.getLenRemaining()
    game.setState("postTurn")
    clearNumRaises()
    bet()
    remaining = game.getRemaining()
    if len(remaining) > 1:
        showdown()
    elif not game.finished :
        player_won(remaining[0])
    random.shuffle(game.getPlayers())
    #game.getTable().clear_table()
    #deck = cards.card_deck()


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

