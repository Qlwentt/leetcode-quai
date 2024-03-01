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
        prev = None
        while current:
            copy = Node(current.val)
            if prev:
                copyPrev = originalToCopy[prev]
                copyPrev.next = copy
            originalToCopy[current] = copy
            prev = current
            current = current.next
        
        current = head
        while current:
            randomCopy = originalToCopy[current.random] if current.random else None
            copy = originalToCopy[current]
            copy.random = randomCopy
            current = current.next
        
        return originalToCopy[head]