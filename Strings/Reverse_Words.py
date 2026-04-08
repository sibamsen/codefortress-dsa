"""
Reverse Words in a String

Problem:
Given a string s, reverse the order of words.

Conditions:
- Remove leading/trailing spaces
- Maintain only one space between words

--------------------------------------------------
Algorithm:
String Manipulation (Split + Reverse)

Steps:
1. Split string into words
2. Reverse words using two pointers
3. Join words with single space

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverseWords(s):
    words = s.split()
    left, right = 0, len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return ' '.join(words)


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Reversed Words:", reverseWords(s))
