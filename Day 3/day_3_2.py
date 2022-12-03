def main():
    data = [x.strip() for x in open('data', 'r').readlines()]
    list_to_sum = []
    dupes_list = []
    for count, my_list in enumerate(data):
        if count % 3 == 0:
            dupes_list = list(set(data[count - 3]) & set(data[count - 2]) & set(data[count - 1]))[0]
            [list_to_sum.append(ord(a) - 96) if (a.islower()) else list_to_sum.append(ord(a.lower()) - 96 + 26) for a in
             dupes_list]
    total = 0
    total = sum(list_to_sum, start=total)
    print(total)


if __name__ == '__main__':
    main()
