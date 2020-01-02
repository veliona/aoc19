import math

with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split(",")
    numbers = [int(x) for x in numbers]
    input = 1
    for index in range(0, len(numbers), 4):
        opcode = numbers[index]
        first_num = opcode % 100
        second_num = math.floor(opcode % 1000 / 100)
        third_num = math.floor(opcode % 10000 / 1000)
        fourt_num = math.floor(opcode / 10000)

        
        if opcode == 1:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]

        if opcode == 2:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]

        if opcode == 3:
            numbers[numbers[index + 1]] = input

        if opcode == 4:
            numbers[numbers[index + 1]] = output
    print(numbers)
