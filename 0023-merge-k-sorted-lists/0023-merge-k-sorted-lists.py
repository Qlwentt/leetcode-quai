# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def mergeTwoLists(l1,l2):
            dummy = ListNode()
            end = dummy
            while l1 or l2:
                val1 = l1.val if l1 else float('inf')
                val2 = l2.val if l2 else float('inf')
                
                if val1 < val2:
                    end.next = l1
                    l1 = l1.next
                else:
                    end.next = l2
                    l2 = l2.next
                end = end.next
            return dummy.next
        
        while len(lists) > 1:
            mergedLists = []
            while lists:
                a = lists.pop()
                b = lists.pop() if lists else None
                mergedLists.append(mergeTwoLists(a,b))
            lists = mergedLists
            
        return lists[0]