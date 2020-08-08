#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFPatrol version Web
Learn more about RRF on https://f5nlg.wordpress.com
Check video about RRFTracker on https://www.youtube.com/watch?v=rVW8xczVpEo
73 & 88 de F4HWN Armel
'''

import settings as s
import lib as l

import sys
import time

def main(argv):
    # Boucle principale
    while(True):
        l.read_log()
        time.sleep(s.main_loop)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
