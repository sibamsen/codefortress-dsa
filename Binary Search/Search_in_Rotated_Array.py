"""
Search in Rotated Sorted Array (LeetCode 33)

Algorithm Used:
Modified Binary Search

Problem:
Given a sorted array rotated at some pivot,
find the index of target.

If target is not present,
return -1.

Key Observation:
At any point,
either left half or right half
will always be sorted.

Use this sorted half to decide
which side to continue searching.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half sorted
            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Driver Code
if __name__ == "__main__":

    nums = [4,5,6,7,0,1,2]
    target = 0

    sol = Solution()

    print(sol.search(nums, target))
