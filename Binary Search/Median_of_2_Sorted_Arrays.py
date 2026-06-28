## Problem
'''Median of Two Sorted Arrays (LeetCode 4)

## Approach
- Use **Binary Search on the smaller array** to find the correct partition.
- For every partition in `nums1`, calculate the partition in `nums2` automatically.
- Find the four boundary elements:
  - `l1` = Last element on the left of `nums1`
  - `r1` = First element on the right of `nums1`
  - `l2` = Last element on the left of `nums2`
  - `r2` = First element on the right of `nums2`
- If `l1 <= r2` and `l2 <= r1`, the partition is correct.
- If the total number of elements is even, return `(max(l1, l2) + min(r1, r2)) / 2`.
- Otherwise, return `max(l1, l2)`.
- If `l2 > r1`, move Binary Search to the right.
- Otherwise, move Binary Search to the left.

## Time Complexity
O(log(min(m, n)))

## Space Complexity
O(1)
'''
## Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)

        low = 0
        high = n1

        while low <= high:

            partition1 = (low + high) // 2
            partition2 = (n1 + n2 + 1) // 2 - partition1

            l1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            r1 = float('inf') if partition1 == n1 else nums1[partition1]

            l2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            r2 = float('inf') if partition2 == n2 else nums2[partition2]

            if l1 <= r2 and l2 <= r1:

                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)

            elif l2 > r1:
                low = partition1 + 1

            else:
                high = partition1 - 1
```

## Driver Code

```python
nums1 = [1, 2]
nums2 = [3, 4]

obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))
```
