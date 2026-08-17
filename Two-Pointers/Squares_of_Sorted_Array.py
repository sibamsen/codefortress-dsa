# Squares of a Sorted Array (LeetCode 977)

## 1. Brute Force
> Algorithm: Square each element and then sort the array  
> Time Complexity: O(n log n)  
> Space Complexity: O(1) auxiliary space

```python
class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        nums.sort()

        return nums

## 2. Better Approach
> Algorithm: Split negative and non-negative numbers + Two-Pointer Merge
> Time Complexity: O(n)
> Space Complexity: O(n)

class Solution:
    def sortedSquares(self, nums):
        negative = []
        positive = []

        # Separate negative and non-negative numbers
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        # Start from the negative number closest to zero
        i = len(negative) - 1

        # Start from the smallest non-negative number
        j = 0

        result = []

        # Merge the two sorted sequences of squares
        while i >= 0 and j < len(positive):
            if abs(negative[i]) < positive[j]:
                result.append(negative[i] ** 2)
                i -= 1
            else:
                result.append(positive[j] ** 2)
                j += 1

        # Add remaining negative numbers
        while i >= 0:
            result.append(negative[i] ** 2)
            i -= 1

        # Add remaining non-negative numbers
        while j < len(positive):
            result.append(positive[j] ** 2)
            j += 1

        return result

## 3. Optimal Approach
> Algorithm: Two Pointers from Both Ends
> Time Complexity: O(n)
> Space Complexity: O(n) for the output array

class Solution:
    def sortedSquares(self, nums):
        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1

        # Fill the result array from right to left
        for k in range(n - 1, -1, -1):

            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            # The larger square will go at the current position
            if left_square > right_square:
                result[k] = left_square
                left += 1
            else:
                result[k] = right_square
                right -= 1

        return result
