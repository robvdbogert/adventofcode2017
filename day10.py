numbers = list(range(256))
lengths = [70, 66, 255, 2, 48, 0, 54, 48, 80, 141, 244, 254, 160, 108, 1, 41]

if __name__ == '__main__':
    length_index = 0
    cur_pos = 0
    skip_size = 0
    while length_index < len(lengths):
        length = lengths[length_index]

        nr_to_select_remaining = length
        start_pos = cur_pos
        selection = []
        while nr_to_select_remaining > 0:
            selection += numbers[start_pos:start_pos + nr_to_select_remaining]
            start_pos += len(selection)
            start_pos %= len(numbers)
            nr_to_select_remaining -= len(selection)

        reversed_selection = list(reversed(selection))

        for i in range(0, length):
            numbers[(cur_pos + i) % len(numbers)] = reversed_selection[i]

        length_index += 1

        cur_pos += length + skip_size
        cur_pos %= len(numbers)
        skip_size += 1

    print('Multiplying first two numbers {} * {} = {}'.format(numbers[0], numbers[1], numbers[0] * numbers[1]))
