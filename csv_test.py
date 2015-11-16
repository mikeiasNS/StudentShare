# encoding=utf8 
import csv, sys, json, ast
from pymongo import MongoClient
from bson import json_util

# To fix the unicode problem
reload(sys)
sys.setdefaultencoding('utf8')

#instance of mongoDB
client = MongoClient()
db = client.studentShareTest

def saveStudents():
	# loads a csv file
	db.students.delete_many({})
	csv_reader = csv.reader(open("students.csv", "r"), delimiter = ";")

	my_dict = {}

	# iterate in the csv reader
	for row in csv_reader:
		my_dict[row[1]] = {}

	csv_reader = csv.reader(open("students.csv", "r"), delimiter = ";")

	for row in csv_reader:
		my_dict[row[1]].update({row[2] : row[3]})

	db.students.insert_one(my_dict)

def getStudents():
	stud = db.students.find()
	return json_util.dumps(stud)

def saveModels():
	db.models.delete_many({})
	
	# loads a csv file
	csv_reader = csv.reader(open("models.csv", "r"), delimiter = ";")

	my_dict = {}

	# iterate in the csv reader
	for row in csv_reader:
		my_dict[row[0]] = {}

	csv_reader = csv.reader(open("models.csv", "r"), delimiter = ";")

	for row in csv_reader:
		my_dict[row[0]].update({row[1] : row[2]})


	db.models.insert_one(my_dict)

def getModels():
	mod = db.models.find()
	mod = json_util.dumps(mod)
	mod = json.loads(mod)
	mod = ast.literal_eval(json.dumps(mod[0]))

	return mod