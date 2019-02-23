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
fighters.append(Player('Blaydes', -234, 8700, 1))
fighters.append(Player('Ngannou', 190, 7500, 1))
fighters.append(Player('Pavlovich', -132, 8200, 2))
fighters.append(Player('Overeem', 107, 8000, 2))
fighters.append(Player('Yadong', -540, 9100, 3))
fighters.append(Player('Morales', 394, 7100, 3))
fighters.append(Player('Jingliang', -186, 8500, 4))
fighters.append(Player('Zawada', 155, 7700, 4))
fighters.append(Player('Kenan', -122, 8300, 5))
fighters.append(Player('Morono', -102, 7900, 5))
fighters.append(Player('Mueller', -416, 9200, 6))
fighters.append(Player('Yanan', 317, 7000, 6))
fighters.append(Player('Coulter', -115, 8400, 7))
fighters.append(Player('Yaozong', -108, 7800, 7))
fighters.append(Player('Weili', -532, 9300, 8))
fighters.append(Player('Aguilar', 391, 6900, 8))
fighters.append(Player('Pingyuan', -240, 8900, 9))
fighters.append(Player('Day', 193, 7300, 9))
fighters.append(Player('Xiaonan', -526, 9400, 10))
fighters.append(Player('Kondo', 386, 6800, 10))
fighters.append(Player('Holland', -532, 9500, 11))
fighters.append(Player('Phillips', 387, 6700, 11))
fighters.append(Player('Smolka', -191, 8800, 12))
fighters.append(Player('Su', 159, 7400, 12))


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
        if 'Blaydes' in p.name or 'Ngannou' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
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
    if total_score > 4.5:
    #if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
