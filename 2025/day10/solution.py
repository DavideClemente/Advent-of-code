"""
Advent of Code - Day 10
https://adventofcode.com/2025/day/10
"""

from common import read_input, read_lines
from pathlib import Path
import sys
from dataclasses import dataclass, field
from py_linq.py_linq import Enumerable
import ast
from itertools import combinations


@dataclass
class Machine():
    _indicator_lights: str = field(init=False)
    _final_state: str
    _buttons: list[list[int]]

    @property
    def indicator_lights(self):
        return self._indicator_lights

    def __post_init__(self):
        self._indicator_lights = '.' * len(self._final_state)

    def reset_lights(self):
        self._indicator_lights = '.' * len(self._final_state)

    def all_on(self):
        return Enumerable(self.indicator_lights).all(lambda x: x == '#')

    def can_start(self):
        return self._indicator_lights == self._final_state

    def switch_indicator_light(self, indicator_index: int):
        indicator_light = self._indicator_lights[indicator_index]
        if indicator_light == '#':
            indicator_light = '.'
        elif indicator_light == '.':
            indicator_light = '#'
        lights_list = list(self._indicator_lights)
        lights_list[indicator_index] = indicator_light
        self._indicator_lights = ''.join(lights_list)

    def press_button(self, buttons):  # buttons is a tuple of button definitions
        for button in buttons:  # button is one button definition like [0, 2]
            for light_index in button:  # light_index is which light to toggle
                self.switch_indicator_light(light_index)

    def solve(self):
        for i in range(1, len(self._buttons) + 1):
            for bt in combinations(self._buttons, r=i):
                self.reset_lights()
                self.press_button(bt)
                if self.can_start():
                    return i
        return


# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    machines = []
    for problem in data:
        state, *buttons, _ = problem.split(' ')
        result = [list(val) if isinstance(
            val := ast.literal_eval(s), tuple) else [val] for s in buttons]
        machine = Machine(_final_state=state[1:-1], _buttons=result)
        machines.append(machine)

    total = 0
    for m in machines:
        total += m.solve()
    return total


def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    pass


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
