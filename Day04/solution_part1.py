def is_increasing_digits_sequence(number):
    sequence = list(map(int, str(number)))
    for n in sequence:
        for i in range(0, 5):
            if int(sequence[i+1]) < int(sequence[i]):
                return False
    return True


def is_equal_digits(number):
    sequence = list(map(int, str(number)))
    for n in sequence:
        for i in range(0, 5):
            if int(sequence[i + 1]) == int(sequence[i]):
                return True
    return False


with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split("-")
    numbers = [int(x) for x in numbers]
    list_numbers = list(range(numbers[0], numbers[1] + 1))
    print(len(list_numbers))
    print(list_numbers[0], list_numbers[len(list_numbers) - 1])
    result_n = 0
    for number in list_numbers:
        if is_increasing_digits_sequence(number) is True & is_equal_digits(number) is True:
            result_n += 1
    print(result_n)
