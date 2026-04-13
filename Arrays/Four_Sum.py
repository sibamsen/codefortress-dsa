"""
4Sum Problem

Problem:
Find all unique quadruplets such that sum = target

Algorithm:
Sorting + Two Pointer

Time Complexity: O(n^3)
Space Complexity: O(1) (excluding output)
"""

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1, n-1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    target = int(input("Enter target: "))
    sol = Solution()
    print(sol.fourSum(nums, target))
