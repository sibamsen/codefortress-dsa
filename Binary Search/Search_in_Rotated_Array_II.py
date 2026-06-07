"""
Search in Rotated Sorted Array II (LeetCode 81)

Algorithm:
Modified Binary Search

Key Idea:
1. One half of a rotated sorted array is always sorted.
2. Use Binary Search to identify the sorted half.
3. Check whether target lies inside the sorted half.
4. Duplicates can hide the pivot.
5. When nums[left] == nums[mid] == nums[right],
   shrink both ends:
        left += 1
        right -= 1

Time Complexity:
Average Case  : O(log n)
Worst Case    : O(n)  (due to duplicates)

Space Complexity:
O(1)
"""

class Solution(object):

    def search(self, nums, target):

        left, right = 0, len(nums)-1

        while left <= right:

            mid = (left + right)//2

            if nums[mid] == target:
                return True

            # Duplicate confusion case
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

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

        return False


# Driver Code
if __name__ == "__main__":

    nums = [1,0,1,1,1]
    target = 0

    sol = Solution()

    print(sol.search(nums, target))
