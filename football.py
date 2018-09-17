import csv
from itertools import combinations

class Player:
    def __init__(self):
        self.name = name
        self.cost = cost
        

f = open('DKSalariesFootball9-17.csv', 'rb')
reader = csv.reader(f)
data = []
seen = []
for line in reader:
    name = line[2]
    cost = line[5]
    avg_points = line[8]
    roster_position = line[4]
    data.append((name,cost,avg_points,roster_position))
f.close()

# Remove title
data.pop(0)


my_combos = combinations(data, 6)
good_lineups = []
best_score = 0
best_lineup = None

for lineup in my_combos:
    cost = 0
    avg_points = 0
    captain_count = 0
    too_many_captains = False
    #import pdb
    #pdb.set_trace()
    for player in lineup:
        if player[3] == 'CPT':
            captain_count += 1
            if captain_count > 1:
                too_many_captains = True
            cost += float(player[1])
            avg_points += float(player[2])
        else:
            cost += float(player[1])
            avg_points += float(player[2])
    if (cost > 50000) or (too_many_captains == True):
        continue
    double_player = False
    for i in lineup:
        counter = 0
        for j in lineup:
            if i[0] == j[0]:
                counter += 1
                if counter > 1:
                    double_player = True
    if double_player:
        continue
                    
    if avg_points > best_score:
        best_lineup = lineup
        best_score = avg_points
        print(best_lineup)
        print("best_score:", best_score)
        print("cost:", cost)
        print("")

    
