# LeetCode 1901: Find a Peak Element II

## Problem Statement

A peak element in a 2D matrix is an element that is strictly greater than all of its adjacent neighbors (left, right, top, and bottom).

Given an `m x n` matrix `mat`, return the position `[row, col]` of any peak element.

You may assume that the matrix is surrounded by an outer perimeter with the value `-1`.

---

# Algorithm: Binary Search on Columns

## Approach

1. Apply Binary Search on columns.
2. Find the middle column.
3. Find the maximum element in the middle column.
4. Compare the maximum element with its left and right neighbors.
5. If the maximum element is greater than both neighbors, return its position.
6. If the right neighbor is greater, move right.
7. Otherwise, move left.
8. Repeat until a peak element is found.

---

## Intuition

Consider the matrix:

```
10   20   15

21   30   14

7    16   32
```

Initially:

```python
low = 0
high = 2
```

Find the middle column:

```python
mid = (low + high) // 2
```

```
mid = 1
```

Middle column:

```
20

30

16
```

Maximum element:

```
30
```

Position:

```
[1, 1]
```

Neighbors:

```
left = 21

right = 14
```

Since:

```
30 > 21

30 > 14
```

Therefore:

```python
return [1, 1]
```

---

## Cases

### Case 1: Peak Found

```
left = 21

current = 30

right = 14
```

```
30 > 21

30 > 14
```

Return:

```python
[maxRow, mid]
```

---

### Case 2: Move Right

```
left = 21

current = 25

right = 30
```

```
30 > 25
```

Move right:

```python
low = mid + 1
```

---

### Case 3: Move Left

```
left = 40

current = 25

right = 20
```

```
40 > 25
```

Move left:

```python
high = mid - 1
```

---

## Code

```python
class Solution:

    def findPeakGrid(self, mat):

        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1

        while low <= high:

            mid = (low + high) // 2

            maxRow = 0

            for i in range(n):

                if mat[i][mid] > mat[maxRow][mid]:

                    maxRow = i

            left = -1
            right = -1

            if mid - 1 >= 0:
                left = mat[maxRow][mid - 1]

            if mid + 1 < m:
                right = mat[maxRow][mid + 1]

            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:

                return [maxRow, mid]

            elif right > mat[maxRow][mid]:

                low = mid + 1

            else:

                high = mid - 1

        return [-1, -1]
```

---

## Dry Run

Matrix:

```
10   20   15

21   30   14

7    16   32
```

Initial values:

```python
low = 0
high = 2
```

### Iteration 1

```python
mid = (0 + 2) // 2
```

```
mid = 1
```

Middle column:

```
20

30

16
```

Maximum element:

```
30
```

Position:

```
[1, 1]
```

Neighbors:

```
left = 21

right = 14
```

Check:

```
30 > 21

30 > 14
```

Peak found.

Return:

```python
[1, 1]
```

---

## Time Complexity

Finding the maximum element in one column:

```
O(n)
```

Binary Search on columns:

```
O(log m)
```

Overall complexity:

```
O(n * log m)
```

---

## Space Complexity

Only constant extra space is used:

```
O(1)
```

---

## Complexity Analysis

| Operation | Complexity |
| ---------- | ---------- |
| Find maximum in a column | O(n) |
| Binary Search on columns | O(log m) |
| Total Time Complexity | O(n log m) |
| Space Complexity | O(1) |

---

## Key Idea

1. Pick the middle column.
2. Find the maximum element in that column.
3. Compare it with the left and right neighbors.
4. Move in the direction of the larger neighbor.
5. Repeat until a peak element is found.
