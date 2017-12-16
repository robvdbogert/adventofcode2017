def get_puzzle_input():
    with open('./input/day9.txt') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    puzzle_input = get_puzzle_input()

    i = 0
    group_level = 0
    garbage = False
    ignore_next = False
    score = 0
    nr_garbage_chars = 0
    while i < len(puzzle_input):
        if ignore_next:
            print('Ignoring {}'.format(puzzle_input[i]))
            ignore_next = False
            i += 1
            continue
        else:
            print('Processing {}'.format(puzzle_input[i]))

        c = puzzle_input[i]

        if c == '{':
            if not garbage:
                print('start group at level {}'.format(group_level))
                group_level += 1
                score += group_level
            else:
                nr_garbage_chars += 1
        elif c == '}':
            if not garbage:
                group_level -= 1
                print('end group at level {}'.format(group_level))
            else:
                nr_garbage_chars += 1
        elif c == '<':
            if not garbage:
                print('start garbage')
                garbage = True
            else:
                nr_garbage_chars += 1
        elif c == '>':
            if garbage:
                print('end garbage')
                garbage = False
        elif c == '!':
            ignore_next = True
        elif garbage:
            nr_garbage_chars += 1

        i += 1

    print('Score = {}'.format(score))
    print('Number of garbage characters = {}'.format(nr_garbage_chars))
