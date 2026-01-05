import math
from typing import List

Vector = List[float]

def add(v1: Vector, v2: Vector) -> Vector:
    """Add two vectors component-wise."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [x + y for x, y in zip(v1, v2)]


def subtract(v1: Vector, v2: Vector) -> Vector:
    """Subtract vector v2 from v1 component-wise."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [x - y for x, y in zip(v1, v2)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply a vector by a scalar."""
    return [c * x for x in v]


def dot_product(v1: Vector, v2: Vector) -> float:
    """Compute the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return sum(x * y for x, y in zip(v1, v2))


def magnitude(v: Vector) -> float:
    """Compute the magnitude (Euclidean norm) of a vector."""
    return math.sqrt(dot_product(v, v))

