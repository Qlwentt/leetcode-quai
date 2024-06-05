# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
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
        
        second_half_reversed = prev
        first_half = head
        
#         1=>2=>3=>2=>1
        
#         1->2
#         1->2->3
        
        while first_half and second_half_reversed:
            if first_half.val != second_half_reversed.val:
                return False
            first_half = first_half.next
            second_half_reversed = second_half_reversed.next
        return True
        
        
        