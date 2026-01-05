def shape(A):
    return len(A), len(A[0])


def transpose(A):
    rows, cols = shape(A)
    return [[A[i][j] for i in range(rows)] for j in range(cols)]


def multiply(A, B):
    rows_A, cols_A = shape(A)
    rows_B, cols_B = shape(B)

    if cols_A != rows_B:
        raise ValueError("Invalid dimensions for matrix multiplication")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result
