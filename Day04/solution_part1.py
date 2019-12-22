def is_increasing_digits_sequence(list_numbers):
    increasing_list = []
    increasing_list_equal = []
    for number in list_numbers:
        sequence = list(map(int, str(number)))
        i = 0
        for n in sequence:
            n = int(n)
            for i in range(0, 4):
                i += 1
                if int(sequence[i+1]) < int(sequence[i]):
                    return False
                else:
                    return True
        increasing_list.append(number)
    print(increasing_list)
    for increasing_number in increasing_list:
        increasing_sequence = list(map(int, str(increasing_number)))
        i = 0
        for increasing_n in increasing_sequence:
            increasing_n = int(increasing_n)
            for i in range(len(increasing_sequence) - 2):
                i += 1
                if int(increasing_sequence[i]) == int(increasing_sequence[i+1]):
                    increasing_list_equal.append(increasing_number)
    print(len(increasing_list_equal))


with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split("-")
    numbers = [int(x) for x in numbers]
    list_numbers = list(range(numbers[0], numbers[1]))
    print(is_increasing_digits_sequence(list_numbers))
