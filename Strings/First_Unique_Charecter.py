"""
First Non-Repeating Character

Problem:
Find first character that appears only once.

--------------------------------------------------
Algorithm:
HashMap (Frequency Count)

Steps:
1. Count frequency of each character
2. Traverse string again
3. Return first char with freq = 1

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(n)
"""

def first_non_repeating(s):
    freq = {}

    # Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find first unique
    for ch in s:
        if freq[ch] == 1:
            return ch

    return '$'


# Driver Code
if __name__ == "__main__":
    s = "geeksforgeeks"
    print(first_non_repeating(s))
