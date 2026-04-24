"""
Single Number (LeetCode 136)

Problem:
Given an array where every element appears twice except one,
find that single element.

Approach 1: Dictionary (Counting)
Time Complexity: O(n)
Space Complexity: O(n)

Approach 2: XOR (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    # Approach 1: Dictionary
    def singleNumber_dict(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count[num] == 1:
                return num


    # Approach 2: XOR (Optimal)
    def singleNumber_xor(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))

    sol = Solution()

    print("Using Dictionary:", sol.singleNumber_dict(nums))
    print("Using XOR:", sol.singleNumber_xor(nums))
