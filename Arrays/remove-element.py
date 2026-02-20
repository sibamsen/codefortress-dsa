"""
LeetCode 27 - Remove Element
Difficulty: Easy

Approach:
Two-pointer technique.
Use a write pointer to place non-val elements at the front.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write
