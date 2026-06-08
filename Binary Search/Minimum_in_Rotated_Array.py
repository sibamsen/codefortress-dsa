"""
Find Minimum in Rotated Sorted Array (LeetCode 153)

Algorithm:
Modified Binary Search

Key Idea:
1. Compare nums[mid] with nums[right].
2. If nums[mid] > nums[right]:
      Minimum lies in right half.
      Move left = mid + 1.
3. Otherwise:
      Minimum lies at mid or left half.
      Move right = mid.
4. When left == right,
      that position stores the minimum element.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):

    def findMin(self, nums):

        left, right = 0, len(nums)-1

        while left < right:

            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        return nums[left]


# Driver Code
if __name__ == "__main__":

    nums = [4,5,6,7,0,1,2]

    sol = Solution()

    print("Minimum Element:", sol.findMin(nums))
