"""
Leaders in an Array

Algorithm:
Greedy + Right-to-Left Traversal + Max Tracking

Why this works:
Right side elements already processed → instant decision

Steps:
1. Traverse from right
2. Track max_so_far
3. If element > max_so_far → leader
4. Reverse result

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def leaders(self, nums):
        max_so_far = float('-inf')
        result = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_so_far:
                result.append(nums[i])
                max_so_far = nums[i]

        return result[::-1]


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    sol = Solution()
    print("Leaders:", sol.leaders(nums))
