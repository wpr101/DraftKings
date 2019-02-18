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
fighters.append(Player('Moraes', 245, 8800, 1))
fighters.append(Player('Assuncao', 520, 7400, 1))
fighters.append(Player('Moicano', 275, 8300, 2)) 
fighters.append(Player('Aldo', 410, 7900, 2))
fighters.append(Player('Maia', 125, 8700, 3))
fighters.append(Player('Good', 285, 7500, 3))
fighters.append(Player('Oliveira', 125, 8500, 4))
fighters.append(Player('Teymur', 300, 7700, 4))
fighters.append(Player('Walker', 130, 9200, 5))
fighters.append(Player('Ledet', 400, 7000, 5))
fighters.append(Player('Souza', 145, 9100, 6))
fighters.append(Player('Frota', 275, 7100, 6))
fighters.append(Player('Hernandez', 170, 8900, 7))
fighters.append(Player('Perez', 245, 7300, 7))
fighters.append(Player('Santos', 355, 8600, 8))
fighters.append(Player('Borella', 350, 7600, 8))
fighters.append(Player('Griffin', 255, 9000, 9))
fighters.append(Player('Alves', 475, 7200, 9))
#fighters.append(Player('Albini', 145, 8100, 10))
fighters.append(Player('Rozenstruik', 170, 8100, 10))
fighters.append(Player('Freitas', 230, 8400, 11))
fighters.append(Player('Colares', 282, 7800, 11))
fighters.append(Player('Nurmagomedov', 750, 8200, 12))
fighters.append(Player('Ramos', 245, 8000, 12))
fighters.append(Player('Bibulatov', 240, 9400, 13))
fighters.append(Player('Bontorin', 569, 6800, 13))

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
        if 'Nurmagomedov' in p.name:
            found_player = True
    if not found_player:
        continue
    '''found_player = False
    for p in lineup:
        if 'Bontorin' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Dillashaw' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Calderwood' in p.name:
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
    #if salary >= 49500:
    #if total_score > .08:
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
