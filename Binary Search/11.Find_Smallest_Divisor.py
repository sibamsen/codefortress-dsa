"""
Find the Smallest Divisor Given a Threshold (LeetCode 1283)

Algorithm:
Binary Search on Answer

Idea:
1. Search divisor from 1 to max(nums).
2. For every divisor:
      Calculate total sum of ceil(num/divisor).
3. If total <= threshold:
      Store answer and try smaller divisor.
4. Else:
      Try larger divisor.
5. Return smallest valid divisor.

Time Complexity:
O(n * log(max(nums)))

Space Complexity:
O(1)
"""

class Solution(object):

    def smallestDivisor(self, nums, threshold):

        left = 1
        right = max(nums)

        ans = right

        while left <= right:

            mid = (left + right)//2

            total = 0

            for num in nums:
                total += (num + mid - 1)//mid

            if total <= threshold:

                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    nums = [1,2,5,9]
    threshold = 6

    sol = Solution()

    print(sol.smallestDivisor(nums, threshold))
