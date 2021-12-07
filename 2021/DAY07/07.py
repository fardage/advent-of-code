# Advent of code 2021 - day 07
from pathlib import Path
import math


def get_input():
    input = []
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        for line in f.readlines():
            for char in line.split(','):
                input.append(int(char))
    return input


def part1_cost(crab_pos, moveTo):
    return abs(crab_pos - moveTo)


def part2_cost(crab_pos, moveTo):
    distance = abs(crab_pos - moveTo)
    cost = 0
    for i in range(1, distance + 1):
        cost = cost + i
    return cost


def brute_force(input, fitness_function):
    min_pos = min(input)
    max_pos = max(input)

    best = math.inf
    best_pos = 0
    for moveTo in range(min_pos, max_pos + 1):
        cost = 0
        for crab_pos in input:
            cost = cost + fitness_function(crab_pos, moveTo)
        if cost < best:
            best = cost
            best_pos = moveTo

    return best, best_pos


if __name__ == "__main__":
    input = get_input()
    print(f"Input data: {input}")
    print(f"Part 1, Cost / Pos: {brute_force(input, part1_cost)}")
    print(f"Part 2, Cost / Pos: {brute_force(input, part2_cost)}")
