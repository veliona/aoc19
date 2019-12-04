def create_list_of_positions(wire):
    wire = wire.split(",")
    positions = dict()
    total_steps = 0
    x = 0
    y = 0
    for move in wire:
        direction = move[0]
        steps = int(move[1:])
        if direction == 'R':
            for i in range(0, steps):
                x += 1
                total_steps += 1
                positions[(x,y)] = total_steps
        elif direction == 'L':
            for i in range(0, steps):
                x -= 1
                total_steps += 1
                positions[(x,y)] = total_steps
        elif direction == 'U':
            for i in range(0, steps):
                y += 1
                total_steps += 1
                positions[(x,y)] = total_steps
        else:
            for i in range(0, steps):
                y -= 1
                total_steps += 1
                positions[(x,y)] = total_steps
    return positions


with open(f'data.txt') as f:
    content = f.readlines()
    wires = [line.strip() for line in content]
    first_list_positions = set(create_list_of_positions(wires[0]).keys())
    second_list_positions = set(create_list_of_positions(wires[1]).keys())
    first_length = create_list_of_positions(wires[0]).values()
    second_length = create_list_of_positions(wires[1]).values()
    intersections_distance = []
    intersections = first_list_positions.intersection(second_list_positions)
    for intersection in intersections:
        intersections_distance.append(create_list_of_positions(wires[0]).get(intersection)
                                      + create_list_of_positions(wires[1]).get(intersection))
    print(min(intersections_distance))
