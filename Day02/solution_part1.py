with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split(",")
    numbers = [int(x) for x in numbers]
    for index in range(0, len(numbers), 4):
        if numbers[index] == 1:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
        elif numbers[index] == 2:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
        else:
            break
    print(numbers)

