"""
Subarray Sum Equals K (LeetCode 560)

Algorithm:
Prefix Sum + HashMap (Frequency Map)

Key Idea:
current_sum - previous_sum = k
→ previous_sum = current_sum - k

If (prefix_sum - k) exists in map,
then a valid subarray with sum = k exists.

Steps:
1. Initialize:
   prefix_sum = 0
   count = 0
   mp = {0:1}

2. Traverse array:
   - Add element to prefix_sum
   - Check if (prefix_sum - k) exists
   - If yes → add its frequency to count
   - Store prefix_sum in map

3. Return count

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        mp = {0: 1}  # Important: handles case when prefix_sum == k

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in mp:
                count += mp[prefix_sum - k]

            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

        return count


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter k: "))
    sol = Solution()
    print("Number of subarrays with sum k:", sol.subarraySum(nums, k))
