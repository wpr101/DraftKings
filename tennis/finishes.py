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
fighters.append(Player('Delbonis', -335, 10000, 1))
fighters.append(Player('Jaziri', 275, 5500, 1))
fighters.append(Player('Fognini', -275, 9600, 2)) 
fighters.append(Player('Aliassime', 235, 5900, 2))
fighters.append(Player('Simon', -290, 9400, 3))
fighters.append(Player('Hoang', 245, 5700, 3))
fighters.append(Player('Watanuki', -275, 9200, 4))
fighters.append(Player('Lacko', 235, 6100, 4))
fighters.append(Player('Daniel', -185, 8900, 5))
fighters.append(Player('Wild', 160, 6300, 5))
fighters.append(Player('Kukushkin', -200, 8700, 6))
fighters.append(Player('Kudla', 170, 6500, 6))
fighters.append(Player('Lajovic', -185, 8500, 7))
fighters.append(Player('Norrie', 160, 6700, 7))
fighters.append(Player('Harris', -155, 8300, 8))
fighters.append(Player('King', 135, 6900, 8))
#fighters.append(Player('Istomin', -140, 8200, 9))
#fighters.append(Player('Lopez', 120, 7100, 9))
fighters.append(Player('Jarry', -130, 8100, 10))
fighters.append(Player('Baena', 110, 7200, 10))
fighters.append(Player('Andreozzi', -130, 8000, 11))
fighters.append(Player('Baena', 110, 7300, 11))
fighters.append(Player('Kyrgios', -120, 7900, 12))
fighters.append(Player('Millman', 100, 7400, 12))
fighters.append(Player('Ymer', 190, 7800, 13))
fighters.append(Player('Londero', -230, 7600, 13))

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
    if total_score > 6.8:#best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
