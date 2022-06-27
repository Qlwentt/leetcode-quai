from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        
        # find the start of the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        # reverse the second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev
        first = head
        # build the list
        while second:
            next1 = first.next
            next2 = second.next
            
            first.next = second
            second.next = next1
            
            first = next1
            second = next2
            
        if first:
            first.next = None

# O(n) time
# O(1) space