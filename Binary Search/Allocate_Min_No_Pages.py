"""
Allocate Minimum Number of Pages

Algorithm:
Binary Search on Answer

Observation:

Maximum Pages = mid

Can all books be allocated
using at most m students?

NO  NO  NO  YES  YES  YES

Pattern:

FFFFTTTT

Find First True

Time Complexity:
O(n * log(sum(nums)))

Space Complexity:
O(1)
"""

class Solution:

    def canAllocate(self, nums, m, limit):

        students = 1
        pages = 0

        for book in nums:

            if pages + book <= limit:

                pages += book

            else:

                students += 1
                pages = book

        return students <= m


    def findPages(self, nums, m):

        n = len(nums)

        if m > n:
            return -1

        left = max(nums)
        right = sum(nums)

        ans = right

        while left <= right:

            mid = (left + right)//2

            if self.canAllocate(nums, m, mid):

                ans = mid
                right = mid - 1

            else:

                left = mid + 1

        return ans


# Driver Code
if __name__ == "__main__":

    nums = [12,34,67,90]
    m = 2

    sol = Solution()

    print(sol.findPages(nums, m))
