"""
Test cases for Day 04
"""

from solution import part1, part2
import pytest
from pathlib import Path
import sys

# Add parent directory to path to import solution
sys.path.append(str(Path(__file__).parent))


EXAMPLE_INPUT = """
# TODO: Add example input from problem description
"""


def test_part1_example():
    """Test part 1 with example input."""
    result = part1(EXAMPLE_INPUT.strip())
    assert result == None  # TODO: Add expected result


def test_part2_example():
    """Test part 2 with example input."""
    result = part2(EXAMPLE_INPUT.strip())
    assert result == None  # TODO: Add expected result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
