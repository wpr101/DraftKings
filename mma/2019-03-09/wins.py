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
fighters.append(Player('DosSantos', -221, 9400, 1))
fighters.append(Player('Lewis', 177, 6800, 1))
fighters.append(Player('Millender', -119, 8200, 2)) 
fighters.append(Player('ZaleskiDos', -105, 8000, 2))
fighters.append(Player('Means', -196, 8800, 3))
fighters.append(Player('Price', 162, 7400, 3))
fighters.append(Player('Ivanov', -130, 8400, 4))
fighters.append(Player('Rothwell', 104, 7800, 4))
fighters.append(Player('Dariush', -188, 9000, 5))
fighters.append(Player('Dober', 156, 7200, 5))
fighters.append(Player('Akhmedov', -142, 8500, 6))
fighters.append(Player('Boetsch', 116, 7700, 6))
fighters.append(Player('Martin', -199, 9200, 7))
fighters.append(Player('Moraes', 164, 7000, 7))
fighters.append(Player('Kunitskaya', -184, 8900, 8))
fighters.append(Player('Reneau', 152, 7300, 8))
fighters.append(Player('Dawson', -179, 8700, 9))
fighters.append(Player('Erosa', 148, 7500, 9))
fighters.append(Player('Hughes', -215, 9300, 10))
fighters.append(Player('Greene', 175, 6900, 10))
fighters.append(Player('Smolka', -107, 8300, 11))
fighters.append(Player('Schnell', -117, 7900, 11))
fighters.append(Player('Morono', -195, 9100, 12))
fighters.append(Player('Ottow', 160, 7100, 12))
fighters.append(Player('White', -166, 8600, 13))
fighters.append(Player('Moret', 137, 7600, 13))

'''
# check salaries add up to 16200, assumes 13 fights
i = 0
while True:
    if i > 24:
        break
    if fighters[i].salary + fighters[i+1].salary == 16200:
        i += 2
        continue
    else:
        print("Salaries are wrong!")
        exit(0)
print("looks good")
exit(0)
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
        if 'DosSantos' in p.name: #or 'Woodley' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Moraes' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Smolka' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Dawson' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Akhmedov' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'Rothwell' in p.name:
            found_player = True
    if not found_player:
        continue
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
    #if total_score > .5:
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
