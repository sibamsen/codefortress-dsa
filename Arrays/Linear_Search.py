"""
Linear Search

Problem:
Find the first occurrence index of target in array.
Return -1 if not found.

Algorithm:
Linear Search

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    target = int(input("Enter target: "))

    sol = Solution()
    result = sol.linearSearch(nums, target)

    print("Index:", result)
