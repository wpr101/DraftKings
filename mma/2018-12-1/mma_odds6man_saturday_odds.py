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
fighters.append(Player('Santos', -141, 8300, 1))
fighters.append(Player('Tuivasa', 117, 7900, 1))
fighters.append(Player('Pedro', -488, 9400, 2))
fighters.append(Player('Rua', 367, 6800, 2))
fighters.append(Player('Willis', -140, 8200, 3))
fighters.append(Player('Hunt', 116, 8000, 3))
fighters.append(Player('Matthews', -125, 8400, 4))
fighters.append(Player('Martin', 102, 7800, 4))
fighters.append(Player('Yusuff', -597, 9300, 5))
fighters.append(Player('Mokhtarian', 426, 6900, 5))
fighters.append(Player('Crute', -263, 8700, 6))
fighters.append(Player('Craig', 212, 7500, 6))
fighters.append(Player('Kunchenko', -332, 9200, 7))
fighters.append(Player('Okami', 260, 7000, 7))
fighters.append(Player('Nguyen', -136, 8500, 8))
fighters.append(Player('Reis', 111, 7700, 8))
fighters.append(Player('Nakamura', -175, 8800, 9))
fighters.append(Player('Touahri', 148, 7400, 9))
fighters.append(Player('KaraFrance', -364, 9100, 10))
fighters.append(Player('Garica', 283, 7100, 10))
fighters.append(Player('Giagos', -367, 9000, 11))
fighters.append(Player('Hirota', 284, 7200, 11))
fighters.append(Player('Ismagulov', -536, 9500, 12))
fighters.append(Player('Gorgees', 391, 6700, 12))


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
        if 'Tuivasa' in p.name or 'Santos' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
    for p in lineup:
        if 'Barcelos' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Ramos' in p.name:
            found_player = True
    if not found_player:
        continue'''
    #if total_score > 4.5:
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        # odds for 5 wins
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
                
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("percentage to win 5 fights:", round(five_wins_prob,3))
        print("")
        best_score = total_score

print("real_lineups", real_lineups)    
