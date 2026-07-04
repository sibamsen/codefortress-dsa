## Algorithm

Prefix Product + Suffix Product

## Approach

1. Create a result array initialized with 1.
2. Traverse from left to right and store prefix products.
3. Traverse from right to left and multiply suffix products.
4. The result array will contain product of all elements except self.
5. Return the result array.

## Time Complexity

- Result array creation → O(n)
- Prefix traversal → O(n)
- Suffix traversal → O(n)

Overall:

O(n)

## Space Complexity

- Result array → O(n)
- Prefix variable → O(1)
- Suffix variable → O(1)

Total:

O(n)

Note: LeetCode considers the output array as not extra space, so the optimized solution is O(1) extra space.

## optimal approach

```python
class Solution(object):
    def productExceptSelf(self, nums):

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
```

## Key Interview Insight

For every index:

answer[i] = product of all left elements × product of all right elements

Using Prefix and Suffix products avoids division and achieves O(n) time complexity.
