# 76. Minimum Window Substring

## 1. Brute Force

### Algorithm
- Generate every possible substring of `s`.
- For each substring, check whether it contains all characters of `t` with the required frequencies.
- Among all valid substrings, return the shortest one.

### Time Complexity 
- **O(m² × n)** in the worst case
  - `m = len(s)`
  - `n = len(t)` 
- There are O(m²) substrings, and checking each substring can take O(m + n).

### Space Complexity
- **O(n)** for the frequency map.

### Code
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        min_len = float('inf')
        result = ""

        for left in range(len(s)):
            for right in range(left, len(s)):

                window = {}

                for i in range(left, right + 1):
                    if s[i] in need:
                        window[s[i]] = window.get(s[i], 0) + 1

                valid = True

                for char in need:
                    if window.get(char, 0) < need[char]:
                        valid = False
                        break

                if valid and right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

        return result


## 2. Better
Algorithm
- Build the frequency map need for characters required by t.
- Fix the left boundary of the substring.
- Move the right boundary forward.
- Maintain the frequency of characters in the current substring instead of rebuilding it every time.
- Whenever the current substring contains all required characters, update the minimum answer.

Time Complexity
O(m²)
Space Complexity
O(n)

Code:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        min_len = float('inf')
        start = 0

        for left in range(len(s)):
            window = {}

            for right in range(left, len(s)):
                char = s[right]

                if char in need:
                    window[char] = window.get(char, 0) + 1

                valid = True

                for required_char in need:
                    if window.get(required_char, 0) < need[required_char]:
                        valid = False
                        break

                if valid:
                    length = right - left + 1

                    if length < min_len:
                        min_len = length
                        start = left

                    break

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]


## 3. Optimal — Sliding Window

Time Complexity
O(m + n)
right moves at most m times.
left also moves at most m times.
Building need takes O(n).
Space Complexity
O(n) in general.
For this problem, since s and t contain only English letters, this is effectively O(1).

code:
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = {}

        # Frequency of characters required from t
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0
        formed = 0
        required = len(need)

        min_len = float('inf')
        start = 0

        for right in range(len(s)):

            char = s[right]

            # Add current character to the window
            if char in need:
                window[char] = window.get(char, 0) + 1

                # This character has now reached its required frequency
                if window[char] == need[char]:
                    formed += 1

            # Window is valid, so try to shrink it
            while formed == required:

                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove the leftmost character
                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1

                    # Window has become invalid for this character
                    if window[left_char] < need[left_char]:
                        formed -= 1

                left += 1

        # No valid window found
        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
