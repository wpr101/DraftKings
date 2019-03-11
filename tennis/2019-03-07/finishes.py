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
#fighters.append(Player('Bouchard', -270, 9500, 1))
#fighters.append(Player('Flipkens', 230, 6100, 1))
#fighters.append(Player('Puig', -275, 9400, 2)) 
fighters.append(Player('Rodina', 235, 6000, 2))
fighters.append(Player('Millman', -230, 9300, 3))
fighters.append(Player('Struff', 190, 6200, 3))
fighters.append(Player('Diyas', -210, 9100, 4))
fighters.append(Player('Pegula', 175, 6400, 4))
fighters.append(Player('Ymer', 125, 8700, 5))
fighters.append(Player('Fratangelo', -145, 6800, 5))
fighters.append(Player('Opelka', -170, 8600, 6))
fighters.append(Player('Mayer', 150, 6900, 6))
fighters.append(Player('Sakkari', -150, 8500, 7))
fighters.append(Player('Mchale', 130, 7200, 7))
fighters.append(Player('Humbert', -175, 8400, 8))
fighters.append(Player('Marterer', 155, 7100, 8))
fighters.append(Player('Jaziri', -145, 8300, 9))
#fighters.append(Player('Klahn', 125, 7400, 9))
fighters.append(Player('Paire', -190, 8200, 10))
fighters.append(Player('Gunneswaran', 165, 7300, 10))
fighters.append(Player('Townsend', -115, 8100, 11))
fighters.append(Player('Bonaventure', -105, 7500, 11))


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
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
