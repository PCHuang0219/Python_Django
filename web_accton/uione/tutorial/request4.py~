#!/usr/bin/env python

try:   
    import urllib #python2
except:
    import urllib.request as urllib #python3
import sys

req = urllib.Request(sys.argv[1], headers={'User-Agent':'Mozilla/5.0'})
urllib.urlopen(req)

