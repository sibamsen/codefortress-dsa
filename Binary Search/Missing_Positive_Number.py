"""
Kth Missing Positive Number (LeetCode 1539)

Algorithm:
Binary Search

Observation:
missing_before_index =
arr[i] - (i + 1)

Use Binary Search to find the first position where:

missing_before_index >= k

Final Answer:
answer = left + k

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

class Solution:

    def findKthPositive(self, arr, k):

        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = (left + right)//2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1

            else:
                right = mid - 1

        return left + k


# Driver Code
if __name__ == "__main__":

    arr = [2,3,4,7,11]
    k = 5

    sol = Solution()

    print(sol.findKthPositive(arr, k))
