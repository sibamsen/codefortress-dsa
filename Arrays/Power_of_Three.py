"""
Power of Three

Problem:
Given an integer n, return True if it is a power of three.
Otherwise, return False.

A number is a power of three if:
n = 3^k for some integer k ≥ 0

Algorithm:
Repeated Division (Mathematical Approach)

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def isPowerOfThree(n):
    # Edge case
    if n <= 0:
        return False

    # Keep dividing by 3
    while n % 3 == 0:
        n //= 3   # Use integer division

    # Check if reduced to 1
    return n == 1


# 🔹 Example Usage
if __name__ == "__main__":
    print(isPowerOfThree(27))  # True
    print(isPowerOfThree(30))  # False
    print(isPowerOfThree(1))   # True
    print(isPowerOfThree(0))   # False
