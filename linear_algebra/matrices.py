from typing import List, Tuple

Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    """Return the number of rows and columns of a matrix."""
    return len(A), len(A[0])


def transpose(A: Matrix) -> Matrix:
    """Return the transpose of a matrix."""
    rows, cols = shape(A)
    return [[A[i][j] for i in range(rows)] for j in range(cols)]


def multiply(A: Matrix, B: Matrix) -> Matrix:
    """Multiply two matrices A and B."""
    rows_A, cols_A = shape(A)
    rows_B, cols_B = shape(B)

    if cols_A != rows_B:
        raise ValueError("Inner dimensions must match for matrix multiplication")

    # Create result matrix initialized with zeros
    result = [[0.0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

