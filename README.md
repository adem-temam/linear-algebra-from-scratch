# Linear Algebra From Scratch

## What
A pure Python implementation of core linear algebra concepts, built entirely from scratch without using external libraries such as NumPy.

## Why
To gain a deep and practical understanding of linear algebra by implementing fundamental algorithms manually and clearly.

## Implemented
- **Vectors**: Addition, subtraction, scalar multiplication, dot product, magnitude
- **Matrices**: Shape, transpose, matrix multiplication
- **Linear Systems**:
  - Determinant (recursive and row-reduction methods)
  - Matrix inverse (Gauss–Jordan elimination)
  - Rank (row-reduction)
  - Linear system solver

## Example
```python
from linear_algebra.matrices import multiply
from linear_algebra.solve_linear_systems import solve

# Matrix multiplication
A = [[2.0, 1.0],
     [5.0, 3.0]]
B = [[1.0, 0.0],
     [0.0, 1.0]]

print(multiply(A, B))
# [[2.0, 1.0], [5.0, 3.0]]

# Solving Ax = b
b = [1.0, 2.0]
x = solve(A, b)
print(x)
# [1.0, -1.0]
