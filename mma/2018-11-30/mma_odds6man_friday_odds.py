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
fighters.append(Player('Usman', -276, 9000, 1))
fighters.append(Player('Dos Anjos', 221, 7200, 1))
fighters.append(Player('Espino', -156, 8500, 2))
fighters.append(Player('Frazier', 129, 7700, 2))
fighters.append(Player('Kianzad', -117, 8600, 3))
fighters.append(Player('Chiasson', -106, 7600, 3))
fighters.append(Player('Munhoz', -256, 8800, 4))
fighters.append(Player('Caraway', 206, 7400, 4))
fighters.append(Player('Shahbazyan', -111, 8300, 5))
fighters.append(Player('Stewart', -113, 7900, 5))
fighters.append(Player('Shevchenko', -283, 9300, 6))
fighters.append(Player('Kim', 227, 6900, 6))
fighters.append(Player('Aguilar', -103, 8400, 7))
fighters.append(Player('Glenn', -120, 7800, 7))
fighters.append(Player('Perez', -135, 8200, 8))
fighters.append(Player('Benavidez', 111, 8000, 8))
fighters.append(Player('Greene', -171, 8700, 9))
fighters.append(Player('Batista', 144, 7500, 9))
fighters.append(Player('Letson', -209, 8900, 10))
fighters.append(Player('Stoliarenko', 171, 7300, 10))
fighters.append(Player('Roberts', -313, 9200, 11))
fighters.append(Player('Horcher', 246, 7000, 11))
fighters.append(Player('Means', -364, 9400, 12))
fighters.append(Player('Rainey', 282, 6800, 12))
fighters.append(Player('Barcelos', -515, 9500, 13))
fighters.append(Player('Gutierrez', 382, 6700, 13))


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
        if 'Usman' in p.name or 'Dos Anjos' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
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
    #if total_score >:
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
