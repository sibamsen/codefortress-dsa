# Search a 2D Matrix (LeetCode 74)

## Problem

Given an `m × n` matrix where:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Determine whether a target value exists in the matrix.

Return `True` if found, otherwise return `False`.

---

## Approach

The given properties allow us to imagine the matrix as a single sorted array.

Instead of actually flattening the matrix, perform Binary Search on the imaginary indices.

Whenever a middle index is obtained, convert it into the corresponding matrix position.

### Mapping Formula

```python
row = mid // m
col = mid % m
```

where `m` is the number of columns.

---

## Algorithm

1. Find number of rows (`n`) and columns (`m`).
2. Initialize

```python
low = 0
high = n * m - 1
```

3. Perform Binary Search.
4. Calculate

```python
mid = (low + high) // 2
```

5. Convert index

```python
row = mid // m
col = mid % m
```

6. Compare

```python
matrix[row][col]
```

with target.

- If equal, return `True`.
- If smaller, search right half.
- Otherwise, search left half.

7. If loop finishes, return `False`.

---

## Time Complexity

```text
O(log(n × m))
```

Equivalent to

```text
O(log n + log m)
```

---

## Space Complexity

```text
O(1)
```

---

## Code

```python
class Solution:
    def searchMatrix(self, matrix, target):

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:

            mid = (low + high) // 2

            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False
```

## Driver Code

```python
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 16

obj = Solution()
print(obj.searchMatrix(matrix, target))
```

### Output

```text
True
```
