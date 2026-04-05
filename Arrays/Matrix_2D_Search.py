"""
Search in 2D Matrix

Problem:
Given an m x n matrix where:
- Each row is sorted
- First element of each row is greater than last element of previous row

Return True if target exists, else False.

Algorithm:
Binary Search on virtual 1D array

Time Complexity: O(log(m*n))
Space Complexity: O(1)
"""

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2

        # Convert 1D index to 2D index
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] < target:
            left = mid + 1

        else:
            right = mid - 1

    return False


# 🔹 Example Usage
matrix = [
    [1, 3, 5, 7],
    [10,11,16,20],
    [23,30,34,60]
]

target = 16

print("Target Found:", searchMatrix(matrix, target))
