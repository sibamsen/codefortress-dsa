# 76. Minimum Window Substring

## Optimal Approach — Sliding Window + HashMap

### Time Complexity
- **O(m + n)**, where `m = len(s)` and `n = len(t)`
- Each character is processed at most a constant number of times by the `left` and `right` pointers.

### Space Complexity
- **O(1)** for this problem because `s` and `t` contain only English letters.
- More generally, **O(k)** where `k` is the number of distinct characters being tracked.

### Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        # Frequency of characters required from t
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        # Frequency of required characters in current window
        window = {}

        left = 0

        # Number of character requirements currently satisfied
        formed = 0

        # Number of distinct characters that must be satisfied
        required = len(need)

        min_len = float('inf')
        start = 0

        # Expand the window using right pointer
        for right in range(len(s)):

            char = s[right]

            # Add character to current window
            if char in need:
                window[char] = window.get(char, 0) + 1

                # Requirement for this character is now satisfied
                if window[char] == need[char]:
                    formed += 1

            # Current window contains all required characters
            while formed == required:

                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove the leftmost character
                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1

                    # Removing it made the window invalid
                    if window[left_char] < need[left_char]:
                        formed -= 1

                left += 1

        # No valid window found
        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
```

---

## Why Sliding Window?

We need the **smallest contiguous substring** of `s` that contains all characters of `t`.

Instead of checking every possible substring:

1. Move `right` to **expand** the window until it becomes valid.
2. Once valid, move `left` to **shrink** the window.
3. Keep shrinking while the window remains valid.
4. Store the smallest valid window found.

Pattern:

```text
Expand → Valid → Shrink → Invalid → Expand → Valid → Shrink
```

For:

```text
s = "ADOBECODEBANC"
t = "ABC"
```

the process eventually finds:

```text
"BANC"
```

which is the minimum valid window.

---

## Important Variables

```text
need
```

Stores what `t` requires.

For `t = "ABC"`:

```text
A → 1
B → 1
C → 1
```

```text
window
```

Stores the required characters currently present in the sliding window.

```text
formed
```

Number of distinct character requirements currently satisfied.

```text
required
```

Number of distinct characters required by `t`.

The window is valid when:

```python
formed == required
```

---

# Brute Force Approach

### Algorithm

Generate every possible substring of `s`.

For every substring:
1. Count its characters.
2. Check whether it contains all characters required by `t`.
3. Keep the shortest valid substring.

### Time Complexity

**O(m² × (m + n))** in the straightforward implementation, because there are O(m²) substrings and checking their character frequencies can take O(m + n).

### Space Complexity

**O(k)** for the frequency maps, where `k` is the number of distinct characters.

### Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        min_len = float('inf')
        answer = ""

        for left in range(len(s)):

            window = {}

            for right in range(left, len(s)):

                char = s[right]
                window[char] = window.get(char, 0) + 1

                # Check whether current window satisfies t
                valid = True

                for required_char in need:
                    if window.get(required_char, 0) < need[required_char]:
                        valid = False
                        break

                if valid:
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        answer = s[left:right + 1]

                    # No need to expand this window further
                    break

        return answer
```

---

# Better Approach — Prefix Frequency / Repeated Frequency Checking

### Algorithm

Use prefix frequency information to determine the frequency of characters in each possible substring more efficiently than rebuilding the frequency map from scratch.

We still examine many possible windows, but checking the character counts becomes faster.

### Time Complexity

**O(m² × k)**

where `k` is the number of distinct characters being tracked.

For English letters, `k` is bounded by a constant, so this is effectively **O(m²)**.

### Space Complexity

**O(m × k)** for storing prefix frequency information.

### Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

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

                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        start = left

                    break

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
```
