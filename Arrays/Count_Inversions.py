"""
Count Inversions in an Array

Algorithm:
Merge Sort + Inversion Counting

Problem:
Given an array, count the number of inversions.

An inversion is a pair (i, j) such that:

i < j
nums[i] > nums[j]

Example:

Input:
[2,3,7,1,3,5]

Output:
5

Inversions:
(2,1)
(3,1)
(7,1)
(7,3)
(7,5)

Key Idea:

While merging two sorted halves:

Left  = [2,3,7]
Right = [1,3,5]

If:

left[i] > right[j]

then every remaining element from left[i]
to left[end] will also be greater than right[j].

Therefore:

count += (mid - left + 1)

instead of counting one by one.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
"""

class Solution:

    def merge(self, arr, low, mid, high):

        temp = []

        left = low
        right = mid + 1

        count = 0

        while left <= mid and right <= high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1

            else:
                temp.append(arr[right])

                count += (mid - left + 1)

                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return count

    def mergeSort(self, arr, low, high):

        count = 0

        if low >= high:
            return count

        mid = (low + high) // 2

        count += self.mergeSort(arr, low, mid)

        count += self.mergeSort(arr, mid + 1, high)

        count += self.merge(arr, low, mid, high)

        return count

    def numberOfInversions(self, nums):

        return self.mergeSort(nums, 0, len(nums) - 1)


# Driver Code
if __name__ == "__main__":

    nums = list(map(int, input("Enter array: ").split()))

    S = Solution()

    print("Number of Inversions:", S.numberOfInversions(nums))
