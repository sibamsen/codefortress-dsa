"""
Left Rotate Array by k (Optimal - Reverse Technique)

Problem:
Rotate array to the left by k positions.

Algorithm:
Reversal Technique

Steps:
1. Reverse first k elements
2. Reverse remaining elements
3. Reverse entire array

Time Complexity: O(n)
Space Complexity: O(1)
"""

def rotateLeft(nums, k):
    n = len(nums)
    k = k % n

    # Step 1: Reverse first k elements
    nums[:k] = reversed(nums[:k])

    # Step 2: Reverse remaining elements
    nums[k:] = reversed(nums[k:])

    # Step 3: Reverse whole array
    nums.reverse()


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter k: "))

    rotateLeft(nums, k)
    print("Rotated array:", nums)
