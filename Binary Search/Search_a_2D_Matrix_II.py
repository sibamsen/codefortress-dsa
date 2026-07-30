# LeetCode 240: Search a 2D Matrix II

## Problem Statement

You are given an `m x n` integer matrix with the following properties:

- Each row is sorted in ascending order from left to right.
- Each column is sorted in ascending order from top to bottom.

Return `true` if the target exists in the matrix, otherwise return `false`.

---

# Approach 1: Binary Search on Every Row

## Algorithm

1. Traverse each row.
2. Check whether the target can exist in the current row.

   ```
   row[0] <= target <= row[m-1]
   ```

3. If yes, perform Binary Search on that row.
4. If the target is found, return `True`.
5. Otherwise, continue to the next row.
6. If all rows are checked, return `False`.

---

## Code

```python
class Solution:
    def searchMatrix(self, matrix, target):

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):

            if matrix[i][0] <= target <= matrix[i][m - 1]:

                low = 0
                high = m - 1

                while low <= high:

                    mid = (low + high) // 2

                    if matrix[i][mid] == target:
                        return True

                    elif matrix[i][mid] < target:
                        low = mid + 1

                    else:
                        high = mid - 1

        return False
```

---

## Dry Run

Matrix:

```
[
 [1, 4, 7, 11, 15],
 [2, 5, 8, 12, 19],
 [3, 6, 9, 16, 22]
]
```

Target:

```
16
```

Row 0:

```
1 <= 16 <= 15
```

Skip.

Row 1:

```
2 <= 16 <= 19
```

Binary Search:

```
mid = 2 → 8 < 16
mid = 3 → 12 < 16
mid = 4 → 19 > 16
```

Target not found.

Row 2:

```
mid = 2 → 9 < 16
mid = 3 → 16 == 16
```

Found.

---

## Time Complexity

Binary Search on one row:

```
O(log m)
```

For `n` rows:

```
O(n log m)
```

---

## Space Complexity

```
O(1)
```

---

# Approach 2: Staircase Search (Optimal)

## Algorithm

1. Start from the top-right corner.
2. Compare the current element with the target.
3. If equal, return `True`.
4. If current is smaller, move down.
5. If current is larger, move left.
6. Continue until you leave the matrix.
7. If the target is not found, return `False`.

---

## Code

```python
class Solution:
    def searchMatrix(self, matrix, target):

        n = len(matrix)
        m = len(matrix[0])

        row = 0
        col = m - 1

        while row < n and col >= 0:

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                row += 1

            else:
                col -= 1

        return False
```

---

## Dry Run

Matrix:

```
[
 [1, 4, 7, 11, 15],
 [2, 5, 8, 12, 19],
 [3, 6, 9, 16, 22],
 [10,13,14,17,24],
 [18,21,23,26,30]
]
```

Target:

```
16
```

Step 1:

```
15 < 16
```

Move down.

Step 2:

```
19 > 16
```

Move left.

Step 3:

```
12 < 16
```

Move down.

Step 4:

```
16 == 16
```

Found.

---

## Time Complexity

Maximum downward moves:

```
n
```

Maximum left moves:

```
m
```

Total:

```
O(n + m)
```

---

## Space Complexity

```
O(1)
```

---

# Comparison

| Algorithm                    | Time Complexity | Space Complexity |
| ---------------------------- | --------------- | ---------------- |
| Binary Search on Every Row   | O(n log m)      | O(1)             |
| Staircase Search (Optimal)   | O(n + m)        | O(1)             |

**Optimal Approach:** Staircase Search
