# Advent of code 2021 - day 06
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def simulate(fishes, days):
    # print(f"Initial state: {fishes}")
    for day in range(1, days + 1):
        for i in range(len(fishes)):
            fishes[i] = (fishes[i] - 1) % 9
            if fishes[i] == 8:
                fishes[i] = 6
                fishes.append(8)
        # print(f"After   {day} days: {fishes}")

    return len(fishes)


def count_fishes(fishes, end):
    count_fish_age = [0] * 9
    for f in fishes:
        count_fish_age[f] += 1

    for _ in range(end):
        next_count_fish_age = [0] * 9
        next_count_fish_age[6] = next_count_fish_age[8] = count_fish_age[0]
        for day in range(8):
            next_count_fish_age[day] += count_fish_age[day + 1]
        count_fish_age = next_count_fish_age

    return sum(count_fish_age)


if __name__ == "__main__":
    input = get_input()
    input = [int(i) for i in input[0].split(',')]

    print(f"Part 1: {simulate(input.copy(), 80)}")
    print(f"Part 2: {count_fishes(input.copy(), 256)}")
