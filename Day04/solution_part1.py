def is_increasing_digits_sequence(number):
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


def is_equal_digits(number):
    sequence = list(map(int, str(number)))
    i = 0
    for n in sequence:
        n = int(n)
        for i in range(0, 4):
            i += 1
            if int(sequence[i + 1]) == int(sequence[i]):
                return True
            else:
                return False


with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split("-")
    numbers = [int(x) for x in numbers]
    list_numbers = list(range(numbers[0], numbers[1] + 1))
    print(len(list_numbers))
    result_n = 0
    for number in list_numbers:
        if is_increasing_digits_sequence(number) is True & is_equal_digits(number) is True:
            result_n += 1
    print(result_n)

