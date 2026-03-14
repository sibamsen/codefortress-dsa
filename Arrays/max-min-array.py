"""
Problem: Find maximum and minimum element in array

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [1,2,3,4,5]

maximum = arr[0]
minimum = arr[0]

for i in range(1, len(arr)):

    if arr[i] > maximum:
        maximum = arr[i]

    if arr[i] < minimum:
        minimum = arr[i]

print("Maximum:", maximum)
print("Minimum:", minimum)
