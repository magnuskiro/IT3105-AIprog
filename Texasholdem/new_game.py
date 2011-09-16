#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       play_poker.py
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

import play_poker

running = False
while not running:
    mode = int(raw_input("Play game(1), debug(2) or do a test run(3)?"))

    if mode == 1:
        running = True
        play_poker.main()
    elif mode == 2:
        running = True
        debug.main()
    elif mode == 3:
        running = True
        run_test()
    else:
        print "Please answer 1, 2 or 3"
