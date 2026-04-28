"""
LeetCode 31 - Next Permutation

Approach:
1. Find breakpoint
2. Swap with next greater element
3. Reverse right part

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find breakpoint
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Swap if possible
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    sol = Solution()
    sol.nextPermutation(nums)
    print("Next Permutation:", nums)
