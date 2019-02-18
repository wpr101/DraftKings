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
fighters.append(Player('Dillashaw', -212, 8900, 1))
fighters.append(Player('Cejudo', 172, 7300, 1))
fighters.append(Player('Hardy', -525, 9500, 2)) 
fighters.append(Player('Crowder', 384, 6700, 2))
fighters.append(Player('Gillespie', -535, 9400, 3))
fighters.append(Player('Medeiros', 388, 6800, 3))
fighters.append(Player('Benavidez', -241, 9000, 4))
fighters.append(Player('Ortiz', 193, 7200, 4))
fighters.append(Player('VanZant', -160, 8400, 5))
fighters.append(Player('Ostovich', 132, 7800, 5))
fighters.append(Player('Teixeira', -124, 8300, 6))
fighters.append(Player('Roberson', 100, 7900, 6))
fighters.append(Player('Hernandez', -193, 8600, 7))
fighters.append(Player('Cerrone', 159, 7600, 7))
fighters.append(Player('Lipski', -216, 8800, 8))
fighters.append(Player('Calderwood', 173, 7400, 8))
fighters.append(Player('Menifield', -263, 9100, 9))
fighters.append(Player('Moreira', 210, 7100, 9))
fighters.append(Player('Sandhagen', -479, 9300, 10))
fighters.append(Player('Bautista', 360, 6900, 10))
fighters.append(Player('Edwards', -134, 8200, 11))
fighters.append(Player('Bermudez', 108, 8000, 11))
fighters.append(Player('Neal', -178, 8500, 12))
fighters.append(Player('Muhammad', 147, 7700, 12))
fighters.append(Player('Stewart', -174, 8700, 13))
fighters.append(Player('Rencountre', 149, 7500, 13))

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
        if 'Ortiz' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    '''for p in lineup:
        if 'Teixeira' in p.name:
            found_player = True
    if not found_player:
        continue'''
    found_player = False
    for p in lineup:
        if 'Dillashaw' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Calderwood' in p.name:
            found_player = True
    if not found_player:
        continue
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
    #if total_score > 1.9:
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
