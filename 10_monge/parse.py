import pymongo, json
from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client['test']
collection = db.prize

#read data into db
if(collection.count()==0):
    file = open("data.json", "r")
    content = file.readlines()
    for line in content:
        collection.insert_one(loads(line))

def prize_subject(subject):
    return collection.find({"prizes.category" : subject}, {"_id" : 0, "laureates.firstname" : 1, "laureates.lastname" : 1})
