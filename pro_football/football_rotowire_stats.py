import csv
from itertools import combinations
import random

FOLDER = 'sunday-main-10-19'
ROTO_FACTOR = 0
PFF_FACTOR = 1
OUTSIDERS_FACTOR = 0

class Player():
    def __init__(self, name, position, team, odds, team_points, salary, points, value):
        self.name = name
        self.position = position
        self.team = team
        self.odds = odds
        self.team_points = team_points
        self.salary = salary
        self.points = points
        self.value = value

    def __repr__(self):
        return 'Player(name=%s, position=%s, team=%s, odds=%s, team_points=%s, salary=%s, points=%s, value=%s)' % \
               (self.name, self.position, self.team, self.odds, self.team_points, self.salary, self.points, self.value)
    

f = open('./data/' + FOLDER + './rotowire-NFL-players-outsiders.csv', 'rb')
reader = csv.reader(f)
QBs = []
RBs = []
WRs = []
TEs = []
DSTs = []
count = 0

for line in reader:
    if count < 2:
        count += 1
        continue
    line = line[0].split('\t')
    name = line[0]      
    position = line[1]
    team = line[2]
    odds = int(line[4])
    team_points = float(line[7])
    salary = int(line[9])
    points = float(line[10]) 
    value = float(line[11])
    if points > 0 and 'Ebron' not in name and 'Olson' not in name and 'Watson' not in name:
        points = points * OUTSIDERS_FACTOR
        value = value * OUTSIDERS_FACTOR
        entry = Player(name, position, team, odds, team_points, salary, points, value)
        if position == 'QB':
            QBs.append(entry)
        elif position == 'RB':
            RBs.append(entry)
        elif position == 'WR':
            WRs.append(entry)
        elif position == 'TE':
            TEs.append(entry)
        elif position == 'D':
            DSTs.append(entry)
f.close()


count = 0
f = open('./data/' + FOLDER + '/rotowire-NFL-players-pff.csv', 'rb')
reader = csv.reader(f)
for line in reader:
    if count < 2:
        count += 1
        continue
    line = line[0].split('\t')
    name = line[0]      
    position = line[1]
    team = line[2]
    odds = int(line[4])
    team_points = float(line[7])
    salary = int(line[9])
    points = float(line[10])
    value = float(line[11])
    if points > 0:
        entry = Player(name, position, team, odds, team_points, salary, points, value)
        if position == 'QB':
            for guy in QBs:
                if entry.name == guy.name:
                    guy.points += entry.points * PFF_FACTOR
                    guy.value += entry.value * PFF_FACTOR
        elif position == 'RB':
            for guy in RBs:
                if entry.name == guy.name:
                    guy.points += entry.points * PFF_FACTOR
                    guy.value += entry.value * PFF_FACTOR
        elif position == 'WR':
            for guy in WRs:
                if entry.name == guy.name:
                    guy.points += entry.points * PFF_FACTOR
                    guy.value += entry.value * PFF_FACTOR
        elif position == 'TE':
            for guy in TEs:
                if entry.name == guy.name:
                    guy.points += entry.points * PFF_FACTOR
                    guy.value += entry.value * PFF_FACTOR
        elif position == 'D':
            for guy in DSTs:
                if entry.name == guy.name:
                    guy.points += entry.points * PFF_FACTOR
                    guy.value += entry.value * PFF_FACTOR
f.close()

count = 0
f = open('./data/' + FOLDER + '/rotowire-NFL-players-roto.csv', 'rb')
reader = csv.reader(f)
for line in reader:
    if count < 2:
        count += 1
        continue
    line = line[0].split('\t')
    name = line[0]      
    position = line[1]
    team = line[2]
    odds = int(line[4])
    team_points = float(line[7])
    salary = int(line[9])
    points = float(line[10])
    value = float(line[11])
    if points > 0:
        entry = Player(name, position, team, odds, team_points, salary, points, value)
        if position == 'QB':
            for guy in QBs:
                if entry.name == guy.name:
                    guy.points += entry.points * ROTO_FACTOR
                    guy.value += entry.value * ROTO_FACTOR
        elif position == 'RB':
            for guy in RBs:
                if entry.name == guy.name:
                    guy.points += entry.points * ROTO_FACTOR
                    guy.value += entry.value * ROTO_FACTOR
        elif position == 'WR':
            for guy in WRs:
                if entry.name == guy.name:
                    guy.points += entry.points * ROTO_FACTOR
                    guy.value += entry.value * ROTO_FACTOR
        elif position == 'TE':
            for guy in TEs:
                if entry.name == guy.name:
                    guy.points += entry.points * ROTO_FACTOR
                    guy.value += entry.value * ROTO_FACTOR
        elif position == 'D':
            for guy in DSTs:
                if entry.name == guy.name:
                    guy.points += entry.points * ROTO_FACTOR
                    guy.value += entry.value * ROTO_FACTOR
f.close()





top_points = 0
top_value = 0
while True:
    total_points = 0
    QB = random.choice(QBs)
    while 'Flacco' not in QB.name:
        QB = random.choice(QBs)
    RB1 = random.choice(RBs)
    #while 'Edel' not in RB1.name:
        #RB1 = random.choice(RBs)
    RB2 = random.choice(RBs)
    while RB1.name == RB2.name :
        RB2 = random.choice(RBs)
    WR1 = random.choice(WRs)
    #while 'Brown' not in WR1.name:
        #WR1 = random.choice(WRs)
    count = 0
    while WR1.team != QB.team:
        WR1 = random.choice(WRs)
        count += 1
        if count > 500:
            break
    WR2 = random.choice(WRs)
    while WR1.name == WR2.name:
        WR2 = random.choice(WRs)
    WR3 = random.choice(WRs)
    while (WR3.name == WR2.name) or (WR3.name == WR1.name):
        WR3 = random.choice(WRs)
    TE = random.choice(TEs)
    #while 'Boyle' not in TE.name:
        #TE = random.choice(TEs)
    FLEX = random.choice(RBs + WRs + TEs)
    while (FLEX.name == WR1.name) or (FLEX.name == WR2.name) or (FLEX.name == WR3.name) \
          or (FLEX.name == RB1.name) or (FLEX.name == RB2.name) or (FLEX.name == TE.name):
        FLEX = random.choice(RBs + WRs + TEs)
    DST = random.choice(DSTs)
    #while 'Jag' not in DST.name:
        #DST = random.choice(DSTs)

    total_salary = QB.salary + RB1.salary + RB2.salary + WR1.salary + WR2.salary + WR3.salary + \
                   TE.salary + FLEX.salary + DST.salary
    if total_salary > 50000:
        continue
    total_points = QB.points + RB1.points + RB2.points + WR1.points + WR2.points + WR3.points + \
                   TE.points + FLEX.points + DST.points
    total_value = QB.value + RB1.value + RB2.value + WR1.value + WR2.value + WR3.value + \
                   TE.value + FLEX.value + DST.value
    #if total_points > 149.5:
    if total_points > top_points:
        top_points = total_points
        print(QB)
        print(RB1)
        print(RB2)
        print(WR1)
        print(WR2)
        print(WR3)
        print(TE)
        print(FLEX)
        print(DST)
        print("salary", round(total_salary,2))
        print("points", round(total_points,2))
        print("value", round(total_value,2))
        print("")

    

