import csv
from itertools import combinations

OPKR_DATA = False

f = open('./data/DKSalariesFootball9-23.csv', 'rb')
reader = csv.reader(f)
data = []
seen = []
for line in reader:
    name = line[2]
    cost = line[5]
    avg_points = line[8]
    roster_position = line[4]
    # We have OPKR data
    if OPKR_DATA:
        opkr = line[9]
        data.append((name,cost,avg_points,roster_position,opkr))
    else:
        data.append((name,cost,avg_points,roster_position))
f.close()

# Remove title
data.pop(0)


my_combos = combinations(data, 6)
good_lineups = []
best_score = 0
best_lineup = None
#import pdb
#pdb.set_trace()

for lineup in my_combos:
    cost = 0
    avg_points = 0
    captain_count = 0
    too_many_captains = False
    for player in lineup:
        opkr_factor = 1.0
        if OPKR_DATA:
            opkr = int(player[4])
            if opkr >= 18 and opkr < 25:
                opkr_factor = 1.1
            elif opkr >= 25:
                opkr_factor = 1.2
            elif opkr_factor > 8 and opkr <= 14:
                opkr_factor = 0.9
            elif opkr_factor <= 8:
                opkr_factor = 0.8
        if player[3] == 'CPT':
            captain_count += 1
            if captain_count > 1:
                too_many_captains = True
                break
            cost += float(player[1])
            avg_points += float(player[2]) * 1.5 * opkr_factor
        else:
            cost += float(player[1])
            avg_points += float(player[2]) * opkr_factor
    if (cost > 50000 or cost < 48500) or (too_many_captains == True) or (captain_count == 0):
        continue
    double_player = False
    for i in lineup:
        counter = 0
        for j in lineup:
            if i[0] == j[0]:
                counter += 1
                if counter > 1:
                    double_player = True
                    break
    if double_player:
        continue
    the_captain = False
    for player in lineup:
        if (player[0] == 'Golden Tate') and player[3] == 'CPT':
            the_captain = True
    if not the_captain:
        continue
                    
    '''if avg_points > best_score:
        best_lineup = lineup
        best_score = avg_points
        print(best_lineup)
        print("best_score:", best_score)
        #print("avg_points", avg_points)
        print("cost:", cost)
        print("")'''

    if avg_points > 105:
       print(lineup)
       print("cost:", cost)
       print("avg_points", avg_points)
       print("")

    
