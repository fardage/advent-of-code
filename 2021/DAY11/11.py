# Advent of code 2021 - day 11
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath('input.txt')
    with open(input_file, 'r') as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def get_neighbors(input, row, col):
    neighbors = []
    for rowOffset in range(-1, 2):
        for colOffset in range(-1, 2):
            if rowOffset == 0 and colOffset == 0:
                continue
            if row + rowOffset < 0 or row + rowOffset >= len(input):
                continue
            if col + colOffset < 0 or col + colOffset >= len(input[row]):
                continue
            neighbors.append((row + rowOffset, col + colOffset))
    return neighbors


def flash(input, row, col, has_flashed):
    has_flashed.add((row, col))
    for n_row, n_col in get_neighbors(input, row, col):
        input[n_col][n_row] += 1
        if (n_row, n_col) not in has_flashed and input[n_col][n_row] > 9:
            flash(input, n_row, n_col, has_flashed)
    return has_flashed


def step(input):
    has_flashed = set()
    for row in range(len(input)):
        for col in range(len(input[row])):
            input[row][col] += 1
            if input[row][col] > 9 and (col, row) not in has_flashed:
                has_flashed.union(flash(input, col, row, has_flashed))
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] > 9:
                input[row][col] = 0
    return len(has_flashed), input


def all_are_zero(input):
    for line in input:
        for val in line:
            if val != 0:
                return False
    return True


if __name__ == "__main__":
    input = [[int(x) for x in row] for row in get_input()]
    flashed = 0
    i = 0
    while True:
        i += 1
        c, o = step(input)
        flashed += c
        if i == 100:
            print(f"Part 1: {flashed}")
        if all_are_zero(input):
            print(f"Part 2: {i}")
            break
