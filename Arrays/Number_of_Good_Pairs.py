"""
Q21 - Number of Good Pairs

Given an array nums, return the number of good pairs.

A pair (i, j) is called good if:
1. nums[i] == nums[j]
2. i < j

--------------------------------------------------
Approach 1: Brute Force
--------------------------------------------------
Check all pairs using nested loops.

Time Complexity: O(n^2)
Space Complexity: O(1)

--------------------------------------------------
Approach 2: Optimized (HashMap / Dictionary)
--------------------------------------------------
Use frequency counting.

Key Idea:
Each new duplicate forms pairs with all previous occurrences.

Time Complexity: O(n)
Space Complexity: O(n)
"""


# -------------------------------
# Approach 1: Brute Force
# -------------------------------
def num_identical_pairs_bruteforce(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                count += 1

    return count


# -------------------------------
# Approach 2: Optimized (HashMap)
# -------------------------------
def num_identical_pairs_optimized(nums):
    freq = {}
    count = 0

    for num in nums:
        # Add number of previous occurrences
        count += freq.get(num, 0)

        # Update frequency
        freq[num] = freq.get(num, 0) + 1

    return count


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]

    print("Brute Force Output:", num_identical_pairs_bruteforce(nums))
    print("Optimized Output:", num_identical_pairs_optimized(nums))
