from math import sqrt

critics = {'Lisa Rose': {'Lady in the water': 2.5,
                         'Snakes on a Plane': 3.5,
                         'Just my Luck': 3.0,
                         'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0
                         },
          'Gene Seymour': {'Lady in the water': 2.5,
                         'Snakes on a Plane': 3.5,
                         'Just my Luck': 3.0,
                         'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0
                         },
          'Michael Phillips': {'Lady in the water': 2.5,
                         'Snakes on a Plane': 3.5,
                         'Just my Luck': 3.0,
                         'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0
                         },
          'Claudia Puig': {'Lady in the water': 2.5,
                         'Snakes on a Plane': 3.5,
                         'Just my Luck': 3.0,
                         'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0
                         },
          'Mick LaSalle': {'Lady in the water': 2.5,
                         'Snakes on a Plane': 4.5,
                         'Just my Luck': 3.0,
                         'Superman Returns': 4.0,
                         'You, Me and Dupree': 1.0,
                         'The Night Listener': 3.0
                         },
          'Jack Matthews': {'Lady in the water': 2.5,
                         'Snakes on a Plane': 3.5,
                         'Just my Luck': 3.0,
                         'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0
                         },
          'Toby': {'Snakes on a Plane': 4.5,
                         'You, Me and Dupree': 1.0,
                         'Superman Returns': 4.0}
          }

#Euclidian
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0: return 0

    sum_of_squares = sum([pow(float(prefs[person1][item].replace(",", ".")) - float(prefs[person2][item].replace(",", ".")), 2) for item in si])
    return 1 / (1 + sqrt(sum_of_squares))

def sim_pearson(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1

    n = len(si)
    if n == 0: return 0

    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    sum1Sq = sum([pow(prefs[person1][item], 2) for item in si])
    sum2Sq = sum([pow(prefs[person2][item], 2) for item in si])

    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r

def top_matchs(prefs, person, n = 5):
    scores = [(sim_distance(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

def get_recommendations(prefs, person):
    totals = {}
    sim_sums = {}

    for other in prefs:
        if other == person: continue

        sim = sim_distance(prefs, person, other)

        if sim <= 0: continue

        for item in prefs[other]:

            if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item, 0)
				totals[item] += float(prefs[other][item].replace(",", ".")) * sim
				
				sim_sums.setdefault(item, 0)
				sim_sums[item] += sim

    ranking = [(total/sim_sums[item], item) for item, total in totals.items()]

    ranking.sort()
    #ranking.reverse()

    return ranking