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
import random
import readPreFlopRollouts
import handstrength
from copy import deepcopy

class Strategy:

    #callRate, raiseRate, checkRate, foldRate, aggressive, coward
    def setValues(self, aggressivePoints):
        self.aggressionPoints = aggressivePoints

    def __init__(self, type):
        self.preFlopList = {}
        self.preFlopList = readPreFlopRollouts.read()
        #print self.preFlopList
        if type=="aggressive":
            self.setValues(5)
        elif type=="coward":
            self.setValues(-5)
        elif type=="bluffer":
            self.setValues(0)
        else:
            self.setValues(0)

    def calculateAction(self, table, player, numPlayers):
        #print "calcAct: ", "hand:", player.hand, "table:", table.get_cards()
        action = handstrength.tryit(player.get_hand(), table.get_cards(), numPlayers)
        #action = rr -fr + ((cr + chr) / 2) + random.randrange(0,20)*0.5
        #print "ACTION: ", action
        return action

    def calculateActionPreFlop(self, hand, numPlayers):
        key = self.getPreFlopKey(hand)
        #print key, self.preFlopList[key][1]
        action = self.preFlopList[key][numPlayers-2]
        action = float(action)
        action *= 100
        #print "Player ", player.no, "hand: ", hand, "ACTION: ", action, "chance: ", chance, "handPower1: ", hand[0]
        #print "player HAND: ", player.get_hand()
        return action

    def pot_odds(self, table, player):
        call_amount = table.bet - player.bet
        odds = call_amount*1.0/(table.pot + call_amount)*1.0
        return odds

    def getPreFlopKey(self, playerHand):
        hand = deepcopy(playerHand)
        #print "preFlopKey: ", playerHand
        if hand[0][0] > hand[1][0]:
            hand = [hand[1], hand[0]]
        if hand[0][1] == hand[1][1]:
            hand[0][1] = 'H'
            hand[1][1] = 'H'
        else:
            hand[0][1] = 'H'
            hand[1][1] = 'S'
        hand = str(hand)
        hand = hand.replace("[","")
        hand = hand.replace("]","")
        hand= hand.replace("'","")
        hand = hand.replace(",","")
        hand = hand.replace(" ","")
        return hand

    #returns the action of the player, call/raise/check.
    def getAction(self, game, player):
        if game.getState()=="preFlop":
            handStrength = self.calculateActionPreFlop(player.get_hand(), game.getLenRemaining())
        else:
            handStrength = self.calculateAction(game.getTable(), player, game.getLenRemaining())
        #print "Player Action: ", action
        p = 200/(game.getLenRemaining())
        potOds = self.pot_odds(game.getTable(), player)*10
        strategyVariation = self.aggressionPoints + potOds
        handStrength+=strategyVariation
        #print "HS: ", handStrength, "PO: ", potOds, "aggression: ", self.aggressionPoints, "p: ", p
        if handStrength>p:
            return "raise"
        elif handStrength<p and handStrength>=(p/1.5):
            return "call"
        elif handStrength<(p/1.5) and handStrength>=(p/2):
            return "check"
        elif handStrength<(p/2):
            return "fold"
        else:
            "Never gonna give you up, Never gonna let you down!"

#for testing purposes.
#preFlopList = readPreFlopRollouts.read()
#print preFlopList["2H4S"]

#s  = Strategy("coward")
#print s.callRate, s.raiseRate, s.checkRate, s.foldRate, s.aggressive, s.coward
#print s.test()

