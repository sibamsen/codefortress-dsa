"""
Problem: Find the sum of elements in an array
Approach: Traverse the array and keep adding elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [1,2,3,4,5]
sum_value = 0

for num in arr:
    sum_value += num

print("Sum of array:", sum_value)
