"""
Set Matrix Zeroes (LeetCode 73)

Algorithm:
In-place matrix marking using first row & column

Steps:
1. Check if first row/col has zero
2. Use them as markers
3. Apply changes
4. Handle first row/col separately

Time Complexity: O(m*n)
Space Complexity: O(1)
"""

class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Mark rows & columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Apply markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # First row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # First column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
