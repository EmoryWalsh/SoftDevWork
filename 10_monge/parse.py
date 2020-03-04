from bson.json_util import loads
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.computers

if(collection.count()==0):
    collection = db.senators
    file = open("senators", "r")
    content = loads(file.read())["objects"]
    for line in content:
        collection.insert_one(line)

def ender(gender):
    return senators.find({"person.gender" : gender}, {"person.name" : 1})

def state(state):
    return senators.find({"state" : state}, {"person.name" : 1})

def party(party):
    return senators.find({"party" : party}, {"person.name" : 1})

def website(fname):
    return senators.find({"person.firstname" : fname}, {"person.name" : 1, "website" : 1})

def description(lname):
    return senators.find({"person.lastname" : lname}, {"person.name" : 1, "description" : 1})

def printer(data):
    for answer in data:
        print(item[person])

#Male representatives
printer(gender("male"))
#Democrats
printer(party("Democrat"))
#ME senators
printer(state("ME"))
#Elizabeth's website
printer(website("Elizabeth"))
#Amy Klobuchar description
printer(description("Klobuchar"))
