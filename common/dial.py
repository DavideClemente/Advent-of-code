"""Class for representing a dial and its rotations
    """


from dataclasses import dataclass
from enum import Enum, auto


class Rotation(Enum):
    LEFT = auto()
    RIGHT = auto()


@dataclass()
class Dial:

    def __init__(self, pointer: int = 0):
        self._pointer = pointer
        self._zero_passes = 0
        self._zero_endings = 0

    @property
    def pointer(self) -> int:
        """Get the current pointer position."""
        return self._pointer

    @property
    def zero_passes(self) -> int:
        """Get the number of times the dial has passed zero."""
        return self._zero_passes

    @property
    def zero_endings(self) -> int:
        """Get the number of times the dial has ended on zero."""
        return self._zero_endings

    def rotate(self, direction: Rotation, steps: int = 1) -> None:
        """Rotate the dial in the specified direction by a number of steps."""
        old_pointer = self._pointer

        if direction == Rotation.LEFT:
            new_pointer = (self._pointer - steps) % 100
            # Check if we crossed zero (but didn't start at zero)
            crossed_zero = new_pointer == 0 or new_pointer > old_pointer
        elif direction == Rotation.RIGHT:
            new_pointer = (self._pointer + steps) % 100
            # Check if we crossed zero
            crossed_zero = new_pointer < old_pointer
        else:
            raise ValueError("Invalid rotation direction")

        # Count zero passes (only if we didn't start at zero, crossed it, and didn't land on it)
        if old_pointer != 0 and crossed_zero and new_pointer != 0:
            self._zero_passes += 1

        # Add complete rotations (every 100 steps = 1 pass through zero)
        self._zero_passes += steps // 100

        # Update pointer
        self._pointer = new_pointer

        # Count if we ended on zero
        if self._pointer == 0:
            self._zero_endings += 1
