def main():
    data = [x.strip() for x in open('data', 'r').readlines()]

    my_total = 0
    for play in data:
        op_play = play[0]
        my_play = play[2]

        match my_play:
            case "X":
                match op_play:
                    case "A":       my_play = "C"
                    case "B":       my_play = "A"
                    case "C":       my_play = "B"
            case "Y":       my_play = op_play
            case _:
                match op_play:
                    case "A":       my_play = "B"
                    case "B":       my_play = "C"
                    case "C":       my_play = "A"

        op_value = ord(op_play.lower()) - 96
        my_value = ord(my_play.lower()) - 96

        result_check = (my_value - op_value) % 3
        match result_check:
            case 0:     my_total += (3 + my_value)
            case 1:     my_total += (6 + my_value)
            case 2:     my_total += my_value

    print(my_total)


if __name__ == '__main__':
    main()
