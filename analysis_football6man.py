import csv
from itertools import combinations

f = open('./data/contest-standings-football9-16.csv', 'rb')
reader = csv.reader(f)
data = []
seen = []
for line in reader:
    name = line[2]
    if 'rayofhope' in name:
        lineup = line[5]
        print(lineup)
        print('')
