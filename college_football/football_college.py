import csv
from itertools import combinations
import random

f = open('data/DKSalariesLateNight9-29.csv', 'rb')
reader = csv.reader(f)
QBs = []
RBs = []
WRs = []
flexes = []
super_flexes = []
first_line = True

class Player():
    def __init__(self, spot, name, position, salary, team, points):
        self.spot = spot
        self.name = name
        self.position = position
        self.salary = salary
        self.team = team
        self.points = points

    def __repr__(self):
        return 'Player(name=%s, spot=%s, team=%s, points=%s, salary=%s)' % (self.name, self.spot, self.team, self.points, self.salary)

for line in reader:
    if first_line == True:
        first_line = False
        continue
    spot = line[0]      
    name = line[2]
    position = line[4]
    salary = int(line[5])
    team = line[7]
    points = float(line[8])
    if points > 0 and 'Artavis Pierce' not in name:
        our_boy = Player(spot, name, position, salary, team, points)
        if 'QB' in position:
            QBs.append(our_boy)
        elif 'RB' in position:
            RBs.append(our_boy)
        elif 'WR' in position:
            WRs.append(our_boy)
        elif 'WR' or 'RB' in position:
            flexes.append(our_boy)
        elif 'S-FLEX' in position:
            super_flexes.append(our_boy)
f.close()   


top_points = 0
while True:
    total_points = 0
    QB = random.choice(QBs)
    '''while 'Tagova' not in QB.name:
        QB = random.choice(QBs)'''
    RB1 = random.choice(RBs)
    RB2 = random.choice(RBs)
    while RB1.name == RB2.name:
        RB2 = random.choice(RBs)
    WR1 = random.choice(WRs)
    count = 0
    while WR1.team != QB.team:
        WR1 = random.choice(WRs)
        count += 1
        if count > 1000:
            break
    WR2 = random.choice(WRs)
    while WR1.name == WR2.name:
        WR2 = random.choice(WRs)
    FLEX = random.choice(RBs + WRs)
    while (RB1.name == FLEX.name) or (RB2.name == FLEX.name) or (WR1.name == FLEX.name) \
          or (WR2.name == FLEX.name):
        FLEX = random.choice(RBs + WRs)
    S_FLEX = random.choice(QBs)
    while S_FLEX.name == QB.name:# or 'Ehlinger' not in S_FLEX.name:
        S_FLEX = random.choice(QBs)
    WR3 = random.choice(WRs)
    count = 0
    while (WR3.team != S_FLEX.team) or (WR3.name == WR1.name) or (WR3.name == WR2.name) or (WR3.name == FLEX.name):
        WR3 = random.choice(WRs)
        count += 1
        if count > 1000:
            break


    total_salary = QB.salary + RB1.salary + RB2.salary + WR1.salary + WR2.salary + WR3.salary + \
                   FLEX.salary + S_FLEX.salary
    if total_salary <= 49000 or total_salary > 50000:
        continue
    total_points = QB.points + RB1.points + RB2.points + WR1.points + WR2.points + WR3.points + \
                   FLEX.points + S_FLEX.points
    if total_points > top_points:
        top_points = total_points
        print(QB)
        print(RB1)
        print(RB2)
        print(WR1)
        print(WR2)
        print(WR3)
        print(FLEX)
        print(S_FLEX)
        print("salary", total_salary)
        print("points", round(total_points,2))
        print("")

    

