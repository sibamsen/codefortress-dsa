"""
3Sum Problem (Optimized Approach)

Problem:
Find all unique triplets in the array such that their sum is zero.

Algorithm:
Sorting + Two Pointer

Steps:
1. Sort the array
2. Fix one element
3. Use two pointers to find remaining two elements
4. Skip duplicates to avoid repeated triplets

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    print("Triplets:", threeSum(nums))
