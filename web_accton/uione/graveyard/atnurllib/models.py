from django.db import models
import urllib.request
from html import parser

# Create your models here.
#urllib.request.urlopen('http://www.ibm.com/')
#print(x.read())

# from https://pythonprogramming.net/urllib-tutorial-python-3/
#
#
# used to parse values into the url
import urllib.parse

url = 'https://www.google.com/search'
values = { 'q' : 'python programming turorials'}


data = urllib.parse.urlencode(values)
data = data.encode('utf-8')         # data should be bytes
req = urllib.request.Request(url, data)
