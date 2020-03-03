#Emory Walsh & Leia Park
#SoftDev1 pd9
#K10 -- Import/Export Bank
#2020-03-04

import pymongo, json
from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client['test']
collection = db.representatives

#read data into db
if(collection.count()==0):
    file = open("primer-dataset.json", "r")
    content = file.readlines()
    for line in content:
        collection.insert_one(loads(line))
