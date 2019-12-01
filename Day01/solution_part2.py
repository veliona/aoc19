import math

with open('data.txt') as data:
    numbers = [int(line.strip()) for line in data]
    basic_fuel_results = []
    sum_fuel = 0
    for number in numbers:
        basic_fuel = math.floor(number / 3) - 2
        basic_fuel_results.append(basic_fuel)
    for basic_fuel_value in basic_fuel_results:
        module_fuel_sum = 0
        value = math.floor(basic_fuel_value / 3) - 2
        while value > 0:
            module_fuel_sum += value
            value = math.floor(value / 3) - 2
        sum_fuel = sum_fuel + basic_fuel_value + module_fuel_sum

    print(sum_fuel)