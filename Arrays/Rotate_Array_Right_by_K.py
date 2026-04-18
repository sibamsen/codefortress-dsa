"""
Rotate Array (LeetCode 189)

Problem:
Rotate array to the right by k steps.

Algorithm:
Reverse Technique

Steps:
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        # Reverse entire array
        nums.reverse()

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter k: "))

    sol = Solution()
    sol.rotate(nums, k)

    print("Rotated array:", nums)
