# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge2Lists(l1,l2):
            dummy = ListNode()
            tail = dummy
            
            while l1 or l2:
                val1 = l1.val if l1 else float('inf')
                val2 = l2.val if l2 else float('inf')
                
                if val1 < val2:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            return dummy.next
        while len(lists) > 1:
            newLists = []
            while lists:
                a = lists.pop()
                b = lists.pop() if lists else None
                newLists.append(merge2Lists(a,b))
            lists = newLists
        
        return lists[0]
        