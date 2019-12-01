import math


def fuel_for_value(value):
    return value // 3 - 2


with open('data.txt') as data:
    modules = [int(line.strip()) for line in data]
    total_fuel = 0
    for module_mass in modules:
        fuel_for_module = fuel_for_value(module_mass)
        total_fuel_for_module = 0
        while fuel_for_module > 0:
            total_fuel_for_module += fuel_for_module
            fuel_for_module = fuel_for_value(fuel_for_module)
        total_fuel = total_fuel + total_fuel_for_module
    print(total_fuel)
