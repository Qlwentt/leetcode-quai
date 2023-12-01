"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            current = Node(insertVal)
            current.next = current
            return current
    
    # 1,3,4 5
        # if self.val < self.next.val:
            # if insertVal >= self.val and insertVal <= self.next.val
            # insert it next
        # else:
            # if insertVal >= self.val:
            
        current = head
        while current.next != head:
            if current.val <= current.next.val:
                if insertVal >= current.val and insertVal <= current.next.val:
                    current.next = next_ = Node(insertVal, current.next)
                    return head
            else:
                if  insertVal >= current.val or insertVal <= current.next.val:
                    current.next = next_ = Node(insertVal, current.next)
                    return head
            current = current.next
            
        current.next = Node(insertVal, current.next)
        return head