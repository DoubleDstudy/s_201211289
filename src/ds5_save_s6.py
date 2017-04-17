#coding: utf-8
import json
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.myDB
#db.myCol.insert_one({"Persons":[{"id":"405","이름":"js1"},{"id":"406","이름":"js2"}]})
results = db.myCol.find()
for r in results:
    print r['Persons']