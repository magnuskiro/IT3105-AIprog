#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       player.py
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

class Player:

    def __init__(self, money, number):
        self.money = money
        self.hand = []
        self.bet = 0
        self.in_game = True
        self.no = number
        self.blind = False

    def add_money(self, amount): self.money += amount

    def loose_money(self, amount): self.money -= amount

    def get_money(self): return self.money

    def get_hand(self): return self.hand

    def add_card(self, card): self.hand.append(card)

    def clear_hand(self): del self.hand[:]

    def set_bet(self, amount): self.bet += amount

    def get_bet(self): return self.bet
