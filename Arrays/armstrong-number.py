"""
Problem: Armstrong Number
Difficulty: Easy
Pattern: Digit Manipulation

Definition:
A number is Armstrong if:
sum of (each digit ^ total digits) = number

Example:
153 → 1³ + 5³ + 3³ = 153

Approach:
1. Count number of digits
2. Extract digits using % and //
3. Add digit^power
4. Compare with original number

Time Complexity: O(d)  (d = number of digits)
Space Complexity: O(1)
"""

n = 153
original = n
power = len(str(n))

total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")
