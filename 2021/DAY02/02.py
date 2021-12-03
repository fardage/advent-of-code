# Advent of code 2021 - day 02
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def part1(input):
    posX = 0
    posY = 0

    for line in input:
        command = line.split()
        if command[0] == "forward":
            posX += int(command[1])
        elif command[0] == "down":
            posY += int(command[1])
        elif command[0] == "up":
            posY -= int(command[1])

    print("X: " + str(posX) + "Y: " + str(posY))
    print("Result: " + str(posX * posY))


def part2(input):
    posX = 0
    posY = 0
    aim = 0

    for line in input:
        command = line.split()
        if command[0] == "forward":
            posX += int(command[1])
            posY += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

    print(f"X: {str(posX)} Y: {str(posY)}")
    print(f"Result: {str(posX * posY)}")


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)
