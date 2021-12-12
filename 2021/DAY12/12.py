# Advent of code 2021 - day 12
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath('input.txt')
    with open(input_file, 'r') as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def part1_count_paths(edges, visited, current):
    if current == 'end':
        return 1
    if current.islower() and current in visited:
        return 0

    path_count = 0
    for edge in edges:
        if edge[0] == current and current != edge[1]:
            visited.append(current)
            path_count += part1_count_paths(edges, visited.copy(), edge[1])

    return path_count


def part2_count_paths(edges, visited, current, twice_small=False):
    if current == 'end':
        return 1
    if current.islower() and current in visited and current:
        if twice_small:
            return 0
        else:
            twice_small = True

    path_count = 0
    for edge in edges:
        if edge[0] == current and current != edge[1] and edge[1] != "start":
            visited.append(current)
            path_count += part2_count_paths(edges, visited.copy(), edge[1], twice_small)

    return path_count


if __name__ == "__main__":
    input = get_input()

    # Part 1
    edges = set()
    for line in input:
        split = line.split("-")
        edges.add((split[0], split[1]))
        edges.add((split[1], split[0]))

    print(f"Part 1: {part1_count_paths(edges, [], 'start')}")
    print(f"Part 2: {part2_count_paths(edges, [], 'start')}")
