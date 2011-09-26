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

class Strategy:

    #callRate, raiseRate, checkRate, foldRate, aggressive, coward
    def setValues(self, raiseRate, callRate,  checkRate, foldRate, aggressive, coward):
        self.aggressive = aggressive
        self.coward = coward
        self.callRate = callRate
        self.raiseRate = raiseRate
        self.checkRate = checkRate
        self.foldRate = foldRate

    def __init__(self, type):
        self.preFlopList = {}
        self.preFlopList = readPreFlopRollouts.read()
        print self.preFlopList
        if type=="aggressive":
            self.setValues(10, 5, 5, 1, True, False)
        elif type=="coward":
            self.setValues(2, 5, 8, 6, False, True)
        else:
            self.setValues(0, 0, 0, 0,False, False)

    def calculateAction(self, hand, numPlayers, player):
        rr = self.raiseRate * hand[0]
        cr = self.callRate * hand[0]
        chr = self.checkRate * hand[0]
        fr = self.foldRate * hand[0]
        action = rr -fr + ((cr + chr) / 2) + random.randrange(0,20)*0.5
        print "ACTION: ", action
        return action

    def calculateActionPreFlop(self, hand, numPlayers, player):
        rr = self.raiseRate * hand[0]
        cr = self.callRate * hand[0]
        chr = self.checkRate * hand[0]
        fr = self.foldRate * hand[0]
        key = self.getPreFlopKey(player.hand)
        print key, self.preFlopList[key]
        print "players: ", numPlayers
        chance = self.preFlopList[key][numPlayers-2]
        print float(self.preFlopList[key][numPlayers-2]),"================", chance
        action = rr -fr + ((cr + chr) / 2) + random.randrange(0,20)*0.5
        print "ACtion: ", action, "chance: ", chance
        #action = float(action) * float(chance)
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
    def getAction(self, hand, numPlayers, player, preFlop):
        if preFlop:
            action= self.calculateActionPreFlop(hand, numPlayers, player)
        else:
            action = self.calculateAction(hand, numPlayers, player)
        if action>60:
            return "raise"
        elif action<60 and action >35:
            return "call"
        elif action<35 and action>17:
            return "check"
        else:
            return "fold"

#for testing purposes.
#preFlopList = readPreFlopRollouts.read()
#print preFlopList["2H4S"]

#s  = Strategy("coward")
#print s.callRate, s.raiseRate, s.checkRate, s.foldRate, s.aggressive, s.coward
#print s.test()