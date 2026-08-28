# LeetCode 3 — Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without duplicate characters.

Example:

```text
Input:  s = "abcabcbb"
Output: 3

Explanation:
The longest substrings without repeating characters are:
"abc", "bca", "cab"

Length = 3

# 1. Brute Force — Nested Loops + Set
Algorithm

Generate every possible substring.

Time Complexity

O(n²)

There are O(n²) possible starting and ending positions.

Space Complexity

O(n)

The set can contain up to n characters.

code:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_len = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):

                if s[j] in seen:
                    break

                seen.add(s[j])

                max_len = max(max_len, j - i + 1)

        return max_len


# 2. Better — HashSet + Sliding Window

Time Complexity

O(n)

Although there is a while loop inside the for loop, both left and right only move forward.

Therefore, each character is added and removed at most once.

Space Complexity

O(n)

The set can contain up to n distinct characters.

Code:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len


3. Optimal — HashMap + Variable-Size Sliding Window

Time Complexity

O(n)

right moves from 0 to n - 1 → O(n)
left only moves forward and can move at most n times → O(n)

Therefore:

O(n + n)
= O(2n)
= O(n)
Space Complexity

O(n)

In the worst case, all characters can be distinct, so the HashMap can contain n characters.

code:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)

        freq = {}
        max_len = 0
        left = 0

        for right in range(n):

            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Duplicate character exists
            while freq[s[right]] > 1:

                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            # Current window has no duplicates
            max_len = max(max_len, right - left + 1)

        return max_len
