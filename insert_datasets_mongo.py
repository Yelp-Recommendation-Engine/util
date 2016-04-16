import pymongo 
import json 
from pymongo import MongoClient

connection = MongoClient("mongodb://localhost:27017")

#connection = Connection('localhost', 27017) 
db = connection.recommender 
coll = db.businesses
businesses = {}

with open('yelp_academic_dataset_business.json', 'r') as f:
        for line in f:
        	coll.insert(json.loads(line))
