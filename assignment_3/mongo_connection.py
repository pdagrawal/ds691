import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://mongo-db-user:GzThTOx3Q4Wy87p3@cluster0.fakv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["test"]

post1 = {"_id": 1, "name": "Pradeep1", "score": 5}
post2 = {"_id": 2, "name": "Pradeep1", "score": 5}

collection.update_one({"_id":2}, {"$set":{"name":"Tim"}})
