"""
Problem: Sum of Two Squares

Given a non-negative integer c, determine whether there
exist two integers a and b such that:

a^2 + b^2 = c

Example:
Input: c = 5
Output: True (1^2 + 2^2)

Approach:
Use Two Pointer technique.

Time Complexity: O(√c)
Space Complexity: O(1)
"""

def judge_square_sum(c):
    a = 0
    b = int(c ** 0.5)

    while a <= b:
        value = a*a + b*b

        if value == c:
            return True
        elif value < c:
            a += 1
        else:
            b -= 1

    return False


# 🔹 Example Usage
c = 25
print("Result:", judge_square_sum(c))
