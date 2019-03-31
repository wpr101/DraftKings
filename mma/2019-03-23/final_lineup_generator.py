import csv
from itertools import combinations
import random
import itertools

class Player():
    def __init__(self, name, id_num, odds, salary, fight_num):
        self.name = name
        self.id_num = id_num
        self.odds = int(odds)
        self.salary = int(salary)
        self.fight_num = int(fight_num)

    def __repr__(self):
        return 'Player(name=%s, id_num=%s, odds=%s, salary=%s, fight_num=%s)' % \
    (self.name, self.id_num, self.odds, self.salary, self.fight_num)

def convert_to_percent(odds):
    percent = 1
    if odds < 0:
        percent *= float(odds) / float((odds - 100))
    else:
        percent *= float(100) / float((odds + 100))
    return (percent)


def print_player_only(in_list):
    salary = 0
    for player in in_list:
        print player.name
        salary += player.salary
    print('salary: ' + str(salary))
    print('odds for all six: ' + str(round(calc_6_wins(in_list),3)))

def print_id_only(in_list):
    count = 0
    for player in in_list:
        if count == 5:
            print (str(player.id_num)),
        else:
            print (str(player.id_num) + ','),
        count += 1

def calc_6_wins(lineup):
    total_score = 1
    for player in lineup:
        total_score *= player.odds
    # Conver to %
    total_score *= 100
    return total_score

def gen_best_lineup(fighters):
    my_combos = combinations(fighters, 6)
    best_score = 0
    real_lineups = 0
    best_lineup = None
    my_counter = 0
    text_file = open("final_upload.csv", "w")
    text_file.write('F,F,F,F,F,F')
    text_file.write('\n')
    for lineup in my_combos:
        total_score = 1
        points = 0
        salary = 0
        for player in lineup:
            salary += player.salary
            total_score += int(player.odds)
        if salary > 50000 or salary < 49000:
            continue
        
        double_flag = False
        for p1 in lineup:
            for p2 in lineup:
                if p1.fight_num == p2.fight_num and p1.name != p2.name:
                    double_flag = True
        if double_flag:
            continue

        my_counter += 1
        print my_counter
        print lineup
        print('score: ' + str(total_score))
        print('salary: ' + str(salary))
        print('')
        last_comma_count = 0
        for fighter in lineup:
            if last_comma_count < 5:
                text_file.write(fighter.id_num + ',')
            else:
                text_file.write(fighter.id_num)
            last_comma_count += 1
        text_file.write('\n')
        
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
    fighters = []
    file = open('data_final.csv', "rU")
    reader = csv.reader(file, delimiter=',')
    count = 0
    fight_num = 0
    for row in reader:
        if count < 1:
            pass
        else:
            name = row[2]
            id_num = row[3]
            salary = row[5]
            odds = 0
            fighters.append(Player(name, id_num, odds, salary, fight_num))
        count += 1
        
    for fighter in fighters:
        if fighter.name == 'Bryce Mitchell':
            fighter.fight_num = 7
            fighter.odds = 111
        elif fighter.name == 'Stephen Thompson':
            fighter.fight_num = 1
            fighter.odds = 108
        elif fighter.name == 'Marlon Vera':
            fighter.fight_num = 8
            fighter.odds = 89
        elif fighter.name == 'Chris Gutierrez':
            fighter.fight_num = 11
            fighter.odds = 80
        elif fighter.name == 'Maycee Barber':
            fighter.fight_num = 6
            fighter.odds = 71
        elif fighter.name == 'Justin Willis':
            fighter.fight_num = 2
            fighter.odds = 59
        elif fighter.name == 'Angela Hill':
            fighter.fight_num = 10
            fighter.odds = 44
        elif fighter.name == 'John Makdessi':
            fighter.fight_num = 3
            fighter.odds = 39
        elif fighter.name == 'Deiveson Figueiredo':
            fighter.fight_num = 4
            fighter.odds = 37
        elif fighter.name == 'Jussier Formiga':
            fighter.fight_num = 4
            fighter.odds = 33
            
    gen_best_lineup(fighters)

rotate_fades()
