# Isomorphic Strings
# -----------------------------------
# Problem:
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if characters in s can be replaced to get t.
# - Each character must map to exactly one character
# - No two characters can map to the same character
#
# Example:
# Input: s = "egg", t = "add"
# Output: True
#
# Algorithm:
# Hash Map (Bidirectional Mapping)
# We maintain two dictionaries:
# 1. s -> t mapping
# 2. t -> s mapping
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        # Check s -> t mapping
        if c1 in map_s_t and map_s_t[c1] != c2:
            return False

        # Check t -> s mapping
        if c2 in map_t_s and map_t_s[c2] != c1:
            return False

        map_s_t[c1] = c2
        map_t_s[c2] = c1

    return True


# Test
print(is_isomorphic("egg", "add"))     # True
print(is_isomorphic("foo", "bar"))     # False
