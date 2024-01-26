"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # Case 1: head is None
        # Case 2: Insert into middle of linked list
        #   a: insert val is in between two nodes
        # Case 3: Insert at the end 
            # a: insert val is greater that number at the end
            # b: insert val is less than number at the beginning
        # Case 4: All numbers are the same (also insert at the end - can insert anywhere)
        
        
        if not head:
            current = Node(insertVal)
            current.next = current
            return current
        
        current = head
        #[3,3,5] 5
        #  H
        # stop when you get to the end of the list (next node is head)
        while current.next != head:
            if insertVal >= current.val and insertVal <= current.next.val:
                break
            # if current is the end of the list
            elif current.next.val < current.val:
                # and insert val is greater than number at end or insert val is less than number at the beg
                if insertVal > current.val or insertVal < current.next.val:
                    break
            current = current.next
            
        # all numbers are the same
        current.next = Node(insertVal, current.next)
        return head
            