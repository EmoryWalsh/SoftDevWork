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

def find_gender(gender):
    return senators.find({"person.gender" : gender}, {"_id" : 0, "person.name" : 1})

def find_state(state):
    return senators.find({"state" : state}, {"_id" : 0, "person.name" : 1})

def find_party(party):
    return senators.find({"party" : party}, {"_id" : 0, "person.name" : 1})

def find_website(firstname):
    return senators.find({"person.firstname" : firstname}, {"_id" : 0, "person.name" : 1, "website" : 1})

def find_description(lastname):
    return senators.find({"person.lastname" : lastname}, {"_id" : 0, "person.name" : 1, "description" : 1})




print("-----FINDING ALL SENATORS IN NY-----")
for item in find_state("NY"):
    print(item["person"])

print("-----FINDING ALL DEMOCRATIC SENATORS-----")
for item in find_party("Democrat"):
    print(item["person"])

print("----FINDING ALL FEMALE SENATORS-----")
for item in find_gender("female"):
    print(item["person"])

print("-----FINDING WEBSITE OF SENATORS WHOSE FIRST NAME IS KEVIN")
for item in find_website("kevin"):
    print(item["person"])
