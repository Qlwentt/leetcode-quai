"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        originalToCopy = {}
        
        current = head
        
        while current:
            originalToCopy[current] = Node(current.val)
            current = current.next
            
        current = head
        while current:
            curCopy = originalToCopy[current]
            if current.next:
                curCopy.next = originalToCopy[current.next]
            if current.random:
                curCopy.random = originalToCopy[current.random]
            current = current.next
        
        return originalToCopy[head]