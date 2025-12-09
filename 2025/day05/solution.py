"""
Advent of Code - Day 05
https://adventofcode.com/2025/day/5
"""

from common import read_input, read_lines
from pathlib import Path
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


class Range():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end



def part1(ranges: list[str], ingredients: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    counter = 0
    
    for ingredient in ingredients:
        #isFresh = False
        for range in ranges:
            start, end = map(int, range.split('-'))
            ing_value = int(ingredient)
            
            if ing_value >= start and ing_value <= end:
                counter += 1
                break
    return counter


def part2_2(ranges: list[str]) -> int:
    intervals = [tuple(map(int, r.split('-'))) for r in ranges]
    intervals.sort()

    merged = []
    cur_start, cur_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_end + 1:          # overlap or touching
            cur_end = max(cur_end, e)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    merged.append((cur_start, cur_end))

    # count unique IDs
    return sum(e - s + 1 for s, e in merged)

def part2_davide(ranges: list[str]) -> int:
    parsed_ranges = [Range(*map(int, r.split('-'))) for r in ranges]
    
    parsed_ranges = list(sorted(parsed_ranges, key=lambda e: e.start))
    
    
    s, e = parsed_ranges[0].start, parsed_ranges[0].end
    counter = 0
    simplified_ranges = {s:[s,e]}
    for i in range(1, len(parsed_ranges)):
        start, end = parsed_ranges[i].start, parsed_ranges[i].end
        if start < e:
            if end < e:
                continue
            else:
                simplified_ranges[s] = [s, end]

        else: 
            simplified_ranges[start] = [start, end]
            s = start
        e = end
        
    for s in simplified_ranges.values():
        counter += s[1] - s[0] + 1
    return counter


def part2(ranges: list[str]) -> int:
    
    # 3-5 = 3
    # 10-14 = 5
    # 12-18 = 7
    # 16-20 = 5
    
    
    # 10 > 5
    
    # 10 - 18
    # 16 - 20
    
    # 3 - 5
    # 10 - 20
    
    parsed_ranges = [Range(*map(int, r.split('-'))) for r in ranges]
    
    parsed_ranges = list(sorted(parsed_ranges, key=lambda e: e.start))

    start1, end1 = parsed_ranges[0].start, parsed_ranges[0].end
    counter = end1 - start1 + 1 
    
    
    last_add = 0
    for i in range(1, len(parsed_ranges)):
        start, end = parsed_ranges[i].start, parsed_ranges[i].end

        if start < end1:
            counter -= last_add
            last_add = end - start1 + 1
            counter += last_add
        else:
            last_add = end - start + 1
            counter += last_add
        start1 = start
        end1 = end
                
        
        
    return counter
    """Solve part 2 of the puzzle."""

   


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))
    idx = data.index('')
    ranges, ingredients = data[:idx], data[idx+1:]

    # Solve and print results
    #print(f"Part 1: {part1(ranges, ingredients)}")
    print(f"Part 2: {part2_2(ranges)}")


if __name__ == "__main__":
    main()
