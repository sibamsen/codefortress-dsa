"""
Implement pow(x, n)

Problem:
Given a number x and an integer n, compute x raised to the power n (x^n).

Approaches:
1. Simple Recursion (O(n))
2. Binary Exponentiation (Optimized - O(log n))
"""

# ----------------------------------
# Approach 1: Simple Recursion
# ----------------------------------
def power_recursive(x, n):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n == 0:
        return 1.0
    
    if n < 0:
        return 1.0 / power_recursive(x, -n)
    
    return x * power_recursive(x, n - 1)


# ----------------------------------
# Approach 2: Binary Exponentiation
# ----------------------------------
def power_optimized(x, n):
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    if n == 0:
        return 1.0
    
    if n < 0:
        return 1.0 / power_optimized(x, -n)
    
    half = power_optimized(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# ----------------------------------
# Driver Code
# ----------------------------------
if __name__ == "__main__":
    x = 2.0
    n = 10

    print("Using Recursion:", power_recursive(x, n))
    print("Using Optimized:", power_optimized(x, n))
