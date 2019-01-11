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
fighters.append(Player('Jones', 118, 9100, 1, 88.5))
fighters.append(Player('Gustafsson', 565, 7100, 1, 11))
fighters.append(Player('Cyborg', -125, 9200, 2, 1.5))
fighters.append(Player('Nunes', 113, 7000, 2, 116.5))
fighters.append(Player('Chiesa', 226, 9000, 3, 104))
fighters.append(Player('Condit', 245, 7200, 3, 7.5))
fighters.append(Player('Latifi', 151, 8900, 4, 16.5))
fighters.append(Player('Corey Anderson', 720, 7300, 4, 50))
fighters.append(Player('Mendes', 200, 8700, 5, 42))
fighters.append(Player('Volkanovski', 425, 7500, 5, 107))
fighters.append(Player('Harris', -110, 8600, 6, 50))
fighters.append(Player('Arlovski', 450, 7600, 6, 22))
fighters.append(Player('Zingano', 258, 8500, 7, 1.5))
fighters.append(Player('Megan Anderson', 467, 7700, 7, 91.5))
fighters.append(Player('Yan', 174, 9300, 8, 126))
fighters.append(Player('Andrade', 705, 6900, 8, 14))
fighters.append(Player('Ryan Hall', 245, 9400, 9, 93))
fighters.append(Player('Penn', 610, 6800, 9, 10))
fighters.append(Player('Millender', 239, 8800, 10, 77.5))
fighters.append(Player('Bahadurzada', 245, 7400, 10, 41))
fighters.append(Player('Uriah Hall', 173, 8300, 11, 74.5))
fighters.append(Player('Lewis', 275, 7900, 11, 34))
fighters.append(Player('Wood', 209, 8200, 12, 107.5))
fighters.append(Player('Ewell', 228, 8000, 12, 7.5))
fighters.append(Player('Jackson', 290, 8400, 13, 95))
fighters.append(Player('Kelleher', 415, 7800, 13, 3))

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
        if 'Jones' in p.name or 'Gustafsson' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Cyborg' in p.name or 'Nunes' in p.name:
            found_player = True
    if not found_player:
        continue'''
    found_player = False
    for p in lineup:
        if 'Nunes' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Yan' in p.name:
            found_player = True
    if not found_player:
        continue
    if total_score > .1:
    #if total_score > best_score:
    #if five_wins_prob > best_score:
    #if five_wins_prob > 17:
        total_actual_points = 0
        real_lineups += 1
        for player in lineup:
            #print(player)
            total_actual_points += player.actual_score
        if total_actual_points >= 640.5:
            for player in lineup:
                print(player)
            print("salary", salary)
            print("percentage to win all fights:", round(total_score,3))
            print("points scored", total_actual_points)
            print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
