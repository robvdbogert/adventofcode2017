def get_new_value_part_1(value, offset):
    return value + 1


def get_new_value_part_2(value, offset):
    if offset >= 3:
        return value - 1
    return value + 1

calculations = [get_new_value_part_1, get_new_value_part_2]

if __name__ == '__main__':
    for calculation in calculations:
        puzzle_input = []
        with open('./input/day5.txt') as f:
            for line in f:
                puzzle_input.append(int(line))

        idx = 0
        step = 0
        exit_found = False
        while not exit_found:
            offset = puzzle_input[idx]
            puzzle_input[idx] = calculation(puzzle_input[idx], offset)
            idx += offset
            step += 1

            if idx < 0 or idx >= len(puzzle_input):
                print('Done in {} steps using method {}'.format(step, calculation))
                exit_found = True
