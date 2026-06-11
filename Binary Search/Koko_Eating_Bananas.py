"""
Koko Eating Bananas (LeetCode 875)

Algorithm:
Binary Search on Answer

Key Idea:
1. Search possible eating speeds from 1 to max(piles).
2. For every speed, calculate total hours required.
3. If hours <= h:
      Speed works.
      Store answer and try smaller speed.
4. If hours > h:
      Speed too slow.
      Try larger speed.
5. Return minimum valid speed.

Time Complexity: O(n * log(max(piles)))
Space Complexity: O(1)
"""

class Solution:

    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        ans = right

        while left <= right:

            mid = (left + right)//2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1)//mid

            if hours <= h:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    piles = [3,6,7,11]
    h = 8

    sol = Solution()

    print("Minimum Eating Speed =", sol.minEatingSpeed(piles, h))
