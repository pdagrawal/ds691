import pymongo
import csv
import os

client = pymongo.MongoClient()
db = client['mymongodb']
data_dir = 'data'

for filename in os.listdir(data_dir):
    data_list = []
    with open(data_dir + '/' + filename, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            data = {}
            for index, column in enumerate(header):
                data[column] = row[index]
            data_list.append(data)
    db[filename.split('.')[0]].insert_many(data_list)
