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

    for serveur in s.rrf_serveur:
        # Requete HTTP vers le flux json RRFBlockIP
        try:
            r = requests.get(s.rrf_serveur[serveur], verify=False, timeout=1)
            new_json[serveur] = r.json()
        except:
            return False

    if (new_json != s.rrf_json):
        s.rrf_json = new_json.copy()
        with open(s.path_json, 'w') as f:
            json.dump(s.rrf_json, f)

    return True