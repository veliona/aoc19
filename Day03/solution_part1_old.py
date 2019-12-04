with open(f'data.txt') as f:
    content = f.readlines()
    wires = [line.strip() for line in content]
    first_wire = wires[0]
    second_wire = wires[1]
    print('first line', first_wire)
    first_wire = first_wire.split(",")
    second_wire = second_wire.split(",")
    print('first line after splitting', first_wire)
    position_first_wire = [0, 0]
    position_second_wire = [0, 0]
    list_position_first = []
    list_position_second = []
    for move_first_wire in first_wire:
        direction_first_wire = move_first_wire[0]
        steps_first_wire = int(move_first_wire[1:])
        if direction_first_wire == 'R':
            position_first_wire[0] += steps_first_wire
            list_position_first.append(position_first_wire.copy())
        elif direction_first_wire == 'L':
            position_first_wire[0] -= steps_first_wire
            list_position_first.append(position_first_wire.copy())
        elif direction_first_wire == 'U':
            position_first_wire[1] += steps_first_wire
            list_position_first.append(position_first_wire.copy())
        else:
            position_first_wire[1] -= steps_first_wire
            list_position_first.append(position_first_wire.copy())
    print(list_position_first)
    position_second_wire = [0, 0]
    list_position_second = []
    for move_second_wire in second_wire:
        direction_second_wire = move_second_wire[0]
        steps_second_wire = int(move_second_wire[1:])
        if direction_second_wire == 'R':
            position_second_wire[0] += steps_second_wire
            list_position_second.append(position_second_wire.copy())
        elif direction_second_wire == 'L':
            position_second_wire[0] -= steps_second_wire
            list_position_second.append(position_second_wire.copy())
        elif direction_second_wire == 'U':
            position_second_wire[1] += steps_second_wire
            list_position_second.append(position_second_wire.copy())
        else:
            position_second_wire[1] -= steps_second_wire
            list_position_second.append(position_second_wire.copy())
    print(list_position_second)

    # for each_move in moves:
    #   direction = each_move[0]
    #   steps = each_move[1:]
    #   print(direction, steps)

    # position = [0,0]
    # for each_move in moves:
    #    if each_move.startswith('R'):
    #        position = []