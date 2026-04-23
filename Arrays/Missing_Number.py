"""
Missing Number (LeetCode)

Problem:
Given an array containing n distinct numbers in the range [0, n],
return the missing number.

Algorithm:
Mathematical Sum Formula

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        # Expected sum of numbers from 0 to n
        total_sum = n * (n + 1) // 2

        # Actual sum of array elements
        actual_sum = 0
        for num in nums:
            actual_sum += num

        # Missing number
        return total_sum - actual_sum


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    
    sol = Solution()
    result = sol.missingNumber(nums)
    
    print("Missing number:", result)
