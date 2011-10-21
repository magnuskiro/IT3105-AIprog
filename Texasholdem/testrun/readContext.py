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

def read():
    list = []
    filename = "models.txt"
    file = open(filename, "r")
    dictionary = {}
    line = file.readline()
    while len(line) != 0:
        a = int(line[0])
        if a>=0 and a<=9:
            #print "is digit: ", int(line[0])
            ans = evaluateLine(line)
            #print "ans: \n", ans[1]
            dictionary[ans[0]] = ans[1]
            #print dictionary[ans[0]]
        #print line
        line = file.readline()
    for i in range(0,9):
        if str(i) in dictionary:
            e = dictionary[str(i)]
            #print i, e
            list.append(e)
    #print list
    file.close()
    return list

#liste med dict{}
#dict[244raise] = gjennomsnittet av de verdiene som ligger i lista.

def evaluateLine(line):
    global list
    line = strClean(line)
    line = line.partition(" ")
    playerNumber = line[0]
    #print "player", playerNumber
    line = line[2].partition("]")
    d = {}
    while line[2]:
        conline = line[0][1:]
        #print line
        con = conline.partition(":")
        #print con
        #d[key] = value returned
        d[con[0]]=findAverage(con[2])
        line = line[2].partition("]")
    #print d
    return [playerNumber, d]

def findAverage(line):
    num = 0
    tot = 0
    #print strToList(line)
    for n in strToList(line):
        num+=1
        tot+=float(n)
    #print num
    av = tot/num
    #print "av: ", av
    return av

def strToList(line):
    list = []
    #print "before ", line
    line = strClean(line)
    line = line[1:]
    #print "after ", line
    line = line.partition(" ")
    #print line
    while line[0]:
        #print line[0]
        list.append(line[0])
        line = line[2].partition(" ")
    #print list
    return list

def strClean(line):
    line = line.replace("[","")
    line = line.replace("'","")
    line = line.replace(",","")
    line = line.replace("{","")
    line = line.replace("}","")
    line = line.replace("\n","")
    return line

#read()