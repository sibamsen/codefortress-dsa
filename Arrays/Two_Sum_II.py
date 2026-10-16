# 167. Two Sum II - Input Array Is Sorted

## Problem Understanding

Given a **1-indexed, sorted array** `numbers` and an integer `target`, find two distinct elements whose sum equals the target.

Return their indices using **1-based indexing**.

The array is already sorted in non-decreasing order, and the solution must use **constant extra space**.

### Example

**Input:**
```python
numbers = [2, 7, 11, 15]
target = 9
```

**Output:**
```python
[1, 2]
```

**Explanation:**

`numbers[0] + numbers[1] = 2 + 7 = 9`

Their 1-based indices are `1` and `2`.

---

## Time and Space Complexity

### Time Complexity: O(n)

- Initialize two pointers at the beginning and end of the array.
- In each iteration, move either the left pointer forward or the right pointer backward.
- Each pointer moves in only one direction, so the total number of iterations is at most `n`.

Therefore, **Time Complexity = O(n)**.

### Space Complexity: O(1)

- Only two pointers and one variable for the current sum are used.
- No additional data structure is required.

Therefore, **Space Complexity = O(1)**.

---

## Code

```python
class Solution:
    def twoSum(self, numbers, target):

        i = 0
        j = len(numbers) - 1

        while i < j:

            total = numbers[i] + numbers[j]

            if total == target:
                return [i + 1, j + 1]

            elif total < target:
                i += 1

            else:
                j -= 1


# Driver Code
if __name__ == "__main__":
    numbers = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    sol = Solution()
    result = sol.twoSum(numbers, target)

    print("Indices:", result)
```
