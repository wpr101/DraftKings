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
            if fighter.name == 'Ray Borg':
                fighter.fight_num = 11
                fighter.win_odds = -265
                fighter.finish_odds = 259
            if fighter.name == 'Desmond Green':
                fighter.fight_num = 8
                fighter.win_odds = -449
                fighter.finish_odds = 467
            elif fighter.name == 'Alex Perez':
                fighter.fight_num = 13
                fighter.win_odds = -338
                fighter.finish_odds = 150
            elif fighter.name == 'Marina Rodriguez':
                fighter.fight_num = 7
                fighter.win_odds = -337
                fighter.finish_odds = 415
            elif fighter.name == 'Kennedy Nzechukwu':
                fighter.fight_num = 5
                fighter.win_odds = -169
                fighter.finish_odds = 119
            elif fighter.name == 'Kevin Holland':
                fighter.fight_num = 10
                fighter.win_odds = -193
                fighter.finish_odds = 165
            elif fighter.name == 'Sabina Mazo':
                fighter.fight_num = 12
                fighter.win_odds = -152
                fighter.finish_odds = 616
            elif fighter.name == 'Sodiq Yusuff':
                fighter.fight_num = 6
                fighter.win_odds = -144
                fighter.finish_odds = 210
            elif fighter.name == 'Karolina Kowalkiewicz':
                fighter.fight_num = 4
                fighter.win_odds = -147
                fighter.finish_odds = 870
            elif fighter.name == 'Edson Barboza':
                fighter.fight_num = 1
                fighter.win_odds = -132
                fighter.finish_odds = 120
            elif fighter.name == 'Michael Johnson':
                fighter.fight_num = 3
                fighter.win_odds = -121
                fighter.finish_odds = 255
            elif fighter.name == 'Jack Hermansson':
                fighter.fight_num = 2
                fighter.win_odds = -125
                fighter.finish_odds = 148
            elif fighter.name == 'Enrique Barzola':
                fighter.fight_num = 9
                fighter.win_odds = -127
                fighter.finish_odds = 745
            elif fighter.name == 'Kevin Aguilar':
                fighter.fight_num = 9
                fighter.win_odds = 104
                fighter.finish_odds = 320
            elif fighter.name == 'David Branch':
                fighter.fight_num = 2
                fighter.win_odds = 106
                fighter.finish_odds = 280
            elif fighter.name == 'Josh Emmett':
                fighter.fight_num = 3
                fighter.win_odds = -102
                fighter.finish_odds = 300
            elif fighter.name == 'Justin Gaethje':
                fighter.fight_num = 1
                fighter.win_odds = 108
                fighter.finish_odds = 145
            elif fighter.name == 'Michelle Waterson':
                fighter.fight_num = 4
                fighter.win_odds = 122
                fighter.finish_odds = 440
            elif fighter.name == 'Sheymon Moraes':
                fighter.fight_num = 6
                fighter.win_odds = 119
                fighter.finish_odds = 275
            elif fighter.name == 'Maryna Moroz':
                fighter.fight_num = 12
                fighter.win_odds = 127
                fighter.finish_odds = 520
            elif fighter.name == 'Gerald Meerschaert':
                fighter.fight_num = 10
                fighter.win_odds = 161
                fighter.finish_odds = 240
            elif fighter.name == 'Paul Craig':
                fighter.fight_num = 5
                fighter.win_odds = 142
                fighter.finish_odds = 242
            elif fighter.name == 'Jessica Aguilar':
                fighter.fight_num = 7
                fighter.win_odds = 263
                fighter.finish_odds = 850
            elif fighter.name == 'Mark DeLaRosa':
                fighter.fight_num = 13
                fighter.win_odds = 263
                fighter.finish_odds = 604
            elif fighter.name == 'Ross Pearson':
                fighter.fight_num = 8
                fighter.win_odds = 339
                fighter.finish_odds = 730
            elif fighter.name == 'Casey Kenney':
                fighter.fight_num = 11
                fighter.win_odds = 214
                fighter.finish_odds = 655
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
        fighter.ranking += int(diff_points)
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
        fighter.ranking += int(diff_points) / 2
        #print fighter.name, fighter.ranking
    fighters.sort(key=lambda x: x.ranking, reverse=True)
    for fighter in fighters:
        print fighter.name, fighter.ranking


run_sim()
