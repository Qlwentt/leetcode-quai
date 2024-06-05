# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

# Iterative
#         prev = None
#         current = head
#         while current:
#             nxt = current.next
#             current.next = prev
#             prev = current
#             current = nxt
        
#         return prev

# recursive
        if not head or not head.next:
            return head
        reversed_part = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_part
        
    
        
        