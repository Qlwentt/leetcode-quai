# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        times = length // k
        
        current = head
        newHead = None
        p = None
        for i in range(times):
            prev = None
            next_ = None
            c = current
            for _ in range(k):     
                next_ = c.next
                c.next = prev
                prev = c
                c = next_
                if i==0:
                    newHead = prev
            if i != 0:
                p.next = prev    
    
            p = current
            current.next = next_
            current = current.next   
        
        return newHead
                
            