"""
Approach: Aggressive Cows

Algorithm:
Binary Search on Answer + Greedy

Observation:

Distance 1 -> Possible
Distance 2 -> Possible
Distance 3 -> Possible
Distance 4 -> Not Possible

Pattern:

TTTFFF

Use Binary Search to find
the last True value.

Time Complexity:
O(n log(maxDistance))

Space Complexity:
O(1)
"""
#optmal solution
class Solution:

    def canPlace(self, nums, k, dist):

        cows = 1
        last = nums[0]

        for i in range(1, len(nums)):

            if nums[i] - last >= dist:

                cows += 1
                last = nums[i]

        return cows >= k


    def aggressiveCows(self, nums, k):

        nums.sort()

        left = 1
        right = nums[-1] - nums[0]

        ans = 0

        while left <= right:

            mid = (left + right)//2

            if self.canPlace(nums, k, mid):

                ans = mid
                left = mid + 1

            else:

                right = mid - 1

        return ans


# Driver Code
if __name__ == "__main__":

    nums = [0,3,4,7,10,9]
    k = 4

    sol = Solution()

    print(sol.aggressiveCows(nums, k))
