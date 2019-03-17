import csv
from itertools import combinations
import random
import itertools
import operator

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

def rotate_fades():
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
        
    for fighter in fighters:
        if fighter.name == 'Nathaniel Wood':
            fighter.fight_num = 4
            fighter.odds = -304
        elif fighter.name == 'Dominick Reyes':
            fighter.fight_num = 3
            fighter.odds = -241
        elif fighter.name == 'Darren Till':
            fighter.fight_num = 1
            fighter.odds = -228
        elif fighter.name == 'Joe Duffy':
            fighter.fight_num = 8
            fighter.odds = -192
        elif fighter.name == 'Nicolae Negumereanu':
            fighter.fight_num = 9
            fighter.odds = -161
        elif fighter.name == 'Nad Narimani':
            fighter.fight_num = 13
            fighter.odds = -146
        elif fighter.name == 'Jack Marshman':
            fighter.fight_num = 6
            fighter.odds = -147
        elif fighter.name == 'Arnold Allen':
            fighter.fight_num = 7
            fighter.odds = -143
        elif fighter.name == 'Claudio Silva':
            fighter.fight_num = 5
            fighter.odds = -150
        elif fighter.name == 'Molly McCann':
            fighter.fight_num = 12
            fighter.odds = -192
        elif fighter.name == 'Leon Edwards':
            fighter.fight_num = 2
            fighter.odds = -143
        elif fighter.name == 'Dan Ige':
            fighter.fight_num = 11
            fighter.odds = -137
        elif fighter.name == 'Danny Henry':
            fighter.fight_num = 11
            fighter.odds = 112
        elif fighter.name == 'Gunnar Nelson':
            fighter.fight_num = 2
            fighter.odds = 118
        elif fighter.name == 'Priscila Cachoeira':
            fighter.fight_num = 12
            fighter.odds = 160
        elif fighter.name == 'Danny Roberts':
            fighter.fight_num = 5
            fighter.odds = 124
        elif fighter.name == 'Jordan Rinaldi':
            fighter.fight_num = 7
            fighter.odds = 118
        elif fighter.name == 'John Phillips':
            fighter.fight_num = 6
            fighter.odds = 122
        elif fighter.name == 'Mike Grundy':
            fighter.fight_num = 13
            fighter.odds = 129
        elif fighter.name == 'Saparbeg Safarov':
            fighter.fight_num = 9
            fighter.odds = 134
        elif fighter.name == 'Marc Diakiese':
            fighter.fight_num = 8
            fighter.odds = 158
        elif fighter.name == 'Jorge Masvidal':
            fighter.fight_num = 1
            fighter.odds = 183
        elif fighter.name == 'Volkan Oezdemir':
            fighter.fight_num = 3
            fighter.odds = 194
        elif fighter.name == 'Jose Quinonez':
            fighter.fight_num = 4
            fighter.odds = 242

            
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
    text_file = open("wins_count.txt", "w")
    for f in fighters:
        text_file.write(f.name + ' ' + str(f.ranking) + '\n')
    text_file.close()

rotate_fades()
