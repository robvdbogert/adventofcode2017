if __name__ == '__main__':
    input = []
    with open('./input/day2.txt') as f:
        for line in f:
            row_data = list(map(int, line.split(',')))
            input.append(row_data)

    # Part 1
    checksum = 0
    for row in input:
        checksum += max(row) - min(row)

    print('Part I: checksum = {}'.format(checksum))

    # Part 2
    checksum = 0
    for row in input:
        items = sorted(row)
        for i in range(len(items) - 1, 0, -1):
            for i2 in range(0, i):
                if items[i] % items[i2] == 0:
                    checksum += items[i] / items[i2]

    print('Part II: checksum = {}'.format(checksum))
