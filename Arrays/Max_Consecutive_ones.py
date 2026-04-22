"""
Max Consecutive Ones (LeetCode 485)

Problem:
Given a binary array nums, return the maximum number of consecutive 1's.

Algorithm:
Linear Traversal (Counting Streak)

Approach:
- Maintain a count of current consecutive 1's
- Reset count when 0 is encountered
- Track maximum count throughout

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter binary array: ").split()))
    
    sol = Solution()
    result = sol.findMaxConsecutiveOnes(nums)
    
    print("Max consecutive ones:", result)
