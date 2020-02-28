from pymongo import MongoClient
client = MongoClient()
import json

with open('primer-dataset.json') as json:
    for line in json:
        line.replace("$data", "date") #fixing data set
    data = json.load(json)

print(data)
