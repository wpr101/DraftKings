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
fighters.append(Player('Jones', -530, 9600, 1))
fighters.append(Player('Smith', 744, 6600, 1))
fighters.append(Player('Woodley', 130, 8700, 2)) 
fighters.append(Player('Usman', 495, 7500, 2))
fighters.append(Player('Askren', 335, 9000, 3))
fighters.append(Player('Lawler', 385, 7200, 3))
fighters.append(Player('Zhang', 300, 8300, 4))
fighters.append(Player('Torres', 800, 7900, 4))
fighters.append(Player('Garbrandt', 155, 8500, 5))
fighters.append(Player('Munhoz', 200, 7700, 5))
fighters.append(Player('Zabit', 170, 8900, 6))
fighters.append(Player('Stephens', 310, 7300, 6))
fighters.append(Player('Walker', -105, 8400, 7))
fighters.append(Player('Cirkunov', 140, 7800, 7))
fighters.append(Player('Stamann', 585, 8600, 8))
fighters.append(Player('Perez', 440, 7600, 8))
fighters.append(Player('Gall', -150, 9100, 9))
fighters.append(Player('Sanchez', 950, 7100, 9))
fighters.append(Player('Shahbazyan', 155, 8200, 10))
fighters.append(Player('Byrd', 195, 8000, 10))
fighters.append(Player('Chiasson', -165, 9400, 11))
fighters.append(Player('Mazany', 1000, 6800, 11))
fighters.append(Player('Vera', 180, 8800, 12))
fighters.append(Player('Saenz', 700, 7400, 12))
fighters.append(Player('Viana', -165, 9200, 13))
fighters.append(Player('Cifers', 590, 7000, 13))

'''# check salaries add up to 16200, assumes 13 fights
i = 0
while True:
    if i > 24:
        break
    if fighters[i].salary + fighters[i+1].salary == 16200:
        i += 2
        continue
    else:
        print("Salaries are wrong!")
        exit(0)'''

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
        if 'Usman' in p.name: #or 'Woodley' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Askren' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
    for p in lineup:
        if 'Ismagulov' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Prazeres' in p.name:
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
    #if total_score > .125:
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
