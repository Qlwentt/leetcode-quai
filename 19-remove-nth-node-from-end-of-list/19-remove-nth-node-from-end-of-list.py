# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
            
        targetNode = length - n - 1
        i = 0
        if targetNode < 0:
            return head.next if head else None
        
        curr = head
        while i < targetNode:
            i += 1
            curr = curr.next
        
        curr.next = curr.next.next
        return head
        
        