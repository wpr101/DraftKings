import csv
from itertools import combinations
import random



class Player():
    def __init__(self, name, points, salary):
        self.name = name
        self.points = float(points)
        self.salary = int(salary)

    def __repr__(self):
        return 'Player(name=%s, points=%s, salary=%s)' % \
    (self.name, self.points, self.salary)

'''def convert_to_percent(odds):
    percent = 1
    if odds < 0:
        percent *= float(odds) / float((odds - 100))
    else:
        percent *= float(100) / float((odds + 100))
    return (percent)'''

fighters = []
fighters.append(Player('Harvick', 66.71, 12200))
fighters.append(Player('Logano', 54.13, 11700))
fighters.append(Player('Keselowski', 52.64, 11100)) 
fighters.append(Player('KyleBusch', 36.94, 10500))
fighters.append(Player('Hamlin', 32.17, 10000))
fighters.append(Player('Elliot', 47.19, 9700))
fighters.append(Player('TruexJr', 39.53, 9500))
fighters.append(Player('Larson', 40.43, 9300))
fighters.append(Player('Bowyer', 48.13, 9100))
fighters.append(Player('Blaney', 46.72, 8900))
fighters.append(Player('Almirola', 49.34, 8700))
fighters.append(Player('KURTBusch', 37.13, 8500))
fighters.append(Player('Johnson', 35.93, 8300))
fighters.append(Player('Jones', 33.96, 8100))
fighters.append(Player('Suarez', 27.84, 7900))
fighters.append(Player('AustinDillon', 27.82, 7700))
fighters.append(Player('DiBenedetto', 29.49, 7600))
fighters.append(Player('StenhouseJr', 18.93, 7500))
fighters.append(Player('AlexBowman', 33.43, 7300))
fighters.append(Player('Byron', 33.52, 7100))
fighters.append(Player('Menard', 27.94, 7000))
fighters.append(Player('Newman', 32.93, 6900))
fighters.append(Player('Hemric', 25.92, 6800))
fighters.append(Player('Wallace', 26.94, 6600))
fighters.append(Player('Preece', 26.94, 6400))
fighters.append(Player('Buescher', 28.83, 6200))
'''fighters.append(Player('McDowell', 20.12, 6000))
fighters.append(Player('Ragan', 26.04, 5800))
fighters.append(Player('TyDillon', 26.37, 5600))
fighters.append(Player('Tifft', 24.96, 5500))
fighters.append(Player('Chastain', 21.13, 5400))
fighters.append(Player('Cassill', 19.43, 5300))
fighters.append(Player('Lajoie', 15.15, 5200))
fighters.append(Player('Kligerman', 20.32, 5100))
fighters.append(Player('McLeod', 17.62, 5000))
fighters.append(Player('Ware', 15.63, 4900))
fighters.append(Player('Smithley', 15.92, 4800))
'''
my_combos = combinations(fighters, 6)

best_score = 0
real_lineups = 0
for lineup in my_combos:
    total_score = 1
    points = 0
    salary = 0
    for player in lineup:
        salary += player.salary
        total_score += float(player.points)
    if salary > 50000:
        continue
    if total_score > best_score:
        print(total_score)
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("projected points:", round(total_score,3))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
