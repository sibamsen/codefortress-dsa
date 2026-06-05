"""
Search Insert Position (LeetCode 35)

Algorithm Used:
Binary Search (Lower Bound)

Problem:
Given a sorted array and a target value,
return the index if target exists.

Otherwise return the index where it should
be inserted while maintaining sorted order.

Key Idea:
Search Insert Position is exactly the
Lower Bound of target.

Lower Bound:
First index where nums[i] >= target

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums, target):

        n = len(nums)

        left = 0
        right = n - 1

        ans = n

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] >= target:

                ans = mid
                right = mid - 1

            else:

                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    nums = [1, 3, 5, 6]
    target = 2

    sol = Solution()

    print("Insert Position:", sol.searchInsert(nums, target))
