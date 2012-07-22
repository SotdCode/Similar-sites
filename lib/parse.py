#!/usr/bin/env python
# -*- coding: UTF-8 -*

import json
import urllib2

def results(url):
    """Connect, parse results and return similar sites"""
    similar_sites = []
    try:
        site = json.load(urllib2.urlopen('http://www.similarsitesearch.com/api/similar/%s' % (url)))
    except urllib2.URLError:
        print 'Cant connect'
    else:
        for i in range(0, 19):
            try:
                similar = site['r' + str(i)]
            except KeyError:
                print 'Error parsing, maybe you have exceeded your daily limit on similarsitesearch.com'
                break
            else:
                similar_sites.append(similar)
        return similar_sites