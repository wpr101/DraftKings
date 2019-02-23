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
#fighters.append(Player('Kevin Lee', -135, 9000, 1))
fighters.append(Player('Iaquinta', 452, 7200, 1))
#fighters.append(Player('Hooker', 184, 8200, 2))
#fighters.append(Player('Barboza', 276, 8000, 2))
#fighters.append(Player('Font', 155, 8400, 3))
#fighters.append(Player('Pettis', 685, 7800, 3))
#fighters.append(Player('Oliveira', -179, 8900, 4))
#fighters.append(Player('Miller', 426, 7300, 4))
fighters.append(Player('Grant', -155, 9400, 5))
#fighters.append(Player('Ottow', 465, 6800, 5))
#fighters.append(Player('Klose', 426, 9300, 7))
fighters.append(Player('Green', 665, 6900, 7))
#fighters.append(Player('Gordon', 329, 8600, 8))
#fighters.append(Player('Silva', 235, 7600, 8))
#fighters.append(Player('Hermansson', 155, 8800, 9))
#fighters.append(Player('Meerschaert', 230, 7400, 9))
#fighters.append(Player('Ige', 175, 8500, 10))
#fighters.append(Player('Griffin', 271, 7700, 10))
fighters.append(Player('Milstead', 179, 8700, 11))
#fighters.append(Player('Rodriguez', 190, 7500, 11))
fighters.append(Player('Cummings', 167, 9100, 12))
#fighters.append(Player('Smith', 850, 7100, 12))
#fighters.append(Player('Adams', -290, 9500, 13))
fighters.append(Player('Rocha', 490, 6700, 13))

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
        if 'Iaquinta' in p.name or 'Lee' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Rodriguez' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Gordon' in p.name:
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
    #if total_score > .5:
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
