"""
Maximum Subarray (Kadane's Algorithm)

Problem:
Find the contiguous subarray with the largest sum.

Approach:
Kadane's Algorithm

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return max_sum


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    sol = Solution()
    print("Maximum Subarray Sum:", sol.maxSubArray(nums))
