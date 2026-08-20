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
