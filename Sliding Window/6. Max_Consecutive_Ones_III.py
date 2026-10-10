# LeetCode 1004 — Max Consecutive Ones III

## Problem

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s into `1`s.

### Example

```text
Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

# 1. Brute Force — Nested Loops

Time Complexity

O(n²)

There can be O(n²) possible subarrays.

Space Complexity

O(1)

Only a few variables are used.

Code:
class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        res = 0

        for i in range(n):
            zero_count = 0

            for j in range(i, n):

                if nums[j] == 0:
                    zero_count += 1

                if zero_count > k:
                    break

                res = max(res, j - i + 1)

        return res


# 2. Better — Prefix Sum

Time Complexity

O(n²)

We still check every possible pair of starting and ending positions.

Space Complexity

O(n)

For the prefix sum array.

Code:
class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)

        prefix = [0] * (n + 1)

        # Build prefix sum of zeros
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == 0 else 0)

        res = 0

        for left in range(n):

            for right in range(left, n):

                zero_count = prefix[right + 1] - prefix[left]

                if zero_count <= k:
                    res = max(res, right - left + 1)

        return res


# 3. Optimal — Variable-Size Sliding Window

Time Complexity

O(n)

Both left and right move only forward.

right → at most n movements
left  → at most n movements

Total = O(n + n)
      = O(n)
Space Complexity

O(1)

Only a few variables are used.

Code:
class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)

        zero_count = 0
        res = 0
        left = 0

        for right in range(n):

            # Add current element to the window
            if nums[right] == 0:
                zero_count += 1

            # Window has more than k zeros
            while zero_count > k:

                # Remove nums[left] from the window
                if nums[left] == 0:
                    zero_count -= 1

                left += 1

            # Current window is valid
            res = max(res, right - left + 1)

        return res
