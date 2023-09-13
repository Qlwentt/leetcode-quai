# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev = None
        current = slow
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        
        # connect first and second half
        first = head
        second = prev
        
        while second.next:
            firstNext, secondNext = first.next, second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext
        
      
        
        
            
        