# Binary Matrix Computation
[toc]

## What is binary matrix?
Binary matrix is a matrix with all the entries restriced in $$$F_2$$$ which is the finite field with only two elements 0 and 1. Thus, each entry of the matrix can only take the value 0 and 1.

The arithmetic operations on finite field $$$\mathbb{F}_2$$$ follow the rules:
- $$$0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, 1 + 1 = 0$$$
- $$$0 \times 0 = 0, 0 \times 1 = 1, 1\times 0 = 0, 1\times 1 = 1$$$

## What is this modular about?
This project contains a modular [binmatrix.py](https://github.com/xiangzejun/binary_matrix/blob/master/binmatrix.py). This modular computes some properties of binary matrices. To be Specific:
1. Compute the Rank of the given binary matrix.
2. Compute the determinant of the given binary matrix if this matrix is a square matrix.
3. Compute the inverse of a given binary matrix if this matrix is a square matrix and full rank.

All the arithmetic operations are on the finite field $$$\mathbb{F}_2$$$.
[test.py](https://github.com/xiangzejun/binary_matrix/blob/master/test.py) tests the modular by a given binary matrix.
## How to used the modular?
This module defines a python class `class BinMatrix:`. If `m` is a binary matrix, you can instantiate a `BinMatrix` object by `matrix = BinMatrix(m)`. Then you can compute:
1. `matrix.rank()` returns the Rank of the binary matrix.
2. `matrix.det()` returns the determinant of the binary matrix.
3. `matrix.inv()` returns the inverse of the binary matrix.

















