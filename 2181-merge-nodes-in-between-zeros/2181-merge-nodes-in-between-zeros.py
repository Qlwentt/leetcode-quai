# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head.next
        dummy = ListNode()
        tail = dummy
        cur_sum = 0
        while current:
            if current.val:
                cur_sum += current.val
            else:
                tail.next = ListNode(cur_sum)
                cur_sum = 0
                tail = tail.next
            current = current.next
        
        return dummy.next
            