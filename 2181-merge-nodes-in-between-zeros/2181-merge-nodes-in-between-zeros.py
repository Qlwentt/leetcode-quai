# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head.next
        cur_sum = 0
        first = head.next
        tail = first
        while current and current.next:
            cur_sum += current.val
            if not current.next.val:
                tail.val = cur_sum
                cur_sum = 0
                tail.next = current.next.next
                tail = tail.next
            current = current.next
        return first
        
            