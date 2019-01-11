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
fighters.append(Player('Santos', 145, 8300, 1))
#fighters.append(Player('Tuivasa', 170, 7900, 1))
#fighters.append(Player('Pedro', -200, 9400, 2))
fighters.append(Player('Rua', 548, 6800, 2))
fighters.append(Player('Willis', 236, 8200, 3))
#fighters.append(Player('Hunt', 145, 8000, 3))
fighters.append(Player('Matthews', 287, 8400, 4))
fighters.append(Player('Martin', 500, 7800, 4))
#fighters.append(Player('Yusuff', -225, 9300, 5))
fighters.append(Player('Mokhtarian', 725, 6900, 5))
#fighters.append(Player('Crute', -126, 8700, 6))
fighters.append(Player('Craig', 350, 7500, 6))
fighters.append(Player('Kunchenko', 167, 9200, 7))
fighters.append(Player('Okami', 1100, 7000, 7))
fighters.append(Player('Nguyen', 275, 8500, 8))
fighters.append(Player('Reis', 410, 7700, 8))
fighters.append(Player('Nakamura', 287, 8800, 9))
fighters.append(Player('Touahri', 700, 7400, 9))
fighters.append(Player('KaraFrance', -105, 9100, 10))
fighters.append(Player('Garica', 599, 7100, 10))
fighters.append(Player('Giagos', 324, 9000, 11))
fighters.append(Player('Hirota', 800, 7200, 11))
fighters.append(Player('Ismagulov', -145, 9500, 12))
fighters.append(Player('Gorgees', 821, 6700, 12))


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
    '''found_player = False
    for p in lineup:
        if 'Usman' in p.name or 'Santos' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Barcelos' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Ramos' in p.name:
            found_player = True
    if not found_player:
        continue'''
    #if total_score > .25:
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
