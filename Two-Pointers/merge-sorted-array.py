"""
LeetCode 88 - Merge Sorted Array
Difficulty: Easy

Approach:
Two pointers from the end to avoid overwriting elements.
We fill nums1 from the back using the largest available element.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # last valid element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # last index of nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining nums2 elements if any
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
