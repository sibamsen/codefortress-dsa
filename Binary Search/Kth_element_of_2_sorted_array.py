# Kth Element of Two Sorted Arrays (Binary Search)

## Problem

Given two sorted arrays `arr1` and `arr2` of sizes `n` and `m`, find the **kth smallest element** in the combined sorted order without merging the arrays.

### Example

Input

```text
arr1 = [2,3,6,7,9]

arr2 = [1,4,8,10]

k = 5
```

## Algorithm Used

### Binary Search on Partition

Instead of merging both arrays, we find the **correct partition** using Binary Search.

A partition is correct if:

1. LEFT side contains exactly **k elements**.
2. Every element on LEFT is less than or equal to every element on RIGHT.

To verify the partition, we only compare four boundary elements:

```text
arr1

l1 | r1

arr2

l2 | r2
```

Correct partition condition:

```python
l1 <= r2

and

l2 <= r1
```

Once the correct partition is found,

the answer is

```python
max(l1, l2)
```

because LEFT contains exactly **k elements**, so the largest element on LEFT is the kth smallest element.

---

## Time Complexity

Binary Search is performed only on the smaller array.

```
O(log(min(n1,n2)))
```

---

## Space Complexity

```
O(1)
```

Only constant extra variables are used.

---

## Code

```python
class Solution:

    def kthElement(self, a, b, k):

        n1 = len(a)
        n2 = len(b)

        if n1 > n2:
            return self.kthElement(b, a, k)

        low = max(0, k - n2)
        high = min(k, n1)

        while low <= high:

            partition1 = (low + high) // 2
            partition2 = k - partition1

            l1 = float('-inf') if partition1 == 0 else a[partition1 - 1]
            r1 = float('inf') if partition1 == n1 else a[partition1]

            l2 = float('-inf') if partition2 == 0 else b[partition2 - 1]
            r2 = float('inf') if partition2 == n2 else b[partition2]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)

            elif l2 > r1:
                low = partition1 + 1

            else:
                high = partition1 - 1
```

---

## Driver Code

```python
arr1 = [2,3,6,7,9]
arr2 = [1,4,8,10]

k = 5

obj = Solution()

print(obj.kthElement(arr1, arr2, k))
```

### Output

```text
6
```
