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
fighters.append(Player('Harvick', 47.93, 12500))
fighters.append(Player('KyleBusch', 49.96, 11900))
fighters.append(Player('Keselowski', 49.96, 11400)) 
fighters.append(Player('Logano', 45.62, 10700))
fighters.append(Player('TruexJr', 55.93, 10100))
fighters.append(Player('Larson', 37.28, 9800))
fighters.append(Player('Blaney', 39.84, 9500))
fighters.append(Player('Elliott', 38.16, 9200))
fighters.append(Player('Bowyer', 38.92, 9000))
fighters.append(Player('Hamlin', 34.09, 8800))
fighters.append(Player('Almirola', 43.47, 8600))
fighters.append(Player('ErikJones', 36.29, 8400))
fighters.append(Player('KurtBusch', 44.73, 8200))
fighters.append(Player('JJohnson', 27.83, 8100))
fighters.append(Player('StenhouseJr', 25.94, 7900))
fighters.append(Player('Suarez', 36.93, 7700))
fighters.append(Player('Dillon', 33.41, 7600))
fighters.append(Player('AlexBowman', 32.37, 7400))
fighters.append(Player('RyanNewman', 41.19, 7200))
fighters.append(Player('Hemric', 23.02, 7100))
fighters.append(Player('Menard', 29.12, 6900))
fighters.append(Player('DiBenedetto', 30.04, 6700))
fighters.append(Player('Byron', 36.72, 6600))
fighters.append(Player('Buescher', 32.46, 6500))
'''fighters.append(Player('Wallace', 27.01, 6300))
fighters.append(Player('Preece', 34.63, 6100))
fighters.append(Player('TyDillon', 22.03, 6000))
fighters.append(Player('Ragan', 20.21, 5900))
fighters.append(Player('McDowell', 21.43, 5700))
fighters.append(Player('Tifft', 24.84, 5600))
fighters.append(Player('Chastain', 23.15, 5500))
fighters.append(Player('Kligerman', 22.83, 5300))
fighters.append(Player('Cassill', 18.81, 5200))
fighters.append(Player('Lajoie', 23.07, 5100))
fighters.append(Player('Gase', 18.43, 5000))
fighters.append(Player('Sorenson', 19.32, 4900))
fighters.append(Player('McLeod', 18.04, 4800))
fighters.append(Player('CodyWare', 17.52, 4700))'''

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
