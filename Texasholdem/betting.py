#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       player.py
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

#5. after the flop, players evaluate the power of their hands; weak(1-3), mediocre(4-6), strong(7-9)
#6. weak players fold, call or check at random (perhaps with a weighted randomness, players with a hand of strengt 1 fold more often than 3?)
#7. mediocre players call or raise at random (again, with weighted randomness?)
import random
import cards


def doBet(player, table):
    amount = 10
    player.loose_money(amount)
    table.increase_pot(amount)
    print("betting complete")

def small_blind(player):
    blind = 5
    player.loose_money(blind)
    table.increase_pot(blind)
    player.set_bet(blind)

def big_blind(player):
    blind = 10
    player.loose_money(blind)
    player.set_bet(blind)
    table.increase_pot(blind)
    table.raise_bet(blind)

def fold(player):
    print ("player folds")

def call(player, table):
    amount = table.get_bet() - player.get_bet()
    player.loose_money(amount)
    player.set_bet(amount)
    print ("player calls")

def raise_bet(player, table):
    amount = 10
    difference = table.get_bet() - player.get_bet()
    player.loose_money(amount + difference)
    table.increase_pot(amount + difference)
    table.raise_bet(amount)
    print ("player bets %d" %(amount))
    
def weak(player, table):
    prob = random.randrange(0,6)    # 0-2 = fold, 3-4 = call, 5 = raise
    print ("random is %d" %(prob))
    if prob < 3:
        fold(player)
    elif prob == 3 or prob == 4:
        call(player, table)
    else:
        raise_bet(player, table)
    #print("weak hand: %s" % (hand))
    #return hand

def mediocre(player, table):
    prob = random.randrange(0,8)    # 0-1 = fold, 2-3 = call, 4-7 = raise
    print ("random is %d" %(prob))
    if prob < 2:
        fold(player)
    elif prob == 2 or prob == 3:
        call(player, table)
    else:
        raise_bet(player, table)
    #print("mediocre hand: %s" % (hand))
    #return hand

def strong(player, table):
    prob = random.randrange(0,10)   # 0-1 = fold, 2-3 = call, 5-9 = raise
    print ("random is %d" %(prob))
    if prob < 2:
        fold(player)
    elif prob == 2 or prob == 3:
        call(player, table)
    else:
        raise_bet(player, table)
    #print("strong hand: %s" % (hand))
    #return hand

def evaluateHand(player, table, hand):
    #find out it the hand is weak/mediocre/strong.
    if hand[0] <=3 and hand[0] >=1:
        weak(player, table)
    elif hand[0] >=4 and hand[0] <=6:
        mediocre(player, table)
    elif hand[0] <=9 and hand[0] >=7:
        strong(player, table)
    else:
        print("something is wrong with the betting procedure.")

def playerBet(players):
    for p in players:
        evaluateHand(p.get_hand())



