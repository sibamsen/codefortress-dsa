# LeetCode 259 — 3Sum Smaller

Given an integer array `nums` and an integer `target`, return the number of index triplets `(i, j, k)` such that:

```text
i < j < k
and
nums[i] + nums[j] + nums[k] < target


# 1. Brute Force

Time Complexity

O(n³)

Space Complexity

O(1)

Code:

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1

        return count


2. Better Approach — Sorting + Binary Search
Approach

Sort the array.

Fix the first two elements nums[i] and nums[j].

We need:
nums[i] + nums[j] + nums[k] < target

Therefore:
nums[k] < target - nums[i] - nums[j]

Time Complexity

O(n² log n)

Sorting → O(n log n)
Two nested loops → O(n²)
Binary search → O(log n)

Overall:

O(n² log n)
Space Complexity

O(1) auxiliary space.

Code

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):

                required = target - nums[i] - nums[j]

                left = j + 1
                right = n

                # Find first index where nums[k] >= required
                while left < right:
                    mid = (left + right) // 2

                    if nums[mid] < required:
                        left = mid + 1
                    else:
                        right = mid

                # All indices from j + 1 to left - 1 are valid
                count += left - j - 1

        return count


## 3. Optimal Approach — Sorting + Two Pointers

Time Complexity

O(n²)

Sorting → O(n log n)
For every i, the two pointers move at most n times → O(n²)

Overall:

O(n²)
Space Complexity

O(1) auxiliary space.

code:

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        count = 0

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    # Since the array is sorted,
                    # every index from left + 1 to right
                    # will also form a valid triplet.
                    count += right - left
                    left += 1

                else:
                    right -= 1

        return count
