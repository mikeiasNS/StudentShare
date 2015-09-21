from pymongo import MongoClient

def restaurants():
	client = MongoClient()
	db = client.test

	cursor = db.restaurants.find()

	result = []

	for item in cursor:
		result.append(item)
	
	return result