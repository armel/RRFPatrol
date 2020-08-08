#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFPatrol version Web
Learn more about RRF on https://f5nlg.wordpress.com
Check video about RRFTracker on https://www.youtube.com/watch?v=rVW8xczVpEo
73 & 88 de F4HWN Armel
'''

import settings as s

import requests
import json

def read_log():
    new_json = {}
    check = 0

    print('.')

    for serveur in s.rrf_serveur:
        log = ''
        # Requete HTTP vers le flux json de l'API fournie par F1EVM
        try:
            r = requests.get(s.rrf_serveur[serveur], verify=False, timeout=0.5)
            new_json[serveur] = r.json()
            check += 1
        except:
            pass

    if(check == 4):
        if (new_json != s.rrf_json):
            s.rrf_json = new_json.copy()
            with open(s.path_json, 'w') as f:
                json.dump(s.rrf_json, f)
                print(s.rrf_json)
