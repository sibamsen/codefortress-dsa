"""
Reverse a String

Problem:
Given a string s, return the reversed string.

--------------------------------------------------
Algorithm:
Two Pointer Technique

Steps:
1. Convert string to list
2. Use two pointers (left, right)
3. Swap characters
4. Move pointers inward
5. Convert back to string

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string(s):
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return ''.join(s_list)


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Reversed string:", reverse_string(s))
