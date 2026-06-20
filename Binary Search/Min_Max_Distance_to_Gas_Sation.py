"""
Minimize Max Distance to Gas Station

Algorithm:
Binary Search on Answer (Floating Point)

Observation:

Maximum Allowed Gap = D

Can all gaps be reduced to
at most D using at most k stations?

NO  NO  NO  YES  YES  YES

Pattern:

FFFFTTTT

Find First True

Time Complexity:
O(n * log(maxGap / 1e-6))

Space Complexity:
O(1)
"""

class Solution:

    def possible(self, arr, k, dist):

        stations_needed = 0

        for i in range(len(arr)-1):

            gap = arr[i+1] - arr[i]

            stations_needed += int(gap / dist)

            if gap % dist == 0:
                stations_needed -= 1

        return stations_needed <= k


    def minimiseMaxDistance(self, arr, k):

        left = 0
        right = 0

        for i in range(len(arr)-1):
            right = max(right, arr[i+1] - arr[i])

        while right - left > 1e-6:

            mid = (left + right) / 2

            if self.possible(arr, k, mid):

                right = mid

            else:

                left = mid

        return right


# Example
arr = [1,11]
k = 2

sol = Solution()

print(sol.minimiseMaxDistance(arr, k))
