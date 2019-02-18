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
#fighters.append(Player('Whittaker', 140, 8900, 1))
#fighters.append(Player('Gastelum', 280, 7300, 1))
fighters.append(Player('Adesanya', -150, 9600, 2)) 
fighters.append(Player('Silva', 660, 6600, 2))
fighters.append(Player('Simon', 480, 8200, 3))
fighters.append(Player('Yahya', 165, 8000, 3))
fighters.append(Player('DeLaRosa', 140, 8800, 4))
fighters.append(Player('Kassem', 750, 7400, 4))
fighters.append(Player('Crute', 381, 8300, 5))
fighters.append(Player('Alvey', 215, 7900, 5))
fighters.append(Player('Smith', -140, 8600, 6))
fighters.append(Player('MaKim', 560, 7600, 6))
fighters.append(Player('Young', 175, 9100, 7))
fighters.append(Player('Arnett', 1300, 7100, 7))
fighters.append(Player('KaraFrance', 200, 9000, 8))
fighters.append(Player('Paiva', 660, 7200, 8))
fighters.append(Player('Kang', -105, 9400, 9))
fighters.append(Player('Ishihara', 500, 6800, 9))
fighters.append(Player('Vannata', -210, 9300, 10))
fighters.append(Player('MarcosRosa', 1160, 6900, 10))
fighters.append(Player('Turner', -179, 8700, 11))
fighters.append(Player('Potter', 430, 7500, 11))
fighters.append(Player('Martinez', 255, 8500, 12))
fighters.append(Player('Buren', 600, 7700, 12))

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
        if 'Kang' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Turner' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
    for p in lineup:
        if 'Maia' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Ledet' in p.name:
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
    #if total_score > .4:
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
