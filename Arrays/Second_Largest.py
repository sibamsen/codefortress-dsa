"""
Second Largest Element in Array

Problem:
Find second largest unique element in array.

Algorithm:
Single Pass Traversal

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def secondLargestElement(self, nums):
        largest = float('-inf')
        second = float('-inf')

        for num in nums:
            if num > largest:
                second = largest
                largest = num

            elif num > second and num != largest:
                second = num

        return second if second != float('-inf') else -1


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    sol = Solution()
    print("Second Largest:", sol.secondLargestElement(nums))
