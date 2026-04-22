"""
Union of Two Sorted Arrays

Problem:
Return union of two sorted arrays without duplicates.

Algorithm:
Two Pointer Merge Technique

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

class Solution:
    def unionArray(self, nums1, nums2):
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1

            else:
                if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j += 1

        while i < len(nums1):
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1

        while j < len(nums2):
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1

        return result


# Driver Code
if __name__ == "__main__":
    nums1 = list(map(int, input("Enter nums1: ").split()))
    nums2 = list(map(int, input("Enter nums2: ").split()))

    sol = Solution()
    print("Union:", sol.unionArray(nums1, nums2))
