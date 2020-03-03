#Emory Walsh & Leia Park
#SoftDev1 pd9
#K10 -- Import/Export Bank
#2020-03-04

"""
Dataset: Current US Representatives
Description: Contains data on all current US representatives including personal information and political background
Hyperlink: https://www.govtrack.us/api/v2/role?current=true&role_type=representative&limit=438
Import mechanism summary: By importing pymongo, json, and pprint, we gain access to the codes in those modules.
"""

import pymongo, json, pprint
from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client['test']
collection = db.representatives

#read data into db
if(collection.count()==0):
    file = open("reps.json", "r")
    content = file.readlines()
    for line in content:
        collection.insert_one(loads(line))

# get all the names of US representatives in a certain party
def getParty(party):
    data = collection.find({"party": party})
    for people in data:
        for key, value in people.items():
            if key == "name":
                print("{name: %s}" % value)

# get the details of a specific US representative
def findPerson(fname, lname):
    data = collection.find({"firstname": fname, "lastname": lname})
    for item in data:
        pprint.pprint(item)

# get the phone number of a US representative
def getPhoneNum(fname, lname):
    data = collection.find({"firstname": fname, "lastname": lname})
    for item in data:
        for key, value in data.items():
            if key == "phone":
                print("{phone: %s}" % value)

# get the address of representative's office
def getOffice(fname, lname):
    data = collection.find({"firstname": fname, "lastname": lname})
    for item in data:
        for key, value in data.items():
            if key == "office":
                print("{office %s}" % value)


# TEST
getParty("Democrat")
findPerson("Kevin", "Brady")
getPhoneNum("Jim", "Cooper")
getOffice("Sheila", "Jackson Lee")
