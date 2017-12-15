import collections
import re

class Node:
    def __init__(self, parent, name, weight):
        self.name = name
        self.children = []
        self.parent = parent
        self.weight = weight

    def __repr__(self):
        return self.name + ' ' + str(self.children)


def get_program(node, name):
    if node.name == name:
        return node
    elif len(node.children) > 0:
        for child in node.children:
            result = get_program(child, name)
            if result is not None:
                return result
    return None


def get_puzzle_input():
    with open('./input/day7.txt') as f:
        content = f.readlines()

    return content


def get_weight(node):
    weight = node.weight
    for child_node in node.children:
        weight += get_weight(child_node)
    return weight


def verify_weights(node):
    child_weights = {}
    for child in node.children:
        child_weights[child.name] = get_weight(child)
        verify_weights(child)

    weights = [v for (k,v) in child_weights.items()]
    if len(weights) > 0:
        counter = collections.Counter(weights)
        if len(counter) > 1:
            wrong_weight = next(iter([k for (k, v) in counter.items() if v == 1]))
            correct__weight = next(iter(k for (k, v) in counter.items() if v > 1))
            wrong_child_weight = next(child.weight for child in node.children if get_weight(child) == wrong_weight)
            offset = wrong_weight - correct__weight
            print('The weight {} is incorrect. It should be {}.'.format(
                wrong_child_weight, wrong_child_weight - offset))

if __name__ == '__main__':
    regex = re.compile("(?P<name>[a-z]+) \((?P<weight>\d+)\)(?: -> (?P<children>.*))?")
    lines = [x.strip() for x in get_puzzle_input()]
    programs = {}
    weights = {}
    for line in lines:
        m = regex.match(line)
        name = m.group('name')
        weight = int(m.group('weight'))
        children = m.group('children')
        children = children.split(', ') if children is not None else []

        programs[name] = children
        weights[name] = weight

    tree = Node(None, '', None)
    for program_name in programs:
        # Check if the program is in the tree already
        node = get_program(tree, program_name)
        if node is None:
            node = Node(tree, program_name, weights[program_name])
            tree.children.append(node)

        children = programs[program_name]
        for child in children:
            # Is the child node in the tree already? If so move it now.
            child_node = get_program(tree, child)
            if child_node is None:
                child_node = Node(node, child, weights[child])
                node.children.append(child_node)
            else:
                child_node.parent.children.remove(child_node)
                child_node.parent = node
                node.children.append(child_node)

    print('The bottom program is {}'.format(tree.children[0].name))

    # Part 2: check weights
    verify_weights(tree)
