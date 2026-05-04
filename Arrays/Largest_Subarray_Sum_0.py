"""
Largest Subarray with Sum 0

Explain:
Find the longest subarray whose sum is equal to 0.

Algorithm:
Prefix Sum + HashMap

Why this works:
If prefix_sum repeats → subarray sum = 0

Steps:
1. Maintain prefix_sum
2. If prefix_sum == 0 → update max_len
3. If prefix_sum seen before → calculate length
4. Store first occurrence of prefix_sum

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        max_len = 0
        mp = {}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                max_len = i + 1

            if prefix_sum in mp:
                max_len = max(max_len, i - mp[prefix_sum])
            else:
                mp[prefix_sum] = i

        return max_len


# Driver Code
if __name__ == "__main__":
    arr = list(map(int, input("Enter array: ").split()))
    sol = Solution()
    print("Longest subarray length with sum 0:", sol.maxLen(arr))
