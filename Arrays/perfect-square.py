"""
Problem: Check if a number is a perfect square

Approach: Binary Search

Time Complexity: O(log n)
Space Complexity: O(1)
"""

num = 16

low = 1
high = num

while low <= high:

    mid = (low + high) // 2
    square = mid * mid

    if square == num:
        print(True)
        break

    elif square < num:
        low = mid + 1

    else:
        high = mid - 1

else:
    print(False)
