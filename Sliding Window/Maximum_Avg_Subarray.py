# LeetCode 643 — Maximum Average Subarray I

## Problem

Given an integer array `nums` consisting of `n` elements and an integer `k`, find a contiguous subarray whose length is exactly `k` that has the maximum average value.

Return the maximum average value.

### Example

```text
Input:
nums = [1, 12, -5, -6, 50, 3]
k = 4

Output:
12.75000

Explanation:
The subarray [12, -5, -6, 50] has the maximum average.

Sum = 12 + (-5) + (-6) + 50 = 51
Average = 51 / 4 = 12.75

# 1. Brute Force

Time Complexity
O(n × k)

Space Complexity
O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)

        max_sum = float('-inf')

        for i in range(n - k + 1):
            current_sum = 0

            for j in range(i, i + k):
                current_sum += nums[j]

            max_sum = max(max_sum, current_sum)

        return max_sum / float(k)


# 2. Better — Prefix Sum

Time Complexity
O(n)

Space Complexity
O(n)

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        max_sum = float('-inf')

        for i in range(n - k + 1):
            current_sum = prefix[i + k] - prefix[i]
            max_sum = max(max_sum, current_sum)

        return max_sum / float(k)


# 3. Optimal — Fixed-Size Sliding Window

Time Complexity
O(n)

Space Complexity
O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)

        low, high = 0, k - 1
        window_sum = 0

        # Calculate the sum of the first window
        for i in range(low, high + 1):
            window_sum += nums[i]

        max_sum = window_sum

        # Slide the window
        while high < n:
            max_sum = max(max_sum, window_sum)

            low += 1
            high += 1

            # If the window has moved beyond the array
            if high == n:
                break

            # Remove outgoing element
            window_sum -= nums[low - 1]

            # Add incoming element
            window_sum += nums[high]

        return max_sum / float(k)
