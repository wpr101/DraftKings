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
fighters.append(Player('Jung', 125, 8500, 1))
fighters.append(Player('Rodriguez', 200, 7700, 1))
fighters.append(Player('Perry', -115, 8900, 2))
fighters.append(Player('Cerrone', 325, 7300, 2))
fighters.append(Player('Randamie', 330, 8800, 3))
fighters.append(Player('Pennington', 645, 7400, 3))
#fighters.append(Player('Benavidez', 445, 8300, 4))
#fighters.append(Player('Borg', 475, 7900, 4))
fighters.append(Player('Barber', 150, 9400, 5))
fighters.append(Player('Cifers', 585, 6800, 5))
fighters.append(Player('Pena', 125, 9300, 6))
fighters.append(Player('Trizano', 625, 6900, 6))
#fighters.append(Player('Yoder', 210, 8600, 7))
fighters.append(Player('Cooper', 1000, 7600, 7))
#fighters.append(Player('Skelly', 285, 8400, 8))
fighters.append(Player('Moffett', 420, 7800, 8))
fighters.append(Player('Dariush', 335, 8700, 9))
fighters.append(Player('Moises', 245, 7500, 9))
#fighters.append(Player('Smith', -135, 9100, 10))
fighters.append(Player('Erosa', 445, 7100, 10))
fighters.append(Player('Ramos', -360, 9500, 11))
#fighters.append(Player('Gunther', 1800, 6700, 11))
fighters.append(Player('Shelton', 560, 8200, 12))
fighters.append(Player('Morales', 290, 8000, 12))
fighters.append(Player('Rosa', 155, 9000, 13))
#fighters.append(Player('Sanchez', 895, 7200, 13))


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
    found_player = False
    for p in lineup:
        if 'Jung' in p.name or 'Rodriguez' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    '''for p in lineup:
        if 'Barber' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False'''
    for p in lineup:
        if 'Ramos' in p.name:
            found_player = True
    if not found_player:
        continue
    if total_score > .25:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
