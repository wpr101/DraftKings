import csv
from itertools import combinations
import random

f = open('data/MMA10-6.csv', 'rb')
reader = csv.reader(f)
fighters = []
first_line = True

class Player():
    def __init__(self, name, odds, salary, fppf, fight_num):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)
        self.fppf = float(fppf)
        self.fight_num = int(fight_num)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s, fppf=%s, fight_num=%s)' % \
    (self.name, self.odds, self.salary, self.fppf, self.fight_num)

fighters.append(Player('Nurmagomedov', -175, 8400, 112.4, 1))
fighters.append(Player('Mcgregor', 150, 7800, 104.1, 1))
fighters.append(Player('Ferguson', -345, 9300, 90.6, 2))
fighters.append(Player('A. Pettis', 270, 6900, 64.4, 2))
fighters.append(Player('Reyes', -231, 8900, 108.5, 3))
fighters.append(Player('OSP', 189, 8900, 108.5, 3))
fighters.append(Player('Volkov', -167, 8700, 92.0, 4))
fighters.append(Player('Lewis', 139, 7500, 71.1, 4))
fighters.append(Player('Herrig', -121, 8300, 72.2, 5))
fighters.append(Player('Waterson', -102, 7900, 72.2, 5))
fighters.append(Player('Formiga', 130, 7600, 56.0, 7))
fighters.append(Player('S. Pettis', -155, 8600, 56.0, 7))
fighters.append(Player('Luque', -829, 9400, 85.4, 8))
fighters.append(Player('Turner', 566, 6800, 70, 8))
fighters.append(Player('Ladd', -171, 8200, 94, 9))
fighters.append(Player('Evinger', 143, 8000, 21, 9))
fighters.append(Player('Kunitskaya', -212, 8500, 10.5, 10))
fighters.append(Player('Lansberg', 174, 7700, 39.4, 10))
fighters.append(Player('Patrick', -268, 9100, 77.1, 11))
fighters.append(Player('Holtzman', 216, 7100, 82.5, 11))
fighters.append(Player('Lentz', -241, 9000, 69.1, 12))
fighters.append(Player('Maynard', 195, 7200, 56.7, 12))
fighters.append(Player('LaFlare', -136, 8800, 70.1, 13))
fighters.append(Player('Martin', 113, 7400, 52.2, 13))


my_combos = combinations(fighters, 6)

best_score = 99999
real_lineups = 0
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
    if salary > 50000 or salary < 49500:
        continue
    
    double_flag = False
    for p1 in lineup:
        for p2 in lineup:
            if p1.fight_num == p2.fight_num and p1.name != p2.name:
                double_flag = True
    if double_flag:
        continue
    if total_score < 4.1:
    #if total_score < best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("points", round(points,2))
        print("salary", salary)
        print("total_score", round(total_score,2))
        print("")
        #best_score = total_score

print("real_lineups", real_lineups)    
