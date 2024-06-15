# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        def reverse(head):
            prev = None
            current = head
            
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev
        
        current = reverse(head)
        head = current
        carry = 0
        prev = None
        while current:
            sum_ = current.val + current.val + carry
            digit = sum_ % 10
            carry = sum_ // 10
            prev = current
            current.val = digit
            current = current.next
        
        if carry:
            prev.next = ListNode(carry)
        return reverse(head)