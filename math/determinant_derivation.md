# Determinant: Concept and Computation

## What Is the Determinant?
The determinant is a scalar value associated with a square matrix.

It tells us:
- Whether a matrix is invertible
- How the matrix scales space
- Whether rows (or columns) are linearly independent

If det(A) = 0 → matrix is NOT invertible.

---

## Determinant of Small Matrices

### 1×1 Matrix
det([a]) = a

### 2×2 Matrix
For:
[a  b]
[c  d]

det = ad − bc

---

## Recursive Definition (Laplace Expansion)

For an n×n matrix, the determinant can be computed by expanding along a row:

det(A) = Σ (-1)^(i+j) · aᵢⱼ · det(submatrix)

where the submatrix is formed by removing row i and column j.

This method is:
- Simple
- Easy to understand
- Computationally expensive for large matrices

---

## Determinant via Row Reduction

To compute determinants efficiently, we use row-reduction.

### Important Rules
1. Swapping two rows → determinant changes sign
2. Multiplying a row by k → determinant is multiplied by k
3. Adding a multiple of one row to another → determinant unchanged

---

## Upper Triangular Matrix
After row-reduction, a matrix can be made upper triangular.

For such a matrix:
det(A) = product of diagonal entries

---

## Algorithm Summary
1. Reduce the matrix to upper triangular form
2. Track row swaps (sign changes)
3. Multiply diagonal elements
4. Apply sign changes if needed

---

## Why This Works
Row-reduction simplifies the matrix while preserving determinant behavior.
Once in triangular form, the determinant becomes trivial to compute.

---

## Summary
- Recursive method is conceptually simple
- Row-reduction method is efficient
- det(A) = 0 ⇔ matrix is singular
- Determinant connects linear algebra and geometry
