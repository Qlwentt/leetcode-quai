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
        prev = None
        current = head
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        current = prev
        cur_max = 0
        while current:
            cur_max = max(cur_max, current.val)
            current.val = (current.val, cur_max)
            current = current.next
        
        current = prev
        prev = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        dummy = ListNode(0, prev)
        current = dummy
        
        while current and current.next:
            if current.next.val[0] < current.next.val[1]:
                current.next = current.next.next
            else:
                current.next.val = current.next.val[0]
                current = current.next
        return dummy.next
            
                       
        