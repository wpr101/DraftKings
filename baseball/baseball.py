import csv
from itertools import combinations
import random

f = open('data/DKSalariesBaseball9-30.csv', 'rb')
reader = csv.reader(f)
Ps = []
Cs = []
Firsts = []
Seconds = []
Thirds = []
SSs = []
OFs = []
first_line = True

class Player():
    def __init__(self, name, position, salary, team, points):
        self.name = name
        self.position = position
        self.salary = salary
        self.team = team
        self.points = points

    def __repr__(self):
        return 'Player(name=%s, postion=%s, team=%s, points=%s, salary=%s)' \
    % (self.name, self.position, self.team, self.points, self.salary)

for line in reader:
    if first_line == True:
        first_line = False
        continue     
    name = line[2]
    position = line[4]
    salary = int(line[5])
    team = line[7]
    points = float(line[8])
    if points > 0:
        our_boy = Player(name, position, salary, team, points)
        if 'P' in position:
            Ps.append(our_boy)
        elif 'C' in position:
            Cs.append(our_boy)
        elif '1B' in position:
            Firsts.append(our_boy)
        elif '2B' in position:
            Seconds.append(our_boy)
        elif '3B' in position:
            Thirds.append(our_boy)
        elif 'SS' in position:
            SSs.append(our_boy)
        elif 'OF' in position:
            OFs.append(our_boy)
f.close()   


best_points = 0
while True:
    total_points = 0
    p1 = random.choice(Ps)
    p2 = random.choice(Ps)
    if p1.name == p2.name:
        p2 = random.choice(Ps)
    c = random.choice(Cs)
    first = random.choice(Firsts)
    second = random.choice(Seconds)
    third = random.choice(Thirds)
    ss = random.choice(SSs)
    of1 = random.choice(OFs)
    of2 = random.choice(OFs)
    while of1.name == of2.name:
        of2 = random.choice(OFs)
    of3 = random.choice(OFs)
    while of1.name == of3.name or of2.name == of3.name:
        of3 = random.choice(OFs)

    total_salary = p1.salary + p2.salary + c.salary + first.salary + second.salary + \
                   third.salary + ss.salary + of1.salary + of2.salary + of3.salary
    if total_salary > 50000:
        continue
    total_points = p1.points + p2.points + c.points + first.points + second.points + \
                   third.points + ss.points + of1.points + of2.points + of3.points

    if total_points > best_points:
        best_points = total_points
        print(p1)
        print(p2)
        print(c)
        print(first)
        print(second)
        print(third)
        print(ss)
        print(of1)
        print(of2)
        print(of3)
        print("total_points", round(total_points,2))
        print("total_salary", round(total_salary,2))
        print("")
    
    
