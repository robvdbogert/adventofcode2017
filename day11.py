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


class DistanceCalculator:
    def get_distance(self, point):
        x = 0
        y = 0
        steps = 0
        while x != point[0]:
            if point[0] < x:
                if point[1] < 0:
                    # Move northwest
                    x -= 1
                    y -= 0.5
                elif point[1] > 0:
                    # Move southwest
                    x -= 1
                    y += 0.5
                else:
                    # Move west
                    x -= 1
            elif point[0] > x:
                if point[1] < 0:
                    # Move northeast
                    x += 1
                    y -= 0.5
                elif point[1] > 0:
                    # Move southeast
                    x += 1
                    y += 0.5
                else:
                    # Move east
                    x += 1
            steps += 1

        while y != point[1]:
            if point[1] < y:
                # Move north
                y -= 1
            elif point[1] > y:
                # Move south
                y += 1
            steps += 1

        return steps


if __name__ == '__main__':
    location = [0, 0]

    puzzle_input = get_puzzle_input()
    calculator = DistanceCalculator()
    max_steps_from_start = 0
    steps_from_start = 0
    for instruction in puzzle_input:
        directions = direction_map[instruction]
        location[0] += directions[0]
        location[1] += directions[1]
        steps_from_start = calculator.get_distance(location)
        if steps_from_start > max_steps_from_start:
            max_steps_from_start = steps_from_start

    print('End location = {}'.format(location))
    print('Number of steps = {}'.format(steps_from_start))
    print('Furthest from start = {}'.format(max_steps_from_start))