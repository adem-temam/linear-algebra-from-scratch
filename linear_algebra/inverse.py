from determinant import determinant

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def inverse(A):
    n = len(A)

    if determinant(A) == 0:
        raise ValueError("Matrix is not invertible")

    A = [row[:] for row in A]
    I = identity(n)

    for i in range(n):
        pivot = A[i][i]
        for j in range(n):
            A[i][j] /= pivot
            I[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    I[k][j] -= factor * I[i][j]

    return I
