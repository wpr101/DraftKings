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
good_ones = ['Petr Yan', 'Magomed Ankalaev', 'Aleksei Kunchenko', 'Jordan Johnson' ]
bad_ones = ['Jin Soo Son', 'Thiago Alves', 'Marcin Prachnio', 'Terrion Ware', 'Kajan Johnson', 'Stefan Sekulic', 'Desmond Green']

for item in my_combos:
    lineup_cost = 0
    good_count = 0
    bad_count = 0
    for fighter in item:
        if fighter[0] in good_ones:
            good_count += 1
        if fighter[0] in bad_ones:
            bad_count += 1
        lineup_cost += int(fighter[1])
    if not (lineup_cost <= 50000 and lineup_cost >= 49500):
        continue
    if good_count < 3:
        continue
    if bad_count > 0:
        continue
    
    our_lineups.append(item)
        
print(len(our_lineups))
for lineup in our_lineups:
    print(lineup)
    print('')
