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
#fighters.append(Player('Moraes', -157, 8800, 1))
fighters.append(Player('Assuncao', 130, 7400, 1))
#fighters.append(Player('Moicano', -143, 8300, 2)) 
#fighters.append(Player('Aldo', 118, 7900, 2))
fighters.append(Player('Maia', -187, 8700, 3))
#fighters.append(Player('Good', 157, 7500, 3))
fighters.append(Player('Oliveira', -126, 8500, 4))
#fighters.append(Player('Teymur', 101, 7700, 4))
#fighters.append(Player('Walker', -204, 9200, 5))
fighters.append(Player('Ledet', 168, 7000, 5))
fighters.append(Player('Souza', -219, 9100, 6))
#fighters.append(Player('Frota', 178, 7100, 6))
#fighters.append(Player('Hernandez', -158, 8900, 7))
fighters.append(Player('Perez', 131, 7300, 7))
#fighters.append(Player('Santos', -170, 8600, 8))
#fighters.append(Player('Borella', 141, 7600, 8))
#fighters.append(Player('Griffin', -203, 9000, 9))
#fighters.append(Player('Alves', 167, 7200, 9))
#fighters.append(Player('Albini', -122, 8100, 10))
#fighters.append(Player('Rozenstruik', -102, 8100, 10))
#fighters.append(Player('Freitas', -127, 8400, 11))
#fighters.append(Player('Colares', 103, 7800, 11))
#fighters.append(Player('Nurmagomedov', 117, 8200, 12))
fighters.append(Player('Ramos', -142, 8000, 12))
fighters.append(Player('Bibulatov', -359, 9400, 13))
#fighters.append(Player('Bontorin', 281, 6800, 13))

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
        if 'Assuncao' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    '''for p in lineup:
        if 'Ramos' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
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
    if salary > 49000:
    #if total_score > 1.9:
    #if total_score > best_score:
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
