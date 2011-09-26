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

list = {}

def read():
    global list
    #filename = "prefloprollout/results.txt"
    filename = "results.txt"
    file = open(filename, "r")
    line = file.readline()
    while len(line) != 0:
        evaluateLine(line)
        line = file.readline()
    #test()
    file.close()
    return list

def test():
    global list
    for i in list:
        print i
        print list[i]

def evaluateLine(line):
    global list
    line = line.partition("\"")
    hand = line[2].partition("\"")
    hand = hand[0]
    hand = strClean(hand)
    hand = hand.replace(" ","")
    #print hand
    win = line[2].partition("\"")
    win = win[2].partition(" ")
    win = win[2]
    win = win.replace(")\n", "")
    win = strToList(win)
    print win[7]
    list[hand] = win
    #print list

def strToList(line):
    list = []
    line = strClean(line)
    line = line.partition(" ")
    for i in range(0,9):
        list.append(line[0])
        line = line[2].partition(" ")
    #print list
    return list

def strClean(line):
    line = line.replace("[","")
    line = line.replace("]","")
    line = line.replace("'","")
    line = line.replace(",","")
    return line

read()


