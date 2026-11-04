"""
Find Square Root of a Number

Algorithm:
Binary Search on Answer

Key Idea:
1. Search possible square roots from 1 to n.
2. If mid² <= n:
      mid can be an answer.
      Store it and search larger values.
3. If mid² > n:
      mid cannot be answer.
      Search smaller values.
4. Last valid answer is floor(sqrt(n)).

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:

    def floorSqrt(self, n: int) -> int:

        left, right = 1, n
        ans = 0

        while left <= right:

            mid = (left + right)//2

            if mid * mid <= n:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans


# Driver Code
if __name__ == "__main__":

    n = 36

    sol = Solution()

    print("Floor Square Root =", sol.floorSqrt(n))
