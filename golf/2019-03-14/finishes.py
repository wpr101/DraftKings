import csv
from itertools import combinations
import random
import itertools
import os

class Player():
    def __init__(self, name, id_num, odds, salary):
        self.name = name
        self.id_num = id_num
        self.odds = int(odds)
        self.salary = int(salary)

    def __repr__(self):
        return 'Player(name=%s, id_num=%s, odds=%s, salary=%s)' % \
    (self.name, self.id_num, self.odds, self.salary)

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
    print('odds for all six: ' + str(round(calc_6_wins(in_list),10)))

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
        
        if total_score > best_score:
            real_lineups += 1

            best_score = total_score
            best_lineup = lineup
            #for player in best_lineup:
                #print player
            #print ''
    return best_lineup

def rotate_fades():
    # Generate initial lineup with no fades
    # Setup the data here
    fighters = []
    file = open('data.csv', "rU")
    reader = csv.reader(file, delimiter=',')
    count = 0
    for row in reader:
        if count < 8:
            pass
        else:
            name = row[9]
            id_num = row[10]
            salary = row[12]
            odds = 0
            fighters.append(Player(name, id_num, odds, salary))
        count += 1

    for fighter in fighters:
        if fighter.name == 'Dustin Johnson':
            fighter.odds = 1160
        elif fighter.name == 'Justin Thomas':
            fighter.odds = 1410
        elif fighter.name == 'Rory McIlroy':
            fighter.odds = 1230
        elif fighter.name == 'Justin Rose':
            fighter.odds = 2100
        elif fighter.name == 'Brooks Koepka':
            fighter.odds = 2030
        elif fighter.name == 'Rickie Fowler':
            fighter.odds = 2030
        elif fighter.name == 'Jon Rahm':
            fighter.odds = 2500
        elif fighter.name == 'Bryson DeChambeau':
            fighter.odds = 2800
        elif fighter.name == 'Sergio Garcia':
            fighter.odds = 3000
        elif fighter.name == 'Xander Schauffele':
            fighter.odds = 2800
        elif fighter.name == 'Tommy Fleetwood':
            fighter.odds = 2800
        elif fighter.name == 'Patrick Cantlay':
            fighter.odds = 3250
        elif fighter.name == 'Francesco Molinari':
            fighter.odds = 2230
        elif fighter.name == 'Webb Simpson':
            fighter.odds = 5000
        elif fighter.name == 'Tony Finau':
            fighter.odds = 5000
        elif fighter.name == 'Hideki Matsuyama':
            fighter.odds = 4000
        elif fighter.name == 'Adam Scott':
            fighter.odds = 3500
        elif fighter.name == 'Patrick Reed':
            fighter.odds = 6000
        elif fighter.name == 'Matt Kuchar':
            fighter.odds = 6000
        elif fighter.name == 'Paul Casey':
            fighter.odds = 3500
        elif fighter.name == 'Henrik Stenson':
            fighter.odds = 5000
        elif fighter.name == 'Ian Poulter':
            fighter.odds = 5500
        elif fighter.name == 'Cameron Smith':
            fighter.odds = 6600
        elif fighter.name == 'Marc Leishman':
            fighter.odds = 5500
        elif fighter.name == 'Gary Woodland':
            fighter.odds = 5500
        elif fighter.name == 'Billy Horschel':
            fighter.odds = 8000
        elif fighter.name == 'Rafael Cabrera-Bello':
            fighter.odds = 5000
        elif fighter.name == 'Keegan Bradley':
            fighter.odds = 7500
        elif fighter.name == 'Tyrrell Hatton':
            fighter.odds = 8000
        elif fighter.name == 'Bubba Watson':
            fighter.odds = 7000
        elif fighter.name == 'Charles Howell':
            fighter.odds = 8000
        elif fighter.name == 'Adam Hadwin':
            fighter.odds = 10000
        elif fighter.name == 'Lucas Glover':
            fighter.odds = 6600
        elif fighter.name == 'Kevin Kisner':
            fighter.odds = 10000
        elif fighter.name == 'Matthew Fitzpatrick':
            fighter.odds = 7500
        elif fighter.name == 'Sungjae Im':
            fighter.odds = 10000
        elif fighter.name == 'Byeong-Hun An':
            fighter.odds = 10000
        elif fighter.name == 'Keith Mitchell':
            fighter.odds = 10000
        elif fighter.name == 'Matt Wallace':
            fighter.odds = 8000
        elif fighter.name == 'Daniel Berger':
            fighter.odds = 10000
        elif fighter.name == 'Jason Kokrak':
            fighter.odds = 8000
        elif fighter.name == 'Bud Cauley':
            fighter.odds = 20000
        elif fighter.name == 'Patrick Rodgers':
            fighter.odds = 20000
        elif fighter.name == 'Ryan Palmer':
            fighter.odds = 12500
        elif fighter.name == 'Lucas Bjerregaard':
            fighter.odds = 20000
        elif fighter.name == 'Scott Piercy':
            fighter.odds = 20000
        elif fighter.name == 'Chris Kirk':
            fighter.odds = 20000
        elif fighter.name == 'Aaron Baddeley':
            fighter.odds = 20000
        elif fighter.name == 'Jhonattan Vegas':
            fighter.odds = 17500
        elif fighter.name == 'Sung Kang':
            fighter.odds = 15000

            
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

