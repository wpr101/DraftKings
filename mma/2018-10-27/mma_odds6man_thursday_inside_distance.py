import csv
from itertools import combinations
import random

fighters = []

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

fighters.append(Player('Oezdemir', -141, 8400, 112.4, 1))
fighters.append(Player('Smith', 179, 7800, 104.1, 1))
fighters.append(Player('Johnson', 160, 9500, 90.6, 2))
fighters.append(Player('Lobov', 900, 6700, 64.4, 2))
fighters.append(Player('Cirkunov', -172, 9300, 108.5, 3))
fighters.append(Player('Cummins', 650, 6900, 108.5, 3))
fighters.append(Player('Soukhamthath', 258, 8600, 92.0, 4))
fighters.append(Player('Martinez', 475, 7600, 71.1, 4))
fighters.append(Player('Villante', 111, 9000, 72.2, 5))
fighters.append(Player('Herman', 300, 7300, 72.2, 5))
fighters.append(Player('Garcia', 260, 8500, 72.2, 6))
fighters.append(Player('McGee', 750, 7700, 72.2, 6))
fighters.append(Player('Taleb', 467, 8200, 56.0, 7))
fighters.append(Player('Strickland', 550, 8000, 56.0, 7))
fighters.append(Player('Haqparast', -225, 9700, 85.4, 8))
fighters.append(Player('Gouti', 965, 6500, 70, 8))
fighters.append(Player('Kattar', 206, 9100, 94, 9))
fighters.append(Player('Fishgold', 460, 7100, 21, 9))
fighters.append(Player('Moras', 273, 8700, 10.5, 10))
fighters.append(Player('Bernardo', 585, 7500, 39.4, 10))
fighters.append(Player('Edwards', -240, 9400, 77.1, 11))
fighters.append(Player('Madge', 715, 6800, 82.5, 11))
fighters.append(Player('Bhullar', 370, 8800, 69.1, 12))
fighters.append(Player('Golm', 258, 7400, 56.7, 12))
fighters.append(Player('Ray', 440, 8300, 70.1, 13))
fighters.append(Player('Ayari', 627, 7900, 52.2, 13))


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
    if salary > 50000 or salary < 48000:
        continue
    
    double_flag = False
    for p1 in lineup:
        for p2 in lineup:
            if p1.fight_num == p2.fight_num and p1.name != p2.name:
                double_flag = True
    if double_flag:
        continue
    if total_score < 11:
    #if total_score < best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("total_score", round(total_score,2))
        print("")
        #best_score = total_score

print("real_lineups", real_lineups)    
