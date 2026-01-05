from typing import List

Matrix = List[List[float]]

def determinant_recursive(A: Matrix) -> float:
    """Compute determinant using recursive Laplace expansion (slow for large n)."""
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Matrix must be square")

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    det = 0.0
    for col in range(n):
        submatrix = [
            row[:col] + row[col+1:]
            for row in A[1:]
        ]
        det += ((-1) ** col) * A[0][col] * determinant_recursive(submatrix)

    return det


def determinant_row_reduction(A: Matrix) -> float:
    """Compute determinant using row reduction (Gaussian elimination)."""
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Matrix must be square")

    # Create a copy to avoid modifying the input
    M = [row[:] for row in A]
    det = 1.0

    for i in range(n):
        # Find pivot
        pivot = i
        while pivot < n and M[pivot][i] == 0:
            pivot += 1

        if pivot == n:
            return 0.0

        if pivot != i:
            M[i], M[pivot] = M[pivot], M[i]
            det *= -1

        det *= M[i][i]
        pivot_val = M[i][i]

        for j in range(i + 1, n):
            factor = M[j][i] / pivot_val
            for k in range(i, n):
                M[j][k] -= factor * M[i][k]

    return det

# Default determinant function
determinant = determinant_recursive
