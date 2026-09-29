"""
Count Occurrences in a Sorted Array

Algorithm Used:
Binary Search

Problem:
Given a sorted array and a target value,
find how many times the target appears.

Key Idea:
1. Find first occurrence of target.
2. Find last occurrence of target.
3. Count = last - first + 1

If target is not present:
return 0

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:

    def firstOccurrence(self, arr, target):

        left = 0
        right = len(arr) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] == target:

                ans = mid
                right = mid - 1

            elif arr[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return ans

    def lastOccurrence(self, arr, target):

        left = 0
        right = len(arr) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] == target:

                ans = mid
                left = mid + 1

            elif arr[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return ans

    def countOccurrences(self, arr, target):

        first = self.firstOccurrence(arr, target)

        if first == -1:
            return 0

        last = self.lastOccurrence(arr, target)

        return last - first + 1


# Driver Code
if __name__ == "__main__":

    arr = [0,0,1,1,1,2,3]
    target = 1

    sol = Solution()

    print("Count =", sol.countOccurrences(arr, target))
