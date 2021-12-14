# Advent of code 2021 - day 14
from pathlib import Path
from collections import defaultdict


def get_input():
    input_file = Path(__file__).parent.joinpath('input.txt')
    with open(input_file, 'r') as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


if __name__ == '__main__':
    input_data = get_input()

    rules = {}
    for line in input_data[2:]:
        split = line.split(' -> ')
        rules[split[0]] = split[1]

    value = input_data[0]
    for _ in range(40):
        next_value = value[0]
        for i in range(len(value) - 1):
            pair = value[i:i + 2]
            next_value += rules[pair]
            next_value += pair[1]
        value = next_value

    count = defaultdict(int)
    for c in value:
        count[c] += 1
    most = max(count, key=count.get)
    least = min(count, key=count.get)
    print(count[most] - count[least])

