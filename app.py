# livinus felix bassey
# vefforritun1
# 21.09.2018

from sys import argv

import bottle
from bottle import *
# https://docs.python.org/3/library/urllib.html
import urllib.request, json

with urllib.request.urlopen("http://apis.is/currency/m5") as url:
    data = json.loads(url.read().decode())

@route('/')
def index():
    return template('currency',data=data)

bottle.run(host='0.0.0.0', port=argv[1])
