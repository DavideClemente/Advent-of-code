# 🎄 Advent of Code

My solutions for [Advent of Code](https://adventofcode.com/) challenges.

## 📁 Project Structure

```
advent-of-code/
├── common/              # Shared utilities and helper functions
│   ├── __init__.py
│   ├── file_utils.py    # File reading and parsing utilities
│   ├── grid.py          # Grid and Point classes for 2D problems
│   ├── algorithms.py    # BFS, DFS, Dijkstra, A* implementations
│   └── math_utils.py    # Mathematical utilities (GCD, LCM, primes, etc.)
├── templates/           # Templates for new challenges
│   ├── solution_template.py
│   ├── test_template.py
│   └── README_template.md
├── 2024/               # Solutions organized by year
│   ├── day01/
│   ├── day02/
│   └── ...
├── 2025/               # Current year
│   ├── day01/
│   ├── day02/
│   └── ...
├── new_day.py          # Script to scaffold new day challenges
└── README.md
```

## 🚀 Quick Start

### Creating a New Day

Use the helper script to quickly scaffold a new day's challenge:

```bash
python new_day.py <year> <day>
```

Example:

```bash
python new_day.py 2025 1
```

This creates:

-   `YYYY/dayXX/solution.py` - Main solution file
-   `YYYY/dayXX/test_solution.py` - Test file with example cases
-   `YYYY/dayXX/README.md` - Notes and explanations
-   `YYYY/dayXX/input.txt` - Puzzle input (empty, needs to be filled)

### Running a Solution

```bash
cd 2025/day01
python solution.py
```

### Running Tests

```bash
cd 2025/day01
python -m pytest test_solution.py -v
```

Or run tests for all days:

```bash
python -m pytest -v
```

## 📚 Common Utilities

The `common` module provides reusable utilities:

### File Utilities (`file_utils.py`)

-   `read_input(filepath)` - Read entire file as string
-   `read_lines(filepath)` - Read file as list of lines
-   `read_integers(filepath)` - Parse file as integers
-   `read_grid(filepath)` - Parse file as 2D grid
-   `read_sections(filepath)` - Split file by sections
-   `parse_lines(filepath, parser)` - Apply custom parser to each line

### Grid Utilities (`grid.py`)

-   `Point` - 2D point with arithmetic operations and neighbors
-   `Direction` - Cardinal directions with rotation methods
-   `Grid` - 2D grid with bounds checking, search, and neighbor iteration

### Algorithms (`algorithms.py`)

-   `bfs()` - Breadth-first search
-   `dfs()` - Depth-first search
-   `dijkstra()` - Shortest path algorithm
-   `a_star()` - A\* pathfinding

### Math Utilities (`math_utils.py`)

-   `lcm()`, `gcd()` - Least common multiple and greatest common divisor
-   `factors()` - Find all factors of a number
-   `is_prime()` - Check if number is prime
-   `primes_up_to()` - Sieve of Eratosthenes

## 💡 Usage Examples

### Reading Input

```python
from common import read_input, read_lines, read_integers

# Read as single string
data = read_input("input.txt")

# Read as list of lines
lines = read_lines("input.txt")

# Read as list of integers
numbers = read_integers("input.txt")
```

### Working with Grids

```python
from common import read_grid, Grid, Point

# Create grid from file
grid_data = read_grid("input.txt")
grid = Grid(grid_data)

# Find a character
start = grid.find('S')

# Get neighbors
for neighbor in grid.neighbors(start):
    print(grid.get(neighbor))
```

### Graph Algorithms

```python
from common import bfs, Point

def get_neighbors(point):
    return [n for n in point.neighbors() if grid.get(n) != '#']

# Find shortest distances from start
distances = bfs(start, get_neighbors)
```

## 🎯 Problem-Solving Tips

1. **Read the problem carefully** - Make sure you understand all edge cases
2. **Start with examples** - Test your solution with the provided examples
3. **Think about data structures** - Choose the right structure for the problem
4. **Consider efficiency** - Part 2 often requires optimization
5. **Use the common utilities** - Don't reinvent the wheel

## 📝 Notes

-   Each day's solution should be self-contained in its directory
-   Add puzzle input to `input.txt` (not committed to avoid spoilers)
-   Write tests for examples before implementing the full solution
-   Document your approach in the day's README.md

## 🔗 Links

-   [Advent of Code Website](https://adventofcode.com/)
-   [Advent of Code Subreddit](https://www.reddit.com/r/adventofcode/)

---

Happy coding! 🎄✨
