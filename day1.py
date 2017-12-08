if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        data = f.readline()

    count = len(data)

    offsets = [1, int(count / 2)]

    for offset in offsets:
        sum_digits = 0
        for i in range(0, count):
            if data[i] == data[(i + offset) % count]:
                sum_digits += int(data[i])

        print('Total for offset {} = {}'.format(offset, sum_digits))
