"""
Sort Colors (LeetCode 75)

Problem:
Sort array of 0s, 1s, and 2s in-place.

Approach 1: Counting Sort
Time Complexity: O(n)
Space Complexity: O(k)

Approach 2: Dutch National Flag (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:

    # Approach 1: Counting Sort
    def sortColors_counting(self, nums):
        max_val = max(nums)
        count = [0] * (max_val + 1)

        for num in nums:
            count[num] += 1

        index = 0
        for num in range(len(count)):
            for _ in range(count[num]):
                nums[index] = num
                index += 1


    # Approach 2: Dutch National Flag (Optimal)
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))

    sol = Solution()

    # Using optimal approach
    sol.sortColors(nums)
    print("Sorted array:", nums)
