# 26. Remove Duplicates from Sorted Array

## Problem Explanation

Given a sorted array `nums`, remove the duplicates **in-place** so that each unique element appears only once.

Return the number of unique elements `k`.

The first `k` elements of `nums` must contain the unique elements in sorted order. The elements after index `k - 1` can be ignored.

Example:

```text
Input:
nums = [1,1,2]

Output:
2

Modified nums:
[1,2,_]
```

---

# Brute Force Approach

## Algorithm: Set

Use a set to store only the unique elements.

Then copy the unique elements back into the original array.

## Brute Force Code

```python
class Solution:
    def removeDuplicates(self, nums):

        unique = set(nums)

        k = 0

        for num in unique:

            nums[k] = num
            k += 1

        nums[:k] = sorted(nums[:k])

        return k
```

## Time Complexity

Creating the set:

```text
O(n)
```

Sorting the unique elements:

```text
O(n log n)
```

Therefore:

```text
Time Complexity: O(n log n)
```

## Space Complexity

The set can store up to `n` elements:

```text
Space Complexity: O(n)
```

---

# Better Approach

## Algorithm Name: Extra Array

Since the array is already sorted, duplicates are adjacent.

Traverse the array and store only unique elements in a separate array.

## Better Approach Code

```python
class Solution:
    def removeDuplicates(self, nums):

        unique = []

        for num in nums:

            if not unique or unique[-1] != num:

                unique.append(num)

        for i in range(len(unique)):

            nums[i] = unique[i]

        return len(unique)
```

## Time Complexity

Traverse the array once:

```text
O(n)
```

Copy unique elements back:

```text
O(n)
```

Therefore:

```text
Time Complexity: O(n)
```

## Space Complexity

The extra array can contain up to `n` elements:

```text
Space Complexity: O(n)
```

---

# Optimal Approach

## Algorithm Name: Two Pointers

Because the array is already sorted, duplicates are adjacent.

Use two pointers:

```text
i → position of the last unique element
j → current element being checked
```

If:

```text
nums[j] != nums[i]
```

then `nums[j]` is a new unique element.

Move `i` forward and place `nums[j]` there.

## Optimal Approach Code

```python
class Solution:
    def removeDuplicates(self, nums):

        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):

            if nums[j] != nums[i]:

                i += 1
                nums[i] = nums[j]

        return i + 1
```

## Time Complexity

The `j` pointer traverses the array once:

```text
O(n)
```

The `i` pointer only moves forward and never goes backward.

Therefore:

```text
Time Complexity: O(n)
```

## Space Complexity

Only two pointer variables are used:

```text
O(1)
```

Therefore:

```text
Space Complexity: O(1)
```
