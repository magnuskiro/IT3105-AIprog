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
preFlopList = {}

class Strategy:

    def __init__(self, type):
        global preFlopList
        preFlopList = readPreFlopRollouts.read()
        print preFlopList, "test"
        if type=="aggressive":
            self.aggressive = True
            self.coward = False
            self.raiseRate = 10
            self.callRate = 5
            self.checkRate = 5
            self.foldRate = 0
        elif type=="coward":
            self.aggressive = False
            self.coward = True
            self.raiseRate = 2
            self.callRate = 5
            self.checkRate = 8
            self.foldRate = 6
        else:
            self.aggressive = False
            self.coward = False
            self.callRate = 0
            self.raiseRate = 0
            self.checkRate = 0
            self.foldRate = 0

    def calculateAction(self, hand, numPlayers):
        rr = self.raiseRate * hand[0]
        cr = self.callRate * hand[0]
        chr = self.checkRate * hand[0]
        fr = self.foldRate * hand[0]
        action = rr -fr + ((cr + chr) / 2) + random.randrange(0,20)*0.5
        preFlopList[hand][numPlayers]
        print "ACTION"
        print action
        return action

    #returns the action of the player, call/raise/check.
    def getAction(self, hand, numPlayers):
        action = self.calculateAction(hand, numPlayers)
        if action>60:
            return "raise"
        elif action<60 and action >25:
            return "call"
        else:
            return "fold"

#for testing purposes.
#preFlopList = readPreFlopRollouts.read()
#print preFlopList["2H4S"]