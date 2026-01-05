from linear_algebra.matrices import multiply, transpose, shape
from linear_algebra.solve_linear_systems import solve
from linear_algebra.determinant import determinant
from linear_algebra.inverse import inverse
from linear_algebra.rank import rank

def main():
    print("=== Linear Algebra From Scratch Demo ===\n")

    # 1. Matrix Multiplication
    print("--- 1. Matrix Multiplication ---")
    A = [[2.0, 1.0],
         [5.0, 3.0]]
    B = [[1.0, 0.0],
         [0.0, 1.0]]
    print(f"Matrix A: {A}")
    print(f"Matrix B: {B}")
    product = multiply(A, B)
    print(f"A * B = {product}")
    print()

    # 2. Solving Linear Systems
    print("--- 2. Solving Linear Systems (Ax = b) ---")
    b = [1.0, 2.0]
    print(f"Vector b: {b}")
    x = solve(A, b)
    print(f"Solution x: {x}")
    print("Verification (A * x):", multiply(A, [[val] for val in x])) # x as column vector
    print()

    # 3. Determinant
    print("--- 3. Determinant ---")
    det_A = determinant(A)
    print(f"Determinant of A: {det_A}")
    C = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    print(f"Matrix C (Singular): {C}")
    print(f"Determinant of C: {determinant(C)}")
    print()

    # 4. Inverse
    print("--- 4. Matrix Inverse ---")
    try:
        inv_A = inverse(A)
        print(f"Inverse of A:\n{inv_A}")
        print("Check (A * A_inv):", multiply(A, inv_A))
    except ValueError as e:
        print(e)
    print()

    # 5. Rank
    print("--- 5. Rank ---")
    print(f"Rank of A: {rank(A)}")
    print(f"Rank of C: {rank(C)}")
    print()

if __name__ == "__main__":
    main()
