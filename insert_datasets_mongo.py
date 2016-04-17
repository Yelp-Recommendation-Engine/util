import pymongo 
import json 
from pymongo import MongoClient

connection = MongoClient("mongodb://localhost:27017")

db = connection.recommender 
business_coll = db.businesses
review_coll = db.reviews
user_coll = db.users

with open('yelp_academic_dataset_business.json', 'r') as f:
        for line in f:
        	business_coll.insert(json.loads(line))

with open('yelp_academic_dataset_user.json', 'r') as f:
        for line in f:
        	user_coll.insert(json.loads(line))

with open('yelp_academic_dataset_review.json', 'r') as f:
        for line in f:
	    	data = json.loads(line)
	    	#Remove text field from each review
	    	data.pop("text", None) 
	        review_coll.insert(data)

