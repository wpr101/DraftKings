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
fighters.append(Player('Jones', -435, 9600, 1, 107.5))
fighters.append(Player('Smith', 847, 6600, 1, 18))
fighters.append(Player('Woodley', 150, 8700, 2, 17)) 
fighters.append(Player('Usman', 435, 7500, 2, 131.5))
fighters.append(Player('Askren', 467, 9000, 3, 95))
fighters.append(Player('Lawler', 362, 7200, 3, 21))
fighters.append(Player('Zhang', 318, 8300, 4, 88.5))
fighters.append(Player('Torres', 1160, 7900, 4, 15))
fighters.append(Player('Garbrandt', 183, 8500, 5, 10.5))
fighters.append(Player('Munhoz', 200, 7700, 5, 115.5))
fighters.append(Player('Zabit', 185, 8900, 6, 92))
fighters.append(Player('Stephens', 314, 7300, 6, 20.5))
fighters.append(Player('Walker', -125, 8400, 7, 102))
fighters.append(Player('Cirkunov', 178, 7800, 7, 0.5))
fighters.append(Player('Stamann', 1020, 8600, 8, 54))
fighters.append(Player('Perez', 382, 7600, 8, 25.5))
fighters.append(Player('Gall', -122, 9100, 9, 11.5))
fighters.append(Player('Sanchez', 875, 7100, 9, 133))
fighters.append(Player('Shahbazyan', 172, 8200, 10, 106.5))
fighters.append(Player('Byrd', 231, 8000, 10, 0.5))
fighters.append(Player('Chiasson', -148, 9400, 11, 112.5))
fighters.append(Player('Mazany', 1500, 6800, 11, 7))
#fighters.append(Player('Vera', -214, 8800, 12, 0))
#fighters.append(Player('Saenz', 172, 7400, 12, 0))
fighters.append(Player('Viana', -110, 9200, 13, 38.5))
fighters.append(Player('Cifers', 545, 7000, 13, 73.5))

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
