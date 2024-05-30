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
        
        
        current = slow # mid
        prev = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        second_half = prev
        first_half = head
        
        answer = 0
        while first_half and second_half:
            answer = max(first_half.val + second_half.val, answer)
            first_half = first_half.next
            second_half = second_half.next
        
        return answer
        