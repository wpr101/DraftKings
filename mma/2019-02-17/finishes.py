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
fighters.append(Player('Velasquez', -120, 9000, 1))
fighters.append(Player('Ngannou', 172, 7200, 1))
#fighters.append(Player('Felder', 179, 8200, 2)) 
fighters.append(Player('Vick', 423, 8000, 2))
fighters.append(Player('Calvillo', 175, 9200, 3))
fighters.append(Player('Casey', 900, 7000, 3))
fighters.append(Player('Gracie', -165, 9300, 4))
fighters.append(Player('Caceres', 610, 6900, 4))
fighters.append(Player('Luque', 113, 9400, 5))
fighters.append(Player('Barberena', 610, 6800, 5))
fighters.append(Player('Jury', 320, 8800, 6))
fighters.append(Player('Fili', 725, 7400, 6))
fighters.append(Player('Rivera', 467, 8300, 7))
fighters.append(Player('Sterling', 466, 7900, 7))
#fighters.append(Player('Bermudez', -117, 9100, 8))
fighters.append(Player('Lopez', 325, 7100, 8))
fighters.append(Player('Lee', 235, 8900, 9))
fighters.append(Player('EvansSmith', 700, 7300, 9))
fighters.append(Player('Holtzman', 425, 8500, 10))
fighters.append(Player('Lentz', 582, 7700, 10))
#fighters.append(Player('Penne', 342, 8400, 11))
#fighters.append(Player('Esquibel', 1025, 7800, 11))
fighters.append(Player('Sanders', 255, 8700, 12))
fighters.append(Player('Barao', 255, 7500, 12))
fighters.append(Player('Albu', 250, 8600, 13))
fighters.append(Player('Whitmire', 500, 7600, 13))

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
        if 'Velasquez' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
    for p in lineup:
        if 'Gracie' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Gracie' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Holtzman' in p.name:
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
    #if total_score > .25 and total_score < .3:
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
