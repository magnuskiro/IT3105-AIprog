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

class Strategy:

    #callRate, raiseRate, checkRate, foldRate, aggressive, coward
    def setValues(self, aggressive, coward, ap):
        self.aggressive = aggressive
        self.coward = coward

    def __init__(self, type):
        self.preFlopList = {}
        self.preFlopList = readPreFlopRollouts.read()
        #print self.preFlopList
        if type=="aggressive":
            self.setValues(True, False, 9)
        elif type=="coward":
            self.setValues(False, True, 1)
        else:
            self.setValues(False, False, 5)

    def calculateAction(self, table, player, numPlayers):
        action = handstrength.tryit(player.hand, table.get_cards(), numPlayers)
        #action = rr -fr + ((cr + chr) / 2) + random.randrange(0,20)*0.5
        #print "ACTION: ", action
        return action

    def calculateActionPreFlop(self, player, numPlayers):
        key = self.getPreFlopKey(player.hand)
        #print key, self.preFlopList[key][1]
        action = self.preFlopList[key][numPlayers-2]
        action = float(action)
        action *= 100
        #print "Player ", player.no, "hand: ", hand, "ACTION: ", action, "chance: ", chance, "handPower1: ", hand[0]
        return action

    def getPreFlopKey(self, hand):
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
    def getAction(self, table, player, numPlayers, preFlop):
        if preFlop:
            action= self.calculateActionPreFlop(player, numPlayers)
        else:
            action = self.calculateAction(table, player, numPlayers)
        #print "PLayer Action: ", action
        if action>15:
            return "raise"
        elif action<15 and action >8:
            return "call"
        elif action<8 and action>1:
            return "check"
        else:
            return "fold"

#for testing purposes.
#preFlopList = readPreFlopRollouts.read()
#print preFlopList["2H4S"]

#s  = Strategy("coward")
#print s.callRate, s.raiseRate, s.checkRate, s.foldRate, s.aggressive, s.coward
#print s.test()