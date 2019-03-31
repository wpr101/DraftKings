import csv
from itertools import combinations
import random
import itertools
import operator
from operator import itemgetter

class Player():
    def __init__(self, name, id_num, odds, salary, fight_num, ranking):
        self.name = name
        self.id_num = id_num
        self.odds = int(odds)
        self.salary = int(salary)
        self.fight_num = int(fight_num)
        self.ranking = 0

    def __repr__(self):
        return 'Player(name=%s, id_num=%s, odds=%s, salary=%s, fight_num=%s, ranking=%s)' % \
    (self.name, self.id_num, self.odds, self.salary, self.fight_num, self.ranking)

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
        #player.ranking += 1
        print player.name
        #salary += player.salary
    #print('salary: ' + str(salary))
    #print('odds for all six: ' + str(round(calc_6_wins(in_list),2)))

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
    for f in best_lineup:
        f.ranking += 1
    return best_lineup

def rotate_fades(wins_or_finishes):
    # Generate initial lineup with no fades
    fighters = []
    file = open('data.csv', "rU")
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
            count = 0
            fighters.append(Player(name, id_num, odds, salary, fight_num, count))
        count += 1

    if wins_or_finishes == 'wins':
        for fighter in fighters:
            if fighter.name == 'Stephen Thompson':
                fighter.fight_num = 1
                fighter.odds = -393
            elif fighter.name == 'Luis Pena':
                fighter.fight_num = 5
                fighter.odds = -258
            elif fighter.name == 'John Makdessi':
                fighter.fight_num = 3
                fighter.odds = -318
            elif fighter.name == 'Curtis Blaydes':
                fighter.fight_num = 2
                fighter.odds = -270
            elif fighter.name == 'Maycee Barber':
                fighter.fight_num = 6
                fighter.odds = -254
            elif fighter.name == 'Bobby Moffett':
                fighter.fight_num = 7
                fighter.odds = -160
            elif fighter.name == 'Eric Shelton':
                fighter.fight_num = 12
                fighter.odds = -162
            elif fighter.name == 'Alexis Davis':
                fighter.fight_num = 9
                fighter.odds = -145
            elif fighter.name == 'Deiveson Figueiredo':
                fighter.fight_num = 4
                fighter.odds = -144
            elif fighter.name == 'Marlon Vera':
                fighter.fight_num = 8
                fighter.odds = -163
            elif fighter.name == 'Chris Gutierrez':
                fighter.fight_num = 11
                fighter.odds = -231
            elif fighter.name == 'Angela Hill':
                fighter.fight_num = 10
                fighter.odds = -154
            elif fighter.name == 'Randa Markos':
                fighter.fight_num = 10
                fighter.odds = 127
            elif fighter.name == 'Ryan MacDonald':
                fighter.fight_num = 11
                fighter.odds = 187
            elif fighter.name == 'Frankie Saenz':
                fighter.fight_num = 8
                fighter.odds = 134
            elif fighter.name == 'Jussier Formiga':
                fighter.fight_num = 4
                fighter.odds = 118
            elif fighter.name == 'Jennifer Maia':
                fighter.fight_num = 9
                fighter.odds = 119
            elif fighter.name == 'Jordan Espinosa':
                fighter.fight_num = 12
                fighter.odds = 134
            elif fighter.name == 'Bryce Mitchell':
                fighter.fight_num = 7
                fighter.odds = 132
            elif fighter.name == 'JJ Aldrich':
                fighter.fight_num = 6
                fighter.odds = 202
            elif fighter.name == 'Justin Willis':
                fighter.fight_num = 2
                fighter.odds = 216
            elif fighter.name == 'Jesus Pinedo':
                fighter.fight_num = 3
                fighter.odds = 247
            elif fighter.name == 'Steven Peterson':
                fighter.fight_num = 5
                fighter.odds = 206
            elif fighter.name == 'Anthony Pettis':
                fighter.fight_num = 1
                fighter.odds = 303
                
    elif wins_or_finishes == 'finishes':
        for fighter in fighters:
            if fighter.name == 'Stephen Thompson':
                fighter.fight_num = 1
                fighter.odds = 100
            elif fighter.name == 'Luis Pena':
                fighter.fight_num = 5
                fighter.odds = 169
            elif fighter.name == 'John Makdessi':
                fighter.fight_num = 3
                fighter.odds = 202
            elif fighter.name == 'Curtis Blaydes':
                fighter.fight_num = 2
                fighter.odds = 161
            elif fighter.name == 'Maycee Barber':
                fighter.fight_num = 6
                fighter.odds = 100
            elif fighter.name == 'Bobby Moffett':
                fighter.fight_num = 7
                fighter.odds = 210
            elif fighter.name == 'Eric Shelton':
                fighter.fight_num = 12
                fighter.odds = 475
            elif fighter.name == 'Alexis Davis':
                fighter.fight_num = 9
                fighter.odds = 500
            elif fighter.name == 'Deiveson Figueiredo':
                fighter.fight_num = 4
                fighter.odds = 145
            elif fighter.name == 'Marlon Vera':
                fighter.fight_num = 8
                fighter.odds = 175
            elif fighter.name == 'Chris Gutierrez':
                fighter.fight_num = 11
                fighter.odds = 137
            elif fighter.name == 'Angela Hill':
                fighter.fight_num = 10
                fighter.odds = 604
            elif fighter.name == 'Randa Markos':
                fighter.fight_num = 10
                fighter.odds = 620
            elif fighter.name == 'Ryan MacDonald':
                fighter.fight_num = 11
                fighter.odds = 415
            elif fighter.name == 'Frankie Saenz':
                fighter.fight_num = 8
                fighter.odds = 625
            elif fighter.name == 'Jussier Formiga':
                fighter.fight_num = 4
                fighter.odds = 400
            elif fighter.name == 'Jennifer Maia':
                fighter.fight_num = 9
                fighter.odds = 575
            elif fighter.name == 'Jordan Espinosa':
                fighter.fight_num = 12
                fighter.odds = 382
            elif fighter.name == 'Bryce Mitchell':
                fighter.fight_num = 7
                fighter.odds = 330
            elif fighter.name == 'JJ Aldrich':
                fighter.fight_num = 6
                fighter.odds = 850
            elif fighter.name == 'Justin Willis':
                fighter.fight_num = 2
                fighter.odds = 367
            elif fighter.name == 'Jesus Pinedo':
                fighter.fight_num = 3
                fighter.odds = 460
            elif fighter.name == 'Steven Peterson':
                fighter.fight_num = 5
                fighter.odds = 470
            elif fighter.name == 'Anthony Pettis':
                fighter.fight_num = 1
                fighter.odds = 425
            
    current_best = gen_best_lineup(fighters)
    #print_player_only(current_best)
    #print('')
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
            #print str(global_counter) + ')'
            gen_best_lineup(temp_players)
            #print('')
            global_counter += 1
            fades=[]
    fighters.sort(key=operator.attrgetter('ranking'))
    fighters = fighters[::-1]
    if wins_or_finishes == 'wins':
        text_file = open("wins_count.txt", "w")
    elif wins_or_finishes == 'finishes':
        text_file = open("finishes_count.txt", "w")
    for f in fighters:
        text_file.write(f.name + ' ' + str(f.ranking) + '\n')
    text_file.close()

