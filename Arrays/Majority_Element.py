"""
Majority Element (LeetCode 169)

Problem:
Find element that appears more than n/2 times.

Approach 1: HashMap
Time: O(n), Space: O(n)

Approach 2: Boyer-Moore Voting (Optimal)
Time: O(n), Space: O(1)
"""

class Solution:

    # Approach 1: HashMap
    def majorityElement_hashmap(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count[num] > len(nums) // 2:
                return num


    # Approach 2: Boyer Moore (Optimal)
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))

    sol = Solution()
    print("Majority Element:", sol.majorityElement(nums))
