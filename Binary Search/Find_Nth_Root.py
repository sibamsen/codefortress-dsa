"""
Find Nth Root of a Number

Algorithm:
Binary Search on Answer

Key Idea:
1. Search possible roots from 1 to M.
2. Calculate mid^N.
3. If mid^N == M:
      Found the exact Nth root.
4. If mid^N < M:
      Root must be larger.
      Move right.
5. If mid^N > M:
      Root must be smaller.
      Move left.
6. If no exact root is found,
      return -1.

Time Complexity: O(log M)
Space Complexity: O(1)
"""

class Solution:

    def nthRoot(self, n, m):

        left, right = 1, m

        while left <= right:

            mid = (left + right)//2

            value = pow(mid, n)

            if value == m:
                return mid

            elif value < m:
                left = mid + 1

            else:
                right = mid - 1

        return -1


# Driver Code
if __name__ == "__main__":

    N = 3
    M = 27

    sol = Solution()

    print("Nth Root =", sol.nthRoot(N, M))
