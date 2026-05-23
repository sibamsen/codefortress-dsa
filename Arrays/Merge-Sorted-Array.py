"""
Merge Sorted Array (LeetCode 88)

Algorithm:
Three Pointer Technique (Backward Merge)

Problem:
Merge nums2 into nums1 in sorted order.

Why Backward Merge?
If we merge from front,
values in nums1 may get overwritten.

So we start filling from the end,
because end positions are empty.

Pointers Used:
i -> last valid element of nums1
j -> last element of nums2
k -> last index of nums1

Steps:
1. Compare nums1[i] and nums2[j]
2. Place larger element at nums1[k]
3. Move pointers backward
4. Continue until nums2 finishes

Time Complexity:
O(m + n)

Space Complexity:
O(1)
"""

class Solution:
    def merge(self, nums1, m, nums2, n):

        # Pointer for nums1 valid elements
        i = m - 1

        # Pointer for nums2
        j = n - 1

        # Pointer for final position
        k = m + n - 1

        # Compare from back
        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:

                nums1[k] = nums1[i]
                i -= 1

            else:

                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # If nums2 still has elements
        while j >= 0:

            nums1[k] = nums2[j]

            j -= 1
            k -= 1


# Driver Code
if __name__ == "__main__":

    nums1 = [1,2,3,0,0,0]
    m = 3

    nums2 = [2,5,6]
    n = 3

    sol = Solution()

    sol.merge(nums1, m, nums2, n)

    print("Merged Array:")
    print(nums1)
