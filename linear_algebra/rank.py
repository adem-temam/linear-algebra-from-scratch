from typing import List

Matrix = List[List[float]]

def row_reduce(A: Matrix, tol: float = 1e-9) -> Matrix:
    """Return the row-reduced form of matrix A."""
    # Create copy
    M = [row[:] for row in A]
    rows = len(M)
    if rows == 0:
        return []
    cols = len(M[0])
    
    r = 0 # Current pivot row

    for c in range(cols):
        if r >= rows:
            break

        # Find pivot in current column
        pivot = None
        for i in range(r, rows):
            if abs(M[i][c]) > tol:
                pivot = i
                break

        if pivot is None:
            continue

        # Swap rows
        M[r], M[pivot] = M[pivot], M[r]

        # Normalize pivot row
        pivot_val = M[r][c]
        M[r] = [x / pivot_val for x in M[r]]

        # Eliminate other rows
        for i in range(rows):
            if i != r:
                factor = M[i][c]
                M[i] = [
                    M[i][j] - factor * M[r][j]
                    for j in range(cols)
                ]

        r += 1

    return M


def rank(A: Matrix) -> int:
    """Return the rank of matrix A."""
    R = row_reduce(A)
    return sum(any(abs(x) > 1e-9 for x in row) for row in R)

