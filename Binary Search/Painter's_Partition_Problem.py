"""
Painter's Partition Problem

Algorithm:
Binary Search on Answer

Observation:

Maximum Board Length Assigned
to a Painter = mid

Can all boards be painted
using at most A painters?

NO  NO  NO  YES  YES  YES

Pattern:

FFFFTTTT

Find First True

Time Complexity:
O(n * log(sum(C)))

Space Complexity:
O(1)
"""

class Solution:

    def canPaint(self, boards, painters_allowed, limit):

        painters = 1
        curr_length = 0

        for board in boards:

            if curr_length + board <= limit:

                curr_length += board

            else:

                painters += 1
                curr_length = board

        return painters <= painters_allowed


    def paint(self, A, B, C):

        left = max(C)
        right = sum(C)

        ans = right

        while left <= right:

            mid = (left + right)//2

            if self.canPaint(C, A, mid):

                ans = mid
                right = mid - 1

            else:

                left = mid + 1

        return (ans * B) % 10000003


# Example
A = 2
B = 5
C = [10,20,30,40]

sol = Solution()

print(sol.paint(A, B, C))
