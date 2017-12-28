import re


def get_puzzle_input():
    with open('./input/day12.txt') as f:
        content = f.read().strip()
    return content


def is_linked(program_id, target_id, input_data, stack):
    if program_id == target_id:
        return True

    for linked_program_id in [x for x in input_data[program_id] if x not in stack]:
        stack.append(linked_program_id)
        if linked_program_id == program_id:
            continue
        if linked_program_id == target_id:
            return True
        else:
            if is_linked(linked_program_id, target_id, input_data, stack):
                return True

    return False

if __name__ == '__main__':
    regex = re.compile('(?P<program>\d+) <-> (?P<links>.*)')
    lines = get_puzzle_input().split('\n')
    programs = {}
    target_id = 0
    programs[target_id] = True

    input_data = {}

    for line in lines:
        matches = regex.match(line)

        program = int(matches.group('program'))
        links = [int(x) for x in matches.group('links').split(', ')]

        input_data[program] = links

    for program_id in input_data:
        stack = []
        programs[program_id] = is_linked(program_id, target_id, input_data, stack)

    print('There are {} programs in the group that contains program {}'.format(
        len([x for x in programs if programs[x] is True]),
        target_id
    ))
