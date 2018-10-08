import csv
from itertools import combinations

FOLDER = 'monday-night-10-8'

class Player():
    def __init__(self, name, cost, position):
        self.name = name
        self.position = position
        self.cost = cost
        self.points = 0
        self.value = 0

    def __repr__(self):
        return 'Player(name=%s, cost=%s, position=%s, points=%s)' % \
               (self.name, self.cost, self.position, self.points)
    
f = open('./data/' + FOLDER + '/DKSalaries.csv', 'rb')
reader = csv.reader(f)
data = []
seen = []
for line in reader:
    name = line[2]
    cost = line[5]
    roster_position = line[4]
    avg_points = line[8]
    if avg_points > 0:
        data.append(Player(name,cost,roster_position))
f.close()

# Remove title
data.pop(0)

f_roto = open('./data/' + FOLDER + '/rotowire-NFL-players-roto.csv', 'rb')
f_pff = open('./data/' + FOLDER + '/rotowire-NFL-players-pff.csv', 'rb')
f_outsiders = open('./data/' + FOLDER + '/rotowire-NFL-players-outsiders.csv', 'rb')
r_roto = csv.reader(f_roto)
r_pff = csv.reader(f_pff)
r_outsiders = csv.reader(f_outsiders)

count = 0
for line in r_roto:
    if count < 2:
        count += 1
        continue
    line = line[0].split('\t')
    r_name = line[0]
    for player in data:
        if r_name == player.name:
            player.points = float(line[10])
            player.value = float(line[11])

count = 0
for line in r_pff:
    if count < 2:
        count += 1
        continue
    line = line[0].split('\t')
    r_name = line[0]
    for player in data:
        if r_name == player.name:
            player.points = round((float(line[10]) * .5) + (player.points * .5),2)
            player.value = round((float(line[11]) * .5) + (player.value * .5),2)

count = 0
for line in r_outsiders:
    if count < 2:
        count += 1
        continue
    line = line[0].split('\t')
    r_name = line[0]
    for player in data:
        if r_name == player.name:
            if not float(line[10]) == 10.0:
                player.points = round((float(line[10]) * .3333) + (player.points * .6666),2)
                player.value = round((float(line[11]) * .3333) + (player.value * .6666),2)
            

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
    total_value = 0
    too_many_captains = False
    for player in lineup:       
        if player.position == 'CPT':
            captain_count += 1
            if captain_count > 1:
                too_many_captains = True
                break
            cost += float(player.cost)
            avg_points += float(player.points) * 1.5
        else:
            cost += float(player.cost)
            avg_points += float(player.points)
        total_value += player.value
    if (cost > 50000 or cost < 48500) or (too_many_captains == True) or (captain_count == 0):
        continue
    double_player = False
    for i in lineup:
        counter = 0
        for j in lineup:
            if i.name == j.name:
                counter += 1
                if counter > 1:
                    double_player = True
                    break
    if double_player:
        continue
    the_captain = False
    a_player = False
    for player in lineup:
        if 'Ingram' in player.name and player.position == 'CPT':
            the_captain = True
        '''if 'Crowder' in player.name:
            a_player = True'''
    if not the_captain:# or not a_player:
        continue
                    
    if avg_points > best_score:
        best_lineup = lineup
        best_score = avg_points
        print(best_lineup)
        print("best_score:", round(best_score,2))
        print("total_value:", round(total_value,2))
        #print("avg_points", avg_points)
        print("cost:", cost)
        print("")


    
