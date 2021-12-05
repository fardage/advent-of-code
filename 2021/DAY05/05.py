# Advent of code 2021 - day 05
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def parse_coordinates(input):
    coordinates = []
    max = 0
    for line in input:
        start, end = line.split(' -> ')
        x1, y1 = [int(v) for v in start.split(',')]
        x2, y2 = [int(v) for v in end.split(',')]

        if x1 > max:
            max = x1
        if x2 > max:
            max = x2
        if y1 > max:
            max = y1
        if y2 > max:
            max = y2

        coordinates.append([(x1, y1), (x2, y2)])
    return coordinates, max


def auto_reverse_range(start, stop):
    if stop > start:
        return range(start, stop+1)
    else:
        return range(start, stop-1, -1)


if __name__ == "__main__":
    input = get_input()
    coordinates, max = parse_coordinates(input)
    max += 1
    map = [[0 for x in range(max)] for y in range(max)]

    for start, end in coordinates:
        x1, y1 = start
        x2, y2 = end

        if x1 == x2:
            for y in auto_reverse_range(y1, y2):
                map[y][x1] += 1
        elif y1 == y2:
            for x in auto_reverse_range(x1, x2):
                map[y1][x] += 1
        else:
            x = auto_reverse_range(x1, x2)
            y = auto_reverse_range(y1, y2)
            for i in range(len(x)):
                map[y[i]][x[i]] += 1


    count = 0
    for x in range(max):
        for y in range(max):
            if map[x][y] > 1:
                count += 1
    print(count)



