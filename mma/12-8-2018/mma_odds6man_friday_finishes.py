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

def convert_to_percent(odds):
    percent = 1
    if odds < 0:
        percent *= float(odds) / float((odds - 100))
    else:
        percent *= float(100) / float((odds + 100))
    return (percent)

fighters = []
fighters.append(Player('Holloway', 410, 8300, 1))
fighters.append(Player('Ortega', 110, 7900, 1))
fighters.append(Player('Shevchenko', 195, 9400, 2))
fighters.append(Player('Jedrzejczyk', 945, 6800, 2))
fighters.append(Player('Gunnar Nelson', -110, 8400, 3))
fighters.append(Player('Oliveira', 225, 7800, 3))
fighters.append(Player('Dawodu', 250, 8600, 4))
fighters.append(Player('Bochniak', 620, 7600, 4))
fighters.append(Player('Santos', -130, 8800, 5))
fighters.append(Player('Manuwa', 210, 7400, 5))
fighters.append(Player('Gadelha', 315, 9300, 6))
fighters.append(Player('Ansaroff', 1050, 6900, 6))
fighters.append(Player('Mercier', 445, 8500, 7))
fighters.append(Player('Burns', 225, 7700, 7))
fighters.append(Player('Chookagian', 520, 8700, 8))
fighters.append(Player('Eye', 770, 7500, 8))
fighters.append(Player('Theodorou', 465, 8200, 9))
fighters.append(Player('Anders', 416, 8000, 9))
fighters.append(Player('Katona', 215, 8900, 10))
fighters.append(Player('Lopez', 510, 7300, 10))
fighters.append(Player('Laprise', -110, 9100, 11))
fighters.append(Player('Lima', 700, 7100, 11))
fighters.append(Player('Ferreira', -160, 9200, 12))
fighters.append(Player('Kyle Nelson', 685, 7000, 12))
fighters.append(Player('Rakic', -130, 9500, 12))
fighters.append(Player('Clark', 1150, 6700, 12))

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
        if 'Holloway' in p.name or 'Ortega' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Shevchenkoo' in p.name or 'Jedrzejczyk' in p.name:
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
    if total_score > .4:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)    
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
