import itertools
count = 0
for x in range(,6):
    for comb in itertools.combinations([1, 2, 3, 4, 5, 6], x):
        count += 1
        print comb
   
print(count)
