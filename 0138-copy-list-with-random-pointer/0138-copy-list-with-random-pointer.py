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
        nodeToCopy = {}
        
        current = head
        prevCopy = None
        while current:
            copyCurrent = Node(current.val)
            if prevCopy:
                prevCopy.next = copyCurrent
            prevCopy = copyCurrent
            nodeToCopy[current] = copyCurrent
        
            current = current.next
        
        current = head
        while current:
            curCopy = nodeToCopy[current]
            curCopy.random = nodeToCopy[current.random] if current.random else None
            current = current.next
            
        return nodeToCopy[head]
            
        