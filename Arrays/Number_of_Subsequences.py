"""
Number of Subsequences

Problem:
Given an array nums and an integer target, return the number of
non-empty subsequences such that:

min(subsequence) + max(subsequence) <= target

--------------------------------------------------
Algorithm:
Sorting + Two Pointers + Precomputation

Key Idea:
Fix smallest element and count all valid subsequences
using combinations (2^(right - left)).

--------------------------------------------------
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def numSubseq(nums, target):
    MOD = 10**9 + 7

    # Step 1: Sort the array
    nums.sort()
    n = len(nums)

    # Step 2: Precompute powers of 2
    pow2 = [1] * n
    for i in range(1, n):
        pow2[i] = (pow2[i-1] * 2) % MOD

    # Step 3: Two pointers
    left, right = 0, n - 1
    result = 0

    # Step 4: Count valid subsequences
    while left <= right:
        if nums[left] + nums[right] <= target:
            result = (result + pow2[right - left]) % MOD
            left += 1
        else:
            right -= 1

    return result


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = [3, 5, 6, 7]
    target = 9

    print("Number of subsequences:", numSubseq(nums, target))
