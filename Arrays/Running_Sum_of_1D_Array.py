# LeetCode 1480: Running Sum of 1D Array

## 1. Problem Statement

Given an array of integers `nums`, calculate the running sum of the array.

The running sum at index `i` is defined as:

```python
runningSum[i] = sum(nums[0] ... nums[i])
```

In simple words, each element in the resulting array is the sum of all elements from index `0` to the current index.

Return the running sum of `nums`.

### Example 1

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```python
[1, 3, 6, 10]
```

**Explanation:**

```text
Index 0: 1
Index 1: 1 + 2 = 3
Index 2: 1 + 2 + 3 = 6
Index 3: 1 + 2 + 3 + 4 = 10
```

### Example 2

**Input:**
```python
nums = [1, 1, 1, 1, 1]
```

**Output:**
```python
[1, 2, 3, 4, 5]
```

---

## 2. Approach / Algorithm Name

**Prefix Sum (In-place Modification)**

### Algorithm Steps

1. Find the length of the array `n`.
2. Start traversing the array from index `1`.
3. Add the previous element to the current element:

   ```python
   nums[i] = nums[i] + nums[i-1]
   ```

4. Repeat until the last element.
5. Return the modified array.

**Key Idea:**

The previous element already contains the sum of all elements before the current index.

Therefore, adding it to the current element gives the running sum.

---

## 3. Time and Space Complexity

### Time Complexity: O(n)

- Finding the array length takes `O(1)`.
- The loop traverses the array from index `1` to `n-1`.
- Each iteration performs one addition and one assignment, both taking `O(1)` time.

Therefore:

`O(1) + O(n) = O(n)`

### Space Complexity: O(1)

- The original array is modified directly.
- No additional array or data structure is created.
- Only a constant amount of extra space is used.

Therefore, **Space Complexity = O(1)**.

---

## 4. Code

```python
class Solution:
    def runningSum(self, nums):

        n = len(nums)

        for i in range(1, n):

            nums[i] += nums[i-1]

        return nums
```

---

## 5. Driver Code

```python
if __name__ == "__main__":

    nums = list(map(int, input("Enter array: ").split()))

    sol = Solution()

    result = sol.runningSum(nums)

    print("Running Sum:", result)
```

---

## 6. Output

**Input:**
```text
Enter array: 1 2 3 4
```

**Output:**
```text
Running Sum: [1, 3, 6, 10]
```

### Dry Run

Initial array:

```text
nums = [1, 2, 3, 4]
```

| Iteration | Calculation | Updated Array |
|---|---|---|
| Initial | — | `[1, 2, 3, 4]` |
| i = 1 | 2 + 1 = 3 | `[1, 3, 3, 4]` |
| i = 2 | 3 + 3 = 6 | `[1, 3, 6, 4]` |
| i = 3 | 4 + 6 = 10 | `[1, 3, 6, 10]` |

**Final Answer:**
```python
[1, 3, 6, 10]
```
