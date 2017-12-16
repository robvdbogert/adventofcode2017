import operator
import re

def get_puzzle_input():
    with open('./input/day8.txt') as f:
        content = f.readlines()
    return content


if __name__ == '__main__':
    instructions = get_puzzle_input()

    regex = re.compile(
        "(?P<target>[a-z]+) (?P<instruction>inc|dec) (?P<change>-?\d+) if (?P<source>[a-z]+) (?P<comparison>[<>=!]+) (?P<value>-?\d+)")

    registers = {}
    maximum = 0
    for instruction in instructions:
        matches = regex.match(instruction)

        target = matches.group('target')
        if target not in registers:
            registers[target] = 0

        # Is the condition fulfilled?
        source = matches.group('source')
        if source not in registers:
            registers[source] = 0

        instruction = matches.group('instruction')
        change = int(matches.group('change'))
        expr = '{} {} {}'.format(registers[source], matches.group('comparison'), matches.group('value'))
        if eval(expr):
            if instruction == 'inc':
                registers[target] += change
            else:
                registers[target] -= change

        if registers[target] > maximum:
            maximum = registers[target]

    print(registers)
    sorted_registers = sorted(registers.items(), key=operator.itemgetter(1), reverse=True)
    result = next(item for item in sorted_registers)
    print('Register {} has highest value {}'.format(result[0], result[1]))

    print('Maximum in any register ever was {}'.format(maximum))
