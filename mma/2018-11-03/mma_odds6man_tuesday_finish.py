import csv
from itertools import combinations
import random



class Player():
    def __init__(self, name, odds, salary, fight_num):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)
        self.fight_num = int(fight_num)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s, fight_num=%s)' % \
    (self.name, self.odds, self.salary, self.fight_num)

fighters = []
fighters.append(Player('Cormier', -457, 9600, 1))
fighters.append(Player('Lewis', 630, 6600, 1))
fighters.append(Player('Weidman', 178, 8500, 2))
fighters.append(Player('Souza', 251, 7700, 2))
fighters.append(Player('Branch', 142, 9300, 3))
fighters.append(Player('Cannonier', 537, 6900, 3))
fighters.append(Player('Roberson', -122, 8700, 4))
fighters.append(Player('Marshman', 502, 7500, 4))
fighters.append(Player('Adesanya', 100, 9100, 5))
fighters.append(Player('Brunson', 470, 7100, 5))
fighters.append(Player('Knight', 100, 8800, 6))
fighters.append(Player('Rinaldi', 556, 7400, 6))
fighters.append(Player('Eubanks', 328, 9400, 7))
fighters.append(Player('Modafferi', 1055, 6800, 7))
fighters.append(Player('Arce', 240, 9200, 8))
fighters.append(Player('Moraes', 815, 7000, 8))
fighters.append(Player('Good', -235, 9500, 9))
fighters.append(Player('Saunders', 800, 6700, 9))
fighters.append(Player('Vannata', -116, 8900, 10))
fighters.append(Player('Frevola', 551, 7300, 10))
fighters.append(Player('Burgos', 115, 9000, 11))
fighters.append(Player('Holobaugh', 421, 7200, 11))
fighters.append(Player('Jackson', 250, 8300, 12))
fighters.append(Player('Kelleher', 420, 7900, 12))
fighters.append(Player('Wieczorek', -116, 8600, 13))
fighters.append(Player('Lima', 250, 7600, 13))


my_combos = combinations(fighters, 6)

best_score = 99999
real_lineups = 0
for lineup in my_combos:
    total_score = 0
    points = 0
    salary = 0
    for player in lineup:
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
    if total_score < 11.3:
    #if total_score < best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("total_score", round(total_score,2))
        print("")
        #best_score = total_score

print("real_lineups", real_lineups)    
