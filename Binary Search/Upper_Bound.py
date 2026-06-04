"""
Upper Bound

Problem:
Given a sorted array nums and an integer x,
find the first index where nums[i] > x.

If no such index exists, return len(nums).

Algorithm Used:
Binary Search (Upper Bound)

Key Idea:
Whenever nums[mid] > x,
store mid as a possible answer and search left
for a smaller valid index.

Whenever nums[mid] <= x,
search right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def upperBound(self, nums, x):

        n = len(nums)

        left = 0
        right = n - 1

        ans = n

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] > x:

                ans = mid
                right = mid - 1

            else:

                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    nums = [1, 2, 2, 2, 3]
    x = 2

    sol = Solution()

    print("Upper Bound Index:", sol.upperBound(nums, x))
