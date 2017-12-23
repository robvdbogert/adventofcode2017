direction_map = {
        'ne': (1, -0.5),
        'se': (1, 0.5),
        's': (0, 1),
        'sw': (-1, 0.5),
        'nw': (-1, -0.5),
        'n': (0, -1)
    }


def get_puzzle_input():
    with open('./input/day11.txt') as f:
        content = f.read()
    return content.split(',')


if __name__ == '__main__':
    location = [0, 0]

    puzzle_input = get_puzzle_input()
    for instruction in puzzle_input:
        directions = direction_map[instruction]
        location[0] += directions[0]
        location[1] += directions[1]

    print('End location = {}'.format(location))

    x = 0
    y = 0
    steps = 0
    while x != location[0]:
        if location[0] < x:
            if location[1] < 0:
                # Move northwest
                x -= 1
                y -= 0.5
            elif location[1] > 0:
                # Move southwest
                x -= 1
                y += 0.5
        elif location[0] > x:
            if location[1] < 0:
                # Move northeast
                x += 1
                y -= 0.5
            elif location[1] > 0:
                # Move southeast
                x += 1
                y += 0.5
        steps += 1

    while y != location[1]:
        if location[1] < y:
            # Move north
            y -= 1
        elif location[1] > y:
            # Move south
            y += 1
        steps += 1

    print('Number of steps = {}'.format(steps))