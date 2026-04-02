# String to Integer (atoi)
# -----------------------------------
# Problem:
# Convert a string to a 32-bit signed integer.
#
# Rules:
# 1. Ignore leading spaces
# 2. Check optional sign (+ or -)
# 3. Read digits until non-digit
# 4. Clamp result within [-2^31, 2^31 - 1]
#
# Example:
# Input: " -042"
# Output: -42
#
# Algorithm:
# Simulation / Parsing
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def myAtoi(s):
    i = 0
    n = len(s)

    # Step 1: Skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: Check sign
    sign = 1
    if i < n and s[i] in ['+', '-']:
        if s[i] == '-':
            sign = -1
        i += 1

    # Step 3: Read digits
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit

        # Step 4: Handle overflow
        if result * sign <= -2**31:
            return -2**31
        if result * sign >= 2**31 - 1:
            return 2**31 - 1

        i += 1

    return result * sign


# Test
print(myAtoi("42"))        # 42
print(myAtoi(" -042"))     # -42
print(myAtoi("4193abc"))   # 4193
print(myAtoi("abc123"))    # 0
