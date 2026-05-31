"""
Reverse Pairs (LeetCode 493)

Algorithm Used:
Modified Merge Sort

Problem:
Given an array nums, count pairs (i,j) such that:

1. i < j
2. nums[i] > 2 * nums[j]

These pairs are called Reverse Pairs.

Example:
Input:
[1,3,2,3,1]

Output:
2

Approach:
1. Divide array using Merge Sort.
2. Count reverse pairs in left half.
3. Count reverse pairs in right half.
4. Count cross reverse pairs using two pointers.
5. Merge the sorted halves.
6. Return total count.

Time Complexity:
O(N log N)

Space Complexity:
O(N)
"""

class Solution:

    def countPairs(self, arr, low, mid, high):

        right = mid + 1
        count = 0

        for i in range(low, mid + 1):

            while right <= high and arr[i] > 2 * arr[right]:
                right += 1

            count += right - (mid + 1)

        return count

    def merge(self, arr, low, mid, high):

        temp = []

        left = low
        right = mid + 1

        while left <= mid and right <= high:

            if arr[left] <= arr[right]:

                temp.append(arr[left])
                left += 1

            else:

                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def mergeSort(self, arr, low, high):

        if low >= high:
            return 0

        mid = (low + high) // 2

        count = 0

        count += self.mergeSort(arr, low, mid)

        count += self.mergeSort(arr, mid + 1, high)

        count += self.countPairs(arr, low, mid, high)

        self.merge(arr, low, mid, high)

        return count

    def reversePairs(self, nums):

        return self.mergeSort(nums, 0, len(nums) - 1)


# Driver Code
if __name__ == "__main__":

    nums = [1,3,2,3,1]

    sol = Solution()

    print("Reverse Pairs:", sol.reversePairs(nums))
