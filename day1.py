if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        data = f.readline()

    count = len(data)
    sum_digits = 0
    for i in range(0, count):
        if data[i] == data[(i + 1) % count]:
            sum_digits += int(data[i])

    print('Total =', sum_digits)