# Advent of code 2021 - day 03
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def count_col(input, col):
    countZero = countOne = 0
    for i in range(len(input)):
        if input[i][col] == '0':
            countZero += 1
        else:
            countOne += 1
    return countZero, countOne


def part1(input):
    gammaBinaryString = ""
    epsilonListBinaryString = ""

    for i in range(len(input[0])):
        countZero, countOne = count_col(input, i)

        if countZero > countOne:
            gammaBinaryString += '1'
            epsilonListBinaryString += '0'
        else:
            gammaBinaryString += '0'
            epsilonListBinaryString += '1'

    gamma = int(gammaBinaryString, 2)
    epsilon = int(epsilonListBinaryString, 2)
    print(str(gamma * epsilon))


def part2_oxygen(input):
    while True:
        for i in range(len(input[0])):
            countZero, countOne = count_col(input, i)

            if countZero > countOne:
                input = list(filter(lambda x: x[i] == '1', input))
            else:
                input = list(filter(lambda x: x[i] == '0', input))

            if len(input) == 1:
                return input[0]


def part2_co2(input):
    while True:
        for i in range(len(input[0])):
            countZero, countOne = count_col(input, i)

            if countZero > countOne:
                input = list(filter(lambda x: x[i] == '0', input))
            else:
                input = list(filter(lambda x: x[i] == '1', input))

            if len(input) == 1:
                return input[0]


def part2(input):
    oxygen = int(part2_oxygen(input), 2)
    co2 = int(part2_co2(input), 2)
    print(str(oxygen * co2))


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)
