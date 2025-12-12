"""
Advent of Code - Day 07
https://adventofcode.com/2025/day/7
"""

from common import read_input, read_lines, Grid, read_columns, read_grid, Point, TernaryNode, TernaryTree, Rotation
from pathlib import Path
import sys
from py_linq.py_linq import Enumerable


# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))
        
def find_starting_point(data: list[list[str]]) -> str:
    for x in data[0]:
        if x == 'S':
            return x
    return ""


def solve_tree(grid: Grid, direction: Rotation):
    counter = 0
    for y in range(grid.height):
        for x in range(grid.width):
            current_point = Point(x, y)
            
            if y == 0:
                if grid.get(current_point) == 'S':
                    grid.set(Point(x, y+1), '|')
                    break
            else:
                # Solve dividing
                if grid.get(current_point) == '|':
                    if grid.get(Point(x, y + 1)) == '^':
                        counter *= 2
                        grid.set(Point(x - 1, y + 1), '|')
                        grid.set(Point(x + 1, y + 1), '|')
                    else:
                        grid.set(Point(x, y + 1), '|')
        print(grid)
        print('\n' * 5)
        
    return counter
 
    
def part2_optimized(data: list[list[str]]) -> int:
    grid = Grid(data)
    
    # Find starting position
    start_x = None
    for x in range(grid.width):
        if grid.get(Point(x, 0)) == 'S':
            start_x = x
            break
    
    position_counts = {start_x: 1}
    for y in range(1, grid.height):
        next_counts = {}
        
        for x, count in position_counts.items():
            cell = grid.get(Point(x, y))
            
            if cell == '^':
                # Split: send realities left and realities right
                next_counts[x - 1] = next_counts.get(x - 1, 0) + count
                next_counts[x + 1] = next_counts.get(x + 1, 0) + count
            else:
                # Continue straight: send 'count' realities down
                next_counts[x] = next_counts.get(x, 0) + count
        
        position_counts = next_counts
    return sum(position_counts.values())


def part2(data: list[list[str]]) -> int:
    grid = Grid(data)
    
    # Find starting position
    start_x = None
    for i in range(grid.width):
        if grid.get(Point(i, 0)) == 'S':
            start_x = i
            break
    
    # Track realities as they flow down
    # Each reality is represented by its x-position at current y-level
    current_realities = [start_x]
    
    for y in range(1, grid.height):
        next_realities = []
        
        for x in current_realities:
            cell = grid.get(Point(x, y))
            
            if cell == '^':
                # Split into two realities
                next_realities.append(x - 1)
                next_realities.append(x + 1)
            else:
                # Continue straight down
                next_realities.append(x)
        
        current_realities = next_realities
    
    return len(current_realities)


def part1(data: list[list[str]]) -> int:
    grid = Grid(data)
    counter = 0
    for y in range(grid.height):
        for x in range(grid.width):
            current_point = Point(x, y)
            
            if y == 0:
                if grid.get(current_point) == 'S':
                    grid.set(Point(x, y+1), '|')
                    break
            else:
                # Solve dividing
                if grid.get(current_point) == '|':
                    if grid.get(Point(x, y + 1)) == '^':
                        counter += 1
                        grid.set(Point(x - 1, y + 1), '|')
                        grid.set(Point(x + 1, y + 1), '|')
                    else:
                        grid.set(Point(x, y + 1), '|')
        print(grid)
        print('\n' * 5)
        
    return counter


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_input(str(input_file))

    # Solve and print results
    #print(f"Part 1: {part1(read_grid(str(input_file)))}")
    print(f"Part 2: {part2_optimized(read_grid(str(input_file)))}")


if __name__ == "__main__":
    main()
