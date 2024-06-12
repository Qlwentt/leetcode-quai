# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy = ListNode(0)
        result = dummy
        while p1 or p2:
            node = None
            val1 = p1.val if p1 else float('inf')
            val2 = p2.val if p2 else float('inf')
            
            if val1 < val2:
                node = p1
                p1 = p1.next
            else:
                node = p2
                p2 = p2.next
            result.next = node
            result = result.next
        return dummy.next