"""
Longest Subarray with Sum K

Problem:
Find the length of the longest subarray with sum equal to k.

Algorithm:
Prefix Sum + HashMap

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestSubarray(self, nums, k):
        pre_sum = 0
        max_len = 0

        # Map to store prefix sum and its first occurrence index
        mp = {0: -1}

        for i in range(len(nums)):
            pre_sum += nums[i]

            # Check if there exists a prefix sum such that:
            # current_sum - previous_sum = k
            if (pre_sum - k) in mp:
                length = i - mp[pre_sum - k]
                max_len = max(max_len, length)

            # Store only first occurrence of prefix sum
            if pre_sum not in mp:
                mp[pre_sum] = i

        return max_len


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter k: "))

    sol = Solution()
    result = sol.longestSubarray(nums, k)

    print("Longest subarray length:", result)
