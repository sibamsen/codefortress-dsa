# LeetCode 75 — Sort Colors

## Problem

Given an array `nums` containing `0`, `1`, and `2`, sort the array **in-place** so that all `0`s come first, followed by all `1`s, and then all `2`s.

You must solve the problem **without using the library's sorting function**.

### Example 1

```text
Input:  nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

## 1. Brute Force — Built-in Sorting

Approach

- The simplest way is to use Python's built-in sort() method.

However, LeetCode explicitly says that the library's sorting function cannot be used, so this is only a basic baseline and not a valid submission for the problem.

code:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

Complexity:
Time: O(n log n)
Space: O(1) auxiliary space
Problem requirement: ❌ Not allowed

## 2. Better — Counting

code:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0

        # Count the frequency of 0, 1 and 2
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Overwrite the array
        i = 0

        for _ in range(count0):
            nums[i] = 0
            i += 1

        for _ in range(count1):
            nums[i] = 1
            i += 1

        for _ in range(count2):
            nums[i] = 2
            i += 1

Complexity:
Time: O(n)
Space: O(1)
Passes: 2
Why is it not optimal?

Although the time complexity is already O(n), we need:

- One pass to count the values.
- Another pass to overwrite the array.


## 3. Optimal — Dutch National Flag Algorithm

code:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

Final Optimal Complexity:
Time:  O(n)
Space: O(1)
