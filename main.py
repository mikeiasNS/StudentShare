from recommendations import critics, sim_distance, sim_pearson, top_matchs, get_recommendations
import csv_test, json, ast

jsonStudentsStr = csv_test.getStudents()
jsonModelsStr = csv_test.getModels()

myJson = json.loads(jsonModelsStr)
studJson = json.loads(jsonStudentsStr)

for k in studJson[0]:
	myJson[0][k] = studJson[0][k]

myJson = ast.literal_eval(json.dumps(myJson[0]))
studJson = ast.literal_eval(json.dumps(studJson[0]))

#print ast.literal_eval(json.dumps(myJson[0]))

#print myJson[0]

#print( "Euclidean: ", sim_distance(myJson, 'Mikeias', 'Abner') )
#print( "Pearson: ", sim_pearson(critics, 'Lisa Rose', 'Toby') )

print( "rank ", top_matchs(studJson, 'Mikeias'))
#for item in get_recommendations(studJson, 'Mikeias'):
	#print item