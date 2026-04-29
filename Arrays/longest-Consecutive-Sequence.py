"""
Longest Consecutive Sequence (LeetCode 128)

Algorithm:
HashSet + Greedy Expansion

Why:
Unsorted array → need O(1) lookup

Steps:
1. Convert list to set
2. Start only from sequence beginnings
3. Expand forward
4. Track maximum length

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only start if it's beginning of sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    sol = Solution()
    print("Longest Consecutive Length:", sol.longestConsecutive(nums))
