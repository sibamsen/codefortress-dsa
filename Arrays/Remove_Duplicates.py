"""
Remove Duplicates from Sorted Array

Problem:
Remove duplicates in-place and return count of unique elements.

Algorithm:
Two Pointer (Slow & Fast)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted elements: ").split()))
    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Unique count:", k)
    print("Modified array:", nums[:k])
