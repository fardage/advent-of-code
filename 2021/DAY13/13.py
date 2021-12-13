# Advent of code 2021 - day 13
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath('input.txt')
    with open(input_file, 'r') as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def get_grid_and_instruction():
    input = get_input()

    # Parse for grid and instructions
    coords = []
    instructions = []
    for line in input:
        if ',' in line:
            coords.append(tuple(map(int, line.split(','))))
        if '=' in line:
            split = line.split('=')
            instructions.append((split[0][-1], int(split[1])))

    # Create grid
    maxX = max(coords, key=lambda x: x[0])[0]
    maxY = max(coords, key=lambda x: x[1])[1]
    grid = [[False for _ in range(maxX + 1)] for _ in range(maxY + 1)]

    # Add coordinates
    for coord in coords:
        grid[coord[1]][coord[0]] = True

    return grid, instructions


def print_grid(grid):
    for row in grid:
        print_row(row)


def print_row(row):
    for col in row:
        if col:
            print('#', end='')
        else:
            print('.', end='')
    print()


def merge(upper, lower):
    new_row = []
    for i in range(len(upper)):
        if upper[i] or lower[i]:
            new_row.append(True)
        else:
            new_row.append(False)
    return new_row


def fold_up(grid, at):
    upper_offset = 1
    for lowerIndex in range(at + 1, len(grid)):
        grid[at - upper_offset] = merge(grid[lowerIndex], grid[at - upper_offset])
        upper_offset += 1
    for lowerIndex in range(at + 1, len(grid) + 1):
        grid.pop()
    return grid


def fold_left(grid, at):
    new_grid = []
    for row in grid:
        left = row[:at]
        right = row[at:]
        right.reverse()
        new_grid.append(merge(left, right))
    return new_grid


def do_instructions(grid, instructions):
    for instruction in instructions:
        if 'y' in instruction[0]:
            grid = fold_up(grid, instruction[1])
        if 'x' in instruction[0]:
            grid = fold_left(grid, instruction[1])
        print(sum(map(lambda x: x.count(True), grid)))
    return grid


if __name__ == '__main__':
    grid, instructions = get_grid_and_instruction()
    grid = do_instructions(grid, instructions)
    print_grid(grid)

