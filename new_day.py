#!/usr/bin/env python3
"""
Script to create a new day's challenge directory with template files.
Usage: python new_day.py <year> <day>
"""

import sys
from pathlib import Path
import shutil


def create_day(year: int, day: int):
    """Create directory structure for a new day's challenge."""
    # Create day directory
    day_dir = Path(__file__).parent / str(year) / f"day{day:02d}"
    day_dir.mkdir(parents=True, exist_ok=True)

    # Copy template files
    templates_dir = Path(__file__).parent / "templates"

    # Copy and customize solution template
    solution_template = templates_dir / "solution_template.py"
    solution_file = day_dir / "solution.py"
    content = solution_template.read_text()
    content = content.replace("Day XX", f"Day {day:02d}")
    content = content.replace("YYYY", str(year))
    content = content.replace("/XX", f"/{day}")
    solution_file.write_text(content)

    # Copy and customize test template
    test_template = templates_dir / "test_template.py"
    test_file = day_dir / "test_solution.py"
    content = test_template.read_text()
    content = content.replace("Day XX", f"Day {day:02d}")
    test_file.write_text(content)

    # Copy and customize README template
    readme_template = templates_dir / "README_template.md"
    readme_file = day_dir / "README.md"
    content = readme_template.read_text()
    content = content.replace("Day XX", f"Day {day:02d}")
    readme_file.write_text(content)

    # Create empty input file
    input_file = day_dir / "input.txt"
    input_file.touch()

    print(f"✅ Created challenge directory: {day_dir}")
    print(f"   - solution.py")
    print(f"   - test_solution.py")
    print(f"   - README.md")
    print(f"   - input.txt")
    print(f"\n📝 Don't forget to add your puzzle input to input.txt!")


def main():
    if len(sys.argv) != 3:
        print("Usage: python new_day.py <year> <day>")
        print("Example: python new_day.py 2025 1")
        sys.exit(1)

    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])

        if day < 1 or day > 25:
            print("Error: Day must be between 1 and 25")
            sys.exit(1)

        create_day(year, day)
    except ValueError:
        print("Error: Year and day must be integers")
        sys.exit(1)


if __name__ == "__main__":
    main()
