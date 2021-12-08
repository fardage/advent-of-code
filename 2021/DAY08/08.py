# Advent of code 2021 - day 08
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def part1(lines):
    dic = {2: 1, 4: 4, 3: 7, 7: 8}
    dic_count = {1: 0, 4: 0, 7: 0, 8: 0}
    for line in lines:
        for signal in line[1].split(" "):
            if len(signal) in dic:
                digit = dic[len(signal)]
                dic_count[digit] += 1

    print(f"Part 1: {sum(dic_count.values())}")


def contains_all(str, set):
    if set == "":
        return False
    for c in set:
        if c not in str:
            return False
    return True


def part2(lines):
    numbers = []
    for line in lines:
        signals = line[0].split(" ")
        dic, five_and_two = decode_without_five_or_two(signals)
        two, five = decode_five_and_two(dic, five_and_two)
        dic[2] = two
        dic[5] = five

        digits = line[1].split(" ")
        numbers.append(lookup(dic, digits))
    print(sum(numbers))


def lookup(dic, digits):
    resolved = ""
    for digit in digits:
        for k, v in dic.items():
            if contains_all(digit, v) and len(v) == len(digit):
                resolved += str(k)
    return int(resolved)


def decode_five_and_two(dic, five_and_two):
    if contains_all(dic[6], five_and_two[0]):
        five = five_and_two[0]
        two = five_and_two[1]
    else:
        five = five_and_two[1]
        two = five_and_two[0]
    return two, five


def decode_without_five_or_two(signals):
    dic = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    signals = sorted(signals, key=len)
    five_and_two = []
    for signal in signals:
        if signal in dic.values() or signal == "":
            continue

        if len(signal) == 2:
            dic[1] += signal
        elif len(signal) == 3:
            dic[7] += signal
        elif len(signal) == 4:
            dic[4] += signal
        elif len(signal) == 7:
            dic[8] += signal
        elif len(signal) == 5:
            # It's 3 if all digits from 1 are in signal
            if contains_all(signal, dic[1]):
                dic[3] += signal
            else:
                five_and_two.append(signal)
        elif len(signal) == 6:
            # It's 6 if digits from 1 do not exist in signal
            if not contains_all(signal, dic[1]):
                dic[6] += signal
            # It's 9 if digits from 3 exist in signal
            elif contains_all(signal, dic[3]):
                dic[9] += signal
            else:
                dic[0] += signal
    return dic, five_and_two


if __name__ == "__main__":
    input = get_input()
    lines = [tuple(line.split("|")) for line in input]
    part1(lines)
    part2(lines)
