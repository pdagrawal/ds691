import pymongo
import csv

client = pymongo.MongoClient()
db = client['mymongodb']

movies_collection = db['movies']
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
