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
	db.students.delete_many({})

	# loads a csv file
	csv_reader = csv.reader(open("students.csv", "r"), delimiter = ";")

	my_list = []
	current_registry = ""

	# iterate in the csv reader
	for row in csv_reader:
		if row[0] != current_registry:
			my_list.append({"registry" : row[0], "name" : row[1], "grades" : {row[2] : row[3]} })
			current_registry = row[0]
		else:
			my_list[-1]["grades"].update({row[2] : row[3]})

	db.students.insert_many(my_list)

def getStudents():
	stud = db.students.find()
	stud = json_util.dumps(stud)
	stud = json.loads(stud)
	stud = ast.literal_eval(json.dumps(stud))

	return stud

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