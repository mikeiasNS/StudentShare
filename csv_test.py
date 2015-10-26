# encoding=utf8 
import csv, sys, json
from pymongo import MongoClient
from bson import json_util

# To fix the unicode problem
reload(sys)
sys.setdefaultencoding('utf8')

#instance of mongoDB
client = MongoClient()
db = client.teste

# loads a csv file
csv_reader = csv.reader(open("disciplinas.csv", "r"), delimiter = ";")

my_dict = {}

# iterate in the csv reader
for row in csv_reader:
	my_dict[row[1]] = {}

csv_reader = csv.reader(open("disciplinas.csv", "r"), delimiter = ";")

for row in csv_reader:
	my_dict[row[1]].update({row[2] : row[3]})


db.students.insert_one(my_dict)

cursor = db.students.find()
#rules
for student in cursor:
	print json_util.dumps(student)