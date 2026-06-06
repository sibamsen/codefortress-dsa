"""
Find First and Last Position of Element in Sorted Array (LeetCode 34)

Algorithm Used:
Binary Search

Problem:
Given a sorted array nums and a target value,
return the first and last position of target.

If target does not exist, return [-1, -1].

Key Idea:
Use Binary Search twice.

1. First Occurrence:
   When target found,
   store answer and move LEFT.

2. Last Occurrence:
   When target found,
   store answer and move RIGHT.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):

    def firstOccurrence(self, nums, target):

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                ans = mid
                right = mid - 1

            elif nums[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return ans

    def lastOccurrence(self, nums, target):

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                ans = mid
                left = mid + 1

            elif nums[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return ans

    def searchRange(self, nums, target):

        first = self.firstOccurrence(nums, target)
        last = self.lastOccurrence(nums, target)

        return [first, last]


# Driver Code
if __name__ == "__main__":

    nums = [5,7,7,8,8,10]
    target = 8

    sol = Solution()

    print(sol.searchRange(nums, target))
