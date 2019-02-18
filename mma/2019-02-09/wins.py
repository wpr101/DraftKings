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
#fighters.append(Player('Whittaker', -241, 8900, 1))
#fighters.append(Player('Gastelum', 192, 7300, 1))
fighters.append(Player('Adesanya', -613, 9600, 2)) 
fighters.append(Player('Silva', 428, 6600, 2))
#fighters.append(Player('Simon', -119, 8200, 3))
fighters.append(Player('Yahya', -105, 8000, 3))
fighters.append(Player('DeLaRosa', -259, 8800, 4))
#fighters.append(Player('Kassem', 207, 7400, 4))
#fighters.append(Player('Crute', -138, 8300, 5))
fighters.append(Player('Alvey', 112, 7900, 5))
fighters.append(Player('Smith', -248, 8600, 6))
fighters.append(Player('Ma', 198, 7600, 6))
fighters.append(Player('Young', -311, 9100, 7))
#fighters.append(Player('Arnett', 246, 7100, 7))
fighters.append(Player('KaraFrance', -288, 9000, 8))
#fighters.append(Player('Paiva', 228, 7200, 8))
fighters.append(Player('Kang', -376, 9400, 9))
#fighters.append(Player('Ishihara', 289, 6800, 9))
fighters.append(Player('Vannata', -395, 9300, 10))
#fighters.append(Player('MarcosRosa', 303, 6900, 10))
fighters.append(Player('Turner', -253, 8700, 11))
#fighters.append(Player('Potter', 202, 7500, 11))
fighters.append(Player('Martinez', -163, 8500, 12))
#fighters.append(Player('Buren', 134, 7700, 12))

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
        if 'Whittaker' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Vannata' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Silva' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Vannata' in p.name:
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
