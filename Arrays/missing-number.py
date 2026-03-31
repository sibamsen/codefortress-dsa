"""
Problem: Missing Number

Given an array containing n distinct numbers in the range [0, n],
return the only number missing from the array.

Example:
Input: nums = [3, 0, 1]
Output: 2

Approach:
We use the mathematical formula for sum of first n natural numbers:
Expected Sum = n * (n + 1) // 2

Then subtract the actual sum of array elements.

Missing Number = Expected Sum - Actual Sum

Time Complexity: O(n)
Space Complexity: O(1)
"""

def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# 🔹 Example Usage
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print("Missing Number is:", missing_number(nums))
