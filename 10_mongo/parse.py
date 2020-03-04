#Emory Walsh & Leia Park
#SoftDev1 pd9
#K10 -- Import/Export Bank
#2020-03-04

"""
Dataset: Current US Senators
Description: Contains data on all current US senators including personal information and political background
Hyperlink: https://www.govtrack.us/api/v2/role?current=true&role_type=senator
Import mechanism summary: By importing pymongo, we gain access to the codes in those modules. If there are no collections present in our database, we read from the json file and load them into a collection.
"""

from bson.json_util import loads
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.computers # creates a database
collection = db.senators # adds a collection of senators

# read the data
if(collection.count()==0):
    file = open("senators", "r")
    content = loads(file.read())["objects"]
    for line in content:
        collection.insert_one(line)

# gets US senators of specified gender
def gender(gender):
    return collection.find({"person.gender" : gender}, {"person.name" : 1})

# gets US senators from specified state
def state(state):
    return collection.find({"state" : state}, {"person.name" : 1})

# gets US senators from specified party
def party(party):
    return collection.find({"party" : party}, {"person.name" : 1})

# gets the website of a specific US senator
def website(fname):
    return collection.find({"person.firstname" : fname}, {"person.name" : 1, "website" : 1})

# gets all related information of a specific US senator
def description(lname):
    return collection.find({"person.lastname" : lname}, {"person.name" : 1, "description" : 1})

# helper method
def printer(data):
    for item in data:
        print(item["person"])

# TESTS
print("\nMale representatives")
printer(gender("male"))
print("\nDemocrats")
printer(party("Democrat"))
print("\nME senators")
printer(state("ME"))
print("\nElizabeth's website")
printer(website("Elizabeth"))
print("\nAmy Klobuchar description")
printer(description("Klobuchar"))
