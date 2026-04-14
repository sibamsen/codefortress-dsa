"""
Check if Array is Sorted and Rotated

Problem:
Check if array was originally sorted and then rotated.

Algorithm:
Count inversion points (breaks)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1

        return count <= 1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    sol = Solution()
    print("Is Sorted & Rotated:", sol.check(nums))
