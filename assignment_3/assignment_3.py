import pymongo
import csv

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

results = movies_collection.insert_many(datalist)


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
print('----------------------Question: 4----------------------')
reviews = ['It was full of entertainment.', 'Nice movie']
print('----------------------Question: 4----------------------')
for id in movies_collection.find({}, {'_id': 1}).limit(2):
	movies_collection.update_one({"_id": id['_id']}, {"$set": {"review": reviews.pop(0)}})

for id in movies_collection.find({}, {'_id': 1}).skip(2).limit(1):
	movies_collection.update_one({"_id": id['_id']}, {"$set": {"rating": 5}})


# Question: 5
print('----------------------Question: 5----------------------')
ratings_collection = db['ratings']
tags_collection = db['tags']

movies_list = []
with open("data/movies.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    	movies_list.append({'_id': row[0], 'title': row[1], 'genres': row[2]})

results = movies_collection.insert_many(movies_list)


ratings_list = []
with open("data/ratings.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    	ratings_list.append({'userId': row[0], 'movieId': row[1], 'rating': row[2], 'timestamp': row[3]})

ratings = ratings_collection.insert_many(ratings_list)


tags_list = []
with open("data/tags.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    	tags_list.append({'userId': row[0], 'movieId': row[1], 'tag': row[2], 'timestamp': row[3]})

tags = tags_collection.insert_many(tags_list)
