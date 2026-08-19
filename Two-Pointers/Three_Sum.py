# LeetCode 15 — 3Sum

## Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`
* `i != k`
* `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution must not contain duplicate triplets.

### Example

```text
Input:
nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Approach

### 1. Brute Force

Use three nested loops to check every possible combination of three elements.

```text
i → first element
j → second element
k → third element
```

For every combination, check:

```text
nums[i] + nums[j] + nums[k] == 0
```

This takes `O(n³)` time, so it is too slow for large inputs.

---

### 2. Better Approach — Fix One + Two Sum

Fix one element `nums[i]`.

We then need to find two other numbers such that:

```text
nums[i] + x + y = 0
```

Therefore:

```text
x + y = -nums[i]
```

So the remaining problem becomes a **Two Sum** problem.

A hash set can be used to find the required pair in `O(n)` for each fixed element.

Overall:

```text
Time:  O(n²)
Space: O(n)
```

---

### 3. Optimal Approach — Sorting + Two Pointers

First sort the array.

```python
nums.sort()
```

After sorting, fix one element and use two pointers:

```text
left  → i + 1
right → n - 1
```

Calculate:

```text
total = nums[i] + nums[left] + nums[right]
```

Then:

* If `total < 0`, move `left` forward to increase the sum.
* If `total > 0`, move `right` backward to decrease the sum.
* If `total == 0`, we found a valid triplet.

Because the array is sorted, we can efficiently move the pointers instead of checking every pair.

---

## Handling Duplicates

Duplicate triplets are not allowed.

For the fixed element:

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

This skips duplicate values for `nums[i]`.

After finding a valid triplet, we also skip duplicate values for `left` and `right`.

This ensures that every unique triplet appears only once.

---

## Python Solution

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        n = len(nums)

        for i in range(n):

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    # Found a valid triplet
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
```

---

## Dry Run

```text
Input:
[-1, 0, 1, 2, -1, -4]
```

After sorting:

```text
[-4, -1, -1, 0, 1, 2]
```

### i = 0

```text
nums[i] = -4
```

Try different `left` and `right` values.

The sum remains negative, so `left` keeps moving right.

No valid triplet is found for `-4`.

---

### i = 1

```text
nums[i] = -1
```

Initially:

```text
left = 2
right = 5
```

Calculate:

```text
-1 + (-1) + 2 = 0
```

Triplet found:

```text
[-1, -1, 2]
```

Move both pointers.

Now:

```text
-1 + 0 + 1 = 0
```

Another triplet:

```text
[-1, 0, 1]
```

---

### i = 2

```text
nums[2] == nums[1]
```

Both are `-1`.

Therefore:

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

We skip this iteration to avoid generating duplicate triplets.

---

## Why Two Pointers Work

The array is sorted:

```text
small -----------------> large
```

If:

```text
total < 0
```

we need a larger value, so:

```python
left += 1
```

If:

```text
total > 0
```

we need a smaller value, so:

```python
right -= 1
```

This allows us to search for pairs in linear time for every fixed `i`.

---

## Complexity

### Time Complexity

Sorting:

```text
O(n log n)
```

For every element, the two pointers scan the remaining array:

```text
O(n²)
```

Therefore:

```text
O(n log n) + O(n²)
= O(n²)
```

### Space Complexity

Ignoring the output array:

```text
O(1) auxiliary space
```

---

## Key Pattern

The main pattern to remember is:

```text
3Sum
  ↓
Fix one element
  ↓
Reduce to Two Sum
  ↓
Sort the array
  ↓
Use Two Pointers
```

Whenever you see a problem involving **three numbers**, think:

> Can I fix one number and reduce the remaining problem to Two Sum?

This pattern is also useful for problems such as **4Sum** and **3Sum Closest**.

---

## LeetCode

**Problem:** 15. 3Sum

**Pattern:** Sorting + Two Pointers

**Difficulty:** Medium

**Time:** `O(n²)`

**Space:** `O(1)` auxiliary space
