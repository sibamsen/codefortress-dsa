"""
Container With Most Water

Problem:
Given an array height, find two lines that together with the x-axis
form a container that holds the maximum amount of water.

--------------------------------------------------
Algorithm:
Two Pointer Technique

Key Idea:
- Area = min(height[left], height[right]) * (right - left)
- Move the pointer with smaller height

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxArea(height):
    left, right = 0, len(height) - 1
    maxWater = 0

    while left < right:
        # Step 1: Calculate current area
        current = min(height[left], height[right]) * (right - left)

        # Step 2: Update maximum area
        maxWater = max(maxWater, current)

        # Step 3: Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxWater


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print("Maximum Water:", maxArea(height))
