from operator import itemgetter
w_list = []
for line in open('wins_count.txt', 'r'):
    line = line.split()
    w_list.append(line)

f_list = []
for line in open('finishes_count.txt', 'r'):
    line = line.split()
    f_list.append(line)

print w_list

combined_counts = []
for w in w_list:
    for f in f_list:
        print w
        print f
        if w[0] + w[1] == f[0] + f[1]:
            total_count = int(w[2]) + int(f[2])
            combined_counts.append([w[0] + w[1], total_count])

combined_counts = sorted(combined_counts, key=itemgetter(1), reverse=True)
for f in combined_counts:
    print f
