# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        prev = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        second_half = prev
        first_half = head
        answer = float('-inf')
        while second_half and first_half:
            a = first_half.val
            b = second_half.val
            answer = max(answer, a+b)
            first_half = first_half.next
            second_half = second_half.next
        
        return answer