import csv
from itertools import combinations
import random
import itertools
import operator
from operator import itemgetter

class Player():
    def __init__(self, name, id_num, win_odds, finish_odds, salary, fight_num, ranking):
        self.name = name
        self.id_num = id_num
        self.win_odds = int(win_odds)
        self.finish_odds = int(finish_odds)
        self.salary = int(salary)
        self.fight_num = int(fight_num)
        self.ranking = 0

    def __repr__(self):
        return 'Player(name=%s, id_num=%s, win_odds=%s, finish_odds=%s, salary=%s, fight_num=%s, ranking=%s)' % \
    (self.name, self.id_num, self.win_odds, self.finish_odds, self.salary, self.fight_num, self.ranking)

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

def set_odds():
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
            win_odds = 10000
            finish_odds = 10000
            count = 0
            fighters.append(Player(name, id_num, win_odds, finish_odds, salary, fight_num, count))
        count += 1

    for fighter in fighters:
        if fighter.name == 'Nathaniel Wood':
            fighter.fight_num = 4
            fighter.win_odds = -304
            fighter.finish_odds = 103
        elif fighter.name == 'Dominick Reyes':
            fighter.fight_num = 3
            fighter.win_odds = -241
            fighter.finish_odds = -125
        elif fighter.name == 'Darren Till':
            fighter.fight_num = 1
            fighter.win_odds = -228
            fighter.finish_odds = 188
        elif fighter.name == 'Joe Duffy':
            fighter.fight_num = 8
            fighter.win_odds = -192
            fighter.finish_odds = 150
        elif fighter.name == 'Nicolae Negumereanu':
            fighter.fight_num = 9
            fighter.win_odds = -161
            fighter.finish_odds = 100
        elif fighter.name == 'Nad Narimani':
            fighter.fight_num = 13
            fighter.win_odds = -146
            fighter.finish_odds = 430
        elif fighter.name == 'Jack Marshman':
            fighter.fight_num = 6
            fighter.win_odds = -147
            fighter.finish_odds = 179
        elif fighter.name == 'Arnold Allen':
            fighter.fight_num = 7
            fighter.win_odds = -143
            fighter.finish_odds = 280
        elif fighter.name == 'Claudio Silva':
            fighter.fight_num = 5
            fighter.win_odds = -150
            fighter.finish_odds = -110
        elif fighter.name == 'Molly McCann':
            fighter.fight_num = 12
            fighter.win_odds = -192
            fighter.finish_odds = 248
        elif fighter.name == 'Leon Edwards':
            fighter.fight_num = 2
            fighter.win_odds = -143
            fighter.finish_odds = 490
        elif fighter.name == 'Dan Ige':
            fighter.fight_num = 11
            fighter.win_odds = -137
            fighter.finish_odds = 295
        elif fighter.name == 'Danny Henry':
            fighter.fight_num = 11
            fighter.win_odds = 112
            fighter.finish_odds = 425
        elif fighter.name == 'Gunnar Nelson':
            fighter.fight_num = 2
            fighter.win_odds = 118
            fighter.finish_odds = 195
        elif fighter.name == 'Priscila Cachoeira':
            fighter.fight_num = 12
            fighter.win_odds = 160
            fighter.finish_odds = 400
        elif fighter.name == 'Danny Roberts':
            fighter.fight_num = 5
            fighter.win_odds = 124
            fighter.finish_odds = 335
        elif fighter.name == 'Jordan Rinaldi':
            fighter.fight_num = 7
            fighter.win_odds = 118
            fighter.finish_odds = 520
        elif fighter.name == 'John Phillips':
            fighter.fight_num = 6
            fighter.win_odds = 122
            fighter.finish_odds = 175
        elif fighter.name == 'Mike Grundy':
            fighter.fight_num = 13
            fighter.win_odds = 129
            fighter.finish_odds = 475
        elif fighter.name == 'Saparbeg Safarov':
            fighter.fight_num = 9
            fighter.win_odds = 124
            fighter.finish_odds = 195
        elif fighter.name == 'Marc Diakiese':
            fighter.fight_num = 8
            fighter.win_odds = 158
            fighter.finish_odds = 390
        elif fighter.name == 'Jorge Masvidal':
            fighter.fight_num = 1
            fighter.win_odds = 183
            fighter.finish_odds = 369
        elif fighter.name == 'Volkan Oezdemir':
            fighter.fight_num = 3
            fighter.win_odds = 194
            fighter.finish_odds = 385
        elif fighter.name == 'Jose Quinonez':
            fighter.fight_num = 4
            fighter.win_odds = 242
            fighter.finish_odds = 873
    return fighters

def run_sim():
    wins_table = [[9600, .80], [9500, .78], [9400, .76], [9300, .74], [9200, .72],
                  [9100, .70], [9000, .68], [8900, .66], [8800, .64], [8700, .62],
                  [8600, .60], [8500, .58], [8400, .56], [8300, .54], [8200, .52],
                  [8100, .50], [8000, .48], [7900, .46], [7800, .44], [7700, .42],
                  [7600, .40], [7500, .38], [7400, .36], [7300, .34], [7200, .32],
                  [7100, .30], [7000, .28], [6900, .26], [6800, .24], [6700, .22],
                  [6600, .20]]
    fins_table = [[9600, .80], [9500, .78], [9400, .76], [9300, .74], [9200, .72],
                  [9100, .70], [9000, .68], [8900, .66], [8800, .64], [8700, .62],
                  [8600, .60], [8500, .58], [8400, .56], [8300, .54], [8200, .52],
                  [8100, .50], [8000, .48], [7900, .46], [7800, .44], [7700, .42],
                  [7600, .40], [7500, .38], [7400, .36], [7300, .34], [7200, .32],
                  [7100, .30], [7000, .28], [6900, .26], [6800, .24], [6700, .22],
                  [6600, .20]]
    for field in fins_table:
        field[1] = field[1]/2
    fighters = set_odds()
    for fighter in fighters:
        percent_odds = round(convert_to_percent(fighter.win_odds),4)
        diff_points = 0
        for field in wins_table:
            if field[0] == fighter.salary:
                diff_points = round(percent_odds - field[1], 4)
                # convert to a point value
                diff_points *= 1000
                if diff_points < 0:
                    diff_points = 0
                break
        fighter.ranking += int(diff_points * 2)
        #print fighter.name, fighter.ranking
    for fighter in fighters:
        percent_odds = round(convert_to_percent(fighter.finish_odds),4)
        diff_points = 0
        for field in fins_table:
            if field[0] == fighter.salary:
                diff_points = round(percent_odds - field[1], 4)
                # convert to a point value
                diff_points *= 1000
                if diff_points < 0:
                    diff_points = 0
                break
        fighter.ranking += int(diff_points)
        #print fighter.name, fighter.ranking
    fighters.sort(key=lambda x: x.ranking, reverse=True)
    for fighter in fighters:
        print fighter.name, fighter.ranking


run_sim()
