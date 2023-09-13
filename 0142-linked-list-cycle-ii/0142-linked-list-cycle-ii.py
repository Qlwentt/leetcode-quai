# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head
        slow = head
        didBreak = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                didBreak = True
                break
        
        if not didBreak:
            return None
        
        slow2 = head
        while True:
            if slow2 == slow:
                return slow
            slow2 = slow2.next
            slow = slow.next
        
        