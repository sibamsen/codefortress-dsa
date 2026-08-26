# Maximum Sum Subarray with Exactly K Distinct Elements

Given an array `arr` and an integer `k`, find the maximum sum of a contiguous subarray that contains exactly `k` distinct elements.

---

# 1. Brute Force

### Algorithm

Generate every possible subarray.

For each subarray:

1. Calculate its sum.
2. Find the number of distinct elements.
3. If the number of distinct elements is exactly `k`, update the maximum sum.

### Time Complexity

`O(n³)`

There are `O(n²)` subarrays, and calculating the sum and distinct elements can take `O(n)`.

### Space Complexity

`O(n)`

A set may contain up to `n` distinct elements.

### Code

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        res = float('-inf')

        for i in range(n):
            for j in range(i, n):

                current_sum = sum(arr[i:j + 1])
                distinct = set(arr[i:j + 1])

                if len(distinct) == k:
                    res = max(res, current_sum)

        return 0 if res == float('-inf') else res


# 2. Better — HashSet + Incremental Sum
Algorithm

Instead of recalculating the sum for every subarray, maintain the sum while expanding the subarray.

Time Complexity

O(n²)

There are O(n²) possible subarrays, and each operation inside the loops is O(1) on average.

Space Complexity

O(n)

code:
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        res = float('-inf')

        for i in range(n):

            current_sum = 0
            distinct = set()

            for j in range(i, n):

                current_sum += arr[j]
                distinct.add(arr[j])

                if len(distinct) == k:
                    res = max(res, current_sum)


# 3. Optimal — HashMap + Variable-Size Sliding Window

Time Complexity

O(n)

Space Complexity

O(k)

code:
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        mp = {}
        current_sum = 0
        res = 0

        low = 0

        for high in range(n):

            # Add current element
            mp[arr[high]] = mp.get(arr[high], 0) + 1
            current_sum += arr[high]

            # More than k distinct elements
            while len(mp) > k:

                current_sum -= arr[low]
                mp[arr[low]] -= 1

                if mp[arr[low]] == 0:
                    del mp[arr[low]]

                low += 1

            # Exactly k distinct elements
            if len(mp) == k:
                res = max(res, current_sum)

        return res

# Driver Code
if __name__ == "__main__":

    arr = [1, 2, 1, 3, 4]
    k = 2

    obj = Solution()

    print(obj.maxSubarraySum(arr, k))

Output :  7
