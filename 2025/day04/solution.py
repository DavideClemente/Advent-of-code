"""
Advent of Code - Day 04
https://adventofcode.com/2025/day/4
"""

from common import read_input, read_lines, Grid, Point
from pathlib import Path
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def points_remove(grid: Grid) -> tuple[list[Point], int] :
    points = []

    for y in range(grid.width):
        for x in range(grid.width):
            current_point = Point(x, y)
            neighbors = grid.neighbors(current_point, diagonal=True)
            neighbors_values = list(map(lambda n: grid.get(n), neighbors))
            if grid.get(current_point) == '@' and neighbors_values.count('@') < 4:
                points.append(Point(x,y))
    return points, len(points)

def part1(grid: Grid) -> int:
    """Solve part 1 of the puzzle."""
    return points_remove(grid)[1]


def search_and_remove_paper(grid: Grid, amount: int) -> int:
    pts_remove = points_remove(grid)
    points_len = pts_remove[1]
    if points_len == 0:
        return amount       
    
    print(grid)    
    
    for p in pts_remove[0]:
            grid.set(p, '.') 
    
    print("="*20)
    print(grid)
            
    return search_and_remove_paper(grid, amount+points_len)


def part2(grid: Grid) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    return search_and_remove_paper(grid, 0)


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))
    data = [list(line) for line in data]
    grid = Grid(data)

    # Solve and print results
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
