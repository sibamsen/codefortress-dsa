"""
Find Peak Element (LeetCode 162)

Algorithm:
Binary Search

Key Idea:
1. Compare nums[mid] with nums[mid+1].

2. If nums[mid] < nums[mid+1]:
      We are moving uphill.
      Peak must exist on right side.
      Move left = mid + 1.

3. Otherwise:
      We are moving downhill.
      Peak exists on left side including mid.
      Move right = mid.

4. When left == right,
      that index is a peak.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):

    def findPeakElement(self, nums):

        left, right = 0, len(nums)-1

        while left < right:

            mid = (left + right)//2

            if nums[mid] < nums[mid+1]:
                left = mid + 1

            else:
                right = mid

        return left


# Driver Code
if __name__ == "__main__":

    nums = [1,2,3,1]

    sol = Solution()

    print("Peak Index:", sol.findPeakElement(nums))
