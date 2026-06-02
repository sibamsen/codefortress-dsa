'''
Rotate String
Problem:
Check if string s can be rotated to form goal.

--------------------------------------------------
Algorithm:
String Trick (s + s)

Key Idea:
If goal is substring of s+s → rotation possible

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
    
        return goal in (s + s)


