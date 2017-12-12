import math

puzzle_input = 277678

if __name__ == '__main__':
    size = 100  # Use a matrix that is big enough
    matrix = [[0 for i in range(size)] for j in range(size)]
    center = [int(math.floor(size / 2)), int(math.floor(size / 2))]
    matrix[center[1]][center[0]] = 1

    current_size = 1

    nr = 1
    x = center[0] + 1
    y = center[1]

    matrix[y][x] = nr
    nr += 1

    directions = ['N', 'W', 'S', 'E']
    direction = 0
    while True:
        # Try turning left
        next_dir = directions[(direction + 1) % 4]
        if next_dir == 'N':
            next_cell = (x, y - 1)
        elif next_dir == 'W':
            next_cell = (x - 1, y)
        elif next_dir == 'S':
            next_cell = (x, y + 1)
        else:
            next_cell = (x + 1, y)

        if matrix[next_cell[1]][next_cell[0]] == 0:
            # Turning left is possible
            x = next_cell[0]
            y = next_cell[1]
            direction += 1
            direction %= 4
        else:
            # Cannot turn left, continue in current direction
            if directions[direction] == 'N':
                y -= 1
            elif directions[direction] == 'W':
                x -= 1
            elif directions[direction] == 'S':
                y += 1
            elif directions[direction] == 'E':
                x += 1

        # Get the total value of surrounding cells
        sum_cells = matrix[y - 1][x - 1] + \
                    matrix[y - 1][x] + \
                    matrix[y - 1][x + 1] + \
                    matrix[y][x - 1] + \
                    matrix[y][x + 1] + \
                    matrix[y + 1][x - 1] + \
                    matrix[y + 1][x] + \
                    matrix[y + 1][x + 1]

        matrix[y][x] = sum_cells
        nr += 1

        if sum_cells > puzzle_input:
            print('First number bigger than input = {}'.format(sum_cells))
            break
