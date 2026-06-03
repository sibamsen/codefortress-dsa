"""
Binary Search (LeetCode 704)

Algorithm Used:
Binary Search

Problem:
Given a sorted array nums and a target value,
return its index if found, otherwise return -1.

Example:
Input:
nums = [-1,0,3,5,9,12]
target = 9

Output:
4

Approach:
1. Maintain left and right pointers.
2. Find middle element.
3. If target equals middle element:
      return index.
4. If target is smaller:
      search left half.
5. If target is larger:
      search right half.
6. Repeat until found or search space becomes empty.

Time Complexity:
O(log N)

Space Complexity:
O(1)
"""

class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                right = mid - 1

            else:
                left = mid + 1

        return -1


# Driver Code
if __name__ == "__main__":

    nums = [-1,0,3,5,9,12]
    target = 9

    sol = Solution()

    print("Index =", sol.search(nums, target))
