import csv
from itertools import combinations
import random



class Player():
    def __init__(self, name, odds, salary):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s)' % \
    (self.name, self.odds, self.salary)

def convert_to_percent(odds):
    percent = 1
    if odds < 0:
        percent *= float(odds) / float((odds - 100))
    else:
        percent *= float(100) / float((odds + 100))
    return (percent)

fighters = []
fighters.append(Player('Mcilroy', 655, 11400))
fighters.append(Player('Rose', 1010, 10700))
fighters.append(Player('Fowler', 1200, 10400)) 
fighters.append(Player('Koepka', 1025, 10200))
fighters.append(Player('Day', 1400, 9900))
fighters.append(Player('DeChambeau', 1600, 9700))
fighters.append(Player('Leishman', 2800, 9500)) 
fighters.append(Player('Matsuyama', 2800, 9300))
fighters.append(Player('Mickelson', 4000, 9300))
fighters.append(Player('Fleetwood', 3300, 9100))
fighters.append(Player('Molinari', 3300, 9000)) 
fighters.append(Player('Reed', 3500, 8900))
fighters.append(Player('Horschel', 5000, 8800))
fighters.append(Player('Hatton', 6000, 8700))
fighters.append(Player('Howell', 6000, 8600)) 
fighters.append(Player('Berger', 6000, 8500))
fighters.append(Player('Bradley', 5500, 8400))
fighters.append(Player('Kokrak', 6600, 8300))
fighters.append(Player('Glover', 5000, 8200)) 
fighters.append(Player('Stenson', 4000, 8100))
fighters.append(Player('Poulter', 5000, 8000))
fighters.append(Player('Watson', 5000, 8000))
fighters.append(Player('List', 7000, 7900)) 
fighters.append(Player('Oosthuizen', 5000, 7900))
fighters.append(Player('WooKim', 7000, 7800))
fighters.append(Player('Holmes', 7500, 7800))
fighters.append(Player('Hadwin', 7000, 7700)) 
fighters.append(Player('ZJohnson', 8500, 7700))
fighters.append(Player('MThompson', 7500, 7600))
fighters.append(Player('CChamp', 9000, 7600))
fighters.append(Player('KMitchell', 9000, 7500)) 
fighters.append(Player('BAn', 7500, 7500))
fighters.append(Player('CabreraBello', 6000, 7500))
fighters.append(Player('MattEvery', 10000, 7400))
fighters.append(Player('MWallace', 8000, 7400)) 
fighters.append(Player('TongLi', 7000, 7400))
fighters.append(Player('Schwartzel', 9000, 7400))
fighters.append(Player('Ancer', 12500, 7300))
fighters.append(Player('Fitzpatrick', 9000, 7300))
fighters.append(Player('Hossler', 12500, 7300)) 
fighters.append(Player('RyanMoore', 11000, 7300))
fighters.append(Player('SPiercy', 10000, 7300))
fighters.append(Player('CHadley', 17500, 7200))
fighters.append(Player('MKaymer', 15000, 7200)) 
fighters.append(Player('SStallings', 20000, 7200))
fighters.append(Player('KKisner', 9000, 7200))
fighters.append(Player('KevinNa', 11000, 7200))
fighters.append(Player('BSnedeker', 11000, 7200)) 
fighters.append(Player('KStanley', 20000, 7100))
fighters.append(Player('SStricker', 20000, 7100))
fighters.append(Player('ShaneLowry', 11000, 7100))
fighters.append(Player('Aphibarnrat', 10000, 7100))
fighters.append(Player('Poston', 14000, 7100)) 
fighters.append(Player('Olesen', 11000, 7100))
fighters.append(Player('Hoffman', 12500, 7000))
fighters.append(Player('Vegas', 15000, 7000))
fighters.append(Player('BrianGay', 16000, 7000))
fighters.append(Player('PatPerez', 20000, 7000)) 
fighters.append(Player('SungjaeIm', 11000, 7000))
fighters.append(Player('AaronWise', 12500, 7000))
fighters.append(Player('DWillett', 12500, 7000))
fighters.append(Player('ChrisKirk', 22500, 6900)) 
fighters.append(Player('HVarner', 15000, 6900))
fighters.append(Player('PRodgers', 12500, 6900))
fighters.append(Player('NLashley', 17500, 6900))
fighters.append(Player('JNiemann', 15000, 6900)) 
fighters.append(Player('HEnglish', 17500, 6900))
fighters.append(Player('GMcDowell', 12500, 6900)) 
fighters.append(Player('KStreelman', 22500, 6800))
fighters.append(Player('TalorGooch', 13500, 6800))
fighters.append(Player('BillHaas', 22500, 6800))
fighters.append(Player('Pepperell', 17500, 6800)) 
fighters.append(Player('CPan', 16000, 6800))
fighters.append(Player('SamRyder', 25000, 6700))
fighters.append(Player('SHorsfield', 20000, 6700))
fighters.append(Player('JDufner', 27500, 6700))
fighters.append(Player('AdamSchenk', 22500, 6700)) 
fighters.append(Player('MLaird', 17500, 6700))
fighters.append(Player('SungKang', 12500, 6700))
fighters.append(Player('SLangley', 25000, 6600))
fighters.append(Player('DannyLee', 17500, 6600)) 
fighters.append(Player('Baddeley', 17500, 6600))
fighters.append(Player('Spaun', 30000, 6600))
fighters.append(Player('Thornberry', 35000, 6600))
fighters.append(Player('ErnieEls', 20000, 6600)) 
fighters.append(Player('Swafford', 27500, 6500))
fighters.append(Player('DBozzeli', 30000, 6500))
fighters.append(Player('VTaylor', 20000, 6500))
fighters.append(Player('SSaunders', 25000, 6500))
fighters.append(Player('AustinCook', 17500, 6500)) 
fighters.append(Player('JWalker', 20000, 6500))


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
    
    '''found_player = False
    for p in lineup:
        if 'Poulter' in p.name:
            found_player = True
    if not found_player:
        continue
    found_player = False
    for p in lineup:
        if 'DeChambeau' in p.name:
            found_player = True
    if not found_player:
        continue'''
    
    if total_score > best_score:
        real_lineups += 1
        for player in lineup:
            print(player)
        print("salary", salary)
        print("percentage to win all fights:", round(total_score,15))
        print("")
        #best_score = five_wins_prob
        best_score = total_score

print("real_lineups", real_lineups)    
