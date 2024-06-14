# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         5,2,13,3,8
#         8,3,13,2,5
        
#         8:8,3:8,13:13,2:13,5:13
        
#         0->5:13->2:13->13:13->3:8->8:8
#          ->2:13           
        def reverse(head):
            prev = None
            current = head

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            return prev
        head = reverse(head)
        dummy = ListNode(0, head)
        current = dummy
        max_val = 0
        
        while current and current.next:
            max_val = max(max_val, current.next.val)
            if current.next.val < max_val:
                current.next = current.next.next
            else:
                current = current.next
        return reverse(dummy.next)
            
                       
        