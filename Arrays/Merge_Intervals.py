"""
Merge Intervals (LeetCode 56)

Algorithm:
Sorting + Greedy Interval Merging

Problem:
Given intervals, merge all overlapping intervals.

Example:
Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

Why Sorting?
Sorting places overlapping intervals together,
making merging easy.

How Algorithm Works:
1. Sort intervals
2. Store first interval
3. Compare current interval with last merged interval
4. If overlapping:
      merge them
5. Else:
      add new interval

Time Complexity:
Sorting  -> O(n log n)
Traversal -> O(n)

Final:
O(n log n)

Space Complexity:
O(n)
"""

class Solution:
    def merge(self, intervals):

        # Step 1: Sort intervals
        intervals.sort()

        # Step 2: Store first interval
        merged = [intervals[0]]

        # Step 3: Traverse remaining intervals
        for start, end in intervals[1:]:

            # Last interval end
            last_end = merged[-1][1]

            # Step 4: Check overlap
            if start <= last_end:

                # Merge intervals
                merged[-1][1] = max(last_end, end)

            else:
                # Add new interval
                merged.append([start, end])

        return merged


# Driver Code
if __name__ == "__main__":

    intervals = [[1,3],[2,6],[8,10],[15,18]]

    sol = Solution()

    print("Merged Intervals:")
    print(sol.merge(intervals))
