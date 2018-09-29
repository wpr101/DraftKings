import csv
from itertools import combinations
import random

FAN_DUEL = False

f = open('/data/DKSalariesROMAN9-30.csv', 'rb')
reader = csv.reader(f)
QBs = []
RBs = []
WRs = []
TEs = []
DSTs = []
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
    if points > 0:
        entry = Player(spot, name, position, salary, team, points)
        if spot == 'QB':
            QBs.append(entry)
        elif spot == 'RB':
            RBs.append(entry)
        elif spot == 'WR':
            WRs.append(entry)
        elif spot == 'TE':
            TEs.append(entry)
        elif spot == 'DST':
            DSTs.append(entry)
f.close()

fd_QBs = []
fd_RBs = []
fd_WRs = []
fd_TEs = []
fd_DSTs = []
if FAN_DUEL == True:
    f = open('./data/FanDuel-NFL-2018-09-30-28509-players-list.csv', 'rb')
    reader = csv.reader(f)
    first_line = True

    for line in reader:
        if first_line == True:
            first_line = False
            continue
        position = line[1]
        name = line[3]
        fd_fppg = round(float(line[5]),2)
        injury = line[11]
        if fd_fppg > 0 and injury == '':
            fd_entry = [position,name,fd_fppg]
            if position == 'QB':
                fd_QBs.append(fd_entry)
            elif position == 'RB':
                fd_RBs.append(fd_entry)
            elif position == 'WR':
                fd_WRs.append(fd_entry)
            elif position == 'TE':
                fd_TEs.append(fd_entry)
            elif position == 'D':
                fd_DSTs.append(fd_entry)

    count = 0
    for dk_qb in QBs:
        for fd_qb in fd_QBs:
            if fd_qb[1] == dk_qb[1]:
                print fd_qb[1]
                print fd_qb[2]
                print dk_qb[3]
                average = round((fd_qb[2] + dk_qb[3]) / 2, 2)
                print average
                print ''



top_points = 0
while True:
    total_points = 0
    QB = random.choice(QBs)
    while 'Manning' not in QB.name:
        QB = random.choice(QBs)
    RB1 = random.choice(RBs)
    RB2 = random.choice(RBs)
    while RB1.name == RB2.name:
        RB2 = random.choice(RBs)
    WR1 = random.choice(WRs)
    count = 0
    while WR1.team != QB.team:
        WR1 = random.choice(WRs)
    WR2 = random.choice(WRs)
    while WR1.name == WR2.name:
        WR2 = random.choice(WRs)
    WR3 = random.choice(WRs)
    while (WR3.name == WR2.name) or (WR3.name == WR1.name):
        WR3 = random.choice(WRs)
    TE = random.choice(TEs)
    FLEX = random.choice(RBs + WRs + TEs)
    while (FLEX.name == WR1.name) or (FLEX.name == WR2.name) or (FLEX.name == WR3.name) \
          or (FLEX.name == RB1.name) or (FLEX.name == RB2.name) or (FLEX.name == TE.name):
        FLEX = random.choice(RBs + WRs + TEs)
    DST = random.choice(DSTs)

    total_salary = QB.salary + RB1.salary + RB2.salary + WR1.salary + WR2.salary + WR3.salary + \
                   TE.salary + FLEX.salary + DST.salary
    if total_salary <= 49000 or total_salary > 50000:
        continue
    total_points = QB.points + RB1.points + RB2.points + WR1.points + WR2.points + WR3.points + \
                   TE.points + FLEX.points + DST.points
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
        print("salary", total_salary)
        print("points", total_points)
        print("")

    

