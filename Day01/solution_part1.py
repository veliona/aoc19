import math

with open('data.csv.txt') as data:
    numbers = [int(line.strip()) for line in data]
    results = []
    for number in numbers:
        result = math.floor(number / 3) - 2
        results.append(result)

    print(sum(results))
