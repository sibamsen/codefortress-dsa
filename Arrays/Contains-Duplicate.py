"""
Problem: Contains Duplicate
Difficulty: Easy
Category: Array / Hash Set
Source: NeetCode 150

Problem Statement
-----------------
Given an integer array nums, return True if any value appears
more than once in the array, otherwise return False.

Example 1:
Input: nums = [1,2,3,3]
Output: True
------------------------------------------------------

Algorithm Used
--------------
Hash Set

Concept
-------
A set only stores unique elements.

While traversing the array:
- If the number already exists in the set → duplicate found
- Otherwise add the number to the set

This allows us to detect duplicates efficiently.

------------------------------------------------------

Steps
-----
1. Create an empty set called 'seen'.
2. Traverse through each element in nums.
3. If the element already exists in seen → return True.
4. Otherwise add it to the set.
5. If loop finishes with no duplicates → return False.

------------------------------------------------------

Time Complexity
---------------
Let n = length of array

Loop runs n times → O(n)

Set lookup → O(1)

Total Time Complexity:
O(n)

------------------------------------------------------

Space Complexity
----------------
In worst case, set stores all elements.

Space Complexity:
O(n)

------------------------------------------------------
"""


class Solution:
    def hasDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
