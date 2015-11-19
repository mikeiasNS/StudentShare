from recommendations import sim_distance, sim_pearson, top_matchs, get_recommendations, get_profile
import csv_test, json, ast
from pymongo import MongoClient

client = MongoClient()
db = client.studentShareTest

csv_test.saveStudents()

studJson = csv_test.getStudents()
modelsJson = csv_test.getModels()

prefs = {stud["registry"] : stud["grades"] for stud in studJson}

db.workData.delete_many({})
for stud in studJson:
	if stud == "_id":
		continue

	workData = {"name" : stud["name"]}
	workData["registry"] = stud["registry"]
	workData["warningSubjects"] = get_recommendations(prefs, stud["registry"], top_match = True)
	workData["recommendedSubjects"] = get_recommendations(prefs, stud["registry"], reverse = True, top_match = True)
	workData["topMatchs"] = top_matchs(prefs, stud["registry"])
	workData["profile"] = get_profile(stud["grades"])
		
	db.workData.insert_one(workData)