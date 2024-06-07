# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = ListNode()
        tail = dummy
        
        while l1 or l2 or remainder:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            sum_ = digit1 + digit2 + remainder
            tail.next = ListNode(sum_%10)
            
            remainder = sum_ // 10
            
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
            
        
        