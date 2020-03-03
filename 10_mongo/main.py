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
    file = open("reps.json", "r")
    data = file.readlines()
    for line in data:
        collection.insert_one(loads(line))
