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
fighters.append(Player('Jung', 165, 8500, 1))
fighters.append(Player('Rodriguez', 160, 7700, 1))
fighters.append(Player('Perry', -110, 8900, 2))
fighters.append(Player('Cerrone', 270, 7300, 2))
fighters.append(Player('Randamie', 336, 8800, 3))
fighters.append(Player('Pennington', 540, 7400, 3))
#fighters.append(Player('Benavidez', 445, 8300, 4))
#fighters.append(Player('Borg', 475, 7900, 4))
fighters.append(Player('Barber', 140, 9400, 5))
fighters.append(Player('Cifers', 550, 6800, 5))
fighters.append(Player('Pena', 110, 9300, 6))
fighters.append(Player('Trizano', 605, 6900, 6))
fighters.append(Player('Yoder', 255, 8600, 7))
fighters.append(Player('Cooper', 655, 7600, 7))
fighters.append(Player('Skelly', 325, 8400, 8))
fighters.append(Player('Moffett', 355, 7800, 8))
fighters.append(Player('Dariush', 260, 8700, 9))
fighters.append(Player('Moises', 230, 7500, 9))
fighters.append(Player('Smith', -135, 9100, 10))
fighters.append(Player('Erosa', 360, 7100, 10))
fighters.append(Player('Ramos', -454, 9500, 11))
fighters.append(Player('Gunther', 1650, 6700, 11))
fighters.append(Player('Shelton', 575, 8200, 12))
fighters.append(Player('Morales', 260, 8000, 12))
fighters.append(Player('Rosa', 140, 9000, 13))
fighters.append(Player('Sanchez', 475, 7200, 13))


my_combos = combinations(fighters, 6)

best_score = 999999
real_lineups = 0
for lineup in my_combos:
    total_score = 1
    points = 0
    salary = 0
    for player in lineup:
        salary += player.salary
        if player.odds < 0:
            total_score += player.salary / (float(player.odds) / float((player.odds - 100)))
        else:
            total_score += player.salary / (float(100) / float((player.odds + 100)))
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
    '''for p in lineup:
        if 'Jung' in p.name or 'Rodriguez' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Barber' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Ramos' in p.name:
            found_player = True
    if not found_player:
        continue'''
    if total_score < 130000:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("score:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
