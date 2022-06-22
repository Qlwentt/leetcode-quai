from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
# Iterative
# O(n) time
# O(1) space
    
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return head
#         reversedList = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return reversedList

# Recursive
# O(n) time
# O(n) space