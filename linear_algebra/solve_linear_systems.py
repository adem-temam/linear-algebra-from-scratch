from typing import List
from .inverse import inverse

Matrix = List[List[float]]
Vector = List[float]

def solve(A: Matrix, b: Vector) -> Vector:
    """Solve Ax = b for x using matrix inversion."""
    if len(A) != len(b):
         # Basic check on rows
         raise ValueError("Matrix rows must match vector length")
    
    A_inv = inverse(A)
    return [sum(A_inv[i][j] * b[j] for j in range(len(b)))
            for i in range(len(A))]

