"""Utilities for reading and parsing input files."""

from pathlib import Path
from typing import List, Callable, Any


def read_input(filepath: str) -> str:
    """
    Read the entire input file as a single string.

    Args:
        filepath: Path to the input file

    Returns:
        The complete file contents as a string
    """
    with open(filepath, 'r') as f:
        return f.read()


def read_lines(filepath: str, strip: bool = True) -> List[str]:
    """
    Read input file and return a list of lines.

    Args:
        filepath: Path to the input file
        strip: Whether to strip whitespace from each line

    Returns:
        List of lines from the file
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [line.strip() if strip else line for line in lines]


def read_integers(filepath: str, separator: str = '\n') -> List[int]:
    """
    Read input file and return a list of integers.

    Args:
        filepath: Path to the input file
        separator: Character(s) to split on (default: newline)

    Returns:
        List of integers from the file
    """
    content = read_input(filepath)
    return [int(x) for x in content.strip().split(separator) if x.strip()]


def read_grid(filepath: str) -> List[List[str]]:
    """
    Read input file and return a 2D grid (list of lists).

    Args:
        filepath: Path to the input file

    Returns:
        2D list representing the grid
    """
    lines = read_lines(filepath)
    return [list(line) for line in lines if line]


def read_sections(filepath: str, separator: str = '\n\n') -> List[str]:
    """
    Read input file and split into sections.

    Args:
        filepath: Path to the input file
        separator: String to split sections on (default: double newline)

    Returns:
        List of sections from the file
    """
    content = read_input(filepath)
    return content.split(separator)


def parse_lines(filepath: str, parser: Callable[[str], Any]) -> List[Any]:
    """
    Read lines and apply a custom parser function to each.

    Args:
        filepath: Path to the input file
        parser: Function to apply to each line

    Returns:
        List of parsed values
    """
    lines = read_lines(filepath)
    return [parser(line) for line in lines if line]
