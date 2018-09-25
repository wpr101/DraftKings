import csv
from itertools import combinations
import random

f = open('./data/DKSalariesROMAN9-30.csv', 'rb')
reader = csv.reader(f)
QBs = []
RBs = []
WRs = []
TEs = []
DSTs = []
first_line = True

for line in reader:
    if first_line == True:
        first_line = False
        continue
        
    position = line[0]
    name = line[2]
    salary = int(line[5])
    points = float(line[8])
    if points > 0:
        entry = (position, name, salary, points)
        if position == 'QB':
            QBs.append(entry)
        elif position == 'RB':
            RBs.append(entry)
        elif position == 'WR':
            WRs.append(entry)
        elif position == 'TE':
            TEs.append(entry)
        elif position == 'DST':
            DSTs.append(entry)
f.close()

top_points = 0
while True:
    total_points = 0
    QB = random.choice(QBs)
    RB1 = random.choice(RBs)
    RB2 = random.choice(RBs)
    while RB1[1] == RB2[1]:
        RB2 = random.choice(RBs)
    WR1 = random.choice(WRs)
    WR2 = random.choice(WRs)
    while WR1[1] == WR2[1]:
        WR2 = random.choice(WRs)
    WR3 = random.choice(WRs)
    while (WR3[1] == WR2[1]) or (WR3[1] == WR1[1]):
        WR3 = random.choice(WRs)
    TE = random.choice(TEs)
    FLEX = random.choice(RBs + WRs + TEs)
    while (FLEX[1] == WR1[1]) or (FLEX[1] == WR2[1]) or (FLEX[1] == WR3[1]) \
          or (FLEX[1] == RB1[1]) or (FLEX[1] == RB2[1]) or (FLEX[1] == TE[1]):
        FLEX = random.choice(RBs + WRs + TEs)
    DST = random.choice(DSTs)

    total_salary = QB[2] + RB1[2] + RB2[2] + WR1[2] + WR2[2] + WR3[2] + \
                   TE[2] + FLEX[2] + DST[2]
    if total_salary <= 49000 or total_salary > 50000:
        continue
    total_points = QB[3] + RB1[3] + RB2[3] + WR1[3] + WR2[3] + WR3[3] + \
                   TE[3] + FLEX[3] + DST[3]
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

    

