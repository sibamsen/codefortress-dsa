# LeetCode 242. Valid Anagram

## Algorithm
Hash Map (Frequency Counter)

## Approach

1. If lengths are different, return False.
2. Create a frequency dictionary for string s.
3. Traverse string t.
4. If character not found in dictionary, return False.
5. Decrease frequency.
6. Remove key when frequency becomes 0.
7. If dictionary becomes empty, return True.

## Time Complexity

- Building frequency map: O(n)
- Traversing second string: O(n)

Overall Time Complexity:

O(n)

## Space Complexity

- HashMap stores character frequencies.

Worst Case:

O(n)

## Code

```python
class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:

            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] == 0:
                del count[ch]

        return len(count) == 0
```

## Key Insight

An anagram must have:

- Same length
- Same characters
- Same frequency of each character

Using a HashMap allows us to verify frequencies in O(n) time instead of sorting both strings, which would take O(n log n).
