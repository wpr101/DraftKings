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
fighters.append(Player('Usman', 300, 9000, 1))
fighters.append(Player('Dos Anjos', 475, 7200, 1))
fighters.append(Player('Espino', 120, 8500, 2))
fighters.append(Player('Frazier', 180, 7700, 2))
fighters.append(Player('Kianzad', 670, 8600, 3))
fighters.append(Player('Chiasson', 275, 7600, 3))
fighters.append(Player('Munhoz', 240, 8800, 4))
fighters.append(Player('Caraway', 1000, 7400, 4))
fighters.append(Player('Shahbazyan', 135, 8300, 5))
fighters.append(Player('Stewart', 140, 7900, 5))
fighters.append(Player('Shevchenko', 370, 9300, 6))
fighters.append(Player('Kim', 700, 6900, 6))
fighters.append(Player('Aguilar', 480, 8400, 7))
fighters.append(Player('Glenn', 390, 7800, 7))
fighters.append(Player('Perez', 250, 8200, 8))
fighters.append(Player('Benavidez', 630, 8000, 8))
fighters.append(Player('Greene', -120, 8700, 9))
fighters.append(Player('Batista', 315, 7500, 9))
'''fighters.append(Player('Letson', 270, 8900, 10))
fighters.append(Player('Stoliarenko', 365, 7300, 10))
fighters.append(Player('Roberts', -105, 9200, 11))
fighters.append(Player('Horcher', 500, 7000, 11))
fighters.append(Player('Means', 180, 9400, 12))
fighters.append(Player('Rainey', 675, 6800, 12))
fighters.append(Player('Barcelos', -135, 9500, 13))
fighters.append(Player('Gutierrez', 875, 6700, 13))'''


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
        if 'Usman' in p.name or 'Dos Anjos' in p.name:
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
    if total_score > .2:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
