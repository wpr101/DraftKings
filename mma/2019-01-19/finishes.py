import csv
from itertools import combinations
import random



class Player():
    def __init__(self, name, odds, salary, fight_num, actual_score):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)
        self.fight_num = int(fight_num)
        self.actual_score = actual_score

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
#fighters.append(Player('Dillashaw', 155, 8900, 1, 0))
fighters.append(Player('Cejudo', 550, 7300, 1, 109))
#fighters.append(Player('Hardy', -350, 9500, 2)) 
fighters.append(Player('Crowder', 465, 6700, 2, 87))
fighters.append(Player('Gillespie', -160, 9400, 3, 151.5))
#fighters.append(Player('Medeiros', 620, 6800, 3))
fighters.append(Player('Benavidez', 370, 9000, 4, 101.5))
#fighters.append(Player('Ortiz', 555, 7200, 4))
fighters.append(Player('VanZant', 285, 8400, 5, 81.5))
#fighters.append(Player('Ostovich', 520, 7800, 5))
fighters.append(Player('Teixeira', 150, 8300, 6, 107))
#fighters.append(Player('Roberson', 170, 7900, 6))
#fighters.append(Player('Hernandez', 140, 8600, 7))
fighters.append(Player('Cerrone', 260, 7600, 7, 125))
#fighters.append(Player('Lipski', 183, 8800, 8))
fighters.append(Player('Calderwood', 610, 7400, 8, 94.5))
fighters.append(Player('Menifield', -162, 9100, 9, 116.5))
#fighters.append(Player('Moreira', 306, 7100, 9))
fighters.append(Player('Sandhagen', -145, 9300, 10, 119.5))
#fighters.append(Player('Bautista', 686, 6900, 10))
#fighters.append(Player('Edwards', 160, 8200, 11))
fighters.append(Player('Bermudez', 318, 8000, 11, 110.5))
fighters.append(Player('Neal', 165, 8500, 12, 85.5))
#fighters.append(Player('Muhammad', 330, 7700, 12))
#fighters.append(Player('Stewart', 233, 8700, 13))
fighters.append(Player('Rencountre', 431, 7500, 13, 106))

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
    '''for p in lineup:
        if 'Lipski' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Ortiz' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Calderwood' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Gillespie' in p.name:
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
    if total_score > .1:
    #if total_score > best_score:
    #if five_wins_prob > best_score:
    #if five_wins_prob > .46:
        total_actual_points = 0
        real_lineups += 1
        for player in lineup:
            #print(player)
            total_actual_points += player.actual_score
        if total_actual_points >= 722:
            for player in lineup:
                print(player)
            print("salary", salary)
            print("percentage to win all fights:", round(total_score,3))
            print("points scored", total_actual_points)
            print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
