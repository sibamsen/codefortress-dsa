"""
Find Out How Many Times the Array is Rotated

Algorithm:
Modified Binary Search

Key Idea:
1. Number of rotations = Index of minimum element.
2. Use Binary Search to find the minimum element.
3. Compare nums[mid] with nums[right].
4. If nums[mid] > nums[right]:
      Minimum lies in right half.
      Move left = mid + 1.
5. Otherwise:
      Minimum lies at mid or left half.
      Move right = mid.
6. When left == right,
      left points to minimum element.
7. Return left (rotation count).

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:

    def findKRotation(self, nums):

        left, right = 0, len(nums)-1

        while left < right:

            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        return left


# Driver Code
if __name__ == "__main__":

    nums = [4,5,6,7,0,1,2,3]

    sol = Solution()

    print("Rotation Count:", sol.findKRotation(nums))
