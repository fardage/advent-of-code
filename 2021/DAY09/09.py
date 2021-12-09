# Advent of code 2021 - day 09
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def get_neighbor_values(input, row, col):
    return [input[neighbor[0]][neighbor[1]] for neighbor in get_neighbor_pos(input, row, col)]


def get_neighbor_pos(input, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < len(input) - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < len(input[0]) - 1:
        neighbors.append((row, col + 1))
    return neighbors


def part1(input):
    low_points = []
    for row in range(len(input)):
        for col in range(len(input[row])):
            neighbors = get_neighbor_values(input, row, col)
            if min(neighbors) > input[row][col]:
                low_points.append(input[row][col])
    print(f"Part 1: {sum([x + 1 for x in low_points])}")


def get_basin_group(input, row, col, group):
    if input[row][col] == 9 or (row, col) in group:
        return []

    group.append((row, col))

    for neighbor in get_neighbor_pos(input, row, col):
        group.extend(get_basin_group(input, neighbor[0], neighbor[1], group))

    return list(set(group))


def not_in_any_basin(basins, row, col):
    for basin in basins:
        if (row, col) in basin:
            return False
    return True


def part2(input):
    basins = []
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] != 9 and not_in_any_basin(basins, row, col):
                basins.append(get_basin_group(input, row, col, []))

    basins.sort(key=len, reverse=True)
    print(f"Part 2: {len(basins[0]) * len(basins[1]) * len(basins[2])}")


if __name__ == "__main__":
    input = get_input()
    input = [[int(x) for x in row] for row in input]
    part1(input)
    part2(input)
