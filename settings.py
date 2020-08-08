#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFPatrol version Web
Learn more about RRF on https://f5nlg.wordpress.com
Check video about RRFTracker on https://www.youtube.com/watch?v=rVW8xczVpEo
73 & 88 de F4HWN Armel
'''

# Version

version = '0.0.1'

# Settings

rrf_serveur = {
    'RRF1': 'http://rrf.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
    'RRF2': 'http://rrf2.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
    'RRF3': 'http://rrf3.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
    'RRF4': 'http://serveur.f1tzo.com:8081/cgi-bin/RRFBlockIP.py'
}

rrf_json = []

path_json = '/var/www/RRFTracker/rrf_patrol.json'

main_loop = 2.5		# Main loop tempo
