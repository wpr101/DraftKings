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
fighters.append(Player('Holloway', -110, 8300, 1))
fighters.append(Player('Ortega', -114, 7900, 1))
fighters.append(Player('Shevchenko', -343, 9400, 2))
fighters.append(Player('Jedrzejczyk', 268, 6800, 2))
fighters.append(Player('Nelson', -149, 8400, 3))
fighters.append(Player('Oliveira', 124, 7800, 3))
fighters.append(Player('Dawodu', -174, 8600, 4))
fighters.append(Player('Bochniak', 144, 7600, 4))
fighters.append(Player('Santos', -191, 8800, 5))
fighters.append(Player('Manuwa', 159, 7400, 5))
fighters.append(Player('Gadelha', -330, 9300, 6))
fighters.append(Player('Ansaroff', 259, 6900, 6))
fighters.append(Player('Mercier', -147, 8500, 7))
fighters.append(Player('Burns', 122, 7700, 7))
#fighters.append(Player('Chookagian', -203, 8700, 8))
#fighters.append(Player('Eye', 168, 7500, 8))
fighters.append(Player('Theodorou', -127, 8200, 9))
fighters.append(Player('Anders', 103, 8000, 9))
fighters.append(Player('Katona', -180, 8900, 10))
fighters.append(Player('Lopez', 150, 7300, 10))
fighters.append(Player('Laprise', -387, 9100, 11))
fighters.append(Player('Lima', 298, 7100, 11))
fighters.append(Player('Ferreira', -466, 9200, 12))
fighters.append(Player('Nelson', 358, 7000, 12))
fighters.append(Player('Rakic', -604, 9500, 13))
fighters.append(Player('Clark', 428, 6700, 13))

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
        if 'Holloway' in p.name or 'Ortega' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
    for p in lineup:
        if 'Shevchenko' in p.name or 'Jedrzejczyk' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
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
    #if total_score > 4:
    if total_score > best_score:
    #if five_wins_prob > best_score:
    #if five_wins_prob > 17:
        real_lineups += 1
        for player in lineup:
            print(player)
        # odds for 5 wins

                
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("percentage to win 5 fights:", round(five_wins_prob,3))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
