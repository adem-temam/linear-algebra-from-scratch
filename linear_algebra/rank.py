def row_reduce(A, tol=1e-9):
    A = [row[:] for row in A]
    rows, cols = len(A), len(A[0])
    r = 0

    for c in range(cols):
        if r >= rows:
            break

        pivot = None
        for i in range(r, rows):
            if abs(A[i][c]) > tol:
                pivot = i
                break

        if pivot is None:
            continue

        A[r], A[pivot] = A[pivot], A[r]

        pivot_val = A[r][c]
        A[r] = [x / pivot_val for x in A[r]]

        for i in range(rows):
            if i != r:
                factor = A[i][c]
                A[i] = [
                    A[i][j] - factor * A[r][j]
                    for j in range(cols)
                ]

        r += 1

    return A


def rank(A):
    R = row_reduce(A)
    return sum(any(abs(x) > 1e-9 for x in row) for row in R)
