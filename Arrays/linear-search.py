"""
Problem: Linear Search
Find the index of a given element in an array

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [1,2,3,4,5,6,7,8]
x = 4

for i in range(len(arr)):
    if arr[i] == x:
        print("Element found at index:", i)
        break
else:
    print("Element not found")
