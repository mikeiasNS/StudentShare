from recommendations import sim_distance, sim_pearson, top_matchs, get_recommendations, get_profile
import csv_test, json, ast
from pymongo import MongoClient

client = MongoClient()
db = client.studentShareTest

#csv_test.saveStudents()

jsonStudentsStr = csv_test.getStudents()
modelsJson = csv_test.getModels()

studJson = json.loads(jsonStudentsStr)

studJson = ast.literal_eval(json.dumps(studJson[0]))

#print modelsJson[0]

#print( "Euclidean: ", sim_distance(modelsJson, 'Mikeias', 'Abner') )
#print( "Pearson: ", sim_pearson(critics, 'Lisa Rose', 'Toby') )

#print studJson

db.workData.delete_many({})
for stud in studJson:
	if stud != "_id":
		workData = {"name" : stud}

		workData["warningSubjects"] = get_recommendations(studJson, stud)
		workData["topMatchs"] = top_matchs(studJson, stud)
		workData["profile"] = get_profile(studJson[stud])
		
		db.workData.insert_one(workData)

#for item in cursor:
#	print item
#	print "\n"

#print( "rank ", top_matchs(studJson, 'Mikeias'))
#for item in get_recommendations(studJson, 'Mikeias'):
#	print item
#print csv_test.getStudents()