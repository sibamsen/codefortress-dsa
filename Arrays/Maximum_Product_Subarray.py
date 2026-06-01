"""
Maximum Product Subarray (LeetCode 152)

Algorithm Used:
Dynamic Programming (Optimized Kadane Variant)

Problem:
Given an integer array nums, find the contiguous subarray
having the largest product and return the product.

Example:
Input:
[2,3,-2,4]
 
Output:
6

Explanation:
Subarray [2,3] has product 6 which is the maximum.

Approach:
1. Maintain current maximum product ending at index.
2. Maintain current minimum product ending at index.
3. Minimum is needed because:
   Negative × Negative = Positive.
4. For every element:
   - Compute new maximum product.
   - Compute new minimum product.
5. Update answer using maximum product.
6. Return answer.

Time Complexity:
O(N)

Space Complexity:
O(1)
"""

class Solution:
    def maxProduct(self, nums):

        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for num in nums[1:]:

            temp_max = max_prod

            max_prod = max(
                num,
                num * max_prod,
                num * min_prod
            )

            min_prod = min(
                num,
                num * temp_max,
                num * min_prod
            )

            result = max(result, max_prod)

        return result


# Driver Code
if __name__ == "__main__":

    nums = [2, 3, -2, 4]

    sol = Solution()

    print("Maximum Product =", sol.maxProduct(nums))
