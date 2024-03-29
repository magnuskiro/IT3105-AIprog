#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       table.py
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

import cards
import random

bet = 20
blind = 10
maxRaises = 3

def small_blind(player, table):
    print "Player", player.no, "places small blind"
    player.blind = True
    player.loose_money(blind)
    player.set_bet(blind)
    table.increase_pot(blind)
    table.raise_bet(blind)
    print "Table pot is now", table.get_pot(), "and table bet is", table.get_bet()

def big_blind(player, table):
    print "Player", player.no, "places big blind"
    player.blind = True
    player.loose_money(blind*2)
    player.set_bet(blind*2)
    table.increase_pot(blind*2)
    table.raise_bet(blind)
    print "Table pot is now", table.get_pot(), "and table bet is", table.get_bet()

def fold(player):
    print "Player", player.no, "folds"
    player.in_game = False

def call(player, table):
    print "Player", player.no, "calls"
    current_bet = player.get_bet()
    table_bet = table.get_bet()
    if current_bet < table_bet:
        place_bet(player, table, (table_bet - current_bet))
    else:
        check(player, table)
    print "Player", player.no, "has bet", player.bet, "and has", player.money, "dollars"
    print "Table pot is now", table.get_pot(), "and table bet is", table.get_bet()

def check(player, table):
    if player.get_bet() == table.get_bet():
        print "Player", player.no, "checks"
        return
    else:
        rand = random.randrange(0,2)
        if rand == 1:
            call(player, table)
        else:
            fold(player)

def place_bet(player, table, amount):
    print "Player", player.no, "places a bet of", amount
    player.loose_money(amount)
    player.set_bet(amount)
    table.increase_pot(amount)

def raise_bet(player, table, amount):
    if player.getRoundRaises() >= maxRaises:
        #print "max bet reached"
        call(player, table)
    else:
        player.raises+=1
        difference = table.get_bet() - player.get_bet()
        player.loose_money(amount + difference)
        table.increase_pot(amount + difference)
        table.raise_bet(amount)
        player.set_bet(amount + difference)
        print "Player", player.no, "raises", amount
        print "Player", player.no, "has bet", player.bet, "and has", player.money, "dollars"
        print "Table pot is now", table.pot, "and table bet is", table.bet

def weak(player, table):
    prob = random.randrange(0,6)    # 0-2 = fold, 3-4 = call, 5 = raise
    if prob < 3:
        fold(player)
    elif prob == 3 or prob == 4:
        call(player, table)
    else:
        raise_bet(player, table, bet)
    #print("weak hand: %s" % (hand))
    #return hand

def mediocre(player, table):
    prob = random.randrange(0,8)    # 0-1 = fold, 2-3 = call, 4-7 = raise
    if prob < 2:
        fold(player)
    elif prob == 2 or prob == 3:
        call(player, table)
    else:
        raise_bet(player, table, bet)
    #print("mediocre hand: %s" % (hand))
    #return hand

def strong(player, table):
    prob = random.randrange(0,10)   # 0-1 = fold, 2-3 = call, 5-9 = raise
    if prob < 2:
        fold(player)
    elif prob == 2 or prob == 3:
        call(player, table)
    else:
        raise_bet(player, table, bet)
    #print("strong hand: %s" % (hand))
    #return hand

def evaluateHandNormal(player, table, hand):
    #find out it the hand is weak/mediocre/strong.
    # aggressive 1-2 fold, 3-4 call over raise.
    # coward 1-4 fold 4-6 call 7 or more rasie.
    # normal 1-3 fold, 4-5 call, 6 or more raise.
    if player.strategy.aggressionPoints == 5: # sggressive
        if hand[0]==1:
            fold(player)
        elif hand[0] >=2 and hand[0] <=3:
            call(player, table)
        elif hand[0]>=4:
            raise_bet(player, table, bet)
        else:
            print("something is wrong with the betting procedure.")
    elif player.strategy.aggressionPoints == 0: # normal
        if hand[0] <=3 and hand[0] >=1:
            fold(player)
        elif hand[0] >=4 and hand[0] <=5:
            call(player, table)
        elif hand[0]>=6:
            raise_bet(player, table, bet)
        else:
            print("something is wrong with the betting procedure.")
    elif player.strategy.aggressionPoints == -5: # coward
        if hand[0] <=4 and hand[0] >=1:
            fold(player)
        elif hand[0] >=5 and hand[0] <=6:
            call(player, table)
        elif hand[0] >=7:
            raise_bet(player, table, bet)
        else:
            print("something is wrong with the betting procedure.")
    else:
        print "You fucked up!"


def pre_flop_betting(player, table):
    rand = random.randrange(0,5)
    if rand == 0:
        fold(player)
    elif rand == 1:
        check(player, table)
    elif rand == 2 or rand == 3:
        call(player, table)
    else:
        raise_bet(player, table, bet)

def test(game):
    t = 1000
    pot = 0
    for p in game.getPlayers():
        pot+=p.money
    pot+=game.getTable().get_pot()
    if pot != t:
        print "AVVIK!!!: ", pot, " - ", t

def evaluateHandLastPhase(game, player):
    return 1

    #valid actions from getAction() is raise/call/fold
def evaluateHand(game, player):
    if player.phase == 1:
        gameHand = player.hand + game.getTable().get_cards()
        hand = cards.calc_cards_power(gameHand, len(gameHand))
        #print "PHASE1: ", hand
        evaluateHandNormal(player, game.getTable(), hand)
    elif player.strategy == 3:
        print "PHASE2: "
        evaluateHandLastPhase(game, player)
    #test(game)
    checkValue = player.strategy.getAction(game, player)
    #print checkValue
    #if player.strategy.aggressive == False and player.strategy.coward == False:
    #    evaluateHandNormal(player, table, hand)
    #el
    if checkValue == "raise":
        #print "###################\n RAISE \n#####################"
        #print player.strategy.aggressive
        raise_bet(player, game.getTable(), bet)
    elif checkValue == "call":
        #print "###################\n CALL \n#####################"
        #print player.strategy.aggressive
        call(player, game.getTable())
    elif checkValue == "fold":
        #print "###################\n FOLD \n#####################"
        #print player.strategy.aggressive
        fold(player)
    elif checkValue == "check":
        #print "###################\n CHECK \n#####################"
        check(player, game.getTable())
    else:
        print "Betting strategy do not work!"