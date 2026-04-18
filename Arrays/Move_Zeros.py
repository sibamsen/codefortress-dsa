"""
Move Zeroes (LeetCode 283)

Problem:
Move all zeros to the end while maintaining order of non-zero elements.

Algorithm:
Two Pointer (Slow-Fast)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    Solution().moveZeroes(nums)
    print(nums)
