from itertools import combinations

fights = [0,1,2,3,4,5,6,7,8,9,10,11]

my_combos = combinations(fights, 6)
for lineup in my_combos:
    print(lineup)


