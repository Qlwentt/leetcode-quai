# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-9)
        answer = dummy
        carry = 0
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            summ = num1 + num2 + carry
            digit = summ % 10
            carry = summ // 10
            
            answer.next = ListNode(digit)
            answer = answer.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
            
            