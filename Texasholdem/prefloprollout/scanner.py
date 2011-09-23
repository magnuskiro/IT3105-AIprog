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
import operator

wins = 0
losses = 0
draw = 0
handChances = []
out = "results.txt"
file = open(out, 'wb')

def read():
    global wins
    global losses
    global draw
    new = False
    filename = "rolloutTable.txt"
    file = open(filename, "r")
    line = file.readline()
    if line[0] == "[":
        print "new hand", line
        hand = line
    while len(line) != 0:
        if line[0] == "w" or line[0] == "d" or line[0] == "l":
            #for the 9sets with 1-9 number of opponents.
            for i in range(0,9):
                countLine(line) # counts wins and losses on the give line.
                evaluateLine() # calculate the winning chance.
                resetCount() # reset counters
                line = file.readline()
            record(hand)
        elif line[0] == "[":
            hand = line.rstrip()
            print "new hand", hand
            line = file.readline()

def evaluateLine():
    global wins
    global losses
    global draw
    global handChances
    chance = (wins*1.0)/((wins+losses+draw))
    handChances.append(chance)
    print "winChance: ", chance, " w:", wins, " l:", losses, " d:", draw

def countLine(line):
    global wins
    global losses
    global draw
    for c in line:
        if c == "d":
            draw+=1
        elif c == "w":
            wins+=1
        elif c == "l":
            losses+=1

def resetCount():
    global wins
    global losses
    global draw
    wins = 0
    losses = 0
    draw = 0

def record(hand):
    global handChances
    te = {hand: handChances}
    #print hand, te[hand]
    #print te[hand][5]
    output = hand, handChances
    print >> file, output
    #print "recordOutput: ", output
    handChances = []

read()
file.close()