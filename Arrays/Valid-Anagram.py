"""
Problem: Valid Anagram

Given two strings s and t, return True if t is an
anagram of s, else return False.

Example:
Input: s = "anagram", t = "nagaram"
Output: True

Approach:
Use a hash map to count character frequency.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_anagram(s, t):

    # Step 1: Length check
    if len(s) != len(t):
        return False

    count = {}

    # Step 2: Count characters in s
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Step 3: Reduce using t
    for ch in t:
        if ch not in count:
            return False

        count[ch] -= 1

        if count[ch] == 0:
            del count[ch]

    return len(count) == 0


# 🔹 Example Usage
s = "anagram"
t = "nagaram"
print("Result:", is_anagram(s, t))
