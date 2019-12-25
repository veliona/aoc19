with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split(",")
    numbers = [int(x) for x in numbers]

    def compute_values(numbers):
        for index in range(0, len(numbers), 4):
            if numbers[index] == 1:
                numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
            elif numbers[index] == 2:
                numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
            else:
                break
        return numbers[0]

    for noun in range(0, 99):
        for verb in range(0, 99):
            copy_numbers = numbers.copy()
            print(copy_numbers)
            copy_numbers[1] = noun
            copy_numbers[2] = verb
            if compute_values(copy_numbers) == 19690720:
                print(">>>>", 100 * noun + verb)
