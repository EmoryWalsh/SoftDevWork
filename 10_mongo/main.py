#Emory Walsh & Leia Park
#SoftDev1 pd9
#K10 -- Import/Export Bank
#2020-03-04

import pymongo, json
from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client['test']
collection = db.movies

#read data into db
if(collection.count() == 0):
    data = json.load(sys.stdin) # read json data from standard input
    strip_whitespace(data)
    json.dump(data, sys.stdout, indent=2)
    file = open("reps.json", "r")
    data = file.readlines()
    data.strip('\n')
    print data
    for line in data:
        collection.insert_one(loads(line))



import json
import sys
from pkgutil import simplegeneric

@simplegeneric
def get_items(obj):
    while False: # no items, a scalar object
        yield None

@get_items.register(dict)
def _(obj):
    return obj.items() # json object. Edit: iteritems() was removed in Python 3

@get_items.register(list)
def _(obj):
    return enumerate(obj) # json array

def strip_whitespace(json_data):
    for key, value in get_items(json_data):
        if hasattr(value, 'strip'): # json string
            json_data[key] = value.strip()
        else:
            strip_whitespace(value) # recursive call


data = json.load(sys.stdin) # read json data from standard input
strip_whitespace(data)
json.dump(data, sys.stdout, indent=2)
