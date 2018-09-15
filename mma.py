import csv
from itertools import combinations

f = open('DKSalaries.csv', 'rb')
reader = csv.reader(f)
data = []
for line in reader:
    name = line[2]
    cost = line[5]
    data.append((name,cost))
f.close()

# Remove title
data.pop(0)


my_combos = combinations(data, 6)

#134596 combos
#102617 combos under $50000
#13544 combos between $49500 and $50000
#4365 combos with 1 fighter choosen and 49.5-50k range
#917 combos chosen with 2 good fighters
count = 0
our_lineups = []
for item in my_combos:
    lineup_cost = 0
    fighter1 = False
    fighter2 = False
    fighter3 = False
    for fighter in item:
        if fighter[0] == 'Petr Yan':
            fighter1 = True
        if fighter[0] == 'Magomed Ankalaev':
            fighter2 = True
        if fighter[0] == 'Kajan Johnson':#'Jordan Johnson': #or fighter[0] == 'Aleksei Kunchenko':
            figther3 = True
        lineup_cost += int(fighter[1])
    if not (lineup_cost <= 50000 and lineup_cost >= 49000):
        continue
    if (fighter1 is False) or (fighter2 is False) or (fighter3 is False):
        continue
    
    our_lineups.append(item)
        
        

print(len(our_lineups))
