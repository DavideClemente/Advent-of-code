"""
Advent of Code - Day 06
https://adventofcode.com/2025/day/6
"""

from common import read_input, read_lines, read_columns
from pathlib import Path
from enum import Enum, auto
from py_linq.py_linq import Enumerable
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def transpose_matrix(matrix: list[list[str]]) -> list[list[str]]:
    return [list(row) for row in zip(*matrix)]


class Operation(Enum):
    ADD = auto()
    MULTIPLY = auto()

    @property
    def func(self):
        if self == Operation.ADD:
            return lambda x, y: int(x) + int(y)
        return lambda x, y: int(x) * int(y)


op_map = {
    '+': Operation.ADD,
    '*': Operation.MULTIPLY,
}


class MathProblem:

    def __init__(self, operation: Operation, *values):
        self._operation = operation
        self._values = values

    def calculate(self):
        return Enumerable(self._values).aggregate(self._operation.func)


def process_input_part1(data: list[str]):
    grid = [line.split(' ') for line in data]
    clean_grid = []
    for l in grid:
        line = []
        for e in l:
            if e.strip() != '':
                line.append(e)
        clean_grid.append(line)
    print(clean_grid)

    operations = clean_grid[-1]
    transposed = transpose_matrix(clean_grid[:-1])
    print(transposed)
    return transposed, operations


def part1(data: list[str]) -> int:
    numbers, operations = process_input_part1(data)

    """Solve part 1 of the puzzle."""
    result = 0
    for number_set, symbol in zip(numbers, operations):
        operation = op_map.get(symbol)
        result += MathProblem(operation, *number_set).calculate()
    return result


def digit_columns(values: list[str]) -> list[list[int]]:
    max_len = max(len(v) for v in values)

    columns = []
    for i in range(max_len):
        col = []
        for v in values:
            # Align right so the least significant digits line up
            if i < len(v):
                col.append(int(v[-(i+1)]))
        columns.append(list(reversed(col)))

    return list(reversed(columns))


def process_input_part2(data):
    grid = [line.strip("\n") for line in data]
    cols = list(zip(*grid))
    for col in cols[::-1]:
        print("".join(col))


def part2(data) -> int:
    """Solve part 2 of the puzzle."""
    data = data.split('\n')
    operators = data[-1].split(' ')

    operators = Enumerable(operators).where(lambda x: x != '').to_list()

    numbers = data[:-1]

    print(f"Numbers = {numbers}")
            
    def find_divisor(index):
        divisor = 0

        for l in numbers:
            initial_divisor = 0

            for c in l[index:]:
                if c == ' ':
                    break
                initial_divisor += 1

            # IMPORTANT: handle numbers that end at string end
            if initial_divisor > divisor:
                divisor = initial_divisor

        return divisor


    groups = []
    group = []
    index = 0
    for l in numbers:
        while index < len(l):
            divisor = find_divisor(index)
            
            
            group.append(l[index:index+divisor])
            index += divisor + 1
        groups.append(group)
        group = []
        index = 0

    transposed = list(zip(*groups))

    result = 0
    number = ""
    for i, t in enumerate(transposed):
        problem_numbers = []
        for j in range(len(transposed[i][0])):
            number = ""
            for num in t:
                if num[j] != ' ':
                    number += (num[j])
            problem_numbers.append(number)

        operator = operators[i]
        op = op_map.get(operator)
        math_result = MathProblem(op, *problem_numbers).calculate()
        result += math_result

    return result


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Solve and print results
    # print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(read_input(str(input_file)))}")


if __name__ == "__main__":
    main()
