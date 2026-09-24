# LeetCode 209 — Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If there is no such subarray, return `0`.

---

# 1. Brute Force

## Time Complexity

`O(n²)`

## Space Complexity

`O(1)`

## Code

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        min_length = float('inf')

        for i in range(n):
            current_sum = 0

            for j in range(i, n):
                current_sum += nums[j]

                if current_sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break

        if min_length == float('inf'):
            return 0

        return min_length
```

---

# 2. Better — Prefix Sum + Binary Search

## Approach

Create a prefix sum array.

For every starting index `i`, we need to find the smallest index `j` such that:

```text
prefix[j] - prefix[i] >= target
```

Therefore:

```text
prefix[j] >= prefix[i] + target
```

Since all elements are positive, the prefix sum array is sorted, so we can use binary search to find the smallest valid `j`.

## Time Complexity

`O(n log n)`

* Building prefix sum → `O(n)`
* Binary search for every starting index → `O(n log n)`

## Space Complexity

`O(n)`

The prefix sum array requires `O(n)` extra space.

## Code

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        min_length = float('inf')

        for i in range(n):
            required = prefix[i] + target

            left = i + 1
            right = n

            while left <= right:
                mid = (left + right) // 2

                if prefix[mid] >= required:
                    min_length = min(min_length, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1

        if min_length == float('inf'):
            return 0

        return min_length
```

---

# 3. Optimal — Variable-Size Sliding Window

## Approach

Use two pointers:

```text
left
right
```

Expand the window by moving `right` until:

```text
current_sum >= target
```

Once the condition is satisfied, the current window is valid.

Now shrink the window from the left while it remains valid:

```text
current_sum -= nums[left]
left += 1
```

Every time the window is valid, update the minimum length.

Because all numbers are positive:

* Moving `right` increases the sum.
* Moving `left` decreases the sum.

This allows us to find the minimum-length valid subarray in `O(n)` time.

## Time Complexity

`O(n)`

Although there is a `for` loop and a `while` loop, each element is added to the window once and removed at most once.

Therefore:

```text
O(n + n) = O(n)
```

## Space Complexity

`O(1)`

Only a few variables are used.

## Code

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min( 
                    min_length,
                    right - left + 1
                )

                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length
```

