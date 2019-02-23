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
fighters.append(Player('Blaydes', -122, 8700, 1))
fighters.append(Player('Ngannou', 200, 7500, 1))
fighters.append(Player('Pavlovich', 111, 8200, 2))
fighters.append(Player('Overeem', 240, 8000, 2))
fighters.append(Player('Yadong', -167, 9100, 3))
fighters.append(Player('Morales', 820, 7100, 3))
fighters.append(Player('Jingliang', 260, 8500, 4))
fighters.append(Player('Zawada', 346, 7700, 4))
fighters.append(Player('Kenan', 200, 8300, 5))
fighters.append(Player('Morono', 345, 7900, 5))
fighters.append(Player('Mueller', 290, 9200, 6))
fighters.append(Player('Yanan', 628, 7000, 6))
fighters.append(Player('Coulter', 141, 8400, 7))
fighters.append(Player('Yaozong', 134, 7800, 7))
fighters.append(Player('Weili', 261, 9300, 8))
fighters.append(Player('Aguilar', 1450, 6900, 8))
fighters.append(Player('Pingyuan', 325, 8900, 9))
fighters.append(Player('Day', 425, 7300, 9))
fighters.append(Player('Xiaonan', 330, 9400, 10))
fighters.append(Player('Kondo', 1400, 6800, 10))
fighters.append(Player('Holland', -198, 9500, 11))
fighters.append(Player('Phillips', 525, 6700, 11))
fighters.append(Player('Smolka', -130, 8800, 12))
fighters.append(Player('Su', 406, 7400, 12))


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
        if 'Blaydes' in p.name or 'Ngannou' in p.name:
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
    if total_score > .5:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
