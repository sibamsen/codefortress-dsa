"""
Minimum Number of Days to Make m Bouquets (LeetCode 1482)

Algorithm:
Binary Search on Answer

Idea:
1. Search minimum possible day.
2. For every candidate day:
      Check whether we can make m bouquets.
3. If possible:
      Store answer and try smaller day.
4. If not possible:
      Try larger day.
5. Return minimum valid day.

Time Complexity:
O(n * log(max(bloomDay)))

Space Complexity:
O(1)
"""

class Solution:

    def minDays(self, bloomDay, m, k):

        n = len(bloomDay)

        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        ans = -1

        while left <= right:

            mid = (left + right)//2

            bouquets = 0
            flowers = 0

            for day in bloomDay:

                if day <= mid:

                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            if bouquets >= m:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    bloomDay = [1,10,3,10,2]
    m = 3
    k = 1

    sol = Solution()

    print(sol.minDays(bloomDay, m, k))
