"""
Largest Element in Array

Problem:
Find the maximum element in an array.

Approach 1:
Linear Traversal (Recommended)

Approach 2:
Two Pointer Comparison (Alternative)

Time Complexity: O(n)
Space Complexity: O(1)
"""

# -------------------------------
# Approach 1: Linear Scan
# -------------------------------
def largestElement(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


# -------------------------------
# Approach 2: Two Pointer
# -------------------------------
def largestElement_two_pointer(nums):
    left, right = 0, len(nums) - 1
    largest = nums[0]

    while left <= right:
        if nums[left] > nums[right]:
            largest = max(largest, nums[left])
            right -= 1
        else:
            largest = max(largest, nums[right])
            left += 1

    return largest


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))

    print("Largest (Linear):", largestElement(nums))
    print("Largest (Two Pointer):", largestElement_two_pointer(nums))
