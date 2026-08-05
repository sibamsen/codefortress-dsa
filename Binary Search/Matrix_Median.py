# Matrix Median (Binary Search on Answers)

## Problem Statement

Given an `R × C` matrix where each row is sorted and the total number of elements is odd, find the median.

Example:

```text
1 4 9

2 5 6

3 7 8
```

Sorted:

```text
1 2 3 4 5 6 7 8 9
```

Median:

```text
5
```

---

# Brute Force

1. Flatten the matrix.
2. Sort the array.
3. Return:

```python
arr[(R * C) // 2]
```

Time Complexity:

```text
O((R × C) log(R × C))
```

Space Complexity:

```text
O(R × C)
```

---

# Optimal Approach: Binary Search on Answers

Search space:

```python
low = minimum element

high = maximum element
```

Required median index:

```python
required = (R * C) // 2
```

Binary search:

```python
while low <= high:

    mid = (low + high) // 2

    count = 0

    for every row:

        count += bisect_right(row, mid)

    if count <= required:

        low = mid + 1

    else:

        high = mid - 1

return low
```

---

# Why bisect_right()?

```python
from bisect import bisect_right
```

Example:

```python
arr = [1, 4, 9]

bisect_right(arr, 5)
```

Insertion:

```text
1 4 |5| 9
```

Output:

```text
2
```

Meaning:

```text
2 elements are ≤ 5
```

---

# Code

```python
from bisect import bisect_right


class Solution:

    def median(self, matrix, R, C):

        low = float('inf')

        for i in range(R):

            low = min(low, matrix[i][0])

        high = float('-inf')

        for i in range(R):

            high = max(high, matrix[i][C - 1])

        required = (R * C) // 2

        while low <= high:

            mid = (low + high) // 2

            count = 0

            for i in range(R):

                count += bisect_right(matrix[i], mid)

            if count <= required:

                low = mid + 1

            else:

                high = mid - 1

        return low
```

---

# Time Complexity

```text
O(log(maximum - minimum) × R × log(C))
```

---

# Space Complexity

```text
O(1)
```
