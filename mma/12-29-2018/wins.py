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
#fighters.append(Player('Jones', -280, 9100, 1))
fighters.append(Player('Gustafsson', 225, 7100, 1))
fighters.append(Player('Cyborg', -251, 9200, 2))
fighters.append(Player('Nunes', 202, 7000, 2))
fighters.append(Player('Chiesa', -173, 9000, 3))
fighters.append(Player('Condit', 145, 7200, 3))
fighters.append(Player('Latifi', -147, 8900, 4))
fighters.append(Player('Corey Anderson', 121, 7300, 4))
fighters.append(Player('Mendes', -153, 8700, 5))
fighters.append(Player('Volkanovski', 125, 7500, 5))
fighters.append(Player('Harris', -171, 8600, 6))
fighters.append(Player('Arlovski', 143, 7600, 6))
fighters.append(Player('Zingano', -149, 8500, 7))
fighters.append(Player('Megan Anderson', 124, 7700, 7))
fighters.append(Player('Yan', -292, 9300, 8))
fighters.append(Player('Andrade', 233, 6900, 8))
#fighters.append(Player('Ryan Hall', -476, 9400, 9))
fighters.append(Player('Penn', 353, 6800, 9))
fighters.append(Player('Millender', -150, 8800, 10))
fighters.append(Player('Bahadurzada', 123, 7400, 10))
fighters.append(Player('Uriah Hall', -104, 8300, 11))
fighters.append(Player('Lewis', -120, 7900, 11))
fighters.append(Player('Wood', -120, 8200, 12))
fighters.append(Player('Ewell', -104, 8000, 12))
#fighters.append(Player('Jackson', -157, 8400, 13))
fighters.append(Player('Kelleher', 130, 7800, 13))

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
        if 'Gustafsson' in p.name:
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
