"""
Majority Element II (HashMap Approach)

Problem:
Find all elements appearing more than n/3 times.

Algorithm:
HashMap (Frequency Counting)

Steps:
1. Count frequency of each element
2. Traverse unique elements
3. Add elements whose frequency > n/3

Time Complexity: O(n)
Space Complexity: O(n)
"""

def majorityElement(nums):
    n = len(nums)
    freq = {}
    result = []

    # Step 1: Count frequency
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Check for majority elements
    for key in freq:
        if freq[key] > n // 3:
            result.append(key)

    return result


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements: ").split()))
    print("Majority Elements:", majorityElement(nums))
