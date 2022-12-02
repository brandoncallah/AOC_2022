from itertools import groupby

with open('data', 'r') as calorie_file:
    cal_list = calorie_file.readlines()
    calorie_file.close()

stripped_list = [x.strip() for x in cal_list]
split_list = [list(sub) for ele, sub in groupby(stripped_list, key=bool) if ele]
total_list = []

for my_list in split_list:
    total = 0
    for x in my_list:
        total += int(x)
    total_list.append(total)

sorted_list = sorted(total_list)
three_total = 0
for y in sorted_list[-3:]:
    print(y)
    three_total += y
print(three_total)
