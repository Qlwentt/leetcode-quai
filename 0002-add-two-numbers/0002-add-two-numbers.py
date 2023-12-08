# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            sum_ = val1 + val2 + remainder
            digit =  sum_ % 10
            remainder = sum_ // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            tail.next = ListNode(digit)
            tail = tail.next
            
        return dummy.next