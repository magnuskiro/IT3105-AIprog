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


def doBet(player):
    amount = 10
    player.loose_money(amount)
    print("betting complete")

def weak(prob):
    prob = random.randrange(0,6)    # 0-2 = fold, 3-4 = call, 5 = raise
    if prob <= 3:
        # fold
        fold()
    elif prob == 3 or 4:
        # call
        call()
    elif prob == 5:
        raise_bet()
    print("weak hand: %s" % (hand))
    #return hand

def mediocre(prob):
    prob = random.randrange(2,8)
    if prob == 2 or 3:
        fold()
    elif prob == 4 or 5:
        call()
    elif prob == 6 or 7:
        raise_bet()
    print("mediocre hand: %s" % (hand))
    #return hand

def strong(prob):
    prob = random.randrange(4,10)   # 4 = fold, 5-6 = call, 7-9 = raise
    if prob == 4:
        fold()
    elif prob == 5 or 6:
        call()
    elif prob >= 7:
        raise_bet()
    print("strong hand: %s" % (hand))
    #return hand

def evaluateHand(hand):
    #find out it the hand is weak/mediocre/strong.
    #hand = cards.calc_cards_power(hand)
    if hand[0] <=3 and hand[0] >=1:
        weak(hand)
    elif hand[0] >=4 and hand[0] <=6:
        mediocre(hand)
    elif hand[0] <=9 and hand[0] >=7:
        strong(hand)
    else:
        print("something is wrong with the betting procedure.")

def playerBet(players):
    for p in players:
        evaluateHand(p.get_hand())



