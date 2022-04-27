import pymongo
from pymongo import MongoClient
from .creds import *

cluster = MongoClient(MONGODB_URL)
db = cluster["discord"]
collection = db["test"]

post1 = {"_id": 1, "name": "Pradeep1", "score": 5}
post2 = {"_id": 2, "name": "Pradeep1", "score": 5}

collection.update_one({"_id":2}, {"$set":{"name":"Tim"}})
