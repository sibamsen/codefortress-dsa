# LeetCode 1929: Concatenation of Array

## 1. Problem Statement

Given an integer array `nums` of length `n`, create a new array `ans` of length `2 * n` such that:

- `ans[i] == nums[i]`
- `ans[i + n] == nums[i]`

for every index `0 <= i < n`.

In simple words, concatenate the given array with itself and return the resulting array.

### Example

**Input:**
```python
nums = [1, 2, 1]
```

**Output:**
```python
[1, 2, 1, 1, 2, 1]
```

**Explanation:**

The original array is `[1, 2, 1]`.

Concatenating it with itself:

```text
[1, 2, 1] + [1, 2, 1]
```

Result:
```text
[1, 2, 1, 1, 2, 1]
```

---

## 2. Approach / Algorithm Name

**Array Traversal (Single Loop)**

### Algorithm Steps

1. Find the length of the input array `n`.
2. Create a new array `ans` of size `2 * n`, initialized with zeros.
3. Traverse the original array using a loop.
4. Copy each element into two positions:
   - First half: `ans[i] = nums[i]`
   - Second half: `ans[i + n] = nums[i]`
5. Return the resulting array.

---

## 3. Time and Space Complexity

### Time Complexity: O(n)

- Calculating the length: `O(1)`.
- Initializing an array of size `2 * n`: `O(n)`.
- Traversing the original array once: `O(n)`.
- Each iteration performs two constant-time assignments: `O(1)`.

Therefore:

`O(n) + O(n) + O(n) = O(n)`

### Space Complexity: O(n)

- A new array of size `2 * n` is created.
- The extra space grows linearly with the input size.

Therefore, **Space Complexity = O(n)**.

---

## 4. Code

```python
class Solution:
    def getConcatenation(self, nums):

        n = len(nums)

        ans = [0] * (2 * n)

        for i in range(n):

            ans[i] = nums[i]

            ans[i + n] = nums[i]

        return ans
```

---

## 5. Driver Code

```python
if __name__ == "__main__":

    nums = list(map(int, input("Enter array: ").split()))

    sol = Solution()

    result = sol.getConcatenation(nums)

    print("Concatenated Array:", result)
```

---

## 6. Output

**Input:**
```text
Enter array: 1 2 1
```

**Output:**
```text
Concatenated Array: [1, 2, 1, 1, 2, 1]
```

---

### Python Shortcut

Python also provides a simpler way to concatenate lists:

```python
class Solution:
    def getConcatenation(self, nums):
        return nums + nums
```

Both implementations have:

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
