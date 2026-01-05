# Linear Algebra From Scratch

## What
A pure Python implementation of core linear algebra concepts, built from scratch without external libraries like NumPy.

## Why
 To deeply understand the mathematics behind linear algebra algorithms by implementing them by hand.

## Implemented
- **Vectors**: Addition, subtraction, scalar multiplication, dot product, magnitude.
- **Matrices**: Shape, transpose, multiplication.
- **Line Systems**: Determinant (Recursive & Row Reduction), Inverse (Gauss-Jordan), Rank, System Solver.

## Example
```python
from linear_algebra.matrices import multiply
from linear_algebra.solve_linear_systems import solve

# Matrix multiplication
A = [[2.0, 1.0], 
     [5.0, 3.0]]
B = [[1.0, 0.0], 
     [0.0, 1.0]]
print(multiply(A, B)) # [[2.0, 1.0], [5.0, 3.0]]

# Solving Ax = b
b = [1.0, 2.0]
x = solve(A, b)
print(x) # [1.0, -1.0]
```
