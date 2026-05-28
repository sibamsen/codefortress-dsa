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


# Driver Code
if __name__ == "__main__":

    nums = list(map(int, input("Enter array: ").split()))

    sol = Solution()

    ans = sol.findMissingRepeatingNumbers(nums)

    print("Repeating Number:", ans[0])
    print("Missing Number:", ans[1])
