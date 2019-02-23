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
fighters.append(Player('Santos', 139, 8500, 1))
fighters.append(Player('Blachowicz', 127, 7700, 1))
fighters.append(Player('Lima', 226, 8400, 2)) 
fighters.append(Player('Struve', 123, 7800, 2))
fighters.append(Player('Oleksiejczuk', 228, 8900, 3))
fighters.append(Player('Villante', 579, 7300, 3))
fighters.append(Player('Carmouche', 380, 8300, 4))
fighters.append(Player('Pudilova', 725, 7900, 4))
fighters.append(Player('Yan', 363, 9300, 5))
fighters.append(Player('Dodson', 790, 6900, 5))
fighters.append(Player('Ankalaev', -109, 9100, 6))
fighters.append(Player('Abreu', 270, 7100, 6))
fighters.append(Player('PedersoliJr', 365, 8200, 7))
fighters.append(Player('Grant', 329, 8000, 7))
fighters.append(Player('Fishgold', -130, 9000, 8))
fighters.append(Player('Teymur', 480, 7200, 8))
fighters.append(Player('Robertson', 133, 8600, 9))
fighters.append(Player('Macedo', 360, 7600, 9))
fighters.append(Player('Reyes', 175, 8800, 10))
fighters.append(Player('Hadzovic', 209, 7400, 10))
fighters.append(Player('Prazeres', -150, 9400, 11))
fighters.append(Player('Naurdiev', 570, 6800, 11))
fighters.append(Player('Khabilov', 560, 8700, 12))
fighters.append(Player('Ferreira', 260, 7500, 12))
fighters.append(Player('Ismagulov', 160, 9200, 13))
fighters.append(Player('Alvarez', 350, 7000, 13))

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
        if 'Naurdiev' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Ismagulov' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Prazeres' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Holtzman' in p.name:
            found_player = True
    if not found_player:
        continue'''
    five_wins_prob = 0
    for loser in lineup:
        winrate = 1
        for player in lineup:
            if player.name == loser.name:
                winrate *= 1-convert_to_percent(player.odds)
            else:
                winrate *= convert_to_percent(player.odds)
        five_wins_prob += winrate
    five_wins_prob *= 100
    #if salary > 49000:
    #if total_score > .125:
    if total_score > best_score:
    #if five_wins_prob > best_score:
    #if five_wins_prob > 17:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("percentage to win 5 fights:", round(five_wins_prob,3))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
