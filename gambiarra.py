#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (C) 2007 by ULPM: Alexandre Yukio Harano
#                             F�bio Cassarotti Parronchi Navarro
#                             Gabriel Geraldo Fran�a Marcondes
#                             Luiz Carlos Irber J�nior
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys
import os.path
from optparse import OptionParser

# add the libs subdir to the path
basedir = os.path.abspath(os.curdir)
libdir = os.path.join(basedir, "libs")

if not libdir in sys.path:
    sys.path.insert(0, libdir)

from Gambiarra.gambiarra import Game

def main(play_sounds):
    game = Game(play_sounds)
    game.run()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-p', '--profile', action='store_true',
        dest='profile', default=False,
        help='run in profiling mode [default: %default]')
    parser.add_option('-s', '--no-sound', action='store_true',
        dest='sound', default=False,
        help='disable sounds [default: %default]')
    options, args = parser.parse_args()

    if options.profile:
        import cProfile
        cProfile.run('main()', filename='gambiarra.cprof')
    else:
        main(options.sound)
