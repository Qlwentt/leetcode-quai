from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        
        current = head
        
        while current:
            copies[current] = Node(current.val)
            current = current.next
        
        current = head
        dummy = Node(-9)
        copy = dummy
        while current:
            copy.next = copies[current]
            copy.next.random = copies[current.random] if current.random else None
            current = current.next
            copy = copy.next
        return dummy.next

# O(n) time
# O(n) space
            