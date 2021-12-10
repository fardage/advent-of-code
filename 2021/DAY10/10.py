# Advent of code 2021 - day 10
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath('input.txt')
    with open(input_file, 'r') as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def find_illegal_bracket(line, opening_brackets, closing_brackets, points):
    stack = []
    score = 0
    for char in line:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack[-1] == opening_brackets[closing_brackets.index(char)]:
                stack.pop()
            else:
                score += points[char]
                return score
    return score


def part1(input):
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    score = 0
    for i in range(len(input)):
        score += find_illegal_bracket(input[i], opening_brackets, closing_brackets, points)
    print(f"Part 1: {score}")


def auto_complete_brackets(input, opening_brackets, closing_brackets, points):
    stack = []
    score = 0
    for char in input:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            stack.pop()

    while stack:
        score = (score * 5) + points[stack.pop()]

    return score


def part2(input):
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']
    points1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points2 = {'(': 1, '[': 2, '{': 3, '<': 4}

    scores = []
    for i in range(len(input)):
        if find_illegal_bracket(input[i], opening_brackets, closing_brackets, points1) == 0:
            scores.append(auto_complete_brackets(input[i], opening_brackets, closing_brackets, points2))
    scores.sort()
    print(f"Part 2: {scores[len(scores) // 2]}")


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)
