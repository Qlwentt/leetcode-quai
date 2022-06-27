from typing import Optional,List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge2Lists(l1,l2))
            lists = mergedLists
        return lists[0]
    
    def merge2Lists(self,l1,l2):
        dummy = ListNode(0)
        merged = dummy
        while l1 or l2:
            val1 = l1.val if l1 else float("inf")
            val2 = l2.val if l2 else float("inf")
            
            if val1 <= val2:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        
        return dummy.next