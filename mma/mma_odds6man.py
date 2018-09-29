import csv
from itertools import combinations
import random

f = open('data/MMA10-6.csv', 'rb')
reader = csv.reader(f)
fighters = []
first_line = True

class Player():
    def __init__(self, name, odds, salary, fppf):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)
        self.fppf = float(fppf)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s, fppf=%s)' % \
    (self.name, self.odds, self.salary, self.fppf)

fighters.append(Player('Mcgregor', 138, 7800, 104.1))
fighters.append(Player('Ferguson', -344, 9300, 90.6))
fighters.append(Player('Pettis', 269, 6900, 64.4))
fighters.append(Player('Reyes', -219, 8900, 108.5))
fighters.append(Player('Volkov', -173, 8700, 92.0))
fighters.append(Player('Lewis', 144, 7500, 71.1))
fighters.append(Player('Herrig', -131, 8300, 72.2))
fighters.append(Player('Waterson', 107, 7900, 72.2))
fighters.append(Player('OMalley', -316, 9200, 92.5))
fighters.append(Player('Quinonez', 248, 7000, 81.8))
fighters.append(Player('Pettis', 269, 8600, 60.7))
fighters.append(Player('Formiga', 140, 7600, 56.0))
fighters.append(Player('Luque', -769, 9400, 85.4))
fighters.append(Player('Turner', 522, 6800, 70))
fighters.append(Player('Ladd', -166, 8200, 94))
fighters.append(Player('Evinger', 139, 8000, 21))
fighters.append(Player('Kunitskaya', -187, 8500, 10.5))
fighters.append(Player('Lansberg', 155, 7700, 39.4))
fighters.append(Player('Patrick', -252, 9100, 77.1))
fighters.append(Player('Holtzman', -202, 7100, 82.5))
fighters.append(Player('Lentz', -221, 9000, 69.1))
fighters.append(Player('Maynard', 177, 7200, 56.7))
fighters.append(Player('LaFlare', -156, 8800, 70.1))
fighters.append(Player('Martin', 130, 7400, 52.2))

my_combos = combinations(fighters, 6)
best_score = 99999
for lineup in my_combos:
    total_score = 0
    points = 0
    salary = 0
    for player in lineup:
        points += player.fppf
        salary += player.salary
        if player.odds < 0:
            total_score += float(100)/(player.odds *float(-1))
        else:
            total_score += player.odds/float(100)
    if salary > 50000:
        continue
    if total_score < best_score:
        for player in lineup:
            print(player)
        print("points", round(points,2))
        print("salary", salary)
        print("total_score", round(total_score,2))
        print("")
        best_score = total_score

    
