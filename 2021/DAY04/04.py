# Advent of code 2021 - day 04
from pathlib import Path


def get_input():
    input_file = Path(__file__).parent.joinpath("input.txt")
    with open(input_file, "r") as f:
        return [str(line).rstrip('\n') for line in f.readlines()]


def parse_bingo_data(input):
    numbers = input[0].split(",")
    numbers = [int(n) for n in numbers]

    boards = []
    board = []
    for i in range(2, len(input)):
        bingoRow = input[i]
        if input[i] == "":
            boards.append(board)
            board = []
        else:
            bingoRow = bingoRow.replace("  ", " ")
            bingoRow = bingoRow.split(" ")
            bingoRow = list(filter(lambda x: x != "", bingoRow))
            bingoRow = [(int(x), False) for x in bingoRow]
            board.append(bingoRow)

    boards.append(board)
    return numbers, boards


def has_bingo(board):
    for row in board:
        if all(x[1] for x in row):
            return True
    for col in range(len(board[0])):
        if all(x[1] for x in [row[col] for row in board]):
            return True
    return False


def calc_score(board, number):
    sum = 0
    for row in board:
        for i in range(len(row)):
            if not row[i][1]:
                sum += row[i][0]
    return sum * number


def mark_number(board, number):
    for row in board:
        for i in range(len(row)):
            if row[i][0] == number:
                row[i] = (number, True)


if __name__ == "__main__":
    input = get_input()
    numbers, bingoBoards = parse_bingo_data(input)

    done = []
    lastScore = 0
    for number in numbers:
        for bingoBoard in bingoBoards:
            mark_number(bingoBoard, number)
            if has_bingo(bingoBoard) and bingoBoard not in done:
                print(f"BINGO! {number}, {calc_score(bingoBoard, number)}")
                done.append(bingoBoard)

