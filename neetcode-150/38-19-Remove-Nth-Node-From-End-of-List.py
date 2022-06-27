from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        current = head
        
        while current:
            length += 1
            current = current.next
            
        i = length - n
        
        current = head
        while i > 1:
            i -= 1
            current = current.next
        if i > 0:
            current.next = current.next.next
            return head
        else:
            return head.next
# O(n) time
# O(1) space