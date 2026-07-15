"""
Find the Repeating and Missing Number

Algorithm:
Hashing / Frequency Array

Problem:
Given an array containing numbers from 1 to n,
one number repeats and one number is missing.

Find:
[repeating, missing]

Example:
Input:
[3,5,4,1,1]

Output:
[1,2]

Why Frequency Array?
Since numbers are from 1 to n,
we can directly count occurrences using indexing.

Steps:
1. Create frequency array
2. Count occurrences
3. Frequency 2 -> repeating
4. Frequency 0 -> missing

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
#optimal solution
class Solution:
    def findMissingRepeatingNumbers(self, nums):

        n = len(nums)

        # Frequency array
        freq = [0] * (n + 1)

        # Count occurrences
        for num in nums:
            freq[num] += 1

        repeating = -1
        missing = -1

        # Find repeating and missing
        for i in range(1, n + 1):

            if freq[i] == 2:
                repeating = i

            elif freq[i] == 0:
                missing = i

        return [repeating, missing]


"""
# Optimal Approach

Algorithm:
Mathematical Equations (Sum + Sum of Squares)

Key Idea:

Let:
A = Repeating Number
B = Missing Number

Equation 1:
A - B = actual_sum - expected_sum

Equation 2:
A² - B² = actual_square_sum - expected_square_sum

Using:
A² - B² = (A-B)(A+B)

Find:
A+B

Then solve:
A = (x+z)/2
B = z-A

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:
    def find_repeating_missing(self, nums):

        n = len(nums)

        # Expected sum of numbers from 1 to n
        s = n * (n + 1) // 2

        # Actual sum of array
        actual_sum = sum(nums)

        # Expected square sum
        s2 = n * (n + 1) * (2 * n + 1) // 6

        # Actual square sum
        actual_sq_sum = sum(num * num for num in nums)

        # A - B
        x = actual_sum - s

        # A² - B²
        y = actual_sq_sum - s2

        # A + B
        z = y // x

        # Repeating Number
        A = (x + z) // 2

        # Missing Number
        B = z - A

        return [A, B]


# Driver Code
if __name__ == "__main__":

    nums = list(map(int, input("Enter array: ").split()))

    S = Solution()

    ans = S.find_repeating_missing(nums)

    print("Repeating Number:", ans[0])
    print("Missing Number:", ans[1])
