"""
Two Sum (LeetCode 1)

Problem:
Given an array nums and a target,
return indices of the two numbers such that they add up to target.

Approach:
HashMap (Dictionary)

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        mp = {}  # value → index

        for i in range(len(nums)):
            complement = target - nums[i]

            # Check if complement already exists
            if complement in mp:
                return [mp[complement], i]

            # Store current number with index
            mp[nums[i]] = i


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    target = int(input("Enter target: "))

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Indices:", result)
