from recommendations import critics, sim_distance, sim_pearson, top_matchs, get_recommendations
import csv_test, json, ast
from pymongo import MongoClient

client = MongoClient()
db = client.studentShareTest

#csv_test.saveStudents()

jsonStudentsStr = csv_test.getStudents()
jsonModelsStr = csv_test.getModels()

modelsJson = json.loads(jsonModelsStr)
studJson = json.loads(jsonStudentsStr)

modelsJson = ast.literal_eval(json.dumps(modelsJson[0]))
studJson = ast.literal_eval(json.dumps(studJson[0]))

#print modelsJson[0]

#print( "Euclidean: ", sim_distance(modelsJson, 'Mikeias', 'Abner') )
#print( "Pearson: ", sim_pearson(critics, 'Lisa Rose', 'Toby') )

db.workData.delete_many({})
for stud in studJson:
	if stud != "_id":
		workData = {"name" : stud}

		modelsJson[stud] = studJson[stud]
		workData["warningSubjects"] = get_recommendations(studJson, stud)
		workData["topMatchs"] = top_matchs(studJson, stud)
		workData["profile"] = top_matchs(modelsJson, stud)

		modelsJson = json.loads(jsonModelsStr)
		modelsJson = ast.literal_eval(json.dumps(modelsJson[0]))
		
		db.workData.insert_one(workData)

cursor = db.workData.find()

for item in cursor:
	print item
	print "\n"

#print( "rank ", top_matchs(studJson, 'Mikeias'))
#for item in get_recommendations(studJson, 'Mikeias'):
#	print item
#print csv_test.getStudents()