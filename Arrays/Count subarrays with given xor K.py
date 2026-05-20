"""
Count Subarrays With Given XOR K

Algorithm:
Prefix XOR + HashMap

Explain:
Find total number of subarrays whose XOR equals k.

Why this works:
If:
previous_xor ^ current_xor = k

Then:
previous_xor = current_xor ^ k

So if (current_xor ^ k) already exists,
then a valid subarray is found.

Steps:
1. Maintain running XOR
2. Find required XOR:
      x = xr ^ k
3. Check hashmap
4. Store XOR frequency

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def subarraysWithXorK(self, nums, k):
        xr = 0
        count = 0
        mp = {0:1}

        for num in nums:
            xr ^= num

            x = xr ^ k

            if x in mp:
                count += mp[x]

            mp[xr] = mp.get(xr, 0) + 1

        return count


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter k: "))

    sol = Solution()

    print("Count of subarrays with XOR k:",
          sol.subarraysWithXorK(nums, k))
