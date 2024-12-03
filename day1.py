
## part 1
from collections import defaultdict


count = 0
with open('input1.txt', 'r') as f:
    list1, list2 = zip(*map(lambda s: s.strip().split('   '), f.readlines()))

    list1 = sorted(map(int, list1))
    list2 = sorted(map(int, list2))
    
    for i in range(len(list1)):
        count += abs(list1[i] - list2[i])


    print(count)


## part 2
count = 0
with open('input1.txt', 'r') as f:
    list1 = []
    list2_dic = defaultdict(int)

    for line in f:
        line = line.strip().split('   ')

        list2_dic[int(line[1])] += 1

        list1.append(int(line[0]))

    for num in list1:
        count += num * list2_dic[num]

print(f"Part 2: {count}")
