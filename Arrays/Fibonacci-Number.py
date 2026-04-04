"""
Fibonacci Series

Problem:
Given an integer n, return the n-th Fibonacci number.

Fibonacci Definition:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)

Approaches:
1. Recursion (Naive)
2. Iterative (Optimized)
"""

# -------------------------------
# Approach 1: Recursion (Naive)
# -------------------------------
def fib_recursive(n):
    """
    Returns nth Fibonacci number using recursion.
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


# -------------------------------
# Approach 2: Iterative (Optimal)
# -------------------------------
def fib_iterative(n):
    """
    Returns nth Fibonacci number using iteration.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    n = 5

    print("Using Recursion:", fib_recursive(n))
    print("Using Iteration:", fib_iterative(n))
