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

def determinant_row_reduction(A):
    A = [row[:] for row in A]
    n = len(A)
    det = 1

    for i in range(n):
        pivot = i
        while pivot < n and A[pivot][i] == 0:
            pivot += 1

        if pivot == n:
            return 0

        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            det *= -1

        det *= A[i][i]
        pivot_val = A[i][i]

        for j in range(i + 1, n):
            factor = A[j][i] / pivot_val
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    return det

