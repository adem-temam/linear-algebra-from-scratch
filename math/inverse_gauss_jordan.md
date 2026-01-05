# Matrix Inverse Using Gauss–Jordan Elimination

## Goal
Given a square matrix A, find its inverse A⁻¹ such that:

A · A⁻¹ = I

where I is the identity matrix.

---

## Key Idea
Instead of trying to compute the inverse directly, we transform the matrix A
into the identity matrix using row operations.  
At the same time, those same operations transform the identity matrix into A⁻¹.

---

## Augmented Matrix
We start by forming an augmented matrix:

[A | I]

where:
- A is the original matrix
- I is the identity matrix of the same size

---

## Row Operations Used
The Gauss–Jordan method allows only three operations:
1. Swap two rows
2. Multiply a row by a non-zero scalar
3. Add a multiple of one row to another row

These operations do NOT change the solution of a system.

---

## Algorithm Steps
1. Start with the augmented matrix [A | I]
2. For each column:
   - Make the diagonal entry (pivot) equal to 1
   - Make all other entries in that column equal to 0
3. Continue until the left side becomes the identity matrix

At that point, the right side is the inverse A⁻¹.

---

## When the Inverse Does Not Exist
If at any step a pivot cannot be made non-zero, the matrix is singular.

This means:
- det(A) = 0
- A⁻¹ does not exist

---

## Why This Works
Row operations correspond to multiplying by elementary matrices.
Applying them to A transforms it into I.
Applying the same operations to I builds A⁻¹.

---

## Summary
- Gauss–Jordan elimination converts [A | I] → [I | A⁻¹]
- Works only for invertible (non-singular) matrices
- Efficient and conceptually simple
