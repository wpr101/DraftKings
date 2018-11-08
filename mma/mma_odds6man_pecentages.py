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
fighters.append(Player('Cormier', -410, 9600, 1))
fighters.append(Player('Lewis', 534, 6600, 1))
fighters.append(Player('Weidman', 181, 8500, 2))
fighters.append(Player('Souza', 305, 7700, 2))
fighters.append(Player('Branch', 170, 9300, 3))
fighters.append(Player('Cannonier', 550, 6900, 3))
fighters.append(Player('Roberson', -122, 8700, 4))
fighters.append(Player('Marshman', 454, 7500, 4))
fighters.append(Player('Adesanya', 115, 9100, 5))
fighters.append(Player('Brunson', 484, 7100, 5))
fighters.append(Player('Knight', 104, 8800, 6))
fighters.append(Player('Rinaldi', 650, 7400, 6))
fighters.append(Player('Eubanks', 320, 9400, 7))
fighters.append(Player('Modafferi', 950, 6800, 7))
fighters.append(Player('Arce', 280, 9200, 8))
fighters.append(Player('Moraes', 605, 7000, 8))
fighters.append(Player('Good', -270, 9500, 9))
fighters.append(Player('Saunders', 720, 6700, 9))
fighters.append(Player('Vannata', -105, 8900, 10))
fighters.append(Player('Frevola', 540, 7300, 10))
fighters.append(Player('Burgos', 120, 9000, 11))
fighters.append(Player('Holobaugh', 400, 7200, 11))
#fighters.append(Player('Jackson', 316, 8300, 12))
#fighters.append(Player('Kelleher', 425, 7900, 12))
fighters.append(Player('Wieczorek', -120, 8600, 13))
fighters.append(Player('Lima', 230, 7600, 13))


my_combos = combinations(fighters, 6)

best_score = 0
real_lineups = 0
for lineup in my_combos:
    total_score = 1
    points = 0
    salary = 0
    for player in lineup:
        salary += player.salary
        if player.odds < 0:
            total_score *= float(player.odds) / float((player.odds - 100))
        else:
            total_score *= float(100) / float((player.odds + 100))
    # Conver to %
    total_score *= 100
    if salary > 50000:
        continue
    
    double_flag = False
    for p1 in lineup:
        for p2 in lineup:
            if p1.fight_num == p2.fight_num and p1.name != p2.name:
                double_flag = True
    if double_flag:
        continue
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
