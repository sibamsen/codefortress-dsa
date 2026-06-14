"""
Split Array Largest Sum

Algorithm:
Binary Search on Answer

Observation:

Maximum Allowed Subarray Sum = mid

Can array be split into
at most k subarrays?

NO  NO  NO  YES  YES  YES

Pattern:

FFFFTTTT

Find First True

Time Complexity:
O(n * log(sum(nums)))

Space Complexity:
O(1)
"""

class Solution(object):

    def canSplit(self, nums, k, limit):

        subarrays = 1
        curr_sum = 0

        for num in nums:

            if curr_sum + num <= limit:

                curr_sum += num

            else:

                subarrays += 1
                curr_sum = num

        return subarrays <= k

    def splitArray(self, nums, k):

        left = max(nums)
        right = sum(nums)

        ans = right

        while left <= right:

            mid = (left + right)//2

            if self.canSplit(nums, k, mid):

                ans = mid
                right = mid - 1

            else:

                left = mid + 1

        return ans


# Example
nums = [7,2,5,10,8]
k = 2

sol = Solution()
print(sol.splitArray(nums, k))
