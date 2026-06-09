"""
Single Element in a Sorted Array (LeetCode 540)

Algorithm:
Modified Binary Search

Key Idea:
1. Before the single element,
   pairs start at EVEN indexes.

2. After the single element,
   pairs start at ODD indexes.

3. Use Binary Search to detect where
   this pattern breaks.

4. Make mid even before checking pair.

5. If nums[mid] == nums[mid+1]:
      Single element lies on right side.
      Move left = mid + 2.

6. Otherwise:
      Single element lies on left side
      including mid.
      Move right = mid.

7. When left == right,
      nums[left] is the answer.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):

    def singleNonDuplicate(self, nums):

        left, right = 0, len(nums)-1

        while left < right:

            mid = (left + right)//2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


# Driver Code
if __name__ == "__main__":

    nums = [1,1,2,3,3,4,4,8,8]

    sol = Solution()

    print("Single Element:", sol.singleNonDuplicate(nums))
