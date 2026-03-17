"""
Problem: Factorial of a Number
Difficulty: Easy
Pattern: Recursion / Math

Definition:
n! = n × (n-1) × (n-2) × ... × 1

Example:
5! = 5 × 4 × 3 × 2 × 1 = 120

Approach:
Use recursion:
factorial(n) = n * factorial(n-1)

Base Case:
factorial(0) = 1
factorial(1) = 1

Time Complexity: O(n)
Space Complexity: O(n) (recursion stack)
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


n = 5
print("Factorial:", factorial(n))
