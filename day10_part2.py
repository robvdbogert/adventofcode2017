numbers = list(range(256))
lengths = '70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41'
lengths = [ord(c) for c in lengths] + [17, 31, 73, 47, 23]

if __name__ == '__main__':
    cur_pos = 0
    skip_size = 0

    for current_round in range(0, 64):
        length_index = 0
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

    sparse_hash = [0 for i in range(0, 16)]
    for i in range(0, 256, 16):
        for j in range(i, i + 16):
            sparse_hash[int(i / 16)] ^= numbers[j]

    result = ''
    for nr in sparse_hash:
        result += '{0:#0{1}x}'.format(nr, 4)[2:]

    print('The resulting hash is: {}'.format(result))
