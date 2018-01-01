import re

def get_puzzle_input():
    with open('./input/day13.txt') as f:
        content = f.read().strip()
    return content


class App:
    firewalls = {}
    position = 0
    end_position = None
    time = 0

    def move_scanners(self):
        for (fw_key, firewall) in self.firewalls.items():
            if firewall['scanner_pos'] == firewall['range'] - 1:
                firewall['direction'] = -1
            elif firewall['scanner_pos'] == 0:
                firewall['direction'] = 1
            firewall['scanner_pos'] = firewall['scanner_pos'] + firewall['direction']

    def calculate_severity(self):
        if self.is_caught():
            return self.position * self.firewalls[self.position]['range']
        return 0

    def is_caught(self):
        if self.position in self.firewalls:
            return self.firewalls[self.position]['scanner_pos'] == 0
        return False

    def run(self):
        regex = re.compile('(?P<depth>\d+): (?P<range>\d+)')
        layers = get_puzzle_input().split('\n')

        for layer in layers:
            matches = regex.match(layer)
            fw_depth = int(matches.group('depth'))
            fw_range = int(matches.group('range'))

            self.firewalls[fw_depth] = {
                'range': fw_range,
                'scanner_pos': 0,
                'direction': 1
            }

        self.end_position = max(x for x in self.firewalls.keys())

        total_severity = 0
        while self.position <= self.end_position:
            severity = self.calculate_severity()
            total_severity += severity
            self.move_scanners()
            self.position += 1

        print('Total severity = {}'.format(total_severity))

if __name__ == '__main__':
    App().run()
