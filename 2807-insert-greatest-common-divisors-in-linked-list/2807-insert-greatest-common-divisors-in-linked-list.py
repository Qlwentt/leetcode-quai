# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            a = current.val
            b = current.next.val
            c = math.gcd(a,b)
            current.next = ListNode(c, current.next)
            current = current.next.next
        
        return head
            
            