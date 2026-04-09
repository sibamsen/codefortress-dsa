"""
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
"""

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    
    return goal in (s + s)


# Driver Code
if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"
    print(rotateString(s, goal))
