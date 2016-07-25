import urllib2
import sys
import json

class Mode:
    list = 1
    detail = 2


class Argument:
    user = ""
    token = ""
    mode = ""
    def __init__(self,config):
        print "init"
        print config['User']

f = open('config.js', 'r');
config = json.loads(f.read())

print config['User']
x = Argument(config)
