import pymongo
import csv

try:
	client = pymongo.MongoClient()
	client.drop_database('assignment3mongodb')
except Exception as e:
	print(e)

db = client['assignment3mongodb']
movies_collection = db['movies']


# Question: 2
print('----------------------Question: 2----------------------')
datalist = [{'title': 'The Avengers (2012)', 'genre': 'Sci-Fci', 'rating': 9},
			{'title': 'Thor (2011)', 'genre': 'Sci-Fci', 'rating': 9.5},
			{'title': 'Captain Marvel (2019)', 'genre': 'Sci-Fci', 'rating': 7},
			{'title': 'Doctor Strange (2016)', 'genre': 'Sci-Fci', 'rating': 10},
			{'title': 'Guardians of the galaxy (2014)', 'genre': 'Sci-Fci', 'rating': 6}]

results = movies_collection.insert_many(datalist)
print('5 movies added to the database in movies collection')


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
for id in movies_collection.find({}, {'_id': 1}).limit(2):
	movies_collection.update_one({"_id": id['_id']}, {"$set": {"review": reviews.pop(0)}})
print('Reviews added successfully to 2 of the movies')

for id in movies_collection.find({}, {'_id': 1}).skip(2).limit(1):
	movies_collection.update_one({"_id": id['_id']}, {"$set": {"rating": 5}})
print('Rating changed for one other movie')


# Question: 5
print('----------------------Question: 5----------------------')
ratings_collection = db['ratings']
tags_collection = db['tags']

movies_list = []
with open("data/movies.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    	movies_list.append({'movieId': row[0], 'title': row[1], 'genres': row[2]})

results = movies_collection.insert_many(movies_list)
print('Movies inserted successfully from the csv')


ratings_list = []
with open("data/ratings.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    	ratings_list.append({'userId': row[0], 'movieId': row[1], 'rating': row[2], 'timestamp': row[3]})

ratings = ratings_collection.insert_many(ratings_list)
print('Ratings inserted successfully from the csv')


tags_list = []
with open("data/tags.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    	tags_list.append({'userId': row[0], 'movieId': row[1], 'tag': row[2], 'timestamp': row[3]})

tags = tags_collection.insert_many(tags_list)
print('Tags inserted successfully from the csv')


