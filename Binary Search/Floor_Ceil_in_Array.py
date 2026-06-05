"""
Floor and Ceil in Sorted Array

Algorithm Used:
Binary Search

Problem:
Given a sorted array and a value x,
find:

Floor = Largest element <= x
Ceil  = Smallest element >= x

If floor or ceil does not exist,
return -1 for that value.

Key Idea:
If nums[mid] > x:
Current element can be a ceil.
Store it and search left.

If nums[mid] < x:
Current element can be a floor.
Store it and search right.

If nums[mid] == x:
Both floor and ceil are x.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def getFloorAndCeil(self, nums, x):

        n = len(nums)

        floor = -1
        ceil = -1

        left = 0
        right = n - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == x:
                return nums[mid], nums[mid]

            elif nums[mid] > x:

                ceil = nums[mid]
                right = mid - 1

            else:

                floor = nums[mid]
                left = mid + 1

        return floor, ceil


# Driver Code
if __name__ == "__main__":

    nums = [3, 4, 4, 7, 8, 10]
    x = 5

    sol = Solution()

    floor, ceil = sol.getFloorAndCeil(nums, x)

    print("Floor:", floor)
    print("Ceil :", ceil)
