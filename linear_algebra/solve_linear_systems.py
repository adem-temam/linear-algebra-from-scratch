from inverse import inverse

def solve(A, b):
    A_inv = inverse(A)
    return [sum(A_inv[i][j] * b[j] for j in range(len(b)))
            for i in range(len(A))]
