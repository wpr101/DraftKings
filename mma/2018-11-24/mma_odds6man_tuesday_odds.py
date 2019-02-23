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
fighters.append(Player('Blaydes', -221, 8700, 1))
fighters.append(Player('Ngannou', 178, 7500, 1))
fighters.append(Player('Pavlovich', -131, 8200, 2))
fighters.append(Player('Overeem', 106, 8000, 2))
fighters.append(Player('Yadong', -407, 9100, 3))
fighters.append(Player('Morales', 310, 7100, 3))
fighters.append(Player('Jingliang', -161, 8500, 4))
fighters.append(Player('Zawada', 133, 7700, 4))
fighters.append(Player('Kenan', -116, 8300, 5))
fighters.append(Player('Morono', -108, 7900, 5))
fighters.append(Player('Mueller', -445, 9200, 6))
fighters.append(Player('Yanan', 336, 7000, 6))
fighters.append(Player('Coulter', -151, 8400, 7))
fighters.append(Player('Yaozong', 125, 7800, 7))
fighters.append(Player('Weili', -449, 9300, 8))
fighters.append(Player('Aguilar', 338, 6900, 8))
fighters.append(Player('Pingyuan', -249, 8900, 9))
fighters.append(Player('Day', 199, 7300, 9))
fighters.append(Player('Xiaonan', -447, 9400, 10))
fighters.append(Player('Kondo', 336, 6800, 10))
fighters.append(Player('Holland', -444, 9500, 11))
fighters.append(Player('Phillips', 335, 6700, 11))
fighters.append(Player('Smolka', -223, 8800, 12))
fighters.append(Player('Su', 178, 7400, 12))


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
    #if total_score > 3.5:
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
