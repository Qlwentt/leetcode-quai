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
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        current = slow
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        second = prev
        first = head
        
        while second and second.next:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
            