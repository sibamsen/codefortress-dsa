# Find the Row with Maximum Number of 1's

## Problem

Given a binary matrix where every row is sorted in non-decreasing order, return the index of the row having the maximum number of `1`s.

If multiple rows have the same number of `1`s, return the smallest row index.

If no row contains any `1`, return `-1`.

---

## Approach

Since each row is sorted, all `0`s appear before all `1`s.

Instead of counting all `1`s, find the **first occurrence of `1`** using **Lower Bound (Binary Search)**.

If the first `1` is found at index `idx`, then

```text
Number of Ones = Total Columns - idx
```

Repeat this process for every row and keep track of the row with the maximum number of `1`s.

---

## Algorithm

1. Find number of rows (`n`) and columns (`m`).
2. Initialize

```python
maxi = 0
answer = -1
```

3. Traverse every row.
4. Find the lower bound of `1`.
5. Calculate

```python
ones = m - idx
```

6. If

```python
ones > maxi
```

update

```python
maxi = ones
answer = current row
```

7. Return answer.

---

## Time Complexity

```text
O(n log m)
```

- Binary Search on each row → `O(log m)`
- Total rows → `n`

---

## Space Complexity

```text
O(1)
```

---

## Code

```python
class Solution:
    def lowerBound(self, row, x):
        low = 0
        high = len(row) - 1
        ans = len(row)

        while low <= high:
            mid = (low + high) // 2

            if row[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def rowWithMax1s(self, mat):
        n = len(mat)
        m = len(mat[0])

        maxi = 0
        answer = -1

        for i in range(n):
            idx = self.lowerBound(mat[i], 1)
            ones = m - idx

            if ones > maxi:
                maxi = ones
                answer = i

        return answer
```

## Driver Code

```python
mat = [
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1]
]

obj = Solution()
print(obj.rowWithMax1s(mat))
```

### Output

```text
1
```
