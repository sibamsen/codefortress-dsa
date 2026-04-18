"""
Left Rotate Array by One

Problem:
Rotate the given array to the left by one position.

Approach:
1. Store first element
2. Shift all elements left
3. Place first element at end

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def rotateArrayByOne(self, nums):
        if not nums:
            return
        
        first = nums[0]

        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]

        nums[-1] = first


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    
    sol = Solution()
    sol.rotateArrayByOne(nums)

    print("Rotated array:", nums)
