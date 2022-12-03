def main():
    data = [x.strip() for x in open('data', 'r').readlines()]
    list_to_sum = []
    dupes_list = []
    for count, my_list in enumerate(data):
        half_length = len(my_list) // 2
        first_half, sec_half = my_list[:half_length], my_list[half_length:]
        dupes_list = list(set(first_half) & set(sec_half))
        [list_to_sum.append(ord(a) - 96) if (a.islower()) else list_to_sum.append(ord(a.lower()) - 96 + 26) for a in
         dupes_list]
    total = 0
    total = sum(list_to_sum, start=total)
    print(total)


if __name__ == '__main__':
    main()
