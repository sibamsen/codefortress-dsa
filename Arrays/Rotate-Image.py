"""
Rotate Image (LeetCode 48)

Algorithm:
Transpose + Reverse Rows

Steps:
1. Swap matrix[i][j] with matrix[j][i]
2. Reverse each row

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows
        for i in range(n):
            matrix[i].reverse()


# Driver Code
if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    Solution().rotate(matrix)
    print(matrix)
