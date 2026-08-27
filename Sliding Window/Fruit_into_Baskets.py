# LeetCode 904 — Fruit Into Baskets

## Problem

You are given an integer array `fruits`, where `fruits[i]` represents the type of fruit produced by the `i-th` tree.

You have **2 baskets**.

- Each basket can hold only **one type of fruit**.
- There is no limit on how many fruits of that type a basket can hold.
- You must start at some tree and move only to the right.
- You must pick exactly one fruit from every tree you visit.
- Once you encounter a third fruit type, you must stop.

### In simple words

Find the **longest contiguous subarray containing at most 2 distinct values**.

Example:

```text
fruits = [1, 2, 1, 2, 3]

Longest valid subarray:

[1, 2, 1, 2]

Distinct fruit types = {1, 2}
Length = 4

Answer = 4


# 1. Brute Force — Nested Loops + Set
Algorithm

Generate every possible subarray.

Time Complexity

O(n²)

There are O(n²) possible subarrays, and set insertion takes O(1) average time.

Space Complexity

O(n)

The set can contain up to n distinct fruit types.

class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        max_len = 0

        for i in range(n):

            distinct = set()

            for j in range(i, n):

                distinct.add(fruits[j])

                if len(distinct) > 2:
                    break

                max_len = max(max_len, j - i + 1)

        return max_len


# 2. Better — HashMap + Fixed Starting Point
Algorithm

Instead of using a set, use a HashMap to maintain the frequency of each fruit type.

Time Complexity

O(n²)

We consider every possible starting index and expand the right boundary.

Space Complexity

O(n)

The HashMap can contain up to n distinct elements.

code:
class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        max_len = 0

        for i in range(n):

            freq = {}

            for j in range(i, n):

                freq[fruits[j]] = freq.get(fruits[j], 0) + 1

                if len(freq) > 2:
                    break

                max_len = max(max_len, j - i + 1)

        return max_len


# 3. Optimal — HashMap + Variable-Size Sliding Window

Time Complexity

O(n)

The right pointer moves forward n times.

The left pointer also moves forward at most n times in total.

Therefore:

O(n + n)
= O(2n)
= O(n)
Space Complexity

O(1)

The HashMap contains at most 2 distinct fruit types after the window is adjusted.

More generally, it would be O(k), but here k = 2.

code:
class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)

        freq = {}
        left = 0
        max_len = 0

        for right in range(n):

            # Add current fruit
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            # More than 2 distinct fruit types
            while len(freq) > 2:

                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1

            # Current window has at most 2 distinct types
            count = right - left + 1
            max_len = max(max_len, count)

        return max_len