def combine_counts():
    rotate_fades('wins')
    rotate_fades('finishes')

    w_list = []
    for line in open('wins_count.txt', 'r'):
        line = line.split()
        w_list.append(line)

    f_list = []
    for line in open('finishes_count.txt', 'r'):
        line = line.split()
        f_list.append(line)

    combined_counts = []
    for w in w_list:
        for f in f_list:
            if w[0] + w[1] == f[0] + f[1]:
                total_count = int(w[2]) + int(f[2])
                combined_counts.append([w[0] + ' ' +  w[1], total_count])

    text_file = open("combined_count.txt", "w")
    combined_counts = sorted(combined_counts, key=itemgetter(1), reverse=True)
    for f in combined_counts:
        print str(f[0]) + ' ' + str(f[1])
        text_file.write(str(f[0]) + ' ' + str(f[1]) + '\n')
    text_file.close()

def create_data_final_csv():
    MIN_RANKING = 33
    text_file = open("data_final.csv", "w")
    text_file.write('Position,Name + ID,Name,ID,Roster Position,Salary,Game Info,TeamAbbrev,AvgPointsPerGame')
    text_file.write('\n')
    
    for line in open('combined_count.txt', 'r'):
        line = line.split()
        name = line[0] + ' ' + line[1]
        ranking = int(line[2])
        #print name, ranking
        if ranking >= MIN_RANKING:
            file = open('data.csv', "rU")
            reader = csv.reader(file, delimiter=',')
            count = 0
            for row in reader:
                if count > 1:
                    if row[2] == name:
                        #text_file.write(str(row) + '\n')
                        temp_count = 0
                        for i in row:
                            if temp_count < 8:
                                text_file.write(i + ',')
                            else:
                                text_file.write(i)
                            temp_count += 1
                        text_file.write('\n')
                count += 1
    text_file.close()

combine_counts()
create_data_final_csv()
