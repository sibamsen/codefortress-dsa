# Linked List Cycle (LeetCode 141)

## Problem Statement

Given the head of a singly linked list, determine whether the linked list contains a cycle.

A cycle exists if there is some node in the linked list that can be reached again by continuously following the `next` pointer.

Return:
- `True` if a cycle exists.
- `False` if there is no cycle.

---

# 1. Brute Force

### Algorithm: Visited List

Store every node that we visit in a list.

For every node:
- If the node is already present in the list, a cycle exists.
- Otherwise, store it and move to the next node.
- If we reach `None`, there is no cycle.

### Time Complexity
- **O(n²)** because checking whether a node is already in a list takes O(n).

### Space Complexity
- **O(n)** for storing visited nodes.

### Code

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        current = head

        while current is not None:

            if current in visited:
                return True

            visited.append(current)
            current = current.next

        return False


##2. Better
Algorithm: HashSet

Use a set to store the nodes that have already been visited.

A set provides approximately O(1) average-time lookup.

Time Complexity
O(n)
Space Complexity
O(n)

COde:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        current = head

        while current is not None:

            if current in visited:
                return True

            visited.add(current)
            current = current.next

        return False


##3. Optimal
Algorithm: Floyd's Cycle Detection / Slow and Fast Pointers

Use two pointers:

slow moves 1 step at a time.
fast moves 2 steps at a time.

Time Complexity
O(n)
Space Complexity
O(1)

Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
