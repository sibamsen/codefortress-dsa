"""
Capacity To Ship Packages Within D Days (LeetCode 1011)

Algorithm:
Binary Search on Answer

Idea:
1. Search ship capacity from max(weights) to sum(weights).
2. For every capacity:
      Calculate how many days are needed.
3. If days_needed <= days:
      Store answer and try smaller capacity.
4. Else:
      Need larger capacity.
5. Return minimum valid capacity.

Time Complexity:
O(n * log(sum(weights)))

Space Complexity:
O(1)
"""

class Solution(object):

    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        ans = right

        while left <= right:

            mid = (left + right)//2

            days_needed = 1
            current_load = 0

            for weight in weights:

                if current_load + weight <= mid:
                    current_load += weight

                else:
                    days_needed += 1
                    current_load = weight

            if days_needed <= days:

                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5

    sol = Solution()

    print(sol.shipWithinDays(weights, days))
