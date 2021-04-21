#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFPatrol version Web
Learn more about RRF on https://f5nlg.wordpress.com
Check video about RRFTracker on https://www.youtube.com/watch?v=rVW8xczVpEo
73 & 88 de F4HWN Armel
'''

# Version

version = '0.0.4'   # Version
env = 'prod'        # Environnement

# Settings

if env == 'dev':
    rrf_serveur = {
        'RRF1': 'http://localhost/~armel/RRFBlockIP/back/RRFBlockIP.py',
        'RRF2': 'http://localhost/~armel/RRFBlockIP_2/back/RRFBlockIP.py',
        'RRF3': 'http://localhost/~armel/RRFBlockIP_3/back/RRFBlockIP.py',
        'RRF4': 'http://localhost/~armel/RRFBlockIP_4/back/RRFBlockIP.py'
        'RRF5': 'http://localhost/~armel/RRFBlockIP_5/back/RRFBlockIP.py'
    }
    path_json = '/Users/armel/Sites/RRFTracker/rrf_patrol.json'

else:
    rrf_serveur = {
        'RRF1': 'http://rrf.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
        'RRF2': 'http://rrf2.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
        'RRF3': 'http://rrf3.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
        'RRF4': 'http://rrf4.f5nlg.ovh:8080/cgi-bin/RRFBlockIP.py',
        'RRF5': 'http://serveur.f1tzo.com:8081/cgi-bin/RRFBlockIP.py'
    }
    path_json = '/var/www/RRFTracker/rrf_patrol.json'

rrf_json = []

main_loop = 4       # Main loop tempo
