import math
puzzle_input = 277678

if __name__ == '__main__':
    size = math.ceil(math.sqrt(puzzle_input))
    if size % 2 == 0:
        size += 1

    size -= 2
    print('size = {}'.format(size))

    pos = [math.floor(size / 2) + 1, math.floor(size / 2)]
    print('start point = {}'.format(pos))

    current = size * size + 1
    print('start number = {}'.format(current))

    upper_right = current + size
    upper_left = upper_right + size + 1
    lower_left = upper_left + size + 1
    lower_right = lower_left + size + 1

    input_pos = None
    pos_limit = math.floor(size / 2 + 1)
    if puzzle_input < upper_right:
        print('on right side')
        input_pos = [pos[0], pos[1] - (puzzle_input - current)]
    elif puzzle_input < upper_left:
        print('on upper side')
        input_pos = [pos_limit - (puzzle_input - upper_right),
                    0 - pos_limit]
    elif puzzle_input < lower_left:
        print('on left side')
        input_pos = [0 - pos_limit,
                     0 - pos_limit + (puzzle_input - upper_left)]
    elif puzzle_input <= lower_right:
        print('on lower side')
        input_pos = [0 - pos_limit + (puzzle_input - lower_left),
                     pos_limit]
    else:
        print('not found!')

    if input_pos is not None:
        print('at pos {}'.format(input_pos))
        print('steps from center: {}'.format(abs(input_pos[0]) + abs(input_pos[1])))