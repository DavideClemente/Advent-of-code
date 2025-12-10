class Range:
    
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        
    def contains(self, element, inclusive: bool = False) -> bool:
        return self.start <= element <= self.end if inclusive else self.start < element < self.end
    
    def contains_range(self, range: 'Range', inclusive: bool = False) -> bool:
        return self.contains(range.start, inclusive) and self.contains(range.end, inclusive)
    
    def overlaps(self, other: 'Range') -> bool:
        """Check if this range overlaps with another range."""
        return not (self.end < other.start or other.end < self.start)
    
    def __contains__(self, element: int) -> bool:
        return self.contains(element, False)
    
    def __len__(self) -> int:
        """Return the size of the range."""
        return self.end - self.start + 1
    
    def __iter__(self):
        """Make the range iterable."""
        return iter(range(self.start, self.end + 1))
    
    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"