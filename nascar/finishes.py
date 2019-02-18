import csv
from itertools import combinations
import random



class Player():
    def __init__(self, name, odds, salary):
        self.name = name
        self.odds = float(odds)
        self.salary = int(salary)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s)' % \
    (self.name, self.odds, self.salary)

def convert_to_percent(odds):
    percent = 1
    if odds < 0:
        percent *= float(odds) / float((odds - 100))
    else:
        percent *= float(100) / float((odds + 100))
    return (percent)

fighters = []
fighters.append(Player('Keselowski', .1428, 10600))
fighters.append(Player('Logano', .125, 10400))
fighters.append(Player('Bowyer', .1111, 9900)) 
fighters.append(Player('Elliot', .1, 9400))
fighters.append(Player('Hamlin', .1, 10000))
fighters.append(Player('Harvick', .0909, 10200))
fighters.append(Player('KyleBusch', .0909, 9600))
fighters.append(Player('Almirola', .0833, 9200))
fighters.append(Player('Blaney', .0714, 9000))
fighters.append(Player('Stenhouse', .0666, 9800))
fighters.append(Player('KurtBusch', .0625, 8700))
fighters.append(Player('Truex', .0625, 8800))
fighters.append(Player('Johnson', .05, 8500))
fighters.append(Player('Byron', .05, 6800))
fighters.append(Player('Bowman', .0454, 8000))
fighters.append(Player('Suarez', .0454, 8400))
fighters.append(Player('Jones', .04, 8200))
fighters.append(Player('Menard', .04, 7400))
fighters.append(Player('Larson', .0357, 7800))
fighters.append(Player('Dillon', .0303, 7600))
fighters.append(Player('McMurray', .0303, 7500))
fighters.append(Player('Newman', .0303, 7000))
fighters.append(Player('WallaceJr', .025, 7200))
fighters.append(Player('Hemric', .0166, 6600))
fighters.append(Player('DiBenedetto', .0166, 5700))
fighters.append(Player('McDowell', .0166, 5900))

my_combos = combinations(fighters, 6)

best_score = 0
real_lineups = 0
for lineup in my_combos:
    total_score = 1
    points = 0
    salary = 0
    for player in lineup:
        salary += player.salary
        total_score *= float(player.odds)
    if salary > 50000:
        continue
    if total_score > best_score:
        print(total_score)
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,3))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
