# Second Smallest & Second Largest
# ---------------------------------------
# Problem:
# Given an array, find the second smallest and second largest element.
#
# Example:
# Input: [1, 4, 3, 2, 5, 1, 7]
# Output: (2, 5)
#
# Approach:
# 1. First pass → find smallest & largest
# 2. Second pass → find second smallest & second largest
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def second_smallest_largest(arr):
    n = len(arr)

    if n < 2:
        return "Not Enough Elements"

    smallest = float('inf')
    second_smallest = float('inf')

    largest = float('-inf')
    second_largest = float('-inf')

    # First pass → find smallest & largest
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Second pass → find second smallest & second largest
    for num in arr:
        if smallest < num < second_smallest:
            second_smallest = num

        if largest > num > second_largest:
            second_largest = num

    return second_smallest, second_largest


# 🔹 Example Usage
arr = [1, 4, 3, 2, 5, 1, 7]
print("Second Smallest & Largest:", second_smallest_largest(arr))
