"""
Spiral Matrix (LeetCode 54)

Algorithm:
Boundary Traversal

Steps:
1. Define top, bottom, left, right
2. Traverse in spiral order
3. Shrink boundaries

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def spiralOrder(self, matrix):
        result = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


# Driver Code
if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(Solution().spiralOrder(matrix))
