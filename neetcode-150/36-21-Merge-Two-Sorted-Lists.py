from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-999)
        merged = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        if list1:
            merged.next = list1
        elif list2:
            merged.next = list2
            
        return dummy.next
# O(min(n,m)) time
# O(1) space