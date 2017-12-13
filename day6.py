if __name__ == '__main__':
    puzzle_input = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
    size = len(puzzle_input)

    visited_states = {
        (''.join(str(x) for x in puzzle_input)): 0
    }

    done = False
    cycles = 0
    while not done:
        cycles += 1
        highest = max(puzzle_input)
        idx = puzzle_input.index(highest)
        puzzle_input[idx] = 0

        blocks_to_redistribute = highest
        while blocks_to_redistribute > 0:
            idx = (idx + 1) % size
            puzzle_input[idx] += 1
            blocks_to_redistribute -= 1

        # Have we visited the current state before?
        state = ''.join(str(x) for x in puzzle_input)
        if state in visited_states:
            done = True
            print('Done in {} cycles, state {} revisited after {} cycles'.format(
                cycles, state, cycles - visited_states[state]))
        else:
            visited_states[state] = cycles

    print(visited_states)
