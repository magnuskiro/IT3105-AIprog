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

def read():
    global wins
    global losses
    global draw
    new = False
    filename = "results.txt"
    file = open(filename, "r")
    line = file.readline()
    if line[0] == "[":
        print "new hand", line
        line = file.readline()
    while len(line) != 0:
        if line[0] == "w" or line[0] == "d" or line[0] == "l":
            for c in line:
                if c == "d":
                    draw+=1
                elif c == "w":
                    wins+=1
                elif c == "l":
                    losses+=1
        elif line[0] == "[":
            record()
            print "new hand", line
        line = file.readline()


def record():
    global wins
    global losses
    global draw
    
    print wins
    print losses
    print draw
    wins = 0
    losses = 0
    draw = 0

def writeResults():
    return ""

read()