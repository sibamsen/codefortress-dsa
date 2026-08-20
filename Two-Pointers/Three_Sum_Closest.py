# LeetCode 16 — 3Sum Closest

Given an integer array `nums` of length `n` and an integer `target`, find three integers at distinct indices in `nums` such that their sum is closest to `target`.

Return the sum of the three integers.

---

## 1. Brute Force

### Time Complexity
`O(n³)`

### Space Complexity
`O(1)`

### Code

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Initialize with the sum of the first three elements
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    total = nums[i] + nums[j] + nums[k]

                    if abs(total - target) < abs(closest - target):
                        closest = total

        return closest

## 2. Better Approach — Sorting + Binary Search

### Time Complexity
O(n² log n)

Sorting → O(n log n)
Two nested loops → O(n²)
Binary search for each pair → O(log n)

Therefore:

O(n² log n)

### Space Complexity
O(1) auxiliary space

### Code

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            for j in range(i + 1, n - 1):

                required = target - nums[i] - nums[j]

                left = j + 1
                right = n - 1

                # Binary search for the closest third element
                while left <= right:
                    mid = (left + right) // 2

                    total = nums[i] + nums[j] + nums[mid]

                    if abs(total - target) < abs(closest - target):
                        closest = total

                    if nums[mid] < required:
                        left = mid + 1

                    elif nums[mid] > required:
                        right = mid - 1

                    else:
                        return target

        return closest


## 3. Optimal Approach — Sorting + Two Pointers

### Time Complexity
O(n²)

Sorting → O(n log n)
Two-pointer traversal → O(n²)

Therefore:

O(n²)

Therefore:

O(n² log n)

### Space Complexity
O(1) auxiliary space

### Code

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)

        # Initialize with the first possible triplet
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Exact match
                if total == target:
                    return target

                # Need a larger sum
                elif total < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest
