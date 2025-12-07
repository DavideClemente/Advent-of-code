"""Common mathematical utilities."""

from math import gcd
from typing import List, Iterable


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two numbers."""
    return abs(a * b) // gcd(a, b)


def lcm_multiple(numbers: Iterable[int]) -> int:
    """Calculate least common multiple of multiple numbers."""
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result


def gcd_multiple(numbers: Iterable[int]) -> int:
    """Calculate greatest common divisor of multiple numbers."""
    result = 0
    for num in numbers:
        result = gcd(result, num)
    return result


def factors(n: int) -> List[int]:
    """Get all factors of a number."""
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(limit: int) -> List[int]:
    """Generate all primes up to a limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []

    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i*i, limit + 1, i):
                is_prime_arr[j] = False

    return [i for i, prime in enumerate(is_prime_arr) if prime]
