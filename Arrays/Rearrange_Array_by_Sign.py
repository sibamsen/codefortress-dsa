"""
LeetCode 2149 - Rearrange Array Elements by Sign

Problem:
Rearrange array so that:
- Alternate positive and negative numbers
- Start with positive
- Maintain order

Approach:
Use two pointers (even/odd indices)

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n

        pos_index = 0
        neg_index = 1

        for num in nums:
            if num > 0:
                result[pos_index] = num
                pos_index += 2
            else:
                result[neg_index] = num
                neg_index += 2

        return result


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    sol = Solution()
    print("Rearranged Array:", sol.rearrangeArray(nums))
