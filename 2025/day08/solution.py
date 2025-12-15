"""
Advent of Code - Day 08
https://adventofcode.com/2025/day/8
"""

from common import read_input, read_lines, UnionFind
from pathlib import Path
from math import sqrt
from functools import total_ordering
from dataclasses import dataclass
from itertools import combinations
from py_linq.py_linq import Enumerable

import sys

@dataclass
class Box():
    x: int
    y: int
    z: int
    
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __eq__(self, other):
        if not isinstance(other, Box):
            return False
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def distance(self, box: "Box") -> float:
        return sqrt((self.x - box.x)**2 + (self.y - box.y)**2 + (self.z - box.z)**2)

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def part1(data: list[str], pairs: int) -> int:
    """Solve part 1 of the puzzle."""
    
    boxes = Enumerable(data).select(lambda x: Box(*x.split(','))).to_list()
    combs = sorted(combinations(boxes, 2), key=lambda x: x[0].distance(x[1]))
    disjoint_set = UnionFind(items=boxes)
    
    i = 0
    for box1, box2 in combs:
        disjoint_set.union(box1, box2)
        i += 1
        if i == pairs: break
    
    circuits = sorted(disjoint_set.get_component_sizes(),reverse=True)
    
    return Enumerable(circuits).take(3).aggregate(lambda x, y: x * y)


def part2(data: list[str]) -> int:
    boxes = Enumerable(data).select(lambda x: Box(*x.split(','))).to_list()
    combs = sorted(combinations(boxes, 2), key=lambda x: x[0].distance(x[1]))
    disjoint_set = UnionFind(items=boxes)
    
    for box1, box2 in combs:
        disjoint_set.union(box1, box2)
        
        circuits = sorted(disjoint_set.get_component_sizes(),reverse=True)
        if circuits[0] == len(boxes): 
            return box1.x * box2.x # One giant circuit
    return 0



def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Solve and print results
    #print(f"Part 1: {part1(data, 1000)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
