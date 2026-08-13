# 167. Two Sum II - Input Array Is Sorted

## Problem Explanation

Given a 1-indexed array `numbers` that is sorted in non-decreasing order, find two numbers whose sum is equal to the given `target`.

Return the 1-based indices of the two numbers.

Example:

```text
numbers = [2, 7, 11, 15]
target = 9
```

The pair is:

```text
2 + 7 = 9
```

Therefore, the answer is:

```text
[1, 2]
```

---

# Brute Force Approach

Check every possible pair using two nested loops.

## Brute Force Code

```python
class Solution:
    def twoSum(self, numbers, target):

        n = len(numbers)

        for i in range(n):

            for j in range(i + 1, n):

                if numbers[i] + numbers[j] == target:

                    return [i + 1, j + 1]
```

## Time Complexity

Outer loop runs `n` times:

```text
O(n)
```

For each element, the inner loop can also run up to `n` times:

```text
O(n)
```

Therefore:

```text
Time Complexity: O(n²)
```

## Space Complexity

Only constant extra variables are used:

```text
Space Complexity: O(1)
```

---

# Better Approach

## Algorithm Name: HashMap

Store previously visited numbers in a HashMap.

For every element, calculate:

```text
needed = target - current
```

If `needed` already exists in the HashMap, we have found the required pair.

## Better Approach Code

```python
class Solution:
    def twoSum(self, numbers, target):

        hashmap = {}

        for i in range(len(numbers)):

            needed = target - numbers[i]

            if needed in hashmap:

                return [hashmap[needed] + 1, i + 1]

            hashmap[numbers[i]] = i
```

## Time Complexity

We traverse the array once:

```text
O(n)
```

HashMap lookup takes `O(1)` average time.

Therefore:

```text
Time Complexity: O(n)
```

## Space Complexity

The HashMap can store up to `n` elements:

```text
Space Complexity: O(n)
```

---

# Optimal Approach

## Algorithm Name: Two Pointer

Since the array is already sorted, use two pointers:

```text
i = left pointer
j = right pointer
```

If the current sum is smaller than the target, move the left pointer forward.

If the current sum is greater than the target, move the right pointer backward.

## Optimal Approach Code

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
```

## Time Complexity

The left pointer moves only forward and the right pointer moves only backward.

Each element is visited at most once.

Therefore:

```text
Time Complexity: O(n)
```

## Space Complexity

Only two pointers and one variable are used:

```text
Space Complexity: O(1)
```
