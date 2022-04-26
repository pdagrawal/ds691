import pymongo

client = pymongo.MongoClient()

db = client['mymongodb']

# mycollection = mydb['people']

# datalist = [{'name': 'Jane', 'age': 40}, {'name': 'Mark'}]
# results = mycollection.insert_many(datalist)

# print(results.inserted_ids)

# print(client.list_database_names())

collection = db['people']

# for person in collection.find():
# 	print(person)

# for person in collection.find({'name': 'Jane'}):
# 	print(person)

for person in collection.find({"age": {"$gte": 30}}, {'_id': 0, 'name': 1}):
	print(person)
