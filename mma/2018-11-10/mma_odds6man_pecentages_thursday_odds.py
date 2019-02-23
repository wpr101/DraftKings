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
fighters.append(Player('Jung', -138, 8500, 1))
fighters.append(Player('Rodriguez', 114, 7700, 1))
fighters.append(Player('Perry', -211, 8900, 2))
fighters.append(Player('Cerrone', 171, 7300, 2))
#fighters.append(Player('Randamie', -180, 8800, 3))
fighters.append(Player('Pennington', 150, 7400, 3))
#fighters.append(Player('Benavidez', -112, 8300, 4))
#fighters.append(Player('Borg', -113, 7900, 4))
fighters.append(Player('Barber', -431, 9400, 5))
fighters.append(Player('Cifers', 324, 6800, 5))
fighters.append(Player('Pena', -186, 9300, 6))
fighters.append(Player('Trizano', 154, 6900, 6))
#fighters.append(Player('Yoder', -157, 8600, 7))
fighters.append(Player('Cooper', 130, 7600, 7))
#fighters.append(Player('Skelly', -112, 8400, 8))
fighters.append(Player('Moffett', -111, 7800, 8))
fighters.append(Player('Dariush', -151, 8700, 9))
fighters.append(Player('Moises', 125, 7500, 9))
#fighters.append(Player('Smith', -239, 9100, 10))
fighters.append(Player('Erosa', 190, 7100, 10))
fighters.append(Player('Ramos', -972, 9500, 11))
#fighters.append(Player('Gunther', 613, 6700, 11))
fighters.append(Player('Shelton', -120, 8200, 12))
fighters.append(Player('Morales', -104, 8000, 12))
fighters.append(Player('Rosa', -253, 9000, 13))
#fighters.append(Player('Sanchez', 203, 7200, 13))


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
        if 'Perry' in p.name:
            found_player = True
    if not found_player:
        continue'''
    found_player = False
    for p in lineup:
        if 'Ramos' in p.name:
            found_player = True
    if not found_player:
        continue
    if total_score > 4.1:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    