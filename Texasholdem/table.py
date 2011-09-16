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

class Table:

    def __init__ (self):
        self.pot = 0
        self.cards = []
        self.bet = 0
        
    def increase_pot(self, amount): self.pot += amount

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)

    def add_card(self, card): self.cards.append(card)

    def get_cards(self): return self.cards

    def clear_table(self): 
		del self.cards[:]
		#self.pot = 0
		#self.bet = 0

    def raise_bet(self, amount): self.bet += amount

    def get_bet(self): return self.bet
    
    def get_pot(self): return self.pot
