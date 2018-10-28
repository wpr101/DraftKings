import csv
from itertools import combinations
import random

f = open('data/MMA10-6.csv', 'rb')
reader = csv.reader(f)
fighters = []
first_line = True

class Player():
    def __init__(self, name, odds, salary, actual, fight_num):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)
        self.actual = float(actual)
        self.fight_num = int(fight_num)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s, actual=%s, fight_num=%s)' % \
    (self.name, self.odds, self.salary, self.actual, self.fight_num)

fighters.append(Player('Nurmagomedov', -175, 8400, 105, 1))
fighters.append(Player('Mcgregor', 150, 7800, 25.5, 1))
fighters.append(Player('Ferguson', -345, 9300, 127, 2))
fighters.append(Player('A. Pettis', 270, 6900, 32.5, 2))
fighters.append(Player('Reyes', -231, 8900, 87, 3))
fighters.append(Player('OSP', 189, 8900, 24, 3))
fighters.append(Player('Volkov', -167, 8700, 74.5, 4))
fighters.append(Player('Lewis', 139, 7500, 79.5, 4))
fighters.append(Player('Herrig', -121, 8300, 30.5, 5))
fighters.append(Player('Waterson', -102, 7900, 74, 5))
fighters.append(Player('Formiga', 130, 7600, 55, 7))
fighters.append(Player('S. Pettis', -155, 8600, 15, 7))
fighters.append(Player('Luque', -829, 9400, 120.5, 8))
fighters.append(Player('Turner', 566, 6800, 15.5, 8))
fighters.append(Player('Ladd', -171, 8200, 118, 9))
fighters.append(Player('Evinger', 143, 8000, 4.5, 9))
fighters.append(Player('Kunitskaya', -212, 8500, 97, 10))
fighters.append(Player('Lansberg', 174, 7700, 21.5, 10))
fighters.append(Player('Patrick', -268, 9100, 12.5, 11))
fighters.append(Player('Holtzman', 216, 7100, 108.5, 11))
fighters.append(Player('Lentz', -241, 9000, 136.5, 12))
fighters.append(Player('Maynard', 195, 7200, 6.5, 12))
fighters.append(Player('LaFlare', -136, 8800, 17.5, 13))
fighters.append(Player('Martin', 113, 7400, 95, 13))


my_combos = combinations(fighters, 6)

best_score = 0
num_lineups = 0
for lineup in my_combos:
    num_lineups += 1
    total_score = 0
    points = 0
    salary = 0
    for player in lineup:
        points += player.actual
        salary += player.salary
    if salary > 50000:
        continue
    double_flag = False
    for p1 in lineup:
        for p2 in lineup:
            if p1.fight_num == p2.fight_num and p1.name != p2.name:
                double_flag = True
    if double_flag:
        continue
                
    if points > best_score:
        for player in lineup:
            print(player)
        print("points", round(points,2))
        print("salary", salary)
        print("")
        best_score = points
   
