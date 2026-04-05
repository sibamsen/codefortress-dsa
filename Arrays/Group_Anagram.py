"""
Group Anagrams

Problem:
Given an array of strings, group the anagrams together.

Two strings are anagrams if they contain the same characters
in any order.

Example:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

--------------------------------------------------
Algorithm:
HashMap + Sorting

Key Idea:
Sort each string and use it as a key.
Anagrams will have the same sorted representation.

--------------------------------------------------
Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

def groupAnagrams(strs):
    mp = {}

    for word in strs:
        # Step 1: Sort the word to create a key
        key = ''.join(sorted(word))

        # Step 2: Initialize list if key not present
        if key not in mp:
            mp[key] = []

        # Step 3: Append word to corresponding group
        mp[key].append(word)

    # Step 4: Return grouped anagrams
    return list(mp.values())


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = groupAnagrams(strs)

    print("Grouped Anagrams:")
    for group in result:
        print(group)
