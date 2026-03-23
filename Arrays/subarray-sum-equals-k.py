"""
Problem: Subarray Sum Equals Target
Difficulty: Medium
Pattern: Prefix Sum + Hash Map

--------------------------------------------------
Problem Statement:
Given an array of integers and a target value,
find all subarrays whose sum equals the target.

Example:
arr = [3,4,-7,1,3,3,1,-4]
target = 7

Output:
[
 [3,4],
 [3,4,-7,1,3,3],
 [1,3,3],
 [3,3,1]
]

--------------------------------------------------
Concept (Very Important 💙):

prefix_sum[i] = sum of elements from index 0 → i

Subarray sum formula:
subarray_sum = current_sum - previous_sum

So:
target = current_sum - previous_sum

Rearranged:
previous_sum = current_sum - target

Meaning:
If we have seen (current_sum - target) before,
then a subarray exists.

--------------------------------------------------
Approach:

1. Use a variable current_sum to store running sum
2. Use a hashmap to store:
   prefix_sum → list of indices
3. Traverse the array
4. At each step:
   - Add element to current_sum
   - Check if (current_sum - target) exists in map
   - If yes → subarray found
5. Store current_sum in map

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(n)
--------------------------------------------------
"""

arr = [3,4,-7,1,3,3,1,-4]
target = 7

# prefix_sum → list of indices
mp = {0: [-1]}

current_sum = 0
result = []

for i in range(len(arr)):

    # Step 1: Update running sum
    current_sum += arr[i]

    # Step 2: Check if subarray exists
    if (current_sum - target) in mp:

        for start in mp[current_sum - target]:
            result.append(arr[start+1:i+1])

    # Step 3: Store prefix sum
    mp.setdefault(current_sum, []).append(i)


# Output
print("Subarrays with sum =", target)
for sub in result:
    print(sub)
