# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        dummy = ListNode(0)
        result = dummy
        while c1 or c2:
            val = None
            val1 = c1.val if c1 else float('inf')
            val2 = c2.val if c2 else float('inf')
            
            if val1 < val2:
                val = val1
                c1 = c1.next
            else:
                val = val2
                c2 = c2.next
            result.next = ListNode(val)
            result = result.next
        return dummy.next