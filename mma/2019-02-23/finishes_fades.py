import csv
from itertools import combinations
import random
import itertools

class Player():
    def __init__(self, name, odds, salary, fight_num, actual_score):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)
        self.fight_num = int(fight_num)
        self.actual_score = float(actual_score)

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
fighters.append(Player('Santos', 139, 8500, 1, 89))
fighters.append(Player('Blachowicz', 127, 7700, 1, 0))
fighters.append(Player('Lima', 226, 8400, 2, 0)) 
fighters.append(Player('Struve', 123, 7800, 2, 81))
fighters.append(Player('Oleksiejczuk', 228, 8900, 3, 0))
fighters.append(Player('Villante', 579, 7300, 3, 0))
fighters.append(Player('Carmouche', 380, 8300, 4, 0))
fighters.append(Player('Pudilova', 725, 7900, 4, 0))
fighters.append(Player('Yan', 363, 9300, 5, 0))
fighters.append(Player('Dodson', 790, 6900, 5, 0))
fighters.append(Player('Ankalaev', -109, 9100, 6, 0))
fighters.append(Player('Abreu', 270, 7100, 6, 0))
fighters.append(Player('PedersoliJr', 365, 8200, 7, 0))
fighters.append(Player('Grant', 329, 8000, 7, 110))
fighters.append(Player('Fishgold', -130, 9000, 8, 117))
fighters.append(Player('Teymur', 480, 7200, 8, 0))
fighters.append(Player('Robertson', 133, 8600, 9, 118.5))
fighters.append(Player('Macedo', 360, 7600, 9, 0))
fighters.append(Player('Reyes', 175, 8800, 10, 0))
fighters.append(Player('Hadzovic', 209, 7400, 10, 118))
fighters.append(Player('Prazeres', -150, 9400, 11, 0))
fighters.append(Player('Naurdiev', 570, 6800, 11, 0))
fighters.append(Player('Khabilov', 560, 8700, 12, 0))
fighters.append(Player('Ferreira', 260, 7500, 12, 0))
fighters.append(Player('Ismagulov', 160, 9200, 13, 0))
fighters.append(Player('Alvarez', 350, 7000, 13, 0))

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

def print_player_only(in_list):
    salary = 0
    actual_score = 0
    for player in in_list:
        print player.name
        salary += player.salary
        actual_score += player.actual_score
    print('salary: ' + str(salary))
    print('odds for all six: ' + str(round(calc_6_wins(in_list),2)))
    print('actual_score: ' + str(actual_score))

def calc_6_wins(lineup):
    total_score = 1
    for player in lineup:
        if player.odds < 0:
            total_score *= float(player.odds) / float((player.odds - 100))
        else:
            total_score *= float(100) / float((player.odds + 100))
    # Conver to %
    total_score *= 100
    return total_score

def gen_best_lineup(fighters):
    my_combos = combinations(fighters, 6)

    best_score = 0
    real_lineups = 0
    best_lineup = None
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
            '''for player in lineup:
                print(player)
            print("salary", salary)
            print("percentage to win all fights:", round(total_score,3))
            print("")'''
            best_score = total_score
            best_lineup = lineup
    return best_lineup

def rotate_fades():
    # Generate initial lineup with no fades
    current_best = gen_best_lineup(fighters)
    print('Initial best lineup:')
    print_player_only(current_best)
    print('')
    fades = []
    enumerator = 0
    global_counter = 1
    for x in range(1,7):
        for comb in itertools.combinations([1, 2, 3, 4, 5, 6], x):
            temp_players = list(fighters)
            enumerator += 1
            for number in comb:
                fades.append(current_best[number-1])
            count = 0
            for player in temp_players:
                for item in fades:
                    if player.name == item.name:
                        temp_players.pop(count)
                count += 1
            print str(global_counter) + ')'
            print_player_only(gen_best_lineup(temp_players))
            print('')
            global_counter += 1
            fades=[]

rotate_fades()
