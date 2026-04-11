"""
Pascal's Triangle

Problem:
Generate first numRows of Pascal's Triangle

Algorithm:
Dynamic Programming (Row Construction)

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution(object):
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]

            result.append(row)

        return result


# Driver Code
if __name__ == "__main__":
    numRows = int(input("Enter number of rows: "))
    sol = Solution()
    print(sol.generate(numRows))
