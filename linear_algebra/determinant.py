def determinant(A):
    n = len(A)

    if n != len(A[0]):
        raise ValueError("Matrix must be square")

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    det = 0
    for col in range(n):
        submatrix = [
            row[:col] + row[col+1:]
            for row in A[1:]
        ]
        det += ((-1) ** col) * A[0][col] * determinant(submatrix)

    return det
