"""
Problem: Intersection of Two Arrays

Approach:
Store elements of first array in set
Check elements of second array

Time Complexity: O(n + m)
Space Complexity: O(n)
"""

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

set1 = set(nums1)
result = set()

for n in nums2:
    if n in set1:
        result.add(n)

print(list(result))
