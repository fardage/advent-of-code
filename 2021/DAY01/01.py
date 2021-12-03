# Advent of code 2021 - day 01
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [int(line) for line in f.readlines()]


# Count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement.)
def part1(input):
    count = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            count += 1
    return count


# Count the number of times the sum of measurements in this sliding window increases from the previous sum
def part2(input):
    measurement_sum = []
    countIncrease = 0

    for i in range(len(input) - 2):
        measurement_sum.append(sum(input[i:i + 3]))
        if i != 0 and measurement_sum[i] > measurement_sum[i - 1]:
            countIncrease += 1

    return countIncrease


if __name__ == '__main__':
    measurements = get_input()
    print(f"Part 1: {part1(measurements)}")
    print(f"Part 2: {part2(measurements)}")
