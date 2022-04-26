import pymongo

client = pymongo.MongoClient()
db = client['mymongodb']
movies_collection = db['movies']

# Question: 2
print('----------------------Question: 2----------------------')
datalist = [{'name': 'Avenger', 'genre': 'Sci-Fci', 'rating': 9},
			{'name': 'Thor', 'genre': 'Sci-Fci', 'rating': 9.5},
			{'name': 'Captain Marvel', 'genre': 'Sci-Fci', 'rating': 7},
			{'name': 'Doctor Strange', 'genre': 'Sci-Fci', 'rating': 10},
			{'name': 'Guardians of the galaxy', 'genre': 'Sci-Fci', 'rating': 6}]

# results = movies_collection.insert_many(datalist)


# Question: 3
print('----------------------Question: 3----------------------')
## a)
print('==========(a) all movies in the database==========')
for movie in movies_collection.find():
	print(movie)

## b)
print('==========(b) find one movie by name==========')
for movie in movies_collection.find({'name': 'Thor'}):
	print(movie)

## c)
print('==========(c) find top 3 high rated movies==========')
for movie in movies_collection.find( { '$query': {}, '$orderby': { 'rating' : -1 } } ).limit(3):
	print(movie)


# Question: 4
reviews = ['It was full of entertainment.', 'Nice movie']
print('----------------------Question: 4----------------------')
for id in movies_collection.find({}, {'_id': 1}).limit(2):
	movies_collection.update_one({"_id": id['_id']}, {"$set": {"review": reviews.pop(0)}})

for id in movies_collection.find({}, {'_id': 1}).skip(2).limit(1):
	movies_collection.update_one({"_id": id['_id']}, {"$set": {"rating": 5}})


