from recommendations import critics, sim_distance, sim_pearson, top_matchs, get_recommendations

#print( "Euclidean: ", sim_distance(critics, 'Lisa Rose', 'Toby') )
#print( "Pearson: ", sim_pearson(critics, 'Lisa Rose', 'Toby') )

print( "rank ", top_matchs(critics, 'Toby'))
#for item in get_recommendations(critics, 'Toby'):
#	print item