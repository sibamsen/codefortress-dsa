"""
Pascal’s Triangle II (LeetCode 119)

Algorithm:
Combinatorics (nCr) using iterative relation

Key Idea:
C(n, r) = C(n, r-1) * (n - r + 1) / r

Steps:
1. Start with [1]
2. Use previous value to compute next
3. Build row iteratively

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def getRow(self, rowIndex):
        row = [1]
        prev = 1

        for r in range(1, rowIndex + 1):
            curr = prev * (rowIndex - r + 1) // r
            row.append(curr)
            prev = curr

        return row


# Driver Code
if __name__ == "__main__":
    rowIndex = int(input("Enter row index: "))
    sol = Solution()
    print("Pascal Row:", sol.getRow(rowIndex))
